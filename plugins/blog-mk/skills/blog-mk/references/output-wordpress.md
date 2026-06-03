# Especificações de Output — Formato Gutenberg Block Markup

O artigo (`output/[slug]/artigo.html`) é o Documento 2 da entrega. Deve usar **WordPress Gutenberg Block Markup** nativo — o formato interno que o WordPress usa para serializar blocos. Quando colado no "Editor de código" do Gutenberg, renderiza perfeitamente sem nenhuma edição.

**Princípios:**
- Formato: Gutenberg Block Markup (comentários HTML `<!-- wp:bloco -->`)
- Extensão do arquivo: `.html` (não .md — é HTML com blocos Gutenberg)
- Maximizar recursos visuais nativos do Gutenberg (blocos reais, não HTML bruto)
- Zero metadados/comentários técnicos no artigo (vão para o Documento 3)
- SEM Table of Contents / sumário (plugin WordPress gera automaticamente)
- Todos os links funcionais e verificados via `sitemap-urls.md` e `blog-links.md`
- Quando existir mídia real na `media-library.md`, usar URL real em vez de placeholder

---

## Formato do Arquivo

- **Extensão:** `.html`
- **Nome do arquivo:** `[slug-do-artigo]-artigo.html`
- **Encoding:** UTF-8
- **Como usar:** Copiar conteúdo inteiro → WordPress → Novo Post → ícone "..." → "Editor de código" → Colar → Voltar para "Editor visual"

---

## Referência Rápida: Blocos Gutenberg

Cada bloco segue o formato:
```
<!-- wp:nome-do-bloco {"atributo":"valor"} -->
<html do bloco>
<!-- /wp:nome-do-bloco -->
```

Atributos JSON são opcionais (omitir se valores default). Auto-fechamento para blocos sem conteúdo HTML: `<!-- wp:bloco /-->`

### Regra de Aninhamento (CRÍTICA)

Quando um bloco contém blocos filhos (wp:group, wp:quote, wp:list, wp:columns, wp:buttons), o primeiro bloco filho DEVE começar em linha própria após a tag HTML do pai. O fechamento do pai DEVE estar em linha própria após o último filho.

```
ERRADO (gera validation warning):
<div class="wp-block-group ..."><!-- wp:paragraph -->
<p>texto</p>
<!-- /wp:paragraph --></div>

CORRETO:
<div class="wp-block-group ...">
<!-- wp:paragraph -->
<p>texto</p>
<!-- /wp:paragraph -->
</div>
```

Aplicar SEMPRE em: wp:group, wp:quote, wp:list, wp:columns, wp:column, wp:buttons.

---

## Regra CRÍTICA do Tema metakosmos.com.br

O tema do site (Hello Elementor + Elementor Kit 7) aplica CSS global que **CONFLITA** com blocos Gutenberg se não forem configurados corretamente. Regras do tema que afetam o artigo:

### 1. Background e cor global
```css
.elementor-kit-7 {
  background-color: #000000;
  color: #FFFFFF;  /* texto branco é o padrão */
  font-family: "Helvetica";
}
```

**Consequência:** todo bloco com fundo claro precisa forçar `textColor` PRETO explícito no wrapper E em cada parágrafo filho. Senão texto fica branco invisível.

### 2. CSS editorial para posts
```css
.single-post article h1 { margin-top: 6rem !important; }
.single-post article h2 { margin-top: 5.25rem !important; }
.single-post article h3 { margin-top: 4.5rem !important; }
body.single-post .wp-block-heading {
  margin-block-start: 6rem !important;   /* aplica a TODOS os headings! */
  margin-block-end: 2rem !important;
}
```

**Consequência CATASTRÓFICA:** qualquer `<h4>` dentro de card/caixa recebe 96px de margin-top, estourando o layout. **REGRA: NUNCA usar `wp:heading` (h1-h6) dentro de cards, caixas, comparativos ou qualquer bloco aninhado.** Usar `<p><strong>` para títulos internos.

### 3. Links magenta
```css
.elementor-kit-7 a { color: #dc0ca3; }
```
OK — alinhado com Brand Book. Sem ação.

---

## Tabela de Spacing Inline (OBRIGATÓRIO em cada bloco)

