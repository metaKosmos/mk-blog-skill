#!/usr/bin/env python3
"""
update_seo.py — Corrige metadados SEO (Yoast) de posts ja publicados (cliente do broker).

Le references/_seo_updates.json (lista de {id, title?, metadesc?, featured_media?, why?})
e envia o batch ao BROKER, que aplica via WordPress REST API. As credenciais ficam
no GCP — este script nao toca o WordPress diretamente.

Login antes de usar:
    python scripts/auth.py

Uso:
    python scripts/update_seo.py --dry-run   # mostra o que seria atualizado
    python scripts/update_seo.py             # aplica via broker
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from broker_client import update_seo as broker_update_seo, BrokerError  # noqa: E402

SKILL_DIR = Path(__file__).resolve().parent.parent
UPDATES_FILE = SKILL_DIR / "references" / "_seo_updates.json"


def log(msg, level="info"):
    prefix = {"info": "[i]", "ok": "[OK]", "warn": "[!]", "err": "[X]"}.get(level, "[i]")
    print(prefix, msg)


def main():
    ap = argparse.ArgumentParser(description="Atualiza SEO/Yoast de posts via broker")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not UPDATES_FILE.exists():
        log(f"{UPDATES_FILE} nao existe. Gere a lista de updates primeiro.", "err")
        sys.exit(1)

    updates = json.loads(UPDATES_FILE.read_text(encoding="utf-8"))
    log(f"{len(updates)} posts para atualizar (dry-run={args.dry_run})")

    for u in updates:
        changed = []
        if "title" in u:
            changed.append(f'title({len(u["title"])}c)')
        if "metadesc" in u:
            changed.append(f'meta({len(u["metadesc"])}c)')
        if "featured_media" in u:
            changed.append(f'featured={u["featured_media"]}')
        log(f'--- post {u.get("id")} | {u.get("why","")} | {", ".join(changed)}')

    if args.dry_run:
        print(json.dumps(updates, ensure_ascii=False, indent=2))
        return

    try:
        resp = broker_update_seo(updates)
    except BrokerError as e:
        log(str(e), "err")
        sys.exit(1)

    for r in resp.get("results", []):
        ok = r.get("ok")
        log(f"  post {r.get('id')}: {'OK' if ok else 'ERRO'} {r.get('detail','')}",
            "ok" if ok else "err")


if __name__ == "__main__":
    main()
