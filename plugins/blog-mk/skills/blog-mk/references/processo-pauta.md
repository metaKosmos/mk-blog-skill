# Processo de Criação de Pauta — metaKosmos

**Documento 1 da entrega.** Arquivo: `output/[slug]/pauta.md` (pasta dedicada por slug)

Fluxo do modo "Pautar" da skill blog-mk. A pauta é o documento de briefing que antecede e direciona a escrita do artigo. Também é gerada retroativamente nos modos Gerar/Reescrever/Humanizar.

---

## Inputs Obrigatórios (o que o usuário deve fornecer)

| Input | Descrição | Exemplo |
|-------|-----------|---------|
| **Keyword principal** | Termo principal que o artigo visa ranquear | "provador virtual" |
| **Pilar** | Qual dos 7 pilares de conteúdo (1-7) | Pilar 2 — Provador Virtual |
| **Etapa do funil** | TOFU, MOFU, BOFU ou Pain Point | MOFU |
| **Objetivo** | Conquistar KW / atualizar artigo / novo texto | Conquistar KW, novo texto |

## Inputs Opcionais (melhoram a pauta)

| Input | Descrição |
|-------|-----------|
| Quantidade de palavras desejada | **Mínimo 2000** (piso duro). Default: 2.500. Pedidos menores são rejeitados — skill avisa o usuário e escreve 2000+ |
| Keywords secundárias | Termos adicionais para cobrir |
| Direcionamento / ângulo específico | Ex: "declarar a morte das fotos estáticas" |
| Referências externas | URLs de artigos de referência ou concorrentes |
| Vertical específica | Moda, Beleza, Óculos, Móveis, Automotivo, Agências |
| Persona alvo | Persona primária (Lara default) + 1-2 secundárias. Variantes disponíveis em `manual-redacao.md`: Lara Beauty, Lara Casa & Decoração, Cláudio CFO, Camila CMO, Tiago Head Inovação |

---

## Fluxo de Criação da Pauta

### Etapa 1 — Análise de Contexto
Com base nos inputs, Claude deve:
1. Identificar o pilar e verificar keywords âncora e long tails em `pilares-conteudo.md`
2. Verificar se já existe artigo publicado sobre o tema em `blog-links.md`
3. Selecionar 2-3 mKases relevantes de `mkases.md`
4. Identificar dados numéricos proprietários disponíveis de `geo-aeo.md`
5. Mapear **mínimo 6-8 links internos** via `blog-links.md` e `sitemap-urls.md` (composição: 1 Pillar Page + 2 cross-pilar + 2 mKases + 1-2 LPs de produto). Aplicar **regra "first mention link"**: marca cliente citada → linkar para `/mkases/[slug]/`; solução mK citada → linkar para LP correspondente
6. Definir qual CTA e UTM padrão usar de `utm-tracking.md` (URL canônica: `https://form.respondi.app/L4NmIy24`)
7. Mapear **mínimo 5-7 mídias reais** da `media-library.md` (1 hero + 4-6 inline) — priorizar GIFs de produto mK quando solução é citada e imagens de mKase quando cliente é citado

### Etapa 2 — Definição da Estrutura H2
Com base no pilar, funil e ângulo, definir:
- Tipo de abertura (A: Dado+Dor, B: Provocação, C: Comparação de Investimento, D: Gancho de Atenção)
- **8-12 H2s** no corpo do artigo, cada um com ~200-300 palavras para atingir 2000+ (ver `blog-patterns.md`)
- H2s formulados como perguntas ou respostas diretas (regra GEO)
- Posição dos mKases no fluxo
- Posição do storytelling da Lara (ou persona escolhida)
- **Mínimo 10 perguntas do FAQ**, curtas e conversacionais, respondendo dúvidas reais de busca e LLMs

### Etapa 3 — Planejamento de Componentes Visuais
Definir para cada H2 quais componentes Gutenberg usar:
- Cards mKase (onde)
- Blockquotes de dado (quais dados merecem destaque)
- Stat boxes (números headline)
- Caixas de destaque (definições de conceitos proprietários)
- Comparativos em colunas (antes/depois, tradicional vs mK)
- **Pelo menos 2 imagens em coluna com texto ao lado** (mapeadas da `media-library.md`)
- CTAs: 1 banner (fim) + 1-2 inline (meio do artigo)

### Etapa 3 — Montagem do Documento de Pauta

---

## Template de Saída da Pauta