Como o tema não aplica hierarquia editorial por default (só 24px uniforme via `--wp--style--block-gap`), TODOS os blocos do artigo recebem `style.spacing.margin` inline. Valores padrão:

| Elemento | margin-top | margin-bottom |
|----------|------------|---------------|
| H1 | 0 | 2rem |
| H2 (seções principais) | **3rem** | 1rem |
| H3 (FAQ e subtítulos) | **2rem** | 0.75rem |
| Parágrafo comum | — (default 24px basta) | — |
| Imagem full-width | 2rem | 2rem |
| Card mKase | 2.5rem | 2.5rem |
| Caixa de destaque | 2.5rem | 2.5rem |
| CTA banner | 3rem | 3rem |
| CTA inline (wp:buttons) | 2rem | 2rem |
| Comparativo wp:columns | 2.5rem | 2.5rem |
| Blockquote | 2rem | 2rem |
| Stat box (número) | 2.5rem | 0 (grudar no subtítulo) |
| Stat box (subtítulo) | 0.5rem | 2.5rem |
| Separador wp:separator | 3rem | 3rem |
| Spacer wp:spacer | usar height em vez de margin | — |

**Regra crítica:** para blocos aninhados (ex: H3 dentro de CTA banner), usar `margin.top: 0` para não quebrar o layout interno.

---

## Blocos Disponíveis — Templates para o Artigo

### 1. Parágrafo

```html
<!-- wp:paragraph -->
<p>Texto do parágrafo simples.</p>
<!-- /wp:paragraph -->
```

Com keyword em negrito:
```html
<!-- wp:paragraph -->
<p>O <strong>Immersive Commerce</strong> é a resposta que elimina essa lacuna.</p>
<!-- /wp:paragraph -->
```

Com link interno (UTM):
```html
<!-- wp:paragraph -->
<p>Para entender o conceito em profundidade, o <a href="https://metakosmos.com.br/immersive-commerce-guia-completo-comercio-imersivo-lideres-ecommerce/?utm_source=blog&amp;utm_medium=internal-link&amp;utm_campaign=pilar1-immersive-commerce&amp;utm_content=slug-artigo-origem">guia completo de Immersive Commerce</a> detalha cada tecnologia.</p>
<!-- /wp:paragraph -->
```

**IMPORTANTE:** Em URLs dentro de atributos HTML, usar `&amp;` em vez de `&` para separar parâmetros UTM.

---

### 2. Heading (H2, H3)

**REGRA DE SPACING:** Todo H2 e H3 do corpo do artigo precisa de margin explícito inline (o CSS do tema sozinho dá apenas 24px uniforme, sem hierarquia editorial).

H2 padrão (com 3rem antes, 1rem depois):
```html
<!-- wp:heading {"style":{"spacing":{"margin":{"top":"3rem","bottom":"1rem"}}}} -->
<h2 class="wp-block-heading" style="margin-top:3rem;margin-bottom:1rem">O e-commerce tradicional tem um problema estrutural</h2>
<!-- /wp:heading -->
```

H3 (para perguntas do FAQ e subtítulos — 2rem antes, 0.75rem depois):
```html
<!-- wp:heading {"level":3,"style":{"spacing":{"margin":{"top":"2rem","bottom":"0.75rem"}}}} -->
<h3 class="wp-block-heading" style="margin-top:2rem;margin-bottom:0.75rem">O que é Immersive Commerce?</h3>
<!-- /wp:heading -->
```

---

### 3. Imagem (full-width, altura max 500px via CSS no tema)

Toda imagem no artigo deve ser explicitamente centralizada (com `"align":"center"` no JSON do bloco e classe `aligncenter` no figure).

**REGRA CRÍTICA v4.2 — NUNCA usar `style="..."` no `<img>`.** O Gutenberg valida o HTML salvo contra o HTML re-gerado a partir do JSON do bloco. Qualquer `style` inline no `<img>` que não esteja declarado no JSON gera erro **"Este bloco contém conteúdo inesperado ou inválido"** com prompt "Tentar restaurar" no editor. Solução: zero atributos inline no `<img>`.

