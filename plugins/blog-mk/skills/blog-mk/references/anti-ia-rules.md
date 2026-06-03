# Regras Anti-IA + Checklist Unificado de Qualidade

## 25 PADRÕES DE IA — TOLERÂNCIA ZERO

Se qualquer item aparecer no artigo final, está reprovado.

### Grupo 1: Conteúdo
1. **Inflação de importância** — "momento pivotal", "marca uma mudança", "legado indelével". Se importa, mostre com dados.
2. **Linguagem promocional** — "deslumbrante", "vibrante", "renomado". Descreva com precisão.
3. **Atribuições vagas** — "Especialistas argumentam", "Observadores notam". Nomeie a fonte ou corte.
4. **Seções formuláicas** — Não adicione "Desafios e Perspectivas Futuras" mecanicamente.

### Grupo 2: Linguagem
5. **Vocabulário de IA** — Substituir por palavras normais:
   - "Adicionalmente" → "Também" / "E"
   - "panorama" → "cenário" / "situação"
   - "alavancar" → "usar" / "impulsionar"
   - "sinergia" → "colaboração"
   - "holístico" → "completo"
   - "multifacetado" → remover
   - "intrincado" → "complexo"
6. **Cópulas disfarçadas** — "serve como" = "é". "ostenta" = "tem". Simplifique.
7. **Paralelismos negativos** — Inclui DOIS moldes que precisam ser policiados:
   - **"Não apenas X, mas também Y"** → diga X e Y diretamente.
   - **"Não é X, é Y" / "Não é X. É Y." / "A pergunta não é X, é Y"** → cliché de IA. **Máximo 2 ocorrências no artigo inteiro** (incluindo FAQ). Reescrever com afirmação direta: em vez de "Não é projeto de seis meses. É ativação em semanas." use "Ativação em semanas, não em meses." ou simplesmente "Ativação em semanas." Variações que contam para o limite: "Não é X nem Y", "X não é Y, é Z", "A questão não é X, é Y".
8. **Regra do três** — Não force grupos de três. Se são 2 ou 4, mantenha.
9. **Variação elegante** — Escolha uma palavra e mantenha. Não alterne sinônimos sem motivo.

### Grupo 3: Estilo
10. **Travessão (em dash —) PROIBIDO (v4.2)** — **Zero em dashes no artigo inteiro**, incluindo corpo e FAQ. Substituir SEMPRE por: vírgula simples, parênteses, dois pontos, ponto + nova frase, ou reestruturação. Aplica a alt-text também (não usar em alt= de imagens). Verificação programática obrigatória no Passo 2.5 — qualquer ocorrência bloqueia a entrega.
11. **Negrito estratégico** — Usar negrito ativamente para destaques escaneáveis. **Meta: 2-4 trechos em negrito por seção H2** (não por parágrafo). Sempre negritar: dados numéricos (ex: **98 de cada 100**), conceitos-chave mK (ex: **Your 3D Everywhere**), provocações fortes (ex: **Dúvida mata conversão**), nomes de produtos mK no primeiro uso da seção (ex: **mK 3D Shop**), e a afirmação-resumo mais importante de cada parágrafo denso. Evitar negritar parágrafos inteiros — só os trechos-chave.
12. **Listas com mini-headers** — Bullets simples, sem título em cada item.

