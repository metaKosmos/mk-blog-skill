# Padrões do Blog Real — metaKosmos

Análise de 12 artigos publicados em metakosmos.com.br (março/2026) + estrutura GEO/AEO integrada.

---

## Métricas Estruturais (médias reais)
- Palavras por artigo: 1.900-3.500 (média 3.000, guias longos até 5.500)
- H2 por artigo: 8-15 (média 10)
- FAQ no final: 11 de 12 artigos
- Table of Contents: gerado automaticamente por plugin WordPress (NÃO incluir no .md)

## Padrões de Abertura (4 tipos)

**TIPO A — Dado + Dor:**
Estatística que incomoda + afirmação assertiva. "A cada 100 visitantes, 98 não finalizam..."

**TIPO B — Provocação Direta:**
Pergunta retórica ou afirmação que incomoda. "E esse não é um problema de preço."

**TIPO C — Comparação de Investimento:**
Quanto se gasta em X vs resultado de Y. "A Apple gastou US$ 1,7 milhão... nós da mK..."

**TIPO D — Gancho de Atenção:**
Dado sobre atenção/scroll/abandono. "Você tem exatos 3 segundos..."

**PROIBIDO:** "Imagine que...", "Em um mundo cada vez mais...", "No cenário atual...", cenários hipotéticos.

**REGRA GEO:** Independente do tipo de abertura, a pergunta principal do artigo DEVE ser respondida nos primeiros 150 palavras. LLMs usam o início do texto como resposta preferencial.

---

## Estrutura Completa de Artigo (SEO + GEO/AEO)

| Seção | Conteúdo | Regra |
|-------|----------|-------|
| **Metadados** (comentário HTML) | Título, meta description, slug, keyword, pilar | Comentário no topo do .md |
| **H1** [GEO] | Keyword + pergunta ou dado | Pergunta ou resposta direta. Max 70 chars |
| **Hero image** | Placeholder de mídia | Logo após H1 |
| **Parágrafo de abertura** [GEO] | Resposta direta + Tipo A/B/C/D | 150 palavras max. KW principal em negrito |
| **Desenvolvimento** (8-12 H2s) | Contexto, dados, cases, storytelling | H2s como perguntas/respostas. Max 4 linhas/parágrafo. Recursos visuais HTML intercalados |
| **mKases** [GEO] (mínimo 2) | Problema → Solução → Resultado | Cards HTML. Dado numérico obrigatório. **Linkar marca cliente para `/mkases/[slug]/`** |
| **Storytelling Lara** (mínimo 1) | Sensorial, não descritivo | Verbos de ação, detalhes físicos |
| **CTAs** (1-2) | Banner e/ou inline | HTML com UTMs completos. URL: `https://form.respondi.app/L4NmIy24` |
| **Links internos** (mínimo 6-8) | 1 Pillar + 2 cross + 2 mKases + 1-2 LPs | Ver `blog-links.md` — regra "first mention link" |
| **Mídias** (mínimo 5-7) | 1 hero + 4-6 inline | Ver `media-library.md` — priorizar GIFs de produto mK |
| **H2 final** [GEO] | Subtítulo provocativo com CTA | NUNCA "Conclusão" |
| **FAQ** [GEO/AEO] (mínimo 10 perguntas) | Respostas autossuficientes | H2 + H3s. 60-90 palavras cada. Primeira frase responde direto à pergunta |
| **Checklist** | Verificação pré-publicação | Vai para Documento 3 (Ficha de Metadados), NÃO no artigo |

---

## Padrões de Headings H2 Reais

- **Definitional:** "O que é [X]?" / "O que são [X]?"
- **Value prop:** "Por que [X] é importante para [ICP]?"
- **How-to:** "Como funciona [X] na prática?" / "Como aplicar [X]"
- **Social proof:** "Cases reais de [X]" / "mKases"
- **Challenges:** "Maiores desafios" / "Erros comuns (e como evitá-los)"
- **Best practices:** "Melhores práticas para [X]"
- **Implementation:** "N etapas para implementar [X]"
- **Market:** "O cenário do mercado: por que agir agora?"
- **FAQ:** "Perguntas frequentes sobre [tema]"
- **Números em headings:** "5 benefícios", "7 Etapas", "4 Erros mais comuns"