**Como aplicar o limite de altura sem mexer no tema (v4.2 — solução in-skill):** todo artigo abre com um bloco `wp:html` contendo o `<style>` necessário. O bloco `wp:html` aceita HTML arbitrário sem validação, então funciona como mini-folha de estilos local do artigo. Esse bloco fica logo após o H1 (antes da hero image) e nunca aparece visualmente no front-end. Template em "Bloco de CSS local" abaixo.

**Bloco de CSS local (obrigatório no início de cada artigo a partir de v4.2):**

```html
<!-- wp:html -->
<style>.wp-block-image img{max-height:500px;width:auto;height:auto;max-width:100%}.wp-block-image.aligncenter img{margin:0 auto;display:block}.wp-block-column .wp-block-image img{width:100%;max-width:100%}.wp-block-list li{margin-bottom:0.6rem;line-height:1.55}.wp-block-list li:last-child{margin-bottom:0}</style>
<!-- /wp:html -->
```

Inserir esse bloco **imediatamente após o H1**, antes da hero image. Ele aplica três coisas: (1) limite de 500px de altura em todas as imagens, (2) centralização correta da `aligncenter`, (3) espaçamento entre bullets. O `<style>` afeta apenas o artigo onde está inserido.

**Alternativa long-term — CSS no tema** (Customizer → CSS Adicional). Útil se você quiser remover o bloco `wp:html` dos artigos futuros:

```css
.single-post .wp-block-image img {
  max-height: 500px;
  width: auto;
  height: auto;
  max-width: 100%;
}
.single-post .wp-block-image.aligncenter img {
  margin-left: auto;
  margin-right: auto;
  display: block;
}
.single-post .wp-block-column .wp-block-image img {
  max-width: 100%;
  width: 100%;
  object-fit: contain;
}
.single-post .wp-block-list li {
  margin-bottom: 0.6rem;
  line-height: 1.55;
}
.single-post .wp-block-list li:last-child {
  margin-bottom: 0;
}
```

Imagem simples (full-width, centralizada, 2rem de margin top e bottom):
```html
<!-- wp:image {"align":"center","sizeSlug":"large","linkDestination":"none","style":{"spacing":{"margin":{"top":"2rem","bottom":"2rem"}}}} -->
<figure class="wp-block-image aligncenter size-large" style="margin-top:2rem;margin-bottom:2rem"><img src="https://metakosmos.com.br/wp-content/uploads/2025/09/flexform-3D-scaled.png" alt="Visualizador 3D Flexform com Realidade Aumentada da metaKosmos"/></figure>
<!-- /wp:image -->
```

Com ID e legenda (quando a mídia já existe no WP Media Library):
```html
<!-- wp:image {"align":"center","id":1234,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-large"><img src="URL_DA_IMAGEM" alt="Texto alternativo" class="wp-image-1234"/><figcaption class="wp-element-caption">Legenda da imagem</figcaption></figure>
<!-- /wp:image -->
```

### 3b. Imagem em Coluna (lado a lado com texto)

Usar em pelo menos 2 imagens do corpo do artigo. Alternar lado (imagem esquerda / texto direita, e vice-versa).

**REGRA CRÍTICA:** Usar coluna **50/50** (não 40/60). Coluna estreita de 40% combinada com `width:auto` da imagem causa o efeito de "imagem flutuando à esquerda da coluna" — o que o leitor lê como desalinhamento. Com 50/50 + imagem centralizada na coluna, a hierarquia visual fica simétrica e respira.

**Imagem à esquerda + texto à direita:**
```html
<!-- wp:columns {"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center">
<!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%">
<!-- wp:image {"align":"center","sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-large"><img src="URL_IMAGEM" alt="Alt text"/></figure>
<!-- /wp:image -->
</div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%">
<!-- wp:paragraph -->
<p>Texto que acompanha a imagem. Entre 35-40 palavras. Pode ter <strong>destaque em negrito</strong> e link interno se fizer sentido.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
```

**Texto à esquerda + imagem à direita:**
```html
<!-- wp:columns {"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center">
<!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%">
<!-- wp:paragraph -->
<p>Texto que acompanha a imagem, com <strong>pontos em negrito</strong> para escaneabilidade.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%">
<!-- wp:image {"align":"center","sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-large"><img src="URL_IMAGEM" alt="Alt text"/></figure>
<!-- /wp:image -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
```

