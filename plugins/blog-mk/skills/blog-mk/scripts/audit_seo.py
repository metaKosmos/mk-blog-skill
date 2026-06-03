#!/usr/bin/env python3
"""
audit_seo.py — Auditoria de SEO dos posts publicados (somente leitura)

Puxa todos os posts publicados de metakosmos.com.br via REST API, ordenados do
mais antigo para o mais novo, e avalia para cada um:
  - Título SEO (Yoast) e tamanho (>60c trunca no Google)
  - Meta description (Yoast) e tamanho (vazia ou >155c)
  - Imagem destacada (featured_media)
Lê o yoast_head_json, que é público (não precisa de auth para leitura).

Uso:
    python scripts/audit_seo.py            # lista todos, do mais antigo ao mais novo
    python scripts/audit_seo.py 15         # detalha os 15 mais antigos
"""
import json
import re
import sys
import urllib.request

BASE = "https://metakosmos.com.br"
UA = "blog-mk-skill/1.0"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def fetch_posts():
    posts, page = [], 1
    while True:
        url = (f"{BASE}/wp-json/wp/v2/posts?per_page=100&page={page}"
               f"&orderby=date&order=asc&_fields=id,date,slug,link,title,featured_media,yoast_head_json")
        try:
            data = get(url)
        except Exception as e:
            print(f"[!] parou na page {page}: {e}")
            break
        if not data:
            break
        posts.extend(data)
        if len(data) < 100:
            break
        page += 1
    return posts


def strip(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def evalp(p):
    y = p.get("yoast_head_json") or {}
    seo_title = y.get("title") or ""
    metadesc = y.get("description") or ""
    og = y.get("og_image") or []
    ogimg = og[0].get("url", "") if og else ""
    fm = p.get("featured_media") or 0
    issues = []
    if not metadesc:
        issues.append("SEM meta description")
    elif len(metadesc) > 155:
        issues.append(f"meta {len(metadesc)}c>155")
    if len(seo_title) > 60:
        issues.append(f"titulo {len(seo_title)}c>60")
    if not fm:
        issues.append("SEM imagem destacada")
    # título default (templated) = termina com separador + nome do site
    if re.search(r"[-|]\s*metaKosmos\s*$", seo_title, re.IGNORECASE):
        issues.append("titulo SEO default (sem custom)")
    return seo_title, metadesc, fm, ogimg, issues


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    posts = fetch_posts()
    print(f"[i] Total de posts publicados: {len(posts)}\n")
    detail = posts[:n] if n else posts
    for p in detail:
        t, m, fm, og, iss = evalp(p)
        print("---")
        print(f'{p["date"][:10]} | id {p["id"]} | {strip(p["title"]["rendered"])[:62]}')
        print(f'  slug: {p["slug"][:70]}')
        print(f'  SEO title ({len(t)}c): {t[:75]}')
        print(f'  meta ({len(m)}c): {m[:95] if m else "(VAZIA)"}')
        print(f'  imagem destacada: {"id "+str(fm) if fm else "NENHUMA"}')
        if iss:
            print("  [!] " + " | ".join(iss))
    # resumo geral
    no_meta = [p for p in posts if not (p.get("yoast_head_json") or {}).get("description")]
    long_meta = [p for p in posts if len((p.get("yoast_head_json") or {}).get("description") or "") > 155]
    long_title = [p for p in posts if len((p.get("yoast_head_json") or {}).get("title") or "") > 60]
    no_feat = [p for p in posts if not p.get("featured_media")]
    print("\n=== RESUMO (todos os posts) ===")
    print(f"sem meta description : {len(no_meta)}")
    print(f"meta > 155c          : {len(long_meta)}")
    print(f"titulo SEO > 60c     : {len(long_title)}")
    print(f"sem imagem destacada : {len(no_feat)}")
    if no_feat:
        print("  IDs sem imagem destacada:", ", ".join(str(p["id"]) for p in no_feat))
    if no_meta:
        print("  IDs sem meta description:", ", ".join(str(p["id"]) for p in no_meta[:40]))


if __name__ == "__main__":
    main()
