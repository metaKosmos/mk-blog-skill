#!/usr/bin/env python3
"""
wp_publish.py — Modo Publicar da skill blog-mk

Publica artigos da pasta output/[slug]/ no WordPress via REST API com:
- Conteúdo HTML do artigo.html
- Título SEO, meta description, focus keyword (Yoast)
- Pillar Page flag (cornerstone) quando aplicável
- Categoria mapeada pelo pilar
- Tags (lookup ou criação automática)
- Featured image (lookup pela URL na Media Library)
- Autor = Ian Borges (ID 1)
- Status default: draft

Uso:
    python scripts/wp_publish.py --list                          # lista slugs disponíveis
    python scripts/wp_publish.py <slug> --dry-run                # valida sem postar
    python scripts/wp_publish.py <slug>                          # publica como rascunho
    python scripts/wp_publish.py <slug> --status publish         # publica direto (cuidado!)

Requer: blog mK/.env com WP_SITE_URL, WP_USERNAME, WP_PASSWORD.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# === Config ===
SKILL_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = SKILL_DIR / "output"
ENV_FILE = SKILL_DIR / ".env"

# Mapping pilar -> categoria ID (criadas via API previamente)
PILAR_TO_CATEGORY = {
    1: 142,  # Immersive Commerce
    2: 143,  # Provador Virtual
    3: 144,  # Visualizador 3D e AR
}

AUTHOR_IAN = 1  # ID do Ian Borges
USER_AGENT = "blog-mk-skill/1.0"


# === Logging ===
def log(msg, level="info"):
    prefix = {
        "info": "[i]",
        "ok": "[OK]",
        "warn": "[!]",
        "err": "[X]",
    }.get(level, "[i]")
    print(f"{prefix} {msg}")


# === Env ===
def load_env():
    env = {}
    if not ENV_FILE.exists():
        log(f".env nao encontrado em {ENV_FILE}", "err")
        sys.exit(1)
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    required = ["WP_SITE_URL", "WP_USERNAME", "WP_PASSWORD"]
    missing = [k for k in required if k not in env or not env[k]]
    if missing:
        log(f"Variaveis faltando no .env: {missing}", "err")
        sys.exit(1)
    return env


# === HTTP ===
def http(method, url, headers=None, body=None, jwt=None):
    headers = dict(headers or {})
    headers.setdefault("User-Agent", USER_AGENT)
    headers.setdefault("Accept", "application/json")
    if jwt:
        headers["Authorization"] = f"Bearer {jwt}"
    if body is not None and isinstance(body, (dict, list)):
        body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read().decode("utf-8")
            return r.status, json.loads(data) if data else {}
    except urllib.error.HTTPError as e:
        try:
            err_body = json.loads(e.read().decode("utf-8"))
        except Exception:
            err_body = {"raw_error": "non-json response"}
        return e.code, err_body
    except urllib.error.URLError as e:
        return 0, {"error": str(e)}


def authenticate(env):
    log("Autenticando via JWT...")
    auth_url = f"{env['WP_SITE_URL']}/?rest_route=/simple-jwt-login/v1/auth"
    body = urllib.parse.urlencode({
        "username": env["WP_USERNAME"],
        "password": env["WP_PASSWORD"],
    }).encode("utf-8")
    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    req = urllib.request.Request(auth_url, data=body, method="POST", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
    except Exception as e:
        log(f"Erro de autenticacao: {e}", "err")
        sys.exit(1)
    if not data.get("success"):
        log(f"Auth falhou: {data}", "err")
        sys.exit(1)
    jwt = data["data"]["jwt"]
    log(f"JWT obtido ({len(jwt)} chars)", "ok")
    return jwt


# === Parser metadados.md ===
def parse_metadados(md_path):
    text = md_path.read_text(encoding="utf-8")

    def extract(pattern, default=None):
        m = re.search(pattern, text, re.MULTILINE)
        return m.group(1).strip() if m else default

    def clean_size_suffix(s):
        if not s:
            return s
        return re.sub(r"\s*\(\d+\s*caracteres?\)\s*$", "", s).strip()

    title_seo = clean_size_suffix(extract(r"\*\*Título SEO:\*\*\s*(.+)"))
    meta_desc = clean_size_suffix(extract(r"\*\*Meta Description:\*\*\s*(.+)"))
    slug = extract(r"\*\*Slug:\*\*\s*(\S+)")
    keyword_raw = extract(r"\*\*Keyword Principal:\*\*\s*(.+)")
    # Keyword pode ter múltiplas variantes separadas por "/" - pega só a primeira
    keyword = keyword_raw.split("/")[0].strip() if keyword_raw else ""

    tags_str = extract(r"\*\*Tags:\*\*\s*(.+)")
    tags = [t.strip() for t in (tags_str or "").split(",") if t.strip()] if tags_str else []

    pilar_str = extract(r"\*\*Pilar:\*\*\s*(\d+)")
    pilar = int(pilar_str) if pilar_str else None

    # Detecta Pillar Page (cornerstone Yoast).
    # Procura por declaração explícita no metadados:
    #   "**Cornerstone (Pillar Page):** Sim" ou
    #   "Pilar X — Provador Virtual (**Pillar Page do cluster**)"
    # Ignora menções contextuais como "linka para Pillar Page do P1" ou "é satélite do P1".
    is_pillar = bool(
        re.search(r"\*\*Cornerstone[^:]*:\*\*\s*Sim", text, re.IGNORECASE)
        or re.search(r"\*\*Pillar Page do cluster\*\*", text)
    )

    return {
        "title_seo": title_seo or "",
        "meta_description": meta_desc or "",
        "slug": slug or "",
        "keyword": keyword or "",
        "tags": tags,
        "pilar": pilar,
        "is_pillar_page": is_pillar,
    }


# === Hero image ===
def extract_hero_image_url(html_path):
    html = html_path.read_text(encoding="utf-8")
    m = re.search(r'<img\s+[^>]*?src=["\'](https?://[^"\']+)["\']', html)
    return m.group(1) if m else None


# === Strip H1 e Hero do conteúdo (WP renderiza title + featured separadamente) ===
def strip_h1_and_hero(html):
    """
    Remove o primeiro <h1> (wp:heading level:1) e a primeira <img> (wp:image hero)
    do início do artigo. O WordPress renderiza o título do post e o featured_media
    automaticamente — manter no conteúdo causa duplicação visual no front-end.

    Mantém intacto:
    - bloco wp:html com <style> local
    - todos os outros parágrafos, listas, mídias inline, cards, etc.

    Retorna o HTML modificado.
    """
    result = html

    # 1) Remove o primeiro wp:heading level:1 (o H1 do artigo).
    # JSON do bloco pode ter chaves aninhadas (style, spacing, etc.),
    # então casamos qualquer coisa até o "-->" da abertura.
    h1_pattern = re.compile(
        r'<!--\s*wp:heading\s*\{[^\n]*?"level"\s*:\s*1[^\n]*?-->\s*'
        r'<h1[^>]*>.*?</h1>\s*'
        r'<!--\s*/wp:heading\s*-->\s*\n?',
        re.DOTALL
    )
    result, n_h1 = h1_pattern.subn('', result, count=1)

    # 2) Remove o primeiro wp:image (hero) — só se aparecer ANTES de qualquer wp:paragraph
    #    Isso garante que estamos removendo a hero do topo, não uma imagem no meio do texto.
    first_paragraph = result.find('<!-- wp:paragraph')
    first_image = result.find('<!-- wp:image')
    n_img = 0
    if first_image != -1 and (first_paragraph == -1 or first_image < first_paragraph):
        img_pattern = re.compile(
            r'<!--\s*wp:image\s+[^\n]*?-->\s*'
            r'<figure[^>]*>.*?</figure>\s*'
            r'<!--\s*/wp:image\s*-->\s*\n?',
            re.DOTALL
        )
        result, n_img = img_pattern.subn('', result, count=1)

    return result, n_h1, n_img


# === WP operations ===
def find_media_by_url(jwt, env, source_url):
    """Acha o ID da media no WP Library pela URL."""
    filename = source_url.rsplit("/", 1)[-1]
    base = re.sub(r"(-\d+x\d+|-scaled)(?=\.\w+$)", "", filename)
    base_no_ext = re.sub(r"\.\w+$", "", base)
    search_url = f"{env['WP_SITE_URL']}/wp-json/wp/v2/media?search={urllib.parse.quote(base_no_ext)}&per_page=10"
    code, items = http("GET", search_url, jwt=jwt)
    if code != 200 or not isinstance(items, list):
        return None
    # Match exato pela URL
    for it in items:
        if it.get("source_url") == source_url:
            return it["id"]
    # Match aproximado pelo basename
    for it in items:
        if base_no_ext in (it.get("slug") or ""):
            return it["id"]
    return items[0]["id"] if items else None


def resolve_tags(jwt, env, tag_names):
    """Para cada tag: lookup por slug/name, cria se não existir, retorna lista de IDs."""
    ids = []
    base = f"{env['WP_SITE_URL']}/wp-json/wp/v2/tags"
    for name in tag_names:
        slug_guess = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

        # Tenta por slug
        code, items = http("GET", f"{base}?slug={urllib.parse.quote(slug_guess)}", jwt=jwt)
        if code == 200 and isinstance(items, list) and items:
            ids.append(items[0]["id"])
            continue

        # Tenta por search/name
        code, items = http("GET", f"{base}?search={urllib.parse.quote(name)}&per_page=10", jwt=jwt)
        found = None
        if code == 200 and isinstance(items, list):
            for it in items:
                if it.get("name", "").lower() == name.lower():
                    found = it
                    break
        if found:
            ids.append(found["id"])
            continue

        # Cria
        code, new_tag = http("POST", base, body={"name": name}, jwt=jwt)
        if code in (200, 201) and isinstance(new_tag, dict) and "id" in new_tag:
            ids.append(new_tag["id"])
            log(f"  tag criada: '{name}' -> ID {new_tag['id']}")
        elif isinstance(new_tag, dict) and new_tag.get("code") == "term_exists":
            ids.append(new_tag["data"]["term_id"])
        else:
            log(f"  falha ao criar tag '{name}': {new_tag}", "warn")
    return ids


# === Main ===
def publish(slug, status="draft", dry_run=False, update_id=None):
    article_dir = OUTPUT_DIR / slug
    if not article_dir.exists():
        log(f"Pasta nao encontrada: {article_dir}", "err")
        sys.exit(1)

    html_path = article_dir / "artigo.html"
    md_path = article_dir / "metadados.md"
    if not html_path.exists():
        log(f"artigo.html nao encontrado em {article_dir}", "err")
        sys.exit(1)
    if not md_path.exists():
        log(f"metadados.md nao encontrado em {article_dir}", "err")
        sys.exit(1)

    env = load_env()
    meta = parse_metadados(md_path)

    log(f"Slug: {meta['slug']}")
    log(f"Titulo SEO ({len(meta['title_seo'])}c): {meta['title_seo']}")
    log(f"Meta Desc ({len(meta['meta_description'])}c)")
    log(f"Keyword: {meta['keyword']}")
    log(f"Pilar: {meta['pilar']}  |  Pillar Page (cornerstone): {meta['is_pillar_page']}")
    log(f"Tags planejadas: {len(meta['tags'])}")

    # Validações de SEO
    if len(meta["title_seo"]) > 60:
        log(f"Titulo SEO acima de 60c ({len(meta['title_seo'])}c)", "warn")
    if len(meta["meta_description"]) > 155:
        log(f"Meta Description acima de 155c ({len(meta['meta_description'])}c)", "warn")

    jwt = authenticate(env)

    cat_id = PILAR_TO_CATEGORY.get(meta["pilar"])
    if not cat_id:
        log(f"Pilar {meta['pilar']} sem categoria mapeada — usando 'Nao categorizado'", "warn")
    else:
        log(f"Categoria: ID {cat_id}", "ok")

    log("Resolvendo tags (lookup/criar)...")
    tag_ids = resolve_tags(jwt, env, meta["tags"])
    log(f"Tags resolvidas: {len(tag_ids)}/{len(meta['tags'])}", "ok")

    hero_url = extract_hero_image_url(html_path)
    featured_id = None
    if hero_url:
        log(f"Hero image: {hero_url[:90]}")
        featured_id = find_media_by_url(jwt, env, hero_url)
        if featured_id:
            log(f"Featured media ID: {featured_id}", "ok")
        else:
            log("Hero image nao encontrada na Media Library (post sem featured image)", "warn")

    html_content_raw = html_path.read_text(encoding="utf-8")
    html_content, removed_h1, removed_img = strip_h1_and_hero(html_content_raw)
    log(f"Conteudo HTML: {len(html_content_raw)} chars (raw) -> {len(html_content)} chars (after strip H1 + hero)")
    if removed_h1:
        log(f"  - H1 removido do topo (WP renderiza o title automaticamente)", "ok")
    if removed_img:
        log(f"  - Hero image removida do topo (WP renderiza o featured_media)", "ok")

    yoast_meta = {
        "_yoast_wpseo_title": meta["title_seo"],
        "_yoast_wpseo_metadesc": meta["meta_description"],
        "_yoast_wpseo_focuskw": meta["keyword"],
        "_yoast_wpseo_is_cornerstone": "1" if meta["is_pillar_page"] else "0",
    }

    payload = {
        "title": meta["title_seo"] or meta["slug"],
        "slug": meta["slug"],
        "status": status,
        "author": AUTHOR_IAN,
        "content": html_content,
        "categories": [cat_id] if cat_id else [],
        "tags": tag_ids,
        "meta": yoast_meta,
    }
    if featured_id:
        payload["featured_media"] = featured_id

    if dry_run:
        log("=== DRY RUN — payload pronto (sem chamar API de criação) ===", "warn")
        preview = {k: v for k, v in payload.items() if k != "content"}
        preview["content"] = f"<{len(html_content)} chars>"
        print(json.dumps(preview, ensure_ascii=False, indent=2))
        return

    if update_id:
        log(f"Atualizando post existente ID {update_id} como '{status}'...")
        code, resp = http("POST", f"{env['WP_SITE_URL']}/wp-json/wp/v2/posts/{update_id}",
                          body=payload, jwt=jwt)
    else:
        log(f"Criando post como '{status}'...")
        code, resp = http("POST", f"{env['WP_SITE_URL']}/wp-json/wp/v2/posts",
                          body=payload, jwt=jwt)

    if code in (200, 201):
        log(f"Post criado! ID {resp['id']}", "ok")
        log(f"Status: {resp['status']}", "ok")
        log(f"Slug final: {resp.get('slug')}", "ok")
        log(f"Preview/Link: {resp.get('link')}", "ok")
        edit_url = f"{env['WP_SITE_URL']}/wp-admin/post.php?post={resp['id']}&action=edit"
        log(f"Editor: {edit_url}", "ok")

        # Persistencia Yoast
        meta_resp = resp.get("meta") or {}
        yoast_persisted = sum(1 for k in yoast_meta if meta_resp.get(k))
        log(f"Yoast fields persistidos: {yoast_persisted}/{len(yoast_meta)}", "ok")
    else:
        log(f"Erro HTTP {code}: {json.dumps(resp, ensure_ascii=False)[:500]}", "err")
        sys.exit(1)


def main():
    p = argparse.ArgumentParser(
        description="Publica artigo do blog-mk no WordPress via REST API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("slug", nargs="?", help="Slug da pasta em output/")
    p.add_argument("--status", choices=["draft", "publish", "pending"], default="draft",
                   help="Status do post (default: draft)")
    p.add_argument("--dry-run", action="store_true",
                   help="Valida e monta payload sem criar o post")
    p.add_argument("--list", action="store_true",
                   help="Lista slugs disponiveis em output/")
    p.add_argument("--update", type=int, metavar="POST_ID",
                   help="Atualiza post existente (em vez de criar novo)")
    args = p.parse_args()

    if args.list:
        if not OUTPUT_DIR.exists():
            log(f"output/ nao existe ({OUTPUT_DIR})", "err")
            return
        # Ignora pastas-arquivo (Postado/, Arquivado/, etc.) e auxiliares (_briefing, etc.)
        ARCHIVE_FOLDERS = {"Postado", "Arquivado", "Drafts"}
        slugs = [d.name for d in sorted(OUTPUT_DIR.iterdir())
                 if d.is_dir()
                 and not d.name.startswith("_")
                 and d.name not in ARCHIVE_FOLDERS
                 and (d / "artigo.html").exists()]
        if not slugs:
            log("Nenhum artigo encontrado em output/", "warn")
            return
        log(f"Artigos disponiveis em output/ ({len(slugs)}):")
        for s in slugs:
            print(f"  {s}")
        return

    if not args.slug:
        p.error("slug eh obrigatorio (ou use --list)")

    publish(args.slug, status=args.status, dry_run=args.dry_run, update_id=args.update)


if __name__ == "__main__":
    main()