Quando NÃO existir mídia disponível, usar placeholder como comentário HTML:
```html
<!-- wp:html -->
<!-- MÍDIA NECESSÁRIA: [TIPO] — [Descrição detalhada para o editor buscar/produzir] -->
<!-- ALT-TEXT SUGERIDO: [texto alternativo] -->
<!-- /wp:html -->
```

---

### 4. Separador

```html
<!-- wp:separator {"style":{"spacing":{"margin":{"top":"3rem","bottom":"3rem"}}}} -->
<hr class="wp-block-separator has-alpha-channel-opacity" style="margin-top:3rem;margin-bottom:3rem"/>
<!-- /wp:separator -->
```

---

### 5. Lista (com espaçamento entre bullets — v4.2)

**REGRA v4.2:** Sempre usar `style.spacing.blockGap` na `wp:list` E `style.spacing.margin.bottom` em cada `wp:list-item`. Sem isso, o Gutenberg renderiza bullets grudados sem respiro visual.

```html
<!-- wp:list {"style":{"spacing":{"blockGap":"0.75rem","margin":{"top":"1.5rem","bottom":"1.5rem"}}}} -->
<ul class="wp-block-list" style="margin-top:1.5rem;margin-bottom:1.5rem">
<!-- wp:list-item {"style":{"spacing":{"margin":{"bottom":"0.6rem"}}}} -->
<li style="margin-bottom:0.6rem">Projeta o sofá em tamanho real na sala pelo celular (AR)</li>
<!-- /wp:list-item -->

<!-- wp:list-item {"style":{"spacing":{"margin":{"bottom":"0.6rem"}}}} -->
<li style="margin-bottom:0.6rem">Experimenta o batom no próprio rosto em tempo real</li>
<!-- /wp:list-item -->

<!-- wp:list-item {"style":{"spacing":{"margin":{"bottom":"0.6rem"}}}} -->
<li style="margin-bottom:0.6rem">Gira o tênis em 360 graus e vê cada costura de perto</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
```

**Para listas dentro de cards/grupos (com texto colorido forçado):**
```html
<!-- wp:list {"style":{"color":{"text":"#000000"},"spacing":{"blockGap":"0.75rem"}}} -->
<ul class="wp-block-list has-text-color" style="color:#000000">
<!-- wp:list-item {"style":{"spacing":{"margin":{"bottom":"0.6rem"}}}} -->
<li style="margin-bottom:0.6rem">Item de lista dentro de card</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
```

**Fallback CSS no tema (caso plataforma ignore o blockGap):**
```css
.single-post .wp-block-list li {
  margin-bottom: 0.6rem;
  line-height: 1.55;
}
.single-post .wp-block-list li:last-child {
  margin-bottom: 0;
}
```

---

### 6. Blockquote — Dado de Impacto

```html
<!-- wp:quote {"style":{"spacing":{"margin":{"top":"2rem","bottom":"2rem"}}}} -->
<blockquote class="wp-block-quote" style="margin-top:2rem;margin-bottom:2rem">
<!-- wp:paragraph -->
<p><strong>98 de cada 100 visitantes</strong> com intenção de compra abandonam o e-commerce sem finalizar. A foto estática informa, mas não elimina a dúvida. E a dúvida mata a conversão.</p>
<!-- /wp:paragraph -->
</blockquote>
<!-- /wp:quote -->
```

---

### 7. CTA Banner — Grupo com Background (bloco nativo)

```html
<!-- wp:group {"style":{"color":{"background":"#000000","text":"#ffffff"},"spacing":{"padding":{"top":"2.5rem","right":"2rem","bottom":"2.5rem","left":"2rem"},"margin":{"top":"3rem","bottom":"3rem"}},"border":{"radius":"16px"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-text-color has-background" style="color:#ffffff;background-color:#000000;margin-top:3rem;margin-bottom:3rem;padding-top:2.5rem;padding-right:2rem;padding-bottom:2.5rem;padding-left:2rem;border-radius:16px">
<!-- wp:heading {"textAlign":"center","level":3,"style":{"color":{"text":"#ffffff"},"spacing":{"margin":{"top":"0","bottom":"0.75rem"}}}} -->
<h3 class="wp-block-heading has-text-align-center has-text-color" style="color:#ffffff;margin-top:0;margin-bottom:0.75rem">Sua marca ainda depende de fotos estáticas para convencer?</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#cccccc"}}} -->
<p class="has-text-align-center has-text-color" style="color:#cccccc">Fale com um mentor da metaKosmos e descubra em quanto tempo você pode virar o jogo.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons">
<!-- wp:button {"style":{"color":{"background":"#7C16DB","text":"#ffffff"},"border":{"radius":"8px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background wp-element-button" style="border-radius:8px;color:#ffffff;background-color:#7C16DB" href="https://form.respondi.app/L4NmIy24?utm_source=blog&amp;utm_medium=cta-banner&amp;utm_campaign=pilar1-immersive-commerce&amp;utm_content=cta-fale-mentor">Fale com um Mentor →</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:group -->
```

