"""
wp.py — Operacoes no WordPress (server-side, dentro do broker).

Porta a logica de rede que antes vivia nos scripts locais da skill
(wp_publish.py / update_seo.py / sync_assets.py). Roda no Cloud Run com as
credenciais lidas do Secret Manager — nunca expostas ao cliente.

So usa a stdlib (urllib), como os scripts originais.
"""

import json
import re
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "blog-mk-broker/1.0"
AUTHOR_IAN = 1  # ID do Ian Borges no WP

# Mapeamento pilar -> categoria (criadas previamente no WP)
PILAR_TO_CATEGORY = {
    1: 142,  # Immersive Commerce
    2: 143,  # Provador Virtual
    3: 144,  # Visualizador 3D e AR
}


def _http(method, url, headers=None, body=None, jwt=None, timeout=60):
    headers = dict(headers or {})
    headers.setdefault("User-Agent", USER_AGENT)
    headers.setdefault("Accept", "application/json")
    if jwt:
        headers["Authorization"] = f"Bearer {jwt}"
    if isinstance(body, (dict, list)):
        body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read().decode("utf-8")
            return r.status, (json.loads(data) if data else {})
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8"))
        except Exception:
            return e.code, {"raw_error": "non-json response"}
    except urllib.error.URLError as e:
        return 0, {"error": str(e)}


