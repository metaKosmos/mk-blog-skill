#!/usr/bin/env python3
"""
wp_publish.py — Modo Publicar da skill blog-mk (cliente do broker).

Le a pasta output/[slug]/ (artigo.html + metadados.md), monta o payload do post
e envia ao BROKER (Cloud Run), que faz a autenticacao no WordPress, resolve
tags/categoria/featured image e cria o post como rascunho. As credenciais do
WordPress ficam no GCP Secret Manager — nunca nesta maquina.

Antes de publicar, faca login uma vez:
    python scripts/auth.py

Uso:
    python scripts/wp_publish.py --list                 # lista slugs disponiveis
    python scripts/wp_publish.py <slug> --dry-run        # monta o payload sem publicar
    python scripts/wp_publish.py <slug>                  # publica como rascunho
    python scripts/wp_publish.py <slug> --status publish # publica direto (cuidado!)
    python scripts/wp_publish.py <slug> --update 4701    # atualiza post existente

A parte de ESCRITA do artigo e do Claude lendo o SKILL.md. Este script so publica.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from broker_client import publish as broker_publish, BrokerError  # noqa: E402

# === Config local ===
SKILL_DIR = Path(__file__).resolve().parent.parent
# A pasta output/ fica relativa ao diretorio de trabalho do usuario (onde o Claude
# gera os artigos). Como plugin, o SKILL_DIR e read-only — por isso NAO usamos
# SKILL_DIR/output. Override: env BLOG_MK_OUTPUT_DIR ou flag --dir.
OUTPUT_DIR = Path(os.environ.get("BLOG_MK_OUTPUT_DIR", "output"))


# === Logging ===
def log(msg, level="info"):
    prefix = {"info": "[i]", "ok": "[OK]", "warn": "[!]", "err": "[X]"}.get(level, "[i]")
    print(f"{prefix} {msg}")


# === Parser metadados.md (local, sem credencial) ===
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
    keyword = keyword_raw.split("/")[0].strip() if keyword_raw else ""

    tags_str = extract(r"\*\*Tags:\*\*\s*(.+)")
    tags = [t.strip() for t in (tags_str or "").split(",") if t.strip()] if tags_str else []

    pilar_str = extract(r"\*\*Pilar:\*\*\s*(\d+)")
    pilar = int(pilar_str) if pilar_str else None

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


# === Hero image (local) ===
def extract_hero_image_url(html_path):
    html = html_path.read_text(encoding="utf-8")
    m = re.search(r'<img\s+[^>]*?src=["\'](https?://[^"\']+)["\']', html)
    return m.group(1) if m else None


# === Strip H1 e Hero do conteudo (local) ===
def strip_h1_and_hero(html):
    """
    Remove o primeiro <h1> e a primeira <img> (hero) do topo do artigo.
    O WordPress renderiza title + featured_media separadamente; manter no
    conteudo causa duplicacao no front-end. Retorna (html, n_h1, n_img).
    """
    result = html

    h1_pattern = re.compile(
        r'<!--\s*wp:heading\s*\{[^\n]*?"level"\s*:\s*1[^\n]*?-->\s*'
        r'<h1[^>]*>.*?</h1>\s*'
        r'<!--\s*/wp:heading\s*-->\s*\n?',
        re.DOTALL,
    )
    result, n_h1 = h1_pattern.subn('', result, count=1)

    first_paragraph = result.find('<!-- wp:paragraph')
    first_image = result.find('<!-- wp:image')
    n_img = 0
    if first_image != -1 and (first_paragraph == -1 or first_image < first_paragraph):
        img_pattern = re.compile(
            r'<!--\s*wp:image\s+[^\n]*?-->\s*'
            r'<figure[^>]*>.*?</figure>\s*'
            r'<!--\s*/wp:image\s*-->\s*\n?',
            re.DOTALL,
        )
        result, n_img = img_pattern.subn('', result, count=1)

    return result, n_h1, n_img


def build_payload(slug, status, update_id):
    """Le output/[slug]/ e monta o payload para o broker (sem tocar rede)."""
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

    meta = parse_metadados(md_path)

    log(f"Slug: {meta['slug']}")
    log(f"Titulo SEO ({len(meta['title_seo'])}c): {meta['title_seo']}")
    log(f"Meta Desc ({len(meta['meta_description'])}c)")
    log(f"Keyword: {meta['keyword']}")
    log(f"Pilar: {meta['pilar']}  |  Pillar Page (cornerstone): {meta['is_pillar_page']}")
    log(f"Tags planejadas: {len(meta['tags'])}")

    if len(meta["title_seo"]) > 60:
        log(f"Titulo SEO acima de 60c ({len(meta['title_seo'])}c)", "warn")
    if len(meta["meta_description"]) > 155:
        log(f"Meta Description acima de 155c ({len(meta['meta_description'])}c)", "warn")

    hero_url = extract_hero_image_url(html_path)
    if hero_url:
        log(f"Hero image: {hero_url[:90]}")

    html_raw = html_path.read_text(encoding="utf-8")
    html_content, removed_h1, removed_img = strip_h1_and_hero(html_raw)
    log(f"Conteudo: {len(html_raw)} -> {len(html_content)} chars (apos strip H1 + hero)")
    if removed_h1:
        log("  - H1 do topo removido (WP renderiza o title)", "ok")
    if removed_img:
        log("  - Hero do topo removida (WP renderiza o featured_media)", "ok")

    return {
        "title": meta["title_seo"] or meta["slug"],
        "slug": meta["slug"],
        "status": status,
        "content": html_content,
        "tag_names": meta["tags"],
        "pilar": meta["pilar"],
        "is_pillar_page": meta["is_pillar_page"],
        "hero_url": hero_url,
        "yoast": {
            "title": meta["title_seo"],
            "metadesc": meta["meta_description"],
            "focuskw": meta["keyword"],
            "is_cornerstone": meta["is_pillar_page"],
        },
        "update_id": update_id,
    }


def run_publish(slug, status="draft", dry_run=False, update_id=None):
    payload = build_payload(slug, status, update_id)

    if dry_run:
        log("=== DRY RUN — payload pronto (nao enviado ao broker) ===", "warn")
        preview = {k: v for k, v in payload.items() if k != "content"}
        preview["content"] = f"<{len(payload['content'])} chars>"
        print(json.dumps(preview, ensure_ascii=False, indent=2))
        return

    log(f"Enviando ao broker para publicar como '{status}'...")
    try:
        resp = broker_publish(payload)
    except BrokerError as e:
        log(str(e), "err")
        sys.exit(1)

    log(f"Post {'atualizado' if update_id else 'criado'}! ID {resp.get('post_id')}", "ok")
    log(f"Status: {resp.get('status')}", "ok")
    if resp.get("url"):
        log(f"Link: {resp['url']}", "ok")
    if resp.get("edit_url"):
        log(f"Editor: {resp['edit_url']}", "ok")
    if "yoast_persisted" in resp:
        log(f"Yoast fields persistidos: {resp['yoast_persisted']}", "ok")


def main():
    p = argparse.ArgumentParser(
        description="Publica artigo do blog-mk no WordPress via broker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("slug", nargs="?", help="Slug da pasta em output/")
    p.add_argument("--status", choices=["draft", "publish", "pending"], default="draft",
                   help="Status do post (default: draft)")
    p.add_argument("--dry-run", action="store_true",
                   help="Monta o payload sem enviar ao broker")
    p.add_argument("--list", action="store_true",
                   help="Lista slugs disponiveis em output/")
    p.add_argument("--update", type=int, metavar="POST_ID",
                   help="Atualiza post existente (em vez de criar novo)")
    p.add_argument("--dir", metavar="PATH",
                   help="Pasta onde estao os artigos (default: ./output)")
    args = p.parse_args()

    if args.dir:
        global OUTPUT_DIR
        OUTPUT_DIR = Path(args.dir)

    if args.list:
        if not OUTPUT_DIR.exists():
            log(f"output/ nao existe ({OUTPUT_DIR})", "err")
            return
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

    run_publish(args.slug, status=args.status, dry_run=args.dry_run, update_id=args.update)


if __name__ == "__main__":
    main()
