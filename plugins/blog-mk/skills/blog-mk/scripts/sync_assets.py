#!/usr/bin/env python3
"""
sync_assets.py — Sincronizador do banco de assets da skill blog-mk (cliente do broker).

Operacao de MANUTENCAO (mantenedor): atualiza references/assets-db.json com as
midias, posts e paginas do WordPress, preservando as avaliacoes visuais ja feitas,
e verifica links mortos. A busca dos dados no WP e feita pelo BROKER (que tem as
credenciais); o processamento, a heuristica e o DB ficam locais.

Login antes de usar:
    python scripts/auth.py

Uso:
    python scripts/sync_assets.py                 # sync completo
    python scripts/sync_assets.py --no-linkcheck   # pula verificacao de links mortos
    python scripts/sync_assets.py --media-only
    python scripts/sync_assets.py --links-only
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from broker_client import sync_assets as broker_sync_assets, BrokerError  # noqa: E402

SKILL_DIR = Path(__file__).resolve().parent.parent
REFS_DIR = SKILL_DIR / "references"
DB_FILE = REFS_DIR / "assets-db.json"
REPORT_MD = REFS_DIR / "sync-report.md"
USER_AGENT = "blog-mk-skill/4.1"


def log(msg, level="info"):
    prefix = {"info": "[i]", "ok": "[OK]", "warn": "[!]", "err": "[X]"}.get(level, "[i]")
    print(f"{prefix} {msg}")


# === Heuristica de midia (local) ===
def heuristic_media(m):
    slug = (m.get("slug") or "").lower()
    md = m.get("media_details") or {}
    w = md.get("width") or 0
    mime = m.get("mime_type", "")
    date = (m.get("date") or "")[:10]
    blob = f"{slug} {(m.get('alt_text') or '').lower()}"

    if any(k in blob for k in ["selo", "logo", "partner", "cartela"]):
        cat = "logo"
    elif any(k in blob for k in ["depoimento", "stephanie", "guilherme", "elaine",
                                 "fernando", "monica", "celso", "hugo", "mariana", "daniela"]):
        cat = "depoimento"
    elif any(k in blob for k in ["dashboard", "metricas", "roi", "infografico", "grafico"]):
        cat = "infografico"
    elif any(k in blob for k in ["thumb", "capa", "hero", "cover"]):
        cat = "hero"
    elif mime == "image/gif" or "gif" in blob or "demo" in blob:
        cat = "gif_produto"
    else:
        cat = "inline"

    score = 3
    if w >= 1500:
        score += 1
    if w and w < 600:
        score -= 1
    if date >= "2026-01":
        score += 1
    if mime in ("image/svg+xml", "application/pdf"):
        score -= 2
    return cat, max(0, min(5, score))


def detect_brand(slug):
    brand_map = {
        "flexform": "Flexform", "boca-rosa": "Boca Rosa", "toymania": "Toymania",
        "bio-extratus": "Bio Extratus", "bioextratus": "Bio Extratus", "loreal": "L'Oréal",
        "avon": "Avon", "natura": "Natura", "gm": "GM", "general-motors": "GM",
        "gregory": "Gregory", "osklen": "Osklen", "redley": "Redley", "mascavo": "Mascavo",
        "stanley": "Stanley", "heineken": "Heineken", "globo": "Globo", "fuel": "Fuel Eyewear",
        "epoca": "Época", "skala": "Skala", "anasol": "Anasol", "mili": "Mili", "copra": "Copra",
        "freeco": "Freeco", "aneethun": "Aneethun", "wap": "WAP", "oba": "Oba Hortifruti",
        "ilha-pura": "Ilha Pura",
    }
    s = (slug or "").lower()
    for k, v in brand_map.items():
        if k in s:
            return v
    return None


def classify_post(post):
    slug = post.get("slug", "")
    title = (post.get("title") or {}).get("rendered", "")
    is_pillar = "guia-completo" in slug or "guia" in slug.split("-")[:2]
    return {
        "url": post.get("link", ""),
        "type": "pillar" if is_pillar else "article",
        "title": re.sub(r"&[a-z]+;", "", title),
        "slug": slug,
        "wp_id": post.get("id"),
        "categories": post.get("categories", []),
        "status": post.get("status", "publish"),
    }


def check_link(url, timeout=15):
    """HEAD a uma URL publica do blog (sem credencial). Retorna status HTTP ou 0."""
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def load_db():
    if DB_FILE.exists():
        return json.loads(DB_FILE.read_text(encoding="utf-8"))
    return {"meta": {}, "media": [], "links": []}


def save_db(db):
    DB_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Sincroniza banco de assets com o WordPress via broker")
    ap.add_argument("--no-linkcheck", action="store_true", help="Pula verificacao de links mortos")
    ap.add_argument("--media-only", action="store_true")
    ap.add_argument("--links-only", action="store_true")
    args = ap.parse_args()

    log("Buscando dados do WP via broker...")
    try:
        data = broker_sync_assets()
    except BrokerError as e:
        log(str(e), "err")
        sys.exit(1)

    wp_media = data.get("media", [])
    posts = data.get("posts", [])
    pages = data.get("pages", [])
    log(f"Recebido do broker: {len(wp_media)} midias, {len(posts)} posts, {len(pages)} paginas", "ok")

    db = load_db()
    media_by_id = {m["id"]: m for m in db.get("media", [])}
    links_by_url = {l["url"]: l for l in db.get("links", [])}

    report = [f"# Sync Report — {datetime.now(timezone.utc).isoformat()}\n"]
    new_media = new_links = dead_links = 0

    # === MIDIAS ===
    if not args.links_only:
        wp_media_ids = set()
        for m in wp_media:
            mid = m["id"]
            wp_media_ids.add(mid)
            md = m.get("media_details") or {}
            cat, score = heuristic_media(m)
            brand = detect_brand(m.get("slug", ""))
            if mid in media_by_id:
                rec = media_by_id[mid]
                rec["url"] = m.get("source_url", rec.get("url"))
                rec["width"] = md.get("width", rec.get("width"))
                rec["height"] = md.get("height", rec.get("height"))
                rec["alt"] = m.get("alt_text", rec.get("alt"))
                if rec.get("eval_method") in (None, "none"):
                    rec["auto_category"], rec["score"] = cat, score
            else:
                media_by_id[mid] = {
                    "id": mid, "url": m.get("source_url"), "slug": m.get("slug"),
                    "mime": m.get("mime_type"), "width": md.get("width"), "height": md.get("height"),
                    "date": (m.get("date") or "")[:10], "alt": m.get("alt_text", ""), "brand": brand,
                    "auto_category": cat, "use_category": None, "theme_tags": [], "score": score,
                    "best_use": "", "eval_method": "none", "evaluated_at": None,
                }
                new_media += 1
        for mid, rec in media_by_id.items():
            rec["in_wp"] = mid in wp_media_ids
        db["media"] = list(media_by_id.values())
        a_avaliar = sum(1 for m in db['media'] if m.get('eval_method') != 'visual')
        report.append(f"- Midias no WP: **{len(wp_media)}**")
        report.append(f"- Midias novas: **{new_media}**")
        report.append(f"- Midias a avaliar visualmente: **{a_avaliar}**")

    # === LINKS (posts + mKases + LPs) ===
    if not args.media_only:
        mkases, lps = [], []
        for pg in pages:
            link = pg.get("link") or ""
            if "/mkases/" in link:
                mkases.append(pg)
            elif re.search(r"/mk-[a-z0-9-]+/?$", link) or "/mklabs/" in link:
                lps.append(pg)

        records = [classify_post(p) for p in posts]
        for mk in mkases:
            records.append({
                "url": mk.get("link", ""), "type": "mkase",
                "title": re.sub(r"&[a-z]+;", "", (mk.get("title") or {}).get("rendered", "")),
                "slug": mk.get("slug"), "wp_id": mk.get("id"), "categories": [],
                "status": mk.get("status", "publish"),
            })
        for lp in lps:
            records.append({
                "url": lp.get("link", ""), "type": "lp",
                "title": re.sub(r"&[a-z]+;", "", (lp.get("title") or {}).get("rendered", "")),
                "slug": lp.get("slug"), "wp_id": lp.get("id"), "categories": [],
                "status": lp.get("status", "publish"),
            })

        for rec in records:
            url = rec["url"]
            if not url:
                continue
            if url in links_by_url:
                links_by_url[url].update({
                    "title": rec["title"] or links_by_url[url].get("title"),
                    "type": rec["type"], "status": rec["status"],
                })
            else:
                links_by_url[url] = {
                    "url": url, "type": rec["type"], "title": rec["title"], "slug": rec.get("slug"),
                    "pilar": None, "score": 5 if rec["type"] in ("pillar", "lp") else 4,
                    "best_use": "", "status_http": None, "last_checked": None, "status": rec["status"],
                }
                new_links += 1

        if not args.no_linkcheck:
            log("Verificando status HTTP dos links (pode demorar)...")
            for url, rec in links_by_url.items():
                st = check_link(url)
                rec["status_http"] = st
                rec["last_checked"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
                if st not in (200, 301, 302):
                    dead_links += 1
                time.sleep(0.1)

        db["links"] = list(links_by_url.values())
        report.append(f"- Posts: **{len(posts)}** | mKases: **{len(mkases)}** | LPs: **{len(lps)}**")
        report.append(f"- Links novos: **{new_links}** | Links mortos: **{dead_links}**")
        if dead_links:
            report.append("\n### Links mortos detectados:")
            for rec in db["links"]:
                if rec.get("status_http") not in (200, 301, 302, None):
                    report.append(f"  - [{rec.get('status_http')}] {rec['url']}")

    db["meta"] = {
        "last_sync": datetime.now(timezone.utc).isoformat(),
        "total_media": len(db.get("media", [])),
        "total_links": len(db.get("links", [])),
        "media_evaluated_visual": sum(1 for m in db.get("media", []) if m.get("eval_method") == "visual"),
    }
    save_db(db)
    REPORT_MD.write_text("\n".join(report) + "\n", encoding="utf-8")
    log(f"Banco salvo: {DB_FILE}", "ok")
    log(f"Relatorio salvo: {REPORT_MD}", "ok")
    print()
    log(f"RESUMO: {new_media} midias novas | {new_links} links novos | {dead_links} links mortos", "ok")


if __name__ == "__main__":
    main()