def authenticate(creds):
    """Troca username/password por um JWT via Simple JWT Login."""
    site = creds["WP_SITE_URL"]
    auth_url = f"{site}/?rest_route=/simple-jwt-login/v1/auth"
    body = urllib.parse.urlencode({
        "username": creds["WP_USERNAME"],
        "password": creds["WP_PASSWORD"],
    }).encode("utf-8")
    req = urllib.request.Request(
        auth_url, data=body, method="POST",
        headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if not data.get("success"):
        raise RuntimeError(f"Auth WP falhou: {data}")
    return data["data"]["jwt"]


def resolve_tags(jwt, site, tag_names):
    """Para cada nome de tag: lookup por slug/name, cria se nao existir. Retorna IDs."""
    ids = []
    base = f"{site}/wp-json/wp/v2/tags"
    for name in tag_names or []:
        slug_guess = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        code, items = _http("GET", f"{base}?slug={urllib.parse.quote(slug_guess)}", jwt=jwt)
        if code == 200 and isinstance(items, list) and items:
            ids.append(items[0]["id"])
            continue
        code, items = _http("GET", f"{base}?search={urllib.parse.quote(name)}&per_page=10", jwt=jwt)
        found = None
        if code == 200 and isinstance(items, list):
            for it in items:
                if it.get("name", "").lower() == name.lower():
                    found = it
                    break
        if found:
            ids.append(found["id"])
            continue
        code, new_tag = _http("POST", base, body={"name": name}, jwt=jwt)
        if code in (200, 201) and isinstance(new_tag, dict) and "id" in new_tag:
            ids.append(new_tag["id"])
        elif isinstance(new_tag, dict) and new_tag.get("code") == "term_exists":
            ids.append(new_tag["data"]["term_id"])
    return ids


def find_media_by_url(jwt, site, source_url):
    """Acha o ID da media no WP Library pela URL do hero."""
    if not source_url:
        return None
    filename = source_url.rsplit("/", 1)[-1]
    base = re.sub(r"(-\d+x\d+|-scaled)(?=\.\w+$)", "", filename)
    base_no_ext = re.sub(r"\.\w+$", "", base)
    search_url = f"{site}/wp-json/wp/v2/media?search={urllib.parse.quote(base_no_ext)}&per_page=10"
    code, items = _http("GET", search_url, jwt=jwt)
    if code != 200 or not isinstance(items, list):
        return None
    for it in items:
        if it.get("source_url") == source_url:
            return it["id"]
    for it in items:
        if base_no_ext in (it.get("slug") or ""):
            return it["id"]
    return items[0]["id"] if items else None


def publish_post(creds, payload):
    """
    Cria (ou atualiza) um post no WP a partir do payload do cliente.

    payload: title, slug, status, content (HTML), tag_names[], pilar,
             is_pillar_page, hero_url, yoast{title,metadesc,focuskw,is_cornerstone},
             update_id
    Retorna: {post_id, url, edit_url, status, yoast_persisted}
    """
    site = creds["WP_SITE_URL"]
    jwt = authenticate(creds)

    cat_id = PILAR_TO_CATEGORY.get(payload.get("pilar"))
    tag_ids = resolve_tags(jwt, site, payload.get("tag_names"))
    featured_id = find_media_by_url(jwt, site, payload.get("hero_url"))

    yoast = payload.get("yoast") or {}
    yoast_meta = {
        "_yoast_wpseo_title": yoast.get("title", ""),
        "_yoast_wpseo_metadesc": yoast.get("metadesc", ""),
        "_yoast_wpseo_focuskw": yoast.get("focuskw", ""),
        "_yoast_wpseo_is_cornerstone": "1" if yoast.get("is_cornerstone") else "0",
    }

    wp_payload = {
        "title": payload.get("title") or payload.get("slug"),
        "slug": payload.get("slug"),
        "status": payload.get("status", "draft"),
        "author": AUTHOR_IAN,
        "content": payload.get("content", ""),
        "categories": [cat_id] if cat_id else [],
        "tags": tag_ids,
        "meta": yoast_meta,
    }
    if featured_id:
        wp_payload["featured_media"] = featured_id

    update_id = payload.get("update_id")
    if update_id:
        code, resp = _http("POST", f"{site}/wp-json/wp/v2/posts/{update_id}", body=wp_payload, jwt=jwt)
    else:
        code, resp = _http("POST", f"{site}/wp-json/wp/v2/posts", body=wp_payload, jwt=jwt)

    if code not in (200, 201):
        raise RuntimeError(f"WP retornou {code}: {json.dumps(resp, ensure_ascii=False)[:400]}")

    meta_resp = resp.get("meta") or {}
    yoast_persisted = sum(1 for k in yoast_meta if meta_resp.get(k))
    return {
        "post_id": resp["id"],
        "status": resp.get("status"),
        "url": resp.get("link"),
        "edit_url": f"{site}/wp-admin/post.php?post={resp['id']}&action=edit",
        "yoast_persisted": f"{yoast_persisted}/{len(yoast_meta)}",
    }


def update_seo(creds, updates):
    """Aplica batch de atualizacoes SEO/Yoast em posts existentes."""
    site = creds["WP_SITE_URL"]
    jwt = authenticate(creds)
    results = []
    for u in updates or []:
        pid = u.get("id")
        meta = {}
        if "title" in u:
            meta["_yoast_wpseo_title"] = u["title"]
        if "metadesc" in u:
            meta["_yoast_wpseo_metadesc"] = u["metadesc"]
        body = {}
        if meta:
            body["meta"] = meta
        if "featured_media" in u:
            body["featured_media"] = u["featured_media"]
        code, resp = _http("POST", f"{site}/wp-json/wp/v2/posts/{pid}", body=body, jwt=jwt)
        results.append({"id": pid, "ok": code in (200, 201),
                        "detail": "" if code in (200, 201) else f"HTTP {code}"})
    return {"results": results}


def _fetch_paginated(jwt, site, endpoint, fields, extra=""):
    items = []
    page = 1
    while True:
        url = (f"{site}/wp-json/wp/v2/{endpoint}"
               f"?per_page=100&page={page}&_fields={fields}{extra}")
        code, data = _http("GET", url, jwt=jwt)
        if code != 200 or not isinstance(data, list) or not data:
            break
        items.extend(data)
        if len(data) < 100:
            break
        page += 1
    return items


def sync_assets(creds):
    """Retorna os dados crus do WP (media + posts + pages) para o cliente processar."""
    site = creds["WP_SITE_URL"]
    jwt = authenticate(creds)
    media = _fetch_paginated(jwt, site, "media",
                             "id,date,slug,source_url,mime_type,alt_text,media_details")
    posts = _fetch_paginated(jwt, site, "posts",
                             "id,slug,link,title,categories,status", extra="&status=publish")
    pages = _fetch_paginated(jwt, site, "pages",
                             "id,slug,link,title,status", extra="&status=publish")
    return {"media": media, "posts": posts, "pages": pages}
