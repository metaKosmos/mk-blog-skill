# UTM Tracking e Links Internos — metaKosmos

Taxonomia oficial de UTMs para rastreamento orgânico. Todo link publicado em artigo deve carregar UTMs estruturados.

---

## Princípio: Se não tem UTM, não existe para o dashboard.

---

## Boas Práticas de Nomenclatura

- **Sempre minúsculas:** "Blog" e "blog" são valores diferentes no GA4
- **Sem espaços:** Substituir por hífens. Ex: "provador-virtual"
- **Sem acentos ou caracteres especiais:** "visualizador-3d" (não "3D")
- **Descritivo, não genérico:** "pilar2-provador-virtual" (não "pilar2")

---

## Taxonomia Oficial

### utm_source — A Origem

| Valor | Quando usar |
|-------|-------------|
| `blog` | Link interno entre artigos ou de artigo para LP |
| `pillar-page` | Link de Pillar Page para artigo satélite |
| `linkedin-organico` | Post orgânico no LinkedIn |
| `instagram-bio` | Link na bio do Instagram |
| `newsletter` | Link em newsletter orgânica |
| `whatsapp-comercial` | Artigo compartilhado pelo time de vendas |

### utm_medium — O Canal

| Valor | Significado |
|-------|-------------|
| `internal-link` | Link de texto dentro de artigo para outro artigo |
| `cta-banner` | Banner de conversão no meio ou fim do artigo |
| `cta-inline` | CTA em texto (não banner) no corpo do artigo |
| `cta-final` | CTA na última seção (antes do rodapé) |
| `pillar-link` | Link da Pillar Page para artigo satélite |
| `organic-social` | Post orgânico em redes sociais |
| `email` | Link em newsletter ou e-mail de relacionamento |
| `glossary-link` | Link do glossário de termos |

### utm_campaign — O Pilar ou Campanha

| Valor | Pilar |
|-------|-------|
| `pilar1-immersive-commerce` | P1 — Immersive Commerce |
| `pilar2-provador-virtual` | P2 — Provador Virtual |
| `pilar3-visualizador-3d-ar` | P3 — Visualizador 3D e AR |
| `pilar4-fooh-videos-ia` | P4 — FOOH e Vídeos IA |
| `pilar5-performance-ecommerce` | P5 — Performance do E-commerce |
| `pilar6-mkases-cases` | P6 — Dados, Cases e Prova Social |
| `pilar7-futuro-ecommerce` | P7 — Futuro do E-commerce |
| `state-of-immersive-2026` | Relatório proprietário |
| `lancamento-mk-fashion-plus` | Campanha mK Fashion+ |
| `lancamento-shop-the-look` | Campanha mK Shop The Look |
| `glossario-immersive` | Glossário (ativo GEO/AEO) |

### utm_content — O Elemento Específico

| Valor | O que rastreia |
|-------|---------------|
| `[slug-do-artigo]` | Artigo de origem do clique |
| `cta-fale-mentor` | CTA "Fale com um Mentor metaKosmos" |
| `cta-demo-mk-fashion` | CTA demo mK Fashion+ |
| `cta-demo-mk-beauty` | CTA demo mK Beauty |
| `cta-demo-mk-3d-shop` | CTA demo mK 3D Shop |
| `cta-roi-calculator` | Link para calculadora de ROI |
| `cta-state-of-immersive` | Download do State of IC 2026 |
| `cta-case-[nome]` | Link para case específico |
| `internal-link-pillar` | Link para Pillar Page do cluster |
| `internal-link-related` | Link para artigo do mesmo pilar |
| `internal-link-cross` | Link para artigo de outro pilar |

---

## Fórmula de Montagem de URL

**Para links internos (artigos, LPs, mKases):**
```
https://metakosmos.com.br/[caminho-destino]/?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]
```

**Para CTAs principais (Fale com Mentor / Solicite Demo):**
```
https://form.respondi.app/L4NmIy24?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]
```

> A URL canônica de conversão é `https://form.respondi.app/L4NmIy24` (formulário externo no Respondi). UTMs funcionam como query string normalmente — o Respondi preserva os parâmetros para tracking via GA4 cross-domain.

### Exemplos Práticos

**Link interno entre artigos (mesmo pilar):**
```
https://metakosmos.com.br/provador-virtual/?utm_source=blog&utm_medium=internal-link&utm_campaign=pilar2-provador-virtual&utm_content=como-reduzir-devolucoes-moda
```

**Link cross-pilar:**
```
https://metakosmos.com.br/blog/taxa-conversao-ecommerce/?utm_source=blog&utm_medium=internal-link&utm_campaign=pilar5-performance-ecommerce&utm_content=roi-provador-virtual
```

**CTA Banner "Fale com Mentor" (URL oficial — form externo no Respondi):**
```
https://form.respondi.app/L4NmIy24?utm_source=blog&utm_medium=cta-banner&utm_campaign=pilar2-provador-virtual&utm_content=cta-fale-mentor
```

**IMPORTANTE:** A URL canônica de CTA principal é `https://form.respondi.app/L4NmIy24`. NÃO usar `metakosmos.com.br/contato/` nem `metakosmos.com.br/endform/` (legado). UTMs funcionam normalmente como query string mesmo sendo domínio externo — o Respondi preserva os parâmetros para tracking via GA4 cross-domain.

**CTA inline demo mK Fashion+:**
```
https://metakosmos.com.br/mk-fashion-plus/demo/?utm_source=blog&utm_medium=cta-inline&utm_campaign=pilar2-provador-virtual&utm_content=cta-demo-mk-fashion
```