**Variações de texto para botões:**
- "Fale com um Mentor →"
- "Solicite uma Demo →"
- "Veja o mK Fashion+ em Ação →"
- "Baixe o State of Immersive Commerce 2026 →"
- "Calcule seu ROI Imersivo →"

**URL padrão de conversão:** `https://form.respondi.app/L4NmIy24` (formulário oficial de lead/contato)

---

### 8. CTA Inline — Botão Centralizado

```html
<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"2rem","bottom":"2rem"}}}} -->
<div class="wp-block-buttons" style="margin-top:2rem;margin-bottom:2rem">
<!-- wp:button {"style":{"color":{"background":"#7C16DB","text":"#ffffff"},"border":{"radius":"8px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background wp-element-button" style="border-radius:8px;color:#ffffff;background-color:#7C16DB" href="https://form.respondi.app/L4NmIy24?utm_source=blog&amp;utm_medium=cta-inline&amp;utm_campaign=pilar1-immersive-commerce&amp;utm_content=slug-artigo">Solicite uma Demo →</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
```

---

### 9. Card mKase — Grupo com Borda

**REGRA:** SEM `wp:heading` dentro (CSS editorial do tema adiciona 96px de margin). Usar `<p>` com `<strong>` como título. SEMPRE forçar `color:#000000` no wrapper E em cada parágrafo filho.

```html
<!-- wp:group {"style":{"border":{"width":"1px","color":"#e0e0e0","radius":"12px"},"color":{"background":"#F3F3F3","text":"#000000"},"spacing":{"padding":{"top":"1.5rem","right":"1.5rem","bottom":"1.5rem","left":"1.5rem"},"margin":{"top":"2.5rem","bottom":"2.5rem"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-border-color has-text-color has-background" style="border-color:#e0e0e0;border-width:1px;border-radius:12px;color:#000000;background-color:#F3F3F3;margin-top:2.5rem;margin-bottom:2.5rem;padding-top:1.5rem;padding-right:1.5rem;padding-bottom:1.5rem;padding-left:1.5rem">
<!-- wp:paragraph {"style":{"color":{"text":"#000000"},"typography":{"fontSize":"1.15rem","fontWeight":"700"},"spacing":{"margin":{"top":"0","bottom":"0.75rem"}}}} -->
<p class="has-text-color" style="color:#000000;font-size:1.15rem;font-weight:700;margin-top:0;margin-bottom:0.75rem">mKase: Flexform</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"color":{"text":"#000000"}}} -->
<p class="has-text-color" style="color:#000000"><strong>Desafio:</strong> Vender móveis de alto padrão online sem o consumidor ver o produto no ambiente real.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"color":{"text":"#000000"}}} -->
<p class="has-text-color" style="color:#000000"><strong>Solução mK:</strong> mK 3D Shop — visualizador 3D com Realidade Aumentada para o catálogo completo.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"color":{"text":"#000000"}}} -->
<p class="has-text-color" style="color:#000000"><strong>Resultado:</strong> <strong>20 milhões+ de visualizações 3D acumuladas.</strong></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
```

---

### 10. Caixa de Destaque / Definição GEO

**REGRA:** Forçar `color:#000000` no wrapper E em cada parágrafo filho.