```markdown
# Pauta para Produção de Conteúdo — metaKosmos

## Título do Texto
[H1 otimizado: Keyword + pergunta ou dado. Max 70 caracteres]

## Meta Description
[150 caracteres com keyword principal e benefício. Dado numérico quando possível]

## Slug sugerido
[slug-com-keyword-principal]

---

## Palavra-chave Principal
**[Keyword]**: [Breve definição contextualizada — 1-2 frases]

## Palavras-chave Secundárias
- [KW secundária 1]
- [KW secundária 2]
- [KW secundária 3]

---

## Direcionamento
[2-3 frases explicando o ângulo editorial, argumento central e posicionamento da mK neste artigo]

## Observações
[Objetivo: conquistar KW / atualizar] | [Etapa do funil: TOFU/MOFU/BOFU] | [Tipo: novo texto / reescrita]

## Pilar
[Nome e número do pilar]

## Persona Alvo
**Primária:** [Lara, Lara Beauty, Lara Casa & Decoração, Cláudio CFO, Camila CMO, Tiago Head Inovação, Marketing Grandes Marcas, Agências, PME] — explicar como o artigo a atinge
**Secundárias:** [1-2 personas adicionais que devem se identificar com seções específicas]
**Mapa Persona × Pilar:** ver tabela em `manual-redacao.md` para default por pilar

## Quantidade de Palavras
[Número alvo — mínimo 2000, default 2500]

---

## Dados e mKases a Incluir

### Dados Proprietários mK
- [Dado 1 — ex: +94% conversão com visualizador 3D]
- [Dado 2]

### mKases Obrigatórios (mínimo 2)
- **[Marca 1]:** [Breve contexto + métrica principal]
- **[Marca 2]:** [Breve contexto + métrica principal]

### Fonte Externa Recomendada (max 2)
- [Fonte 1 — nome + tipo de dado que buscar]

---

## Links Internos a Incluir (mínimo 4, verificados via sitemap-urls.md)
- [Artigo 1 — título + URL] (mesmo pilar / Pillar Page)
- [Artigo 2 — título + URL] (mesmo pilar)
- [Artigo 3 — título + URL] (cross-pilar)
- [Artigo 4 — título + URL] (mKase)

## Mídias Reais Mapeadas (da media-library.md)
- **Hero:** [URL da imagem + alt-text sugerido]
- **Corpo (full-width):** [URL + contexto]
- **Corpo (coluna com texto):** [URL + lado — esq/dir]
- **Corpo (coluna com texto):** [URL + lado — esq/dir]

## CTA Principal
- **Tipo:** [banner / inline / final]
- **Texto sugerido:** [Ex: "Fale com um mentor da metaKosmos e descubra seu potencial imersivo"]
- **Destino com UTM:** [URL completa com UTMs]

---

## Referências Externas (para pesquisa do redator)
- [URL 1]
- [URL 2]

---

## Estrutura do Texto

### Título
[H1 completo]

### Tipo de Abertura
[A/B/C/D] — [Breve descrição]

### Conteúdo

- **Introdução (150-200 palavras):**
  [Direcionamento específico. Qual dor/dado abrir. Responder pergunta principal nos primeiros 150 palavras (regra GEO)]

- **H2: [Subtítulo 1]**
  **Direcionamento:** [O que cobrir, qual ângulo, qual dado/case usar]

- **H2: [Subtítulo 2]**
  **Direcionamento:** [Idem]

[... repetir para cada H2 ...]

- **H2: [Subtítulo N — CTA provocativo, NÃO "Conclusão"]**
  **Direcionamento:** [Fechamento com CTA + provocação estratégica]

- **H2: Perguntas frequentes sobre [tema]** (mínimo 10 perguntas)
  - H3: [Pergunta 1 — o que é / definição]
  - H3: [Pergunta 2 — como funciona]
  - H3: [Pergunta 3 — quanto custa / investimento]
  - H3: [Pergunta 4 — quais os benefícios / resultados]
  - H3: [Pergunta 5 — qual a diferença de X para Y]
  - H3: [Pergunta 6 — vale a pena]
  - H3: [Pergunta 7 — quanto tempo leva para implementar]
  - H3: [Pergunta 8 — para quem é / público alvo]
  - H3: [Pergunta 9 — como escolher / critérios]
  - H3: [Pergunta 10 — próximos passos / como começar]
  - [+ perguntas adicionais se fizerem sentido para o tema]
```

---

## Critérios de Qualidade da Pauta

A pauta está pronta quando:
- [ ] H1 formulado como pergunta ou resposta direta
- [ ] Meta description com keyword + dado numérico
- [ ] Slug alinhado com keyword principal
- [ ] Pilar e etapa do funil definidos
- [ ] Persona alvo identificada
- [ ] **Alvo mínimo 2000 palavras** definido
- [ ] Mínimo 2 mKases selecionados com métricas
- [ ] Mínimo 1 dado numérico proprietário identificado
- [ ] **Mínimo 4 links internos** mapeados (verificados via sitemap-urls.md)
- [ ] **Mídias reais da media-library.md** mapeadas para H2s principais
- [ ] **Pelo menos 2 imagens em coluna** com texto planejadas
- [ ] **Todos os links verificados em blog-links.md ou sitemap-urls.md** — zero URLs inventadas
- [ ] **Links não verificados sinalizados ao usuário** antes de prosseguir
- [ ] CTA definido com URL + UTM completo
- [ ] **8-12 H2s** com direcionamento claro
- [ ] Tipo de abertura definido (A/B/C/D)
- [ ] **Mínimo 10 perguntas de FAQ** esboçadas
- [ ] Abertura planejada para responder pergunta nos primeiros 150 palavras (GEO)
- [ ] Nenhum H2 "Conclusão" — último H2 é provocativo com CTA
- [ ] Componentes visuais Gutenberg planejados (cards, blockquotes, stat boxes, CTAs, caixas de destaque)