### Grupo 4: Comunicação
13. **Artefatos de chatbot** — "Espero que isso ajude", "Certamente!"
14. **Tom bajulador** — Não seja excessivamente positivo
15. **Conclusões genéricas + Frases-conclusão PROIBIDAS (v4.2)** — Nada de "futuros brilhantes", "possibilidades empolgantes" ou variantes. E **proibidas estas aberturas de fechamento**: "Em conclusão...", "Para concluir...", "Concluindo...", "Em resumo...", "Resumindo...", "Em suma...", "Por fim...", "Para finalizar...", "Em última análise...", "Considerando tudo...", "Em síntese...". O fechamento do artigo é um H2 provocativo + CTA, nunca uma frase-conclusão genérica. Verificação programática obrigatória no Passo 2.5 — qualquer ocorrência destas aberturas bloqueia a entrega.
16. **Hedging excessivo** — Corte "potencialmente", "possivelmente", "talvez" quando pode ser direto
17. **Frases de preenchimento** — "A fim de" → "Para". "Neste momento" → "Agora". "tem a capacidade de" → "pode"
18. **Transições formuláicas** — Elimine "Além disso", "Por outro lado", "Em resumo", "Diante disso". Use transições orgânicas.
19. **Advérbios em -mente** — Corte "particularmente", "essencialmente", "fundamentalmente", "drasticamente", "significativamente"
20. **Abertura com gerúndio** — Não comece frases com "Considerando...", "Analisando...", "Observando..."
21. **Perguntas retóricas forçadas** — Não use "Mas afinal, o que isso significa?" como transição
22. **Linguagem de impacto** — Corte "transformador", "revolucionário", "disruptivo" a menos que literalmente verdade
23. **Metáforas batidas** — "navegar pelas águas", "abrir portas", "pavimentar o caminho" → linguagem direta
24. **Preâmbulos** — Não comece com "Em um mundo cada vez mais..." ou "No cenário atual..." — entre direto
25. **Frases curtas sem conector + Anáfora staccato (v4.2 — REFORÇADO)** — Tique de IA travestido de "ritmo". Duas regras agora vigoram:
   - **(a) Anáfora staccato:** Sequência de 3+ frases curtas consecutivas começando com a mesma palavra ou estrutura. Limite: zero.
   - **(b) Frases curtas sem conector (NOVO v4.2):** Duas ou mais frases curtas (≤10 palavras cada) consecutivas dentro do mesmo parágrafo sem conectivo entre elas configura "ponto seco". **Limite: máximo 1 frase curta isolada por parágrafo** (que conta como recurso retórico de impacto). Para ideias paralelas, converter em frase única com lista ou intercalar conectivo (ainda que coloquial: "e", "mas", "porque", "porque sim", "afinal").
   - **✗ Errado:** "Não é preço. Não é frete. Não é tráfego." | "Foto estática não responde. Tabela de medidas também não. Vídeo no Reels muito menos." | "Conversão sobe. Devolução cai. Ticket médio segue."
   - **✓ Certo:** "Não é preço, frete nem tráfego." | "Foto estática não responde a essas perguntas, e tabela de medidas ou vídeo no Reels também não." | "Conversão sobe, devolução cai e ticket médio segue."
   - **Exceção liberada:** uma frase-parágrafo isolada de 4-8 palavras por artigo, como recurso retórico de impacto (ex: "Frictionless por design.", "Não foi sorte.", "From Good to WooW.").

### Aberturas e Frases PROIBIDAS
- "Imagine que..." / "Imagine um mundo onde..."
- "Parece ficção científica?" / "Pode parecer futurista, mas..." / "Parece distante?"
- "Neste artigo, vamos..." / meta-comentários sobre o próprio texto
- "A analogia mais simples:" / declarar a analogia antes de fazê-la
- "Pense num..." / "Pense em..." — fazer a analogia diretamente
- "Em um mundo cada vez mais..." / "No cenário atual..."

---

## CHECKLIST UNIFICADO DE QUALIDADE (30 itens)

Artigo reprovado se faltar qualquer item marcado como [BLOQUEADOR]. Demais itens são fortemente recomendados.

### Conteúdo e Estrutura
- [ ] [BLOQUEADOR] Keyword principal no primeiro parágrafo, em negrito
- [ ] [BLOQUEADOR] Abertura com dor/dado (NÃO "Imagine...", NÃO "Pense num...")
- [ ] [BLOQUEADOR] Pergunta principal respondida nos primeiros 150 palavras (GEO)
- [ ] [BLOQUEADOR] Mínimo 2 mKases com métricas reais
- [ ] [BLOQUEADOR] Pelo menos 1 dado numérico verificável com fonte (GEO)
- [ ] [BLOQUEADOR] **Mínimo 2000 palavras** no artigo (sem contar FAQ)
- [ ] Mínimo 1 storytelling SENSORIAL (Lara com detalhes físicos/emocionais, NÃO descritivo)
- [ ] Estatísticas distribuídas no fluxo (NÃO em seção isolada)
- [ ] 8-12 H2s seguindo padrões reais do blog
- [ ] H2s formulados como perguntas ou respostas diretas (GEO)

### FAQ e GEO/AEO
- [ ] [BLOQUEADOR] **FAQ com mínimo 10 perguntas** no final
- [ ] [BLOQUEADOR] Respostas do FAQ de 60-90 palavras com primeira frase autossuficiente respondendo direto à pergunta
- [ ] FAQ responde dúvidas reais de busca (o que é, como funciona, quanto custa, vale a pena, etc.)
- [ ] "metaKosmos" associada a resultado no mínimo 3 vezes (GEO)
- [ ] Conceitos proprietários mK definidos de forma factual e citável (GEO)
- [ ] Zero afirmações tipo "pode ajudar" ou "segundo especialistas" sem dado (GEO)
- [ ] Max 2 fontes externas reconhecidas com link (GEO)