```html
<!-- wp:group {"style":{"color":{"background":"#F3F3F3","text":"#000000"},"border":{"radius":"12px","left":{"color":"#7C16DB","width":"4px"}},"spacing":{"padding":{"top":"1.5rem","right":"1.5rem","bottom":"1.5rem","left":"1.5rem"},"margin":{"top":"2.5rem","bottom":"2.5rem"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-text-color has-background" style="color:#000000;background-color:#F3F3F3;border-radius:12px;border-left-color:#7C16DB;border-left-width:4px;margin-top:2.5rem;margin-bottom:2.5rem;padding-top:1.5rem;padding-right:1.5rem;padding-bottom:1.5rem;padding-left:1.5rem">
<!-- wp:paragraph {"style":{"color":{"text":"#000000"}}} -->
<p class="has-text-color" style="color:#000000"><strong>Immersive Commerce</strong> — Conjunto de tecnologias imersivas — Realidade Aumentada, visualizadores 3D e provadores virtuais com IA — aplicadas à jornada de compra online para eliminar a dúvida do consumidor. No Brasil, a metaKosmos é líder nesse segmento, com soluções que aumentam conversão em até 315%.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
```

---

### 11. Comparativo — Colunas (Antes vs Depois)

**REGRA:** SEM `wp:heading` dentro (trocar por `<p>` com `<strong>`). Forçar `color:#000000` no wrapper E em cada filho. Cores do Brand Book (fundo claro do F3F3F3 com borda colorida para diferenciar).

```html
<!-- wp:columns {"style":{"spacing":{"margin":{"top":"2.5rem","bottom":"2.5rem"}}}} -->
<div class="wp-block-columns" style="margin-top:2.5rem;margin-bottom:2.5rem">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:group {"style":{"color":{"background":"#F3F3F3","text":"#000000"},"border":{"radius":"12px","width":"2px","color":"#DC0C9F"},"spacing":{"padding":{"top":"1.25rem","right":"1.25rem","bottom":"1.25rem","left":"1.25rem"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-border-color has-text-color has-background" style="border-color:#DC0C9F;border-width:2px;border-radius:12px;color:#000000;background-color:#F3F3F3;padding-top:1.25rem;padding-right:1.25rem;padding-bottom:1.25rem;padding-left:1.25rem">
<!-- wp:paragraph {"style":{"color":{"text":"#DC0C9F"},"typography":{"fontSize":"1.15rem","fontWeight":"700"}}} -->
<p class="has-text-color" style="color:#DC0C9F;font-size:1.15rem;font-weight:700">E-commerce Tradicional</p>
<!-- /wp:paragraph -->

<!-- wp:list {"style":{"color":{"text":"#000000"}}} -->
<ul class="wp-block-list has-text-color" style="color:#000000">
<!-- wp:list-item -->
<li>Conversão: 1-3%</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Devoluções: 5-25%</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Experiência: foto estática + texto</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:group {"style":{"color":{"background":"#F3F3F3","text":"#000000"},"border":{"radius":"12px","width":"2px","color":"#7C16DB"},"spacing":{"padding":{"top":"1.25rem","right":"1.25rem","bottom":"1.25rem","left":"1.25rem"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group has-border-color has-text-color has-background" style="border-color:#7C16DB;border-width:2px;border-radius:12px;color:#000000;background-color:#F3F3F3;padding-top:1.25rem;padding-right:1.25rem;padding-bottom:1.25rem;padding-left:1.25rem">
<!-- wp:paragraph {"style":{"color":{"text":"#7C16DB"},"typography":{"fontSize":"1.15rem","fontWeight":"700"}}} -->
<p class="has-text-color" style="color:#7C16DB;font-size:1.15rem;font-weight:700">Immersive Commerce</p>
<!-- /wp:paragraph -->

<!-- wp:list {"style":{"color":{"text":"#000000"}}} -->
<ul class="wp-block-list has-text-color" style="color:#000000">
<!-- wp:list-item -->
<li>Conversão: até +94% com 3D/AR</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Devoluções: redução de até 61%</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Experiência: 3D + AR + IA interativa</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
```

---

### 12. Stat Box — Número de Destaque

