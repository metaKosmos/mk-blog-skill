#!/usr/bin/env bash
# setup.sh — Configuracao inicial (uma vez) da skill blog-mk.
#
# A skill usa so a biblioteca padrao do Python, entao nao instala dependencias.
# Este script: (1) confere que o Python 3 existe, (2) faz o login por email mK.
#
# Uso:  bash scripts/setup.sh

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "== blog-mk · setup =="

# 1) Python 3
if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
else
  echo "[X] Python 3 nao encontrado. Instale o Python 3 e rode de novo."
  exit 1
fi
echo "[OK] $($PY --version)"

# 2) dependencias (certifi — CA bundle para HTTPS no macOS python.org)
echo "[i] Instalando dependencias (certifi)..."
$PY -m pip install -q -r "$DIR/../requirements.txt" || {
  echo "[!] pip falhou. Tentando com --user..."
  $PY -m pip install -q --user -r "$DIR/../requirements.txt"
}

# 3) Liga auto-update do marketplace mk-skills (atualizacoes chegam sozinhas)
echo "[i] Ligando atualizacao automatica da skill..."
$PY - <<'PYEOF' || echo "[!] nao consegui ligar auto-update (segue assim mesmo; o aviso de versao cobre)."
import json, pathlib
p = pathlib.Path.home() / ".claude" / "settings.json"
d = json.loads(p.read_text()) if p.exists() else {}
mk = d.setdefault("extraKnownMarketplaces", {}).setdefault("mk-skills", {
    "source": {"source": "github", "repo": "metaKosmos/mk-blog-skill"}})
mk["autoUpdate"] = True
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(d, indent=2) + "\n")
print("[OK] auto-update ligado (mk-skills)")
PYEOF

# 4) Login por email mK
echo ""
echo "[i] Agora o login. Vai abrir o navegador — entre com sua conta @metakosmos.com.br."
$PY "$DIR/auth.py"

echo ""
echo "[OK] Pronto. Para publicar: python scripts/wp_publish.py <slug>"
