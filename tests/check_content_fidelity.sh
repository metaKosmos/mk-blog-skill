#!/usr/bin/env bash
# check_content_fidelity.sh — Prova que o CONTEUDO de escrita da skill hospedada
# e identico a V4 do Patrick (mesma qualidade de escrita por construcao).
#
# Compara, por checksum, os arquivos de referencia (style DNA, anti-IA, mKases,
# GEO/AEO, etc.) e mostra que so o SKILL.md mudou (e so na secao de PUBLICACAO).
#
# Uso:  bash tests/check_content_fidelity.sh <dir-da-skill-V4>
#   ex:  bash tests/check_content_fidelity.sh /caminho/para/blog_MK/extracted
#
# Onde <dir-da-skill-V4> contem SKILL.md + references/ da versao do Patrick.

set -e
V4_DIR="${1:-}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOSTED="$REPO/plugins/blog-mk/skills/blog-mk"

if [ -z "$V4_DIR" ] || [ ! -d "$V4_DIR/references" ]; then
  echo "Uso: bash tests/check_content_fidelity.sh <dir-da-skill-V4-com-references>"
  exit 2
fi

echo "== Fidelidade de conteudo: V4 (Patrick) vs hospedada =="
echo "V4:       $V4_DIR"
echo "hospedada:$HOSTED"
echo ""

DIFF=0
echo "--- referencias (.md) — devem ser IDENTICAS ---"
for f in "$V4_DIR"/references/*.md; do
  name="$(basename "$f")"
  h="$HOSTED/references/$name"
  if [ ! -f "$h" ]; then
    echo "  [X] FALTA na hospedada: $name"; DIFF=$((DIFF+1)); continue
  fi
  if cmp -s "$f" "$h"; then
    echo "  [OK] identico: $name"
  else
    echo "  [!] DIFERENTE: $name"; DIFF=$((DIFF+1))
  fi
done

echo ""
echo "--- SKILL.md — esperado MUDAR so na secao de publicacao ---"
if cmp -s "$V4_DIR/SKILL.md" "$HOSTED/SKILL.md"; then
  echo "  [OK] SKILL.md identico"
else
  echo "  [i] SKILL.md mudou. Linhas alteradas que NAO sejam de publicacao/versao:"
  # mostra um resumo do diff, sinalizando se toca os modos de escrita
  diff <(sed -n '1,/Modo 5/p' "$V4_DIR/SKILL.md") \
       <(sed -n '1,/Modo 5/p' "$HOSTED/SKILL.md") > /tmp/skill_writing_diff.txt 2>&1 || true
  if [ -s /tmp/skill_writing_diff.txt ]; then
    echo "      >>> ATENCAO: ha diferencas ANTES do Modo 5 (publicacao):"
    grep -E '^[<>]' /tmp/skill_writing_diff.txt | head -40
  else
    echo "      [OK] nenhuma diferenca nos modos de escrita (so a partir do Modo 5/publicacao)."
  fi
fi

echo ""
if [ "$DIFF" -eq 0 ]; then
  echo "RESULTADO: conteudo de escrita IDENTICO a V4. Qualidade preservada."
else
  echo "RESULTADO: $DIFF referencia(s) divergiram — investigar."
  exit 1
fi