```html
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"3.5rem","fontStyle":"normal","fontWeight":"700"},"color":{"text":"#7C16DB"},"spacing":{"margin":{"top":"2.5rem","bottom":"0"}}}} -->
<p class="has-text-align-center has-text-color" style="color:#7C16DB;margin-top:2.5rem;margin-bottom:0;font-size:3.5rem;font-style:normal;font-weight:700">+94%</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#AAAAAA"},"typography":{"fontSize":"1.1rem"},"spacing":{"margin":{"top":"0.5rem","bottom":"2.5rem"}}}} -->
<p class="has-text-align-center has-text-color" style="color:#AAAAAA;margin-top:0.5rem;margin-bottom:2.5rem;font-size:1.1rem">de conversão com visualizador 3D e AR da metaKosmos</p>
<!-- /wp:paragraph -->
```

---

### 13. Citação / Depoimento

```html
<!-- wp:quote {"citation":"Stephanie Tardin, L\u0027Oréal Professionnel"} -->
<blockquote class="wp-block-quote">
<!-- wp:paragraph -->
<p>Ficamos muito felizes com o profissionalismo e criatividade da metaKosmos.</p>
<!-- /wp:paragraph -->
<cite>Stephanie Tardin, L'Oréal Professionnel</cite>
</blockquote>
<!-- /wp:quote -->
```

---

### 14. Espaçador

```html
<!-- wp:spacer {"height":"30px"} -->
<div style="height:30px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
```

---

## Estrutura Completa do Artigo

```html
<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">[Título do Artigo]</h1>
<!-- /wp:heading -->

<!-- wp:html -->
<style>.wp-block-image img{max-height:500px;width:auto;height:auto;max-width:100%}.wp-block-image.aligncenter img{margin:0 auto;display:block}.wp-block-column .wp-block-image img{width:100%;max-width:100%}.wp-block-list li{margin-bottom:0.6rem;line-height:1.55}.wp-block-list li:last-child{margin-bottom:0}</style>
<!-- /wp:html -->

[Bloco de imagem hero — mídia real ou placeholder]

[Parágrafos de abertura — responder pergunta nos primeiros 150 palavras]

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

[H2s com conteúdo, componentes visuais intercalados]

[Separador entre cada H2]

[H2 final provocativo + CTA Banner]

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Perguntas frequentes sobre [tema]</h2>
<!-- /wp:heading -->

[H3 + parágrafo para cada pergunta do FAQ]
```

**O que NÃO vai no artigo:**
- Metadados SEO (vão para Documento 3)
- Checklist (vai para Documento 3)
- Table of Contents (plugin gera)
- Instruções para editor (vão para Documento 3)
- Emojis nos headings ou corpo de texto

---

## Mídias: Estratégia Real vs Placeholder

### Prioridade 1: Usar mídia real existente
Consultar `media-library.md` e o sitemap de blog (que lista imagens por post) para encontrar mídias existentes. Se uma imagem existente se encaixar, usar diretamente com bloco `wp:image`.

### Prioridade 2: Placeholder documentado
Se não existir mídia adequada, inserir bloco `wp:html` com comentário descritivo para o editor. Documentar no Documento 3 (Metadados) com instruções de produção.

### Frequência (v4.1):
- **Hero image:** 1 (obrigatória, logo após H1) — escolher de "Hero Candidates" em `media-library.md`
- **Mídias no corpo:** 4-6 distribuídas (1 a cada 1-2 seções)
- **Total mínimo:** 5-7 mídias por artigo (era 3-5 — subiu na v4.1)
- **Mix recomendado:** 1 hero + 1-2 GIFs de produto mK + 1-2 imagens de mKase/cliente + 1 infográfico/dashboard + 0-1 foto de depoimento

---

## Links — Verificação Obrigatória

### Fontes de verdade para URLs:
1. `sitemap-urls.md` — Todas as URLs do site (páginas, LPs, mKases)
2. `blog-links.md` — Artigos de blog com pilar
3. `utm-tracking.md` — Taxonomia UTM por pilar

### URL de conversão principal:
**`https://form.respondi.app/L4NmIy24`** (formulário oficial de lead — usar em todos os CTAs "Fale com Mentor", "Solicite Demo", "Calcule ROI", etc.)

### Encoding de UTMs em HTML:
Dentro de atributos `href`, usar `&amp;` em vez de `&`:
```
href="https://form.respondi.app/L4NmIy24?utm_source=blog&amp;utm_medium=cta-banner&amp;utm_campaign=pilar1-immersive-commerce&amp;utm_content=cta-fale-mentor"
```

---

## Frequência Mínima de Componentes Visuais

