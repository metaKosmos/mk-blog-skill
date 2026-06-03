#!/usr/bin/env python3
"""
evaluate_media.py — Avaliação visual híbrida das mídias do banco

A avaliação VISUAL (ver a imagem e dar nota) é feita por mim (Claude) numa sessão.
Este script faz a parte mecânica:

  --prepare [N]   Seleciona N mídias prioritárias ainda não avaliadas visualmente
                  (heroes, gifs de produto, infográficos), baixa os arquivos para
                  uma pasta local e gera _eval_queue.json com a fila.
                  Eu então uso o Read tool em cada imagem, vejo, e escrevo as
                  avaliações em _eval_results.json.

  --save          Lê _eval_results.json e grava as avaliações no assets-db.json
                  (score, use_category, theme_tags, best_use, eval_method="visual").

Prioridade de seleção: heroes > gif_produto > infografico > depoimento, ordenado por
score heurístico desc e data desc, apenas PNG/JPG/WEBP (formatos que o Read renderiza).

Uso:
    python scripts/evaluate_media.py --prepare 10
    # (eu vejo as imagens em _eval_media/ e escrevo _eval_results.json)
    python scripts/evaluate_media.py --save
"""

import argparse
import json
import urllib.request
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REFS = SKILL_DIR / "references"
DB_FILE = REFS / "assets-db.json"
EVAL_DIR = REFS / "_eval_media"
QUEUE_FILE = REFS / "_eval_queue.json"
RESULTS_FILE = REFS / "_eval_results.json"
USER_AGENT = "blog-mk-skill/1.0"

VIEWABLE = ("image/png", "image/jpeg", "image/webp")
PRIORITY = {"hero": 0, "gif_produto": 1, "infografico": 2, "depoimento": 3, "inline": 4, "logo": 5}


def load_db():
    return json.loads(DB_FILE.read_text(encoding="utf-8"))


def save_db(db):
    DB_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def prepare(n):
    db = load_db()
    # candidatos: in_wp, não avaliados visualmente, formato visualizável
    cands = [
        m for m in db["media"]
        if m.get("in_wp", True)
        and m.get("eval_method") != "visual"
        and m.get("mime") in VIEWABLE
    ]
    cands.sort(key=lambda m: (
        PRIORITY.get(m.get("auto_category"), 9),
        -(m.get("score") or 0),
        m.get("date") or "",
    ))
    batch = cands[:n]

    EVAL_DIR.mkdir(exist_ok=True)
    queue = []
    for i, m in enumerate(batch):
        ext = ".png" if m["mime"] == "image/png" else (".webp" if m["mime"] == "image/webp" else ".jpg")
        local = EVAL_DIR / f"{i:02d}_{m['id']}{ext}"
        try:
            req = urllib.request.Request(m["url"], headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as r:
                local.write_bytes(r.read())
            queue.append({
                "id": m["id"], "slug": m["slug"], "url": m["url"],
                "auto_category": m["auto_category"], "score_heuristic": m["score"],
                "local_file": str(local),
            })
        except Exception as e:
            print(f"  falha ao baixar {m['id']}: {e}")

    QUEUE_FILE.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")
    # Template de resultados para eu preencher
    template = [{
        "id": q["id"], "slug": q["slug"],
        "score": None, "use_category": "", "theme_tags": [], "best_use": ""
    } for q in queue]
    RESULTS_FILE.write_text(json.dumps(template, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[OK] {len(queue)} mídias baixadas em {EVAL_DIR}")
    print(f"[OK] Fila: {QUEUE_FILE}")
    print(f"[OK] Template de resultados: {RESULTS_FILE}")
    print("\nArquivos para avaliar:")
    for q in queue:
        print(f"  {q['local_file']}  (slug: {q['slug']}, cat: {q['auto_category']})")


def save():
    db = load_db()
    results = json.loads(RESULTS_FILE.read_text(encoding="utf-8"))
    by_id = {m["id"]: m for m in db["media"]}
    applied = 0
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for r in results:
        if r.get("score") is None:
            continue
        m = by_id.get(r["id"])
        if not m:
            continue
        m["score"] = r["score"]
        m["use_category"] = r.get("use_category") or m.get("auto_category")
        m["theme_tags"] = r.get("theme_tags", [])
        m["best_use"] = r.get("best_use", "")
        m["eval_method"] = "visual"
        m["evaluated_at"] = today
        applied += 1
    db["meta"]["media_evaluated_visual"] = sum(1 for m in db["media"] if m.get("eval_method") == "visual")
    save_db(db)
    print(f"[OK] {applied} avaliações visuais aplicadas no banco")
    print(f"[OK] Total avaliado visualmente: {db['meta']['media_evaluated_visual']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prepare", type=int, metavar="N", help="Prepara N mídias para avaliação")
    ap.add_argument("--save", action="store_true", help="Aplica _eval_results.json no banco")
    args = ap.parse_args()
    if args.prepare:
        prepare(args.prepare)
    elif args.save:
        save()
    else:
        ap.error("use --prepare N ou --save")


if __name__ == "__main__":
    main()
