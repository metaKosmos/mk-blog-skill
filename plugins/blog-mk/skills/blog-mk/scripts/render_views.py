#!/usr/bin/env python3
"""
render_views.py — Gera as views .md a partir do assets-db.json

Atualiza media-library.md e blog-links.md com um CATÁLOGO AUTO-GERADO do banco,
preservando todo o conteúdo curado manual (regras de uso, "first mention link", etc.).

O catálogo é inserido entre marcadores:
    <!-- AUTO-CATALOG-START -->
    ... conteúdo gerado (substituído a cada render) ...
    <!-- AUTO-CATALOG-END -->

Se os marcadores não existirem no arquivo, o bloco é anexado no final (sem tocar no resto).

Uso:
    python scripts/render_views.py
"""

import json
from datetime import datetime
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REFS = SKILL_DIR / "references"
DB_FILE = REFS / "assets-db.json"
MEDIA_MD = REFS / "media-library.md"
LINKS_MD = REFS / "blog-links.md"

START = "<!-- AUTO-CATALOG-START -->"
END = "<!-- AUTO-CATALOG-END -->"


def inject(md_path, block):
    """Insere/atualiza o bloco auto-gerado entre os marcadores, preservando o resto."""
    text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
    new_section = f"{START}\n{block}\n{END}"
    if START in text and END in text:
        pre = text.split(START)[0]
        post = text.split(END, 1)[1]
        text = pre + new_section + post
    else:
        text = text.rstrip() + "\n\n---\n\n" + new_section + "\n"
    md_path.write_text(text, encoding="utf-8")


def render_media(db):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    media = [m for m in db["media"] if m.get("in_wp", True)]

    lines = [
        f"## CATÁLOGO DE MÍDIAS (auto-gerado do banco em {ts})",
        "",
        f"Total no banco: **{len(media)} mídias** | "
        f"Avaliadas visualmente: **{db['meta'].get('media_evaluated_visual',0)}**",
        "",
        "> Este bloco é gerado por `render_views.py`. Não editar à mão (será sobrescrito).",
        "> Score: 0-5. `[V]` = avaliação visual minha, `[h]` = heurística por metadados.",
        "> Para reavaliar, rode `evaluate_media.py`.",
        "",
    ]

    CAT_TITLES = {
        "hero": "Hero / Capa (destaque após H1)",
        "gif_produto": "GIFs de produto / demos",
        "infografico": "Infográficos / dashboards",
        "depoimento": "Depoimentos / fotos de pessoas",
        "logo": "Logos / selos / parceiros",
        "inline": "Imagens inline (corpo do artigo)",
    }
    # Ordem de exibição
    for cat in ["hero", "gif_produto", "infografico", "depoimento", "inline", "logo"]:
        items = [m for m in media if (m.get("use_category") or m.get("auto_category")) == cat]
        # filtra por score: hero/gif/info/depoimento >= 3; inline/logo >= 4 (corta volume)
        min_score = 3 if cat in ("hero", "gif_produto", "infografico", "depoimento") else 4
        items = [m for m in items if (m.get("score") or 0) >= min_score]
        # ordena por score desc, depois data desc
        items.sort(key=lambda m: ((m.get("score") or 0), m.get("date") or ""), reverse=True)
        # limita volume por categoria
        limit = {"hero": 40, "gif_produto": 50, "infografico": 25,
                 "depoimento": 20, "inline": 60, "logo": 25}.get(cat, 40)
        items = items[:limit]
        if not items:
            continue
        lines.append(f"### {CAT_TITLES.get(cat, cat)} ({len(items)})")
        lines.append("")
        lines.append("| Score | Slug | Brand | Melhor uso | URL |")
        lines.append("|-------|------|-------|------------|-----|")
        for m in items:
            mark = "V" if m.get("eval_method") == "visual" else "h"
            score = f"{m.get('score','?')}{mark}"
            brand = m.get("brand") or ""
            best = (m.get("best_use") or "").replace("|", "/")[:70]
            lines.append(f"| {score} | {m.get('slug','')[:40]} | {brand} | {best} | {m.get('url','')} |")
        lines.append("")

    return "\n".join(lines)


def render_links(db):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    links = db["links"]

    lines = [
        f"## CATÁLOGO DE LINKS (auto-gerado do banco em {ts})",
        "",
        f"Total: **{len(links)} links** | "
        f"Última verificação de status: ver coluna HTTP",
        "",
        "> Bloco gerado por `render_views.py`. As REGRAS de linkagem (first mention link, "
        "mínimos por artigo) estão preservadas acima, na parte curada manual.",
        "",
    ]

    TYPE_TITLES = {
        "pillar": "Pillar Pages",
        "article": "Artigos satélite",
        "mkase": "mKases (/mkases/)",
        "lp": "LPs de produto (/mk-*/)",
    }
    for typ in ["pillar", "article", "lp", "mkase"]:
        items = [l for l in links if l.get("type") == typ]
        items.sort(key=lambda l: l.get("title") or l.get("url"))
        if not items:
            continue
        lines.append(f"### {TYPE_TITLES.get(typ, typ)} ({len(items)})")
        lines.append("")
        lines.append("| Título | URL | HTTP |")
        lines.append("|--------|-----|------|")
        for l in items:
            st = l.get("status_http")
            st_str = str(st) if st else "-"
            if st and st not in (200, 301, 302):
                st_str = f"**{st} MORTO**"
            title = (l.get("title") or "").replace("|", "/")[:55]
            lines.append(f"| {title} | {l.get('url','')} | {st_str} |")
        lines.append("")

    return "\n".join(lines)


def main():
    db = json.loads(DB_FILE.read_text(encoding="utf-8"))
    inject(MEDIA_MD, render_media(db))
    print(f"[OK] media-library.md atualizado ({db['meta'].get('total_media')} mídias no banco)")
    inject(LINKS_MD, render_links(db))
    print(f"[OK] blog-links.md atualizado ({db['meta'].get('total_links')} links no banco)")


if __name__ == "__main__":
    main()