| Componente | Mínimo | Bloco Gutenberg |
|------------|--------|-----------------|
| CTA Banner | 1-2 | `wp:group` + `wp:buttons` |
| CTA Inline | 1-2 | `wp:buttons` |
| Card mKase | 2 | `wp:group` com borda |
| Blockquote dado | 2-3 | `wp:quote` |
| Caixa destaque | 1-2 | `wp:group` com background |
| Comparativo | 0-1 | `wp:columns` |
| Stat Box | 1-2 | `wp:paragraph` centralizado |
| Citação | 0-1 | `wp:quote` com citation |
| Separadores | Entre todos H2s | `wp:separator` |
| Espaçadores | Conforme necessário | `wp:spacer` |

**Meta: 8-15 componentes visuais por artigo.**

---

## Checklist de Formatação Final

Antes de entregar `output/[slug]/artigo.html`:

### Estrutura Gutenberg
- [ ] Todos os blocos com abertura e fechamento corretos
- [ ] H1 como `wp:heading {"level":1}`
- [ ] H2s como `wp:heading` (level 2 é default, omitir atributo)
- [ ] H3s como `wp:heading {"level":3}`
- [ ] Separadores `wp:separator` entre todos os H2s
- [ ] FAQ com H2 + H3s
- [ ] Caminho do arquivo = `output/[slug]/artigo.html` (pasta dedicada por slug, nome limpo sem repetir slug)

### Auditoria Gutenberg (rodar ANTES da entrega)
- [ ] Blocos aninhados: primeiro filho em linha própria após tag HTML do pai
- [ ] Blocos aninhados: fechamento `</div>`, `</blockquote>`, `</ul>` em linha própria
- [ ] Zero ocorrências de `><!-- wp:` na mesma linha (exceto `<li>` e `<p>` que são leaf blocks)
- [ ] Zero ocorrências de `-->` seguido de `</div>` ou `</blockquote>` na mesma linha
- [ ] UTMs com `&amp;` (não `&`) em todos os atributos href
- [ ] Zero typos em texto visível (rodar verificação ortográfica)
- [ ] Cada bloco `<!-- wp:xxx -->` tem seu `<!-- /wp:xxx -->` correspondente

### Componentes Visuais (meta: 8-15)
- [ ] 1-2 CTA banners (`wp:group` + `wp:buttons`)
- [ ] 1-2 CTAs inline (`wp:buttons`)
- [ ] 2+ cards mKase (`wp:group` com borda)
- [ ] 2-3 blockquotes (`wp:quote`)
- [ ] 1-2 caixas de destaque (`wp:group` com background)
- [ ] 1-2 stat boxes (parágrafo centralizado)

### Mídias (v4.1)
- [ ] Hero image (real da media-library.md, escolhida de "Hero Candidates" por pilar)
- [ ] **5-7 mídias totais** distribuídas (1 hero + 4-6 inline) — atualizado v4.1
- [ ] Pelo menos 1 GIF de produto mK quando solução é citada (mk-3d-shop / mk-beauty / mk-fashion / mk-spaces)
- [ ] Pelo menos 1 imagem de mKase/cliente quando marca é citada
- [ ] Toda `wp:image` full-width com `"align":"center"` no JSON e classe `aligncenter` no figure
- [ ] CSS do `<img>` usa `max-width:100%;height:auto;max-height:500px` (não `width:auto`)
- [ ] Imagens em coluna usam ratio 50/50 (não 40/60), com imagem centralizada dentro da coluna

### Links (v4.1)
- [ ] URLs verificadas em `sitemap-urls.md` / `blog-links.md`
- [ ] UTMs com `&amp;` encoding
- [ ] CTA principal apontando para `https://form.respondi.app/L4NmIy24`
- [ ] **Mínimo 6-8 links internos**: 1 Pillar Page + 2 cross-pilar + 2 mKases + 1-2 LPs de produto
- [ ] Regra "first mention link" aplicada (marca cliente → mKase; solução mK → LP)
- [ ] Zero links inventados

### O que NÃO deve estar no artigo
- [ ] SEM metadados SEO (vão para doc 3)
- [ ] SEM checklist (vai para doc 3)
- [ ] SEM Table of Contents (plugin gera)
- [ ] SEM emojis