**CTA download State of IC:**
```
https://metakosmos.com.br/state-of-immersive-2026/?utm_source=blog&utm_medium=cta-final&utm_campaign=state-of-immersive-2026&utm_content=cta-state-of-immersive
```

---

## UTMs Prontos por Pilar

### Pilar 1 — Immersive Commerce

| source | medium | campaign | content |
|--------|--------|----------|---------|
| blog | cta-banner | pilar1-immersive-commerce | cta-fale-mentor |
| blog | cta-final | pilar1-immersive-commerce | cta-state-of-immersive |
| blog | internal-link | pilar1-immersive-commerce | [slug-artigo-origem] |
| pillar-page | pillar-link | pilar1-immersive-commerce | pillar-immersive-commerce |

### Pilar 2 — Provador Virtual

| source | medium | campaign | content |
|--------|--------|----------|---------|
| blog | cta-banner | pilar2-provador-virtual | cta-demo-mk-fashion |
| blog | cta-inline | pilar2-provador-virtual | cta-case-dressto |
| blog | cta-final | pilar2-provador-virtual | cta-fale-mentor |
| blog | internal-link | pilar2-provador-virtual | [slug-artigo-origem] |
| pillar-page | pillar-link | pilar2-provador-virtual | pillar-provador-virtual |

### Pilar 3 — Visualizador 3D e AR

| source | medium | campaign | content |
|--------|--------|----------|---------|
| blog | cta-banner | pilar3-visualizador-3d-ar | cta-demo-mk-3d-shop |
| blog | cta-inline | pilar3-visualizador-3d-ar | cta-roi-calculator |
| blog | cta-final | pilar3-visualizador-3d-ar | cta-fale-mentor |
| pillar-page | pillar-link | pilar3-visualizador-3d-ar | pillar-visualizador-3d |

### Pilar 4 — FOOH e Vídeos IA

| source | medium | campaign | content |
|--------|--------|----------|---------|
| blog | cta-banner | pilar4-fooh-videos-ia | cta-fale-mentor |
| blog | cta-inline | pilar4-fooh-videos-ia | cta-demo-fooh-briefing |
| linkedin-organico | organic-social | pilar4-fooh-videos-ia | [slug-post-linkedin] |
| pillar-page | pillar-link | pilar4-fooh-videos-ia | pillar-fooh-guia-definitivo |

### Pilar 5 — Performance de E-commerce

| source | medium | campaign | content |
|--------|--------|----------|---------|
| blog | cta-banner | pilar5-performance-ecommerce | cta-roi-calculator |
| blog | cta-inline | pilar5-performance-ecommerce | cta-case-dressto |
| blog | cta-final | pilar5-performance-ecommerce | cta-fale-mentor |
| pillar-page | pillar-link | pilar5-performance-ecommerce | pillar-performance-ecommerce |

### Pilar 6 — Cases e Prova Social

| source | medium | campaign | content |
|--------|--------|----------|---------|
| blog | cta-banner | pilar6-mkases-cases | cta-case-mascavo |
| blog | cta-banner | pilar6-mkases-cases | cta-case-bio-extratus |
| whatsapp-comercial | cta-inline | pilar6-mkases-cases | cta-case-dressto |
| blog | internal-link | pilar6-mkases-cases | [slug-artigo-origem] |

### Pilar 7 — Futuro do E-commerce

| source | medium | campaign | content |
|--------|--------|----------|---------|
| blog | cta-banner | pilar7-futuro-ecommerce | cta-fale-mentor |
| blog | cta-final | pilar7-futuro-ecommerce | cta-state-of-immersive |
| pillar-page | pillar-link | pilar7-futuro-ecommerce | pillar-futuro-ecommerce |

---

## Hierarquia de Links Internos

| Tipo de página | Aponta para | Prioridade |
|----------------|-------------|------------|
| Pillar Page | Todos artigos satélite do pilar | Máxima |
| Artigo TOFU | Pillar Page + 1 artigo MOFU | Alta |
| Artigo MOFU | Pillar Page + 1 artigo BOFU + 1 case | Alta |
| Artigo BOFU | Pillar Page + Página de produto + 1 case | Máxima |
| mKase | Artigo BOFU do pilar + Página de produto | Alta |
| Glossário | Pillar Pages + artigos de definição | Média |

## Quantidade Mínima por Artigo (v4.1)

**Mínimo 6-8 links internos por artigo** (subiu de 4 na v4.1):

- **1 link Pillar Page** do mesmo pilar (obrigatório — sinal de cluster)
- **2 cross-pilar** — artigos de pilares relacionados
- **2 mKases** — `/mkases/[slug]/` para cada marca cliente citada (regra "first mention link")
- **1-2 LPs de produto** — `/mk-3d-shop/`, `/mk-beauty/`, `/mk-fashion/`, etc. quando solução mK é citada
- **1-2 CTAs com UTM** apontando para `https://form.respondi.app/L4NmIy24` (banner + inline)

**Regra "first mention link":** Ao citar marca cliente pela 1ª vez no artigo, linkar nome para `/mkases/[slug]/`. Ao citar solução mK pela 1ª vez, linkar para LP correspondente. Ver `blog-links.md` para a lista completa de mKases (53) e LPs (7).

**Regra do Cluster:** A Pillar Page é o hub central. Todo artigo satélite DEVE linkar para ela. Hub-and-spoke é o sinal mais forte de autoridade temática.
