# Testes — V4 do Patrick vs versão hospedada

Estes testes provam que **hospedar a skill não mudou o que importa**: nem a
qualidade de escrita, nem o que é publicado no WordPress.

## Filosofia: onde está (e onde não está) o risco

A versão hospedada difere da V4 do Patrick em exatamente duas coisas:
1. **Como instala/atualiza** — vira plugin/marketplace no GitHub (não afeta o conteúdo).
2. **Como publica** — os scripts viram clientes finos que chamam um broker no GCP,
   em vez de ler `.env` e falar direto com o WordPress.

A **qualidade de escrita** (modos Pautar/Gerar/Reescrever/Humanizar/Auditar) depende
só do `SKILL.md` + das 14 referências. Logo, ela é preservada **por construção** —
não por sorte. O risco real está no **refactor da publicação**. Os dois testes abaixo
cobrem exatamente esses dois pontos.

## Teste A — Fidelidade de conteúdo (qualidade de escrita preservada)

`check_content_fidelity.sh` compara, por checksum, as referências e o SKILL.md da
versão hospedada contra a V4 do Patrick.

```bash
bash tests/check_content_fidelity.sh <dir-da-skill-V4-com-references>
```

Esperado:
- **15/15 referências byte-idênticas**.
- `SKILL.md` muda **só** no banner de checagem de versão (topo) e na seção de
  publicação (Modo 5). Os modos de escrita ficam intactos — o script destaca
  qualquer diferença antes do Modo 5 para revisão transparente.

> A V4 de referência vem do `blog_MK.zip` que o Patrick enviou (Drive). Aponte o
> script para a pasta onde ele foi extraído.

## Teste B — Equivalência de publicação (refactor fiel)

`test_publish_equivalence.py` dirige os **dois caminhos** com os mesmos inputs e os
mesmos stubs de rede, e exige que o payload final enviado a `POST /wp/v2/posts`
seja **idêntico**:

- Caminho A: `tests/v4_reference.py` (cópia fiel do `wp_publish.py` do Patrick).
- Caminho B: `scripts/wp_publish.py` (cliente) → `broker/wp.py` (`publish_post`).

A rede é neutralizada com stubs idênticos nos dois lados (auth JWT, resolução de
tags, lookup de featured image), então a comparação isola a **lógica de montagem do
post**: parse de metadados, strip de H1/hero, mapping pilar→categoria, tags, Yoast,
author, status.

```bash
python tests/test_publish_equivalence.py
```

Cobre 4 casos: artigo normal com hero, pillar page sem hero, pilar sem categoria
mapeada (fallback) e status `publish`. Roda **offline, sem credenciais**.

Esperado: `PASSOU: 4/4 — a versão hospedada publica idêntico a V4 do Patrick.`

## O que estes testes NÃO fazem

Não re-geram artigos com o modelo para "comparar a escrita". Isso testaria o
modelo, não o nosso refactor — e como as entradas de escrita são idênticas (Teste A),
a saída de qualidade é a mesma. Se você quiser mesmo um A/B de geração ao vivo,
gere um artigo com cada versão e rode o self-audit de 30 itens das
`references/anti-ia-rules.md`; o resultado tende a empatar porque o prompt é o mesmo.