### CTA e Links
- [ ] [BLOQUEADOR] CTA com convite mK (não "Clique aqui")
- [ ] [BLOQUEADOR] Todos os links internos com UTMs completos + `&amp;` encoding
- [ ] [BLOQUEADOR] **Mínimo 6-8 links internos** (atualizado v4.1): 1 Pillar Page + 2 cross-pilar + 2 mKases + 1-2 LPs de produto
- [ ] Regra "first mention link" aplicada: marca cliente → `/mkases/[slug]/`; solução mK → LP
- [ ] CTA principal aponta para `https://form.respondi.app/L4NmIy24`
- [ ] 1-2 CTAs com UTM (banner e/ou inline)
- [ ] Link obrigatório para Pillar Page do pilar
- [ ] [BLOQUEADOR] Todos os links verificados em sitemap-urls.md / blog-links.md — zero links inventados

### Formato Gutenberg e Componentes Visuais
- [ ] Artigo em Gutenberg Block Markup (arquivo `.html`)
- [ ] Artigo SEM metadados inline (vão para doc 3: Ficha de Metadados)
- [ ] Artigo SEM Table of Contents (plugin WordPress gera)
- [ ] Artigo SEM checklist inline (vai para doc 3)
- [ ] Regra de aninhamento: blocos filhos em linha própria após tag HTML do pai
- [ ] UTMs com `&amp;` encoding (não `&` puro) em atributos href
- [ ] Hero image real (ou placeholder se não disponível) logo após H1
- [ ] **5-7 mídias totais** no artigo (1 hero + 4-6 no corpo) — atualizado v4.1
- [ ] Imagens no corpo com URLs reais da media-library.md (priorizar GIFs de produto mK quando solução é citada)
- [ ] **Pelo menos 2 imagens em coluna** com texto ao lado (layout alternado, coluna 50/50)
- [ ] Imagens com `max-height:500px` (altura máxima desktop)
- [ ] Cards Gutenberg (`wp:group`) para mKases destacados
- [ ] 8-15 componentes visuais nativos do Gutenberg no artigo
- [ ] Cores do Brand Book (preto #000000, branco #F3F3F3, roxo #7C16DB) — zero cores inventadas
- [ ] Ficha de Metadados gerada com SEO, self-audit, links e instruções para editor

### Tom e Anti-IA
- [ ] Zero padrões de IA dos 25 listados acima
- [ ] [BLOQUEADOR] **Parágrafos com 35-40 palavras no máximo** (piso duro)
- [ ] [BLOQUEADOR] **Mínimo 2000 palavras** no corpo do artigo
- [ ] Uso estratégico de **negrito** (2-4 trechos por H2 — dados, conceitos, provocações, nomes de produto, afirmações-resumo)
- [ ] [BLOQUEADOR] **Zero em dashes (—)** no artigo inteiro (v4.2: limite duro 0 — verificação programática obrigatória, inclui corpo, FAQ e alt-text)
- [ ] [BLOQUEADOR] **Máximo 2 ocorrências do molde "Não é X, é Y"** (incluindo variações: "Não é X nem Y", "A pergunta não é X, é Y") — verificação programática obrigatória
- [ ] [BLOQUEADOR] **Zero anáforas staccato** (3+ frases curtas com mesmo arranque) e **máximo 1 frase curta isolada por parágrafo** (frases ≤10 palavras consecutivas sem conector também bloqueiam)
- [ ] [BLOQUEADOR] **Zero frases-conclusão** ("Em conclusão", "Para concluir", "Em resumo", "Em suma", "Por fim", "Para finalizar", etc.) — verificação programática obrigatória
- [ ] [BLOQUEADOR] **Título SEO max 60 caracteres** e **Meta Description max 155 caracteres** (Google trunca acima desses limites)
- [ ] Pelo menos 1 referência pop-culture ou histórica
- [ ] Pelo menos 1 "Spoiler:" como recurso retórico
- [ ] Pelo menos 2 parênteses coloquiais
- [ ] Pelo menos 1 frase-parágrafo isolada de 4-8 palavras
- [ ] Pelo menos 1 provocação no nível "dinheiro na mesa" / "achismo" / "furada"
- [ ] Tom confessional em pelo menos 1 ponto ("a real é que...", "aqui na mK...")
- [ ] Estrutura NÃO perfeitamente simétrica — quebre a previsibilidade

---

## Red Flags GEO/AEO (complementares)

Além dos 25 padrões de IA acima, estes itens comprometem especificamente o desempenho em GEO e AEO:

- **Artigo sem FAQ:** Perde principal vetor de AEO
- **Zero dados numéricos:** Se não tem dado mK, usar benchmark de mercado com link
- **Introdução >150 palavras antes de responder:** LLMs usam início do texto
- **Excesso de fontes externas (>2):** Dilui mK como fonte primária
- **Foco semântico difuso:** Artigo cobrindo 10 tópicos — LLMs preferem especialização
- **Autoproclamação sem substantivo factual:** "líder em tecnologia imersiva" sem dado
- **Parágrafos >40 palavras:** LLMs extraem trechos curtos. Regra mK: 35-40 palavras no máximo.