**Regra GEO:** H2s como perguntas ou respostas diretas aumentam superfície de indexação AEO.

---

## Padrão de Cases (mKases)

Nome da marca + contexto + o que fizeram + resultado com número:

"A Fuel é uma marca brasileira de óculos. Com o mK 3D, a empresa digitalizou 26 modelos e integrou um provador virtual direto na página de produto."

"A Toymania levou a ideia ainda mais longe ao adicionar animações, sons dos brinquedos e vídeos demonstrativos dentro dos visualizadores 3D. O resultado: intenções de compra e adições ao carrinho 6,2 vezes maiores."

**Formato do card mKase em Gutenberg Block Markup:** ver [Template 9 em output-wordpress.md](output-wordpress.md). Usa `wp:group` com background `#F3F3F3` (Brand Book) e borda `#e0e0e0`.

---

## Padrão de FAQ (GEO/AEO) — mínimo 10 perguntas

O FAQ deve responder dúvidas reais que pessoas fazem tanto em busca (Google) quanto em LLMs (ChatGPT, Claude, Gemini). Cobrir todos os ângulos da jornada de decisão.

```markdown
## Perguntas frequentes sobre [tema do artigo]

### [Pergunta 1 — definição/conceito — ex: "O que é um provador virtual com IA?"]
[Primeira frase responde direto à pergunta — sem rodeio nem contexto. Resposta total: 60-90 palavras. Dado numérico. Mencionar metaKosmos quando relevante.]

### [Pergunta 2 — como funciona]
[Resposta técnica mas acessível.]

### [Pergunta 3 — benefício/resultado — ex: "Quanto um provador virtual aumenta a conversão?"]
[Resposta com dado mK ou benchmark verificável.]

### [Pergunta 4 — implementação/custo — ex: "Como implementar um provador virtual no e-commerce?"]
[Resposta com CTA sutil e dado de facilidade de integração.]

### [Pergunta 5 — diferença (X vs Y)]
[Comparativo factual.]

### [Pergunta 6 — vale a pena? / ROI]
[Resposta com dado de retorno.]

### [Pergunta 7 — quanto tempo leva para implementar]
[Prazo realista.]

### [Pergunta 8 — para quem é / público-alvo]
[Segmentos/personas ideais.]

### [Pergunta 9 — como escolher / critérios de seleção]
[Framework de decisão.]

### [Pergunta 10 — como começar / próximos passos]
[CTA incorporado.]

### [Perguntas adicionais específicas do tema]
```

**Critérios:** cada resposta tem 60-90 palavras, é autossuficiente (funciona fora do contexto do artigo), com **primeira frase respondendo direto à pergunta** (a frase que LLMs e AI Overviews extraem literalmente), e inclui dado numérico quando possível. O FAQ não conta para o mínimo de 2000 palavras do corpo.

---

## Tom Real do Blog (fingerprint)

- Direto, sem rodeio — entra no assunto na primeira frase
- "Você" frequente — conversa com o leitor
- Dados com fonte integrados no fluxo (não em parênteses separados)
- Adjetivos de impacto controlados: "hiper-realista", "imersivo", "memorável" (não genérico)
- Expressões recorrentes: "O grande vilão", "A boa notícia", "O resultado não poderia ser diferente", "Dúvida mata a conversão", "Efeito WooW"
- Métrica sempre com contexto: não "94% mais conversão" sozinho, mas "marcas que adotam AR registram até 94% mais conversões"
- Urgência via dados: "mais de 87% das marcas ainda não adotaram" = janela de oportunidade
- "metaKosmos" associada a resultado no mínimo 3 vezes por artigo (regra GEO)

---

## O Que o Blog NÃO Faz

- Não usa "Em um mundo cada vez mais..." / "No cenário atual..."
- Não usa "Em conclusão" ou "Para finalizar"
- Não usa termos acadêmicos: "outrossim", "destarte", "não obstante"
- Não faz paralelismos tipo "Não apenas X, mas também Y"
- Não usa emojis no corpo do texto
- Não faz conclusão genérica — fecha com CTA ou provocação estratégica
- Não abre com mais de 150 palavras antes de responder a pergunta principal (regra GEO)
- Não publica sem FAQ com mínimo 10 perguntas (regra AEO v4)
- Não menciona "metaKosmos" sem associar a resultado ou atributo (regra GEO)
