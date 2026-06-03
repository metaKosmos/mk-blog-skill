# Biblioteca de Mídias — metaKosmos WordPress

Extraído via REST API em 2026-04-28. **Total real no WP: 996 mídias**. Listamos abaixo as **~250 mais úteis** para artigos de blog, organizadas por uso recomendado.

**Como usar:** Toda escolha de mídia para artigo deve consultar este arquivo. Em vez de criar placeholder, buscar primeiro aqui por mídia existente. Usar URL real com bloco `wp:image`. **Mínimo 5-7 mídias por artigo** (era 3-5 antes).

**API de busca:** Para encontrar mídia específica que não esteja listada aqui, usar:
```
https://metakosmos.com.br/wp-json/wp/v2/media?search=[termo]&per_page=20
```

---

## REGRAS DE USO

### Quantidade por artigo (atualizado v4.1)
- **Hero image (obrigatória):** 1 — full-width logo após H1, da seção "Hero Candidates" abaixo, escolhida por pilar
- **Mídias no corpo:** 4-6 distribuídas (1 a cada 1-2 H2s)
- **Mínimo total:** 5-7 mídias reais por artigo (antes era 3-5)
- **Máximo recomendado:** 8 mídias (acima disso, polui)

### Mix recomendado por artigo
- 1 hero (thumb_*, mk-hero-*, capa-*)
- 1-2 GIFs de produto mK (mk-3d-shop-*, mk-beauty-*, mk-fashion-*, mk-spaces-*)
- 1-2 imagens de mKase/cliente (Flexform, Boca Rosa, GM, Bio Extratus, Osklen, etc.)
- 1 infográfico/dashboard (metricas, ROI, dashboard analytics)
- 0-1 foto de depoimento (Stephanie Tardin, Hugo Linhares, Celso Bastos, etc.) — quando incluir citação

### Regra de variação
Se o artigo é de **um pilar específico**, variar: pelo menos uma mídia de outro pilar adjacente para reforçar a transversalidade do Immersive Commerce.

---

## 1. HERO CANDIDATES (após H1, full-width)

Use uma destas como hero, escolhendo por pilar/tema do artigo. Todas são thumbnails ou hero images de alta resolução (≥1000px).

### Hero genéricos / brand
| Slug | URL | Uso recomendado |
|------|-----|-----------------|
| state-of-immersive-commerce-capa | https://metakosmos.com.br/wp-content/uploads/2026/03/state-of-immersive-commerce-capa.png | Artigos sobre State of IC, mercado, tendências |
| mk-thumb-10-2 | https://metakosmos.com.br/wp-content/uploads/2026/03/MK-THUMB-10.png | Pilar 1 — Immersive Commerce geral |
| thumb-04-03 | https://metakosmos.com.br/wp-content/uploads/2026/03/thumb-04.03.png | Pilar 3 — RA / 3D |
| thumb-05-03 | https://metakosmos.com.br/wp-content/uploads/2026/03/thumb-05.03.jpg | Pilar 1/3 — visual hero genérico |
| mk-thumb-1 | https://metakosmos.com.br/wp-content/uploads/2026/01/MK-THUMB-1.jpg | Pilar 6 — cases |
| mk-thumb-2-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/MK-THUMB-2.jpg | Pilar 2 — beleza |
| mk-thumb-12 | https://metakosmos.com.br/wp-content/uploads/2025/11/MK-THUMB.jpg | Generic |
| mk-hero-image | https://metakosmos.com.br/wp-content/uploads/2025/07/MK-HERO-IMAGE.jpg | Genérico mK |
| mk-thumb-4-4 | https://metakosmos.com.br/wp-content/uploads/2026/03/MK-THUMB-4.jpg | Pilar 6/7 |
| capa-post | https://metakosmos.com.br/wp-content/uploads/2025/11/capa-post.jpg | Pilar 3 — visualizador |

### Hero por pilar (selecionados)
| Pilar | Slug | URL |
|-------|------|-----|
| P1 — Immersive Commerce | flexform-3D | https://metakosmos.com.br/wp-content/uploads/2025/09/flexform-3D-scaled.png |
| P1 — Immersive Commerce | atencao-e-o-novo-petroleo | https://metakosmos.com.br/wp-content/uploads/2025/09/Atencao-e-o-novo-petroleo.png |
| P1 — Immersive Commerce | interacoes-virtuais-3d | https://metakosmos.com.br/wp-content/uploads/2025/09/Interacoes-Virtuais-se-tornarao-cada-vez-mais-3D.png |
| P1 — Immersive Commerce | 87-marcas-dormindo | https://metakosmos.com.br/wp-content/uploads/2025/09/87-das-marcas-ainda-estao-dormindo-para-essa-revolucao-3D.png |
| P2 — Provador Virtual | mk-beauty-hero-tint | https://metakosmos.com.br/wp-content/uploads/2025/05/MK-BEAUTY-HERO-TINT.mov.png |
| P2 — Provador Virtual | mk-tint-banner | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-TINT-BANNER.png |
| P3 — Visualizador 3D / AR | thumb-04-03 | https://metakosmos.com.br/wp-content/uploads/2026/03/thumb-04.03.png |
| P3 — Visualizador 3D / AR | realidade-aumentada-no-e-commerce-3d-aumenta-vendas-315 | https://metakosmos.com.br/wp-content/uploads/2026/01/Realidade-Aumentada-no-E-commerce-Como-3D-Aumenta-Vendas-em-ate-315.jpg |
| P3 — Visualizador 3D / AR | oculos-ar-c-cenario | https://metakosmos.com.br/wp-content/uploads/2024/12/OCULOS-AR-C-CENARIO.jpg |
| P4 — FOOH e Vídeos IA | thumb-videos-com-ia | https://metakosmos.com.br/wp-content/uploads/2025/12/thumb-videos-com-ia.jpg |
| P4 — FOOH e Vídeos IA | thumbs-loreal-fooh | https://metakosmos.com.br/wp-content/uploads/2024/09/THUMBS-LOREAL-FOOH.jpg |
| P4 — FOOH e Vídeos IA | fooh-4 | https://metakosmos.com.br/wp-content/uploads/2026/03/fooh.jpg |
| P4 — FOOH e Vídeos IA | fooh-5 | https://metakosmos.com.br/wp-content/uploads/2026/03/fooh-1.jpg |
| P5 — Performance | dashboard-de-analytics-consolidado-roi | https://metakosmos.com.br/wp-content/uploads/2026/01/Dashboard-de-analytics-consolidado-para-comprovar-ROI-para-diretoria.png |
| P5 — Performance | metricas-2 | https://metakosmos.com.br/wp-content/uploads/2026/03/metricas.png |
| P6 — Cases | mk-thumb-1 | https://metakosmos.com.br/wp-content/uploads/2026/01/MK-THUMB-1.jpg |
| P6 — Cases | cases-reais | https://metakosmos.com.br/wp-content/uploads/2026/03/Cases-Reais.jpg |
| P7 — Futuro do E-commerce | mk-agente-ia_hero | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-AGENTE-IA_HERO.png |
| P7 — Futuro do E-commerce | mk-tmw-thumb | https://metakosmos.com.br/wp-content/uploads/2024/09/mK-TMW-THUMB.png |

---

## 2. GIFs DE PRODUTO mK (use para H2 que descreve a solução)

GIFs animados curtos demonstrando cada produto. Quando o artigo mencionar um produto mK, **inserir o GIF correspondente como inline image em coluna com texto**.

### mK 3D Shop (visualizador 3D + AR — Pilar 3)
| Slug | URL | Notas |
|------|-----|-------|
| mk-3d-shop-1 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-1.gif | Demo curta 1 |
| mk-3d-shop-2-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-2.gif | Demo curta 2 |
| mk-3d-shop-3-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-3.gif | Demo curta 3 |
| mk-3d-shop-new-3 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-new.gif | Demo HD (2160w) |
| mk-3d-shop-new-4 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-new-1.gif | Demo HD variação |
| mk-3d-shop-3 | https://metakosmos.com.br/wp-content/uploads/2025/07/mK-3D-SHOP.gif | Demo legacy |
| mk3dshop-flexform | https://metakosmos.com.br/wp-content/uploads/2025/08/mK3DShop-Flexform.gif | Demo com cliente Flexform |
| mk3dshop-flexform-site | https://metakosmos.com.br/wp-content/uploads/2025/08/mK3DShop-Flexform-site.gif | Demo Flexform variante |

### mK Beauty (provador virtual de maquiagem — Pilar 2)
| Slug | URL | Notas |
|------|-----|-------|
| mk-beauty-1 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-beauty-1.gif | Demo curta 1 |
| mk-beauty-2-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-beauty-2.gif | Demo curta 2 |
| mk-beauty-3-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-beauty-3.gif | Demo curta 3 |
| mk-beauty-new | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-beauty-new.gif | Demo HD (1920w) |
| mk-beauty-3 | https://metakosmos.com.br/wp-content/uploads/2025/10/MK-BEAUTY-3.gif | Demo legacy |
| mk-beauty-2 | https://metakosmos.com.br/wp-content/uploads/2025/07/mK-BEAUTY.gif | Demo legacy 2 |
| bio-beauty-gif | https://metakosmos.com.br/wp-content/uploads/2025/10/bio-beauty-gif.gif | Demo com Bio Extratus |
| mk-tint-boca-rosa | https://metakosmos.com.br/wp-content/uploads/2025/10/Adobe-Express-mk-TINT-boca-rosa-2.gif | Demo TINT com Boca Rosa |

### mK Fashion+ (provador virtual de moda com IA — Pilar 2)
| Slug | URL | Notas |
|------|-----|-------|
| mk-fashion-1 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-fashion-1.gif | Demo curta 1 |
| mk-fashion-2-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-fashion-2.gif | Demo curta 2 |
| mk-fashion-3-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-fashion-3.gif | Demo curta 3 |
| mk-fashion-4 | https://metakosmos.com.br/wp-content/uploads/2026/01/MK-FASHION-.gif | Demo HD (1920w) |
| mk-fashion-5 | https://metakosmos.com.br/wp-content/uploads/2026/02/mk-fashion.gif | Demo HD variação |
| mk-fashion-2 | https://metakosmos.com.br/wp-content/uploads/2025/07/mK-FASHION.gif | Demo legacy |
| shop-the-look-mk | https://metakosmos.com.br/wp-content/uploads/2026/02/shop-the-look-mk.gif | Demo Shop The Look |
| osklen-shop-the-look | https://metakosmos.com.br/wp-content/uploads/2025/12/osklen-shop-the-look-gif.gif | Demo Shop The Look com Osklen |

### mK Spaces (tour 360° / espaços virtuais — Pilar 1/7)
| Slug | URL | Notas |
|------|-----|-------|
| mk-spaces-1 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-spaces-1.gif | Demo curta 1 |
| mk-spaces-2-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-spaces-2.gif | Demo curta 2 |
| mk-spaces-3-2 | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-spaces-3.gif | Demo curta 3 |
| mk-spaces-2 | https://metakosmos.com.br/wp-content/uploads/2025/07/mK-SPACES.gif | Demo legacy |
| mk-spaces-tour-virtual | https://metakosmos.com.br/wp-content/uploads/2024/10/mK-Spaces-Tour-Virtual-de-Ambientes.jpg | Imagem estática |
| mk-mk-spaces-dispositivos | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-MK-SPACES-DISPOSITIVOS.png | Multi-device mockup |
| conviva-tourvirtual | https://metakosmos.com.br/wp-content/uploads/2024/11/conviva-tourvirtual.gif | Demo com cliente Conviva |

### mK 3D Ads (Pilar 4 — vídeos publicitários com 3D)
| Slug | URL |
|------|-----|
| mk-mk-3d-ads_1 | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MK-3D-ADS_1.png |
| mk-mk-3d-ads_2 | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MK-3D-ADS_2.png |
| mk-mk-3d-ads_3 | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MK-3D-ADS_3.png |

### mK Agentes IA (Pilar 7 — Agentic Commerce)
| Slug | URL |
|------|-----|
| mk-agentes-ia-hero-mockup | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-AGENTES-IA-HERO-MOCKUP.png |
| mk-agentes-ia-hotel | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-AGENTES-IA-HOTEL.png |
| mk-agentes-ia-emagrecimento | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-AGENTES-IA-EMAGRECIMENTO.png |
| mk-agentes-ia-carros | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-AGENTES-IA-CARROS.png |
| agentes-ia-whatsapp | https://metakosmos.com.br/wp-content/uploads/2024/11/Agentes-IA-Whatsapp.jpg |
| mk-agentes-ia-grafico-tempo-resposta | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-AGENTES-IA-GRAFICO-TEMPO-DE-RESPOSTA.png |

### AI Shooting (Pilar 4 — sessões de fotos com IA + 3D)
| Slug | URL | Notas |
|------|-----|-------|
| ai-shooting-exemplo-1 | https://metakosmos.com.br/wp-content/uploads/2026/04/ai-shooting-exemplo-1.png | Exemplo de produção AI |
| GOOD-TO-WOOW | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW.gif | Slogan animado |

---

## 3. mKASES — IMAGENS POR CLIENTE

Quando o artigo cita um cliente como mKase, usar uma destas imagens **e linkar** o nome do cliente para a URL do mKase em `/mkases/[slug]/` (ver `blog-links.md`).

### Beauty / Cosméticos
| Cliente | Slug | URL |
|---------|------|-----|
| **Boca Rosa** | Boca-Rosa_Bianca-Andrade | https://metakosmos.com.br/wp-content/uploads/2024/07/Boca-Rosa_Bianca-Andrade-768x512-1.webp |
| Boca Rosa | thumb-lancamento-boca-rosa | https://metakosmos.com.br/wp-content/uploads/2025/09/thumb-lancamento-Boca-Rosa.jpg |
| Boca Rosa | thumb-lancamento-boca-rosa-2 | https://metakosmos.com.br/wp-content/uploads/2025/09/thumb-lancamento-Boca-Rosa-1.jpg |
| Boca Rosa | mk-tint-boca-rosa | https://metakosmos.com.br/wp-content/uploads/2025/10/Adobe-Express-mk-TINT-boca-rosa-2.gif |
| **Bio Extratus** | Bio-Extratus | https://metakosmos.com.br/wp-content/uploads/2025/12/Bio-Extratus.png |
| Bio Extratus | bio-beauty-gif | https://metakosmos.com.br/wp-content/uploads/2025/10/bio-beauty-gif.gif |
| Bio Extratus | bioextratus-fooh-gif | https://metakosmos.com.br/wp-content/uploads/2025/04/bioextratus-fooh-gif.gif |
| **L'Oréal** | loreal-inoa-ar | https://metakosmos.com.br/wp-content/uploads/2025/12/loreal-inoa-ar.gif |
| L'Oréal | thumbs-loreal-filtro | https://metakosmos.com.br/wp-content/uploads/2024/09/THUMBS-LOREAL-FILTRO.jpg |
| L'Oréal | thumbs-loreal-fooh | https://metakosmos.com.br/wp-content/uploads/2024/09/THUMBS-LOREAL-FOOH.jpg |
| L'Oréal | lorealfooh-gif | https://metakosmos.com.br/wp-content/uploads/2024/07/lorealfooh-gif.gif |
| **Avon** | thumbs-avon-filtro-ar | https://metakosmos.com.br/wp-content/uploads/2024/09/THUMBS-AVON-FILTRO-AR.jpg |
| **Mascavo** | mascavo-gif | https://metakosmos.com.br/wp-content/uploads/2025/09/mascavo-gif.gif |
| Mascavo | thumb-instrucoes-mascavo | https://metakosmos.com.br/wp-content/uploads/2025/09/thumb-instrucoes-Mascavo.jpg |
| **Adcos** (provador virtual) | — | usar mK Beauty GIFs |

### Móveis / Decoração / Casa
| Cliente | Slug | URL |
|---------|------|-----|
| **Flexform** | flexform-3D | https://metakosmos.com.br/wp-content/uploads/2025/09/flexform-3D-scaled.png |
| Flexform | mK3DShop-Flexform | https://metakosmos.com.br/wp-content/uploads/2025/08/mK3DShop-Flexform.gif |
| Flexform | mK3DShop-Flexform-site | https://metakosmos.com.br/wp-content/uploads/2025/08/mK3DShop-Flexform-site.gif |
| **Innerhaus** | (4 mídias disponíveis — buscar via API) | search=innerhaus |
| **Conviva** | conviva-tourvirtual | https://metakosmos.com.br/wp-content/uploads/2024/11/conviva-tourvirtual.gif |

### Moda / Calçados / Acessórios
| Cliente | Slug | URL |
|---------|------|-----|
| **Osklen** | osklen | https://metakosmos.com.br/wp-content/uploads/2026/02/osklen.gif |
| Osklen | osklen-shop-the-look | https://metakosmos.com.br/wp-content/uploads/2025/12/osklen-shop-the-look-gif.gif |
| **Gregory** | gregory-2 | https://metakosmos.com.br/wp-content/uploads/2026/02/gregory.gif |
| **Redley** (9 mídias) | mk-thumb-redley | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-THUMB-REDLEY.jpg |
| **Grendene** | grendene-fooh-gif | https://metakosmos.com.br/wp-content/uploads/2025/09/grendene-fooh-gif.gif |
| **Karen Bachini** | (2 mídias — buscar via API) | search=karen-bachini |
| **Stanley** | stanley-gif | https://metakosmos.com.br/wp-content/uploads/2026/01/stanley-gif.gif |
| Stanley | mariana-camargo-stanley | https://metakosmos.com.br/wp-content/uploads/2026/01/mariana-camargo-stanley.jpg |

### Auto / Mobilidade
| Cliente | Slug | URL |
|---------|------|-----|
| **GM** (General Motors) | GM-3D-Capa | https://metakosmos.com.br/wp-content/uploads/2024/10/GM-3D-Capa.jpg |
| GM | GM-GIF | https://metakosmos.com.br/wp-content/uploads/2026/01/GM-GIF.gif |
| GM | gm-fooh-gif | https://metakosmos.com.br/wp-content/uploads/2025/04/gm-fooh-gif.gif |
| GM | paulo-luciano-lopes-gm | https://metakosmos.com.br/wp-content/uploads/2024/10/Paulo-Luciano-Lopes-GM.jpeg |
| **Mitsubishi** | (2 mídias — buscar via API) | search=mitsubishi |
| **Stellantis** / Fiat | (simuladores — sitemap) | /simulador-fiatstrada/ |

### Brinquedos / Entretenimento / Bebidas
| Cliente | Slug | URL |
|---------|------|-----|
| **Heineken** | heineken | https://metakosmos.com.br/wp-content/uploads/2025/12/heineken.gif |
| Heineken (4 mídias) | search=heineken | — |
| **Anasol** | anasol | https://metakosmos.com.br/wp-content/uploads/2026/03/anasol.gif |
| **Globo** | GLOBO | https://metakosmos.com.br/wp-content/uploads/2026/02/GLOBO.gif |
| **Multishow** / UFC | (2 mídias cada — buscar via API) | search=multishow / search=ufc |

### B2B / Outros
| Cliente | Slug | URL |
|---------|------|-----|
| **Statkraft** (energia) | statkraft01 | https://metakosmos.com.br/wp-content/uploads/2024/09/statkraft01.gif |
| Statkraft | statkraft02 | https://metakosmos.com.br/wp-content/uploads/2024/09/statkraft02.gif |
| **Reenergisa** | (2 mídias — buscar via API) | search=reenergisa |
| **Serasa** (2 mídias) | search=serasa | — |
| **Mercado Pago** | (1 mídia — buscar via API) | search=mercado-pago |
| **Betnacional** (3 mídias) | search=betnacional | — |
| **Montreal** | mk-thumb-montreal | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-THUMB-MONTREAL.jpg |

---

## 4. INFOGRÁFICOS / DADOS VISUAIS

Para H2s sobre métricas, ROI, comparativos. Usar como imagem full-width após parágrafo de dados.

| Slug | Tema | URL |
|------|------|-----|
| metricas-2 | Dashboard de métricas IC | https://metakosmos.com.br/wp-content/uploads/2026/03/metricas.png |
| dashboard-de-analytics-consolidado-roi | Dashboard ROI consolidado | https://metakosmos.com.br/wp-content/uploads/2026/01/Dashboard-de-analytics-consolidado-para-comprovar-ROI-para-diretoria.png |
| dashboard-de-analytics-consolidado | Dashboard analytics simples | https://metakosmos.com.br/wp-content/uploads/2025/09/Dashboard-de-analytics-consolidado.png |
| roi-esperado | ROI esperado por categoria | https://metakosmos.com.br/wp-content/uploads/2026/01/ROI-esperado_-o-que-projetos-bem-implementados-entregam.jpg |
| cases-reais | Cards de cases reais | https://metakosmos.com.br/wp-content/uploads/2026/03/Cases-Reais.jpg |
| categorias-ra-funciona | Quais categorias RA funciona | https://metakosmos.com.br/wp-content/uploads/2026/03/Para-Quais-Categorias-de-Produto-a-Realidade-Aumentada-Funciona.png |
| paginas-imersivas-conceito | O que são páginas imersivas | https://metakosmos.com.br/wp-content/uploads/2026/03/O-que-sao-paginas-de-produto-imersivas.jpg |
| paginas-imersivas-pratica | Como aplicar páginas imersivas | https://metakosmos.com.br/wp-content/uploads/2026/03/Como-aplicar-paginas-de-produto-imersivas-na-pratica.jpg |
| poc-proof-concept | Por que começar com POC | https://metakosmos.com.br/wp-content/uploads/2026/01/Por-que-toda-implementacao-comeca-com-um-POC-Proof-of-Concept.jpg |
| custo-poc-3d | Quanto custa POC | https://metakosmos.com.br/wp-content/uploads/2026/01/Quanto-custa-implementar-um-POC-de-Visualizador-3D.jpg |
| melhores-praticas-implementacao | Melhores práticas | https://metakosmos.com.br/wp-content/uploads/2026/01/Melhores-Praticas-para-Implementacao-Bem-Sucedida.jpg |
| erros-comuns-3d | Erros comuns implementação | https://metakosmos.com.br/wp-content/uploads/2026/01/Erros-Comuns-ao-Implementar-Visualizadores-3D-e1769027830264.jpg |
| mk-infografico-vr-eventos | Infográfico VR em eventos | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-VR-EM-EVENTOS-scaled.jpg |
| mk-infografico-video-3d | Infográfico vídeo 3D | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-VIDEO-3D-scaled.jpg |
| mk-infografico-fooh | Infográfico FOOH | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-FOOH-scaled.jpg |
| mk-infografico-filtro-ar | Infográfico filtro AR | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-FILTRO-AR-scaled.jpg |
| mk-infografico-tint | Infográfico mK TINT | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-TINT-scaled.jpg |
| mk-infografico-tmw | Infográfico TMW | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-TMW-scaled.jpg |
| mk-tint-dashboard | Dashboard TINT | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-TINT-DASHBOARD.png |
| mk-mk-3d-shop-dashboard | Dashboard mK 3D Shop | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-MK-3D-SHOP-DASHBOARD-1.png |
| mk-mk-3d-shop-roi | ROI mK 3D Shop | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MK-3D-SHOP-ROI.png |
| relatorio-de-analytics | Relatório de analytics | https://metakosmos.com.br/wp-content/uploads/2025/01/Relatorio-de-analytics.jpg |
| mk-tint-real-vs-filtro | Comparativo real vs filtro | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-TINT-REAL-VS-FILTRO.png |
| mk-agentes-ia-grafico-tentativas | Gráfico tentativas Agentes IA | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-AGENTES-IA-GRAFICO-NUMERO-DE-TENTATIVAS.png |
| mk-agentes-ia-grafico-tempo | Gráfico tempo resposta Agentes IA | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-AGENTES-IA-GRAFICO-TEMPO-DE-RESPOSTA.png |

---

## 5. AR / RA / TECNOLOGIAS IMERSIVAS

| Slug | Uso | URL |
|------|-----|-----|
| Realidade-Aumentada-sofda | Hero AR/sofá | https://metakosmos.com.br/wp-content/uploads/2026/03/Realidade-Aumentada-sofda.png |
| oculos-ar-c-cenario | AR óculos no cenário | https://metakosmos.com.br/wp-content/uploads/2024/12/OCULOS-AR-C-CENARIO.jpg |
| filtros-ar-press-kits | Filtros AR press kits | https://metakosmos.com.br/wp-content/uploads/2026/02/FILTROS-AR-PARA-PRESS-KITS-E-PDV.gif |
| filtros-sociais-ar-lanc | Filtros AR sociais | https://metakosmos.com.br/wp-content/uploads/2025/08/Filtros-sociais-AR-lanc.gif |
| MK-SERVICOS-AR | Serviços AR mK | https://metakosmos.com.br/wp-content/uploads/2025/07/MK-SERVICOS-AR.gif |
| Espelho-Magico-PDV | Espelho mágico PDV | https://metakosmos.com.br/wp-content/uploads/2025/10/Espelho-Magico-para-PDV.gif |
| post-mk1 | Post mK 1 GIF | https://metakosmos.com.br/wp-content/uploads/2025/11/post-mk1.gif |
| post-mk2 | Post mK 2 GIF | https://metakosmos.com.br/wp-content/uploads/2025/11/post-mk2-e1762785293224.gif |

---

## 6. FOOH / VÍDEOS COM IA (Pilar 4)

| Slug | Uso | URL |
|------|-----|-----|
| fooh-4 | FOOH cena urbana | https://metakosmos.com.br/wp-content/uploads/2026/03/fooh.jpg |
| fooh-5 | FOOH cena urbana 2 | https://metakosmos.com.br/wp-content/uploads/2026/03/fooh-1.jpg |
| videos-fooh-ia-animacoes-3d | Vídeos FOOH IA animações | https://metakosmos.com.br/wp-content/uploads/2026/02/VIDEOS-FOOH-E-IA-ANIMACOES-3D.gif |
| videos-fooh-ia-animacoes-3d-2 | Variação | https://metakosmos.com.br/wp-content/uploads/2026/02/VIDEOS-FOOH-E-IA-ANIMACOES-3D-1.gif |
| thumb-videos-com-ia | Hero vídeos com IA | https://metakosmos.com.br/wp-content/uploads/2025/12/thumb-videos-com-ia.jpg |
| Duolingo | FOOH Duolingo | https://metakosmos.com.br/wp-content/uploads/2025/12/Duolingo.png |
| MK-THUMB-videos | Thumb vídeos | https://metakosmos.com.br/wp-content/uploads/2025/11/MK-THUMB.jpg |
| Gemini-FOOH-guia | FOOH guia abertura | https://metakosmos.com.br/wp-content/uploads/2025/08/Gemini_Generated_Image_bhmfi1bhmfi1bhmf-scaled.png |
| Screenshot-videos-IA | Screenshot vídeos IA | https://metakosmos.com.br/wp-content/uploads/2026/03/Screenshot-2026-03-02-154202.png |

---

## 7. DEPOIMENTOS / FOTOS DE PESSOAS

Quando incluir citação direta de cliente como blockquote, anexar foto da pessoa.

| Pessoa | Empresa | URL |
|--------|---------|-----|
| Stephanie Tardin | L'Oréal Professionnel | https://metakosmos.com.br/wp-content/uploads/2025/07/Stephanie-Tardin-Loreal.jpeg |
| Hugo Linhares | L'Oréal | https://metakosmos.com.br/wp-content/uploads/2025/12/hugo-linhares-loreal.png |
| Guilherme Monteagudo | Jotacom | https://metakosmos.com.br/wp-content/uploads/2025/07/Guilherme-Monteagudo-Jotacom.jpeg |
| Elaine Monteiro | Globo | https://metakosmos.com.br/wp-content/uploads/2025/07/Elaine-Monteiro-Globo.jpeg |
| Fernando Bernardo | Boca Rosa | https://metakosmos.com.br/wp-content/uploads/2025/07/Fernando-Bernardo-Boca-Rosa.jpeg |
| Mônica Marien | Grupo S2 | https://metakosmos.com.br/wp-content/uploads/2025/07/Monica-Marien-Grupo-S2.png |
| Paulo Luciano Lopes | GM | https://metakosmos.com.br/wp-content/uploads/2024/10/Paulo-Luciano-Lopes-GM.jpeg |
| Flávia Zulzke | (cliente) | https://metakosmos.com.br/wp-content/uploads/2025/08/Flavia_Zulzke.jpg |
| Daniela Giannoni | Droga5 | https://metakosmos.com.br/wp-content/uploads/2026/02/Daniela-Giannoni-droga5.jpg |
| Mariana Camargo | Stanley | https://metakosmos.com.br/wp-content/uploads/2026/01/mariana-camargo-stanley.jpg |
| Celso Bastos | Bio Extratus | https://metakosmos.com.br/wp-content/uploads/2025/12/celso-bastos-bio-extratus.jpg |
| Guilherme | (cliente) | https://metakosmos.com.br/wp-content/uploads/2026/01/Guilherme.png |

**Bonus:** Vídeo de depoimento VTEX Day:
- thumb: https://metakosmos.com.br/wp-content/uploads/2025/09/thumb-depoimento-no-VTEX-day.jpg

---

## 8. LOGOS, BRANDING E SELOS

Use somente quando o artigo precisar mostrar parceria (ex: "integrado a VTEX e Wake").

| Asset | URL |
|-------|-----|
| MK Logo branco | https://metakosmos.com.br/wp-content/uploads/2025/01/MK-WHITE.png |
| MK Logo preto | https://metakosmos.com.br/wp-content/uploads/2025/08/MK-BLACK-LOGO.png |
| MK Logo branco SVG | https://metakosmos.com.br/wp-content/uploads/2026/03/MK-WHITE.svg |
| MK Fashion+ Logo branco | https://metakosmos.com.br/wp-content/uploads/2026/02/MK-FASHION-BRANCA.png |
| mK 3D Shop Logo branco | https://metakosmos.com.br/wp-content/uploads/2025/06/MK-3D-SHOP-WHITE.png |
| mK Spaces Logo branco | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-SPACES-BRANCO.png |
| Selo VTEX | https://metakosmos.com.br/wp-content/uploads/2025/09/VTEX-SELO-scaled.jpg |
| Selo Wake | https://metakosmos.com.br/wp-content/uploads/2025/09/WAKE-SELO-scaled.jpg |
| Selo Google | https://metakosmos.com.br/wp-content/uploads/2025/09/GOOGLE-SELO-scaled.jpg |
| Selo Snap | https://metakosmos.com.br/wp-content/uploads/2025/09/SNAP-SELO-scaled.jpg |
| Selo Linx | https://metakosmos.com.br/wp-content/uploads/2025/09/LINX-SELO-scaled.jpg |
| Selo NPS | https://metakosmos.com.br/wp-content/uploads/2024/12/selo-nfs-2-1.png |
| Cartela parceiros desktop | https://metakosmos.com.br/wp-content/uploads/2026/02/partners-desktop-jan26-1.png |
| Cartela parceiros mobile | https://metakosmos.com.br/wp-content/uploads/2026/02/partners-mobile-jan26.png |
| Cartela logos mK Beauty | https://metakosmos.com.br/wp-content/uploads/2025/08/cartela-de-logos-mk-beauty-NEW.png |
| Clientes (logos consolidados) | https://metakosmos.com.br/wp-content/uploads/2025/09/Clientes.png |

---

## 9. CONTEÚDO ESTRATÉGICO MARCANTE

| Slug | Tema | URL |
|------|------|-----|
| Atencao-e-o-novo-petroleo | Conceito atenção como petróleo | https://metakosmos.com.br/wp-content/uploads/2025/09/Atencao-e-o-novo-petroleo.png |
| 87-marcas-dormindo | 87% das marcas dormindo | https://metakosmos.com.br/wp-content/uploads/2025/09/87-das-marcas-ainda-estao-dormindo-para-essa-revolucao-3D.png |
| Interacoes-Virtuais-3D | Interações virtuais 3D | https://metakosmos.com.br/wp-content/uploads/2025/09/Interacoes-Virtuais-se-tornarao-cada-vez-mais-3D.png |
| Mark | Mark Zuckerberg (visão de futuro) | https://metakosmos.com.br/wp-content/uploads/2025/09/Mark.png |
| state-of-immersive-commerce-capa | State of IC capa | https://metakosmos.com.br/wp-content/uploads/2026/03/state-of-immersive-commerce-capa.png |
| GOOD-TO-WOOW | "From Good to WooW" GIF | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW.gif |
| render-cadeira | Render cadeira 3D | https://metakosmos.com.br/wp-content/uploads/2026/03/render-cadeira.jpg |

---

## Como buscar mídia adicional (REST API)

Quando precisar de mídia que não esteja listada aqui:

```bash
# Buscar por termo no slug ou alt
curl "https://metakosmos.com.br/wp-json/wp/v2/media?search=[termo]&per_page=20&_fields=id,slug,source_url,mime_type,alt_text"

# Por exemplo:
curl "https://metakosmos.com.br/wp-json/wp/v2/media?search=karen-bachini&per_page=10"
curl "https://metakosmos.com.br/wp-json/wp/v2/media?search=heineken&per_page=10"
curl "https://metakosmos.com.br/wp-json/wp/v2/media?search=innerhaus&per_page=10"
```

---

**Última atualização:** 2026-04-28 (catálogo expandido via REST API)
**Total no WP:** 996 mídias (916 imagens utilizáveis ≥400px)
**Listadas neste arquivo:** ~250 mídias curadas para uso em artigos de blog

---

<!-- AUTO-CATALOG-START -->
## CATÁLOGO DE MÍDIAS (auto-gerado do banco em 2026-05-28 10:17)

Total no banco: **2291 mídias** | Avaliadas visualmente: **8**

> Este bloco é gerado por `render_views.py`. Não editar à mão (será sobrescrito).
> Score: 0-5. `[V]` = avaliação visual minha, `[h]` = heurística por metadados.
> Para reavaliar, rode `evaluate_media.py`.

### Hero / Capa (destaque após H1) (40)

| Score | Slug | Brand | Melhor uso | URL |
|-------|------|-------|------------|-----|
| 5V | thumb-04-03 |  | Hero ideal para Pilar 3 (Visualizador 3D + AR). Mostra picape, cadeira | https://metakosmos.com.br/wp-content/uploads/2026/03/thumb-04.03.png |
| 4h | mk-hero-image-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/MK-HERO-IMAGE.jpg |
| 4h | state-of-immersive-commerce-capa |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/state-of-immersive-commerce-capa.png |
| 4V | thumb-05-03 |  | Hero generico de produto 3D em tela de notebook (cadeira gamer). Bom p | https://metakosmos.com.br/wp-content/uploads/2026/03/thumb-05.03.jpg |
| 4V | mk-thumb-1 |  | Hero generico de produto 3D em tela de desktop (tenis). Bom para Pilar | https://metakosmos.com.br/wp-content/uploads/2026/01/MK-THUMB-1.jpg |
| 4h | thumb-videos-com-ia |  |  | https://metakosmos.com.br/wp-content/uploads/2025/12/thumb-videos-com-ia.jpg |
| 4h | mk-thumb-12 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/11/MK-THUMB.jpg |
| 4h | capa-post |  |  | https://metakosmos.com.br/wp-content/uploads/2025/11/capa-post.jpg |
| 4h | mk-3d-ads-hero |  |  | https://metakosmos.com.br/wp-content/uploads/2025/09/mK-3D-Ads-Hero.mp4 |
| 4h | hero-mk-3d-ads |  |  | https://metakosmos.com.br/wp-content/uploads/2025/09/Hero-mK-3D-Ads.mp4 |
| 4h | mk-reel-thumb |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/MK-REEL-THUMB.jpg |
| 4h | thumb-no-que-acreditamos |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/THUMB-NO-QUE-ACREDITAMOS.jpg |
| 4h | thumb-solucoes-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/THUMB-SOLUCOES.jpg |
| 4h | thumb-solucoes |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/THUMB-SOLUCOES.jpg |
| 4h | thumb-mitologia |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/THUMB-MITOLOGIA.jpg |
| 4h | mk-beauty-hero-tint-mov |  |  | https://metakosmos.com.br/wp-content/uploads/2025/05/MK-BEAUTY-HERO-TINT.mov.png |
| 4h | mk-thumb-11 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/12/MK-THUMB.jpg |
| 4h | gm-3d-capa | GM |  | https://metakosmos.com.br/wp-content/uploads/2024/10/GM-3D-Capa.jpg |
| 4h | mk-tint-thumb |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-TINT-THUMB.jpg |
| 4h | mk-tmw-thumb-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-TMW-THUMB.jpg |
| 4h | mk-mk-3d-ads_hero |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MK-3D-ADS_HERO.mov |
| 4h | mk-mk-3d-shop_hero |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MK-3D-SHOP_HERO.mov |
| 4h | mk-mkspaces_hero |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MKSPACES_HERO.mov |
| 4h | mk-hero-tint |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-HERO-TINT.mov |
| 4h | thumbs-loreal-fooh | L'Oréal |  | https://metakosmos.com.br/wp-content/uploads/2024/09/THUMBS-LOREAL-FOOH.jpg |
| 4h | thumbs-loreal-filtro | L'Oréal |  | https://metakosmos.com.br/wp-content/uploads/2024/09/THUMBS-LOREAL-FILTRO.jpg |
| 4h | thumbs-avon-filtro-ar | Avon |  | https://metakosmos.com.br/wp-content/uploads/2024/09/THUMBS-AVON-FILTRO-AR.jpg |
| 4h | mk-thumb-montreal-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-THUMB-montreal-1.jpg |
| 4h | mk-thumb-10 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-THUMB.jpg |
| 4h | mk-thumb-montreal |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-THUMB-MONTREAL.jpg |
| 4h | mk-thumb-redley | Redley |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-THUMB-REDLEY.jpg |
| 4h | mk-thumb-5-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/05/VR-office.jpg |
| 4h | mk-thumb-4-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/05/VR-LP.jpg |
| 4h | mk-thumb-6 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/04/MK-THUMB.jpg |
| 4h | mitsubishi-thumb |  |  | https://metakosmos.com.br/wp-content/uploads/2024/03/mitsubishi-thumb.jpg |
| 4h | mk-thumb-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/03/MK-THUMB.jpg |
| 4h | mk-thumb-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/02/MK-THUMB.jpg |
| 4h | mk-thumb-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/MK-THUMB-2.jpg |
| 4h | vogue-covers |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/vogue-covers.png |
| 4h | mk-thumb-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/MK-THUMB-1.jpg |

### GIFs de produto / demos (50)

| Score | Slug | Brand | Melhor uso | URL |
|-------|------|-------|------------|-----|
| 5h | mk-3d-shop-new-6 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/mk-3d-shop-new.gif |
| 5h | mk-fashion-4-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/MK-FASHION-.gif |
| 5h | mk-fashion-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/MK-FASHION-.gif |
| 5h | mk-beauty-new-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-beauty-new.gif |
| 5h | mk-beauty-new |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-beauty-new.gif |
| 5h | mk-3d-shop-new-4-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-new-1.gif |
| 5h | mk-3d-shop-new-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-new-1.gif |
| 5h | mk-3d-shop-new-3-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-new.gif |
| 5h | mk-3d-shop-new-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-3d-shop-new.gif |
| 5h | shop-the-look-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/Shop-The-Look.gif |
| 5h | shop-the-look |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/Shop-The-Look.gif |
| 5h | good-woow-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-WOOW.gif |
| 5h | good-woow |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-WOOW.gif |
| 5h | good-to-woow-2-2-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW-2.gif |
| 5h | good-to-woow-2-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW-2.gif |
| 5h | good-to-woow-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW.gif |
| 5h | good-to-woow |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW.gif |
| 4h | mk-gifs-4-9x16-v1-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/MK-GIFs-4-9x16-V1-4.mp4 |
| 4h | mk-gifs-4-9x16-v1-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/MK-GIFs-4-9x16-V1-3.mp4 |
| 4h | mk-gifs-4-9x16-v1-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/MK-GIFs-4-9x16-V1-2.mp4 |
| 4h | mk-gifs-4-9x16-v1-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/MK-GIFs-4-9x16-V1-1.mp4 |
| 4h | mk-gifs-4-9x16-v1 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/MK-GIFs-4-9x16-V1.mp4 |
| 4h | mk-spaces-2-1 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/mk-spaces-2-1.gif |
| 4h | mk-spaces-2-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/mk-spaces-2.gif |
| 4h | 3h-c-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/03/3h-c.gif |
| 4h | csi-gif-1-1-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/csi-gif-1-1.gif |
| 4h | mitsubishi-portas-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/03/mitsubishi-portas.gif |
| 4h | avon-ai-3-2 | Avon |  | https://metakosmos.com.br/wp-content/uploads/2024/02/AVON-AI-3.gif |
| 4h | 1-14 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/02/1.gif |
| 4h | conviva-virtualtour |  |  | https://metakosmos.com.br/wp-content/uploads/2024/11/conviva-tourvirtual.gif |
| 4h | redley-try-on-gif-3-1 | Redley |  | https://metakosmos.com.br/wp-content/uploads/2024/09/Provador-Redley-gif-3-1.gif |
| 4h | 1024-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/1024.gif |
| 4h | shop-the-look-mk |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/shop-the-look-mk.gif |
| 4h | mk-fashion-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/mk-fashion.gif |
| 4h | videos-fooh-e-ia-animacoes-3d-2-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/VIDEOS-FOOH-E-IA-ANIMACOES-3D-1.gif |
| 4h | videos-fooh-e-ia-animacoes-3d-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/VIDEOS-FOOH-E-IA-ANIMACOES-3D-1.gif |
| 4h | videos-fooh-e-ia-animacoes-3d-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/VIDEOS-FOOH-E-IA-ANIMACOES-3D.gif |
| 4h | videos-fooh-e-ia-animacoes-3d |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/VIDEOS-FOOH-E-IA-ANIMACOES-3D.gif |
| 4h | ativacoes-xr-em-eventos-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/ATIVACOES-XR-EM-EVENTOS.gif |
| 4h | ativacoes-xr-em-eventos |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/ATIVACOES-XR-EM-EVENTOS.gif |
| 4h | filtros-ar-para-press-kits-e-pdv-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/FILTROS-AR-PARA-PRESS-KITS-E-PDV.gif |
| 4h | filtros-ar-para-press-kits-e-pdv |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/FILTROS-AR-PARA-PRESS-KITS-E-PDV.gif |
| 4h | tour-virtual-e-showroom-imersivos-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/TOUR-VIRTUAL-E-SHOWROOM-IMERSIVOS.gif |
| 4h | tour-virtual-e-showroom-imersivos |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/TOUR-VIRTUAL-E-SHOWROOM-IMERSIVOS.gif |
| 4h | mk-beauty-2-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-beauty-2.gif |
| 4h | mk-spaces-2-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mk-spaces-2.gif |
| 4h | good-to-woow-2-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW-1-scaled.gif |
| 4h | good-to-woow-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/GOOD-TO-WOOW-1-scaled.gif |
| 4h | mk-mk-3d-ads-rolex-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/09/MK-MK-3D-ADS-ROLEX.gif |
| 4h | mk-mk-3d-ads-one-plus-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/09/MK-MK-3D-ADS-ONE-PLUS.gif |

### Infográficos / dashboards (20)

| Score | Slug | Brand | Melhor uso | URL |
|-------|------|-------|------------|-----|
| 5h | roi-esperado_-o-que-projetos-bem-impleme |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/ROI-esperado_-o-que-projetos-bem-implementados-entregam.jpg |
| 4h | metricas-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/metricas.png |
| 4V | mk-thumb-10-2 |  | Card de KPIs com bordas neon (+94% conversao, -28% devolucoes, +32% ti | https://metakosmos.com.br/wp-content/uploads/2026/03/MK-THUMB-10.png |
| 4h | dashboard-de-analytics-consolidado-para- |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/Dashboard-de-analytics-consolidado-para-comprovar-ROI-para-diretoria.png |
| 4h | business-intelligence-dashboard |  |  | https://metakosmos.com.br/wp-content/uploads/2025/01/Business-intelligence-dashboard.mp4 |
| 3h | dashboard-de-analytics-consolidado |  |  | https://metakosmos.com.br/wp-content/uploads/2025/09/Dashboard-de-analytics-consolidado.png |
| 3h | mk-verso-infografico |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-VERSO-INFOGRAFICO-scaled.jpg |
| 3h | mk-infografico-vr-em-eventos |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-VR-EM-EVENTOS-scaled.jpg |
| 3h | mk-infografico-video-3d |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-VIDEO-3D-scaled.jpg |
| 3h | mk-infografico-tmw |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-TMW-scaled.jpg |
| 3h | mk-infografico-tint |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-TINT-scaled.jpg |
| 3h | mk-infografico-fooh |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-FOOH-scaled.jpg |
| 3h | mk-infografico-filtro-ar |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-INFOGRAFICO-FILTRO-AR-scaled.jpg |
| 3h | mk-agentes-ia-grafico-numero-de-tentativ |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-AGENTES-IA-GRAFICO-NUMERO-DE-TENTATIVAS.png |
| 3h | mk-tint-dashboard-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-TINT-DASHBOARD.png |
| 3h | mk-tmw-dashboard |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-TMW-DASHBOARD.png |
| 3h | mk-mk-3d-shop-dashboard-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/10/MK-MK-3D-SHOP-DASHBOARD-1.png |
| 3h | mk-mk-3d-shop-roi |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-MK-3D-SHOP-ROI.png |
| 3h | mk-tint-dashboard |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/MK-TINT-DASHBOARD.png |
| 3h | dashboard |  |  | https://metakosmos.com.br/wp-content/uploads/2023/10/dashboard.jpg |

### Depoimentos / fotos de pessoas (20)

| Score | Slug | Brand | Melhor uso | URL |
|-------|------|-------|------------|-----|
| 4h | daniela-giannoni-droga5 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/Daniela-Giannoni-droga5.jpg |
| 4h | mariana-camargo-stanley | Stanley |  | https://metakosmos.com.br/wp-content/uploads/2026/01/mariana-camargo-stanley.jpg |
| 4h | guilherme |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/Guilherme.png |
| 3h | hugo-linhares-loreal | L'Oréal |  | https://metakosmos.com.br/wp-content/uploads/2025/12/hugo-linhares-loreal.png |
| 3h | celso-bastos-bio-extratus | Bio Extratus |  | https://metakosmos.com.br/wp-content/uploads/2025/12/celso-bastos-bio-extratus.jpg |
| 3h | thumb-depoimento-no-vtex-day |  |  | https://metakosmos.com.br/wp-content/uploads/2025/09/thumb-depoimento-no-VTEX-day.jpg |
| 3h | depoimento-no-vtex-day |  |  | https://metakosmos.com.br/wp-content/uploads/2025/09/depoimento-no-VTEX-day.mp4 |
| 3h | fernando-chavarro |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Fernando-Chavarro.png |
| 3h | fernando-bernardo-boca-rosa-2 | Boca Rosa |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Fernando-Bernardo-Boca-Rosa.jpeg |
| 3h | fernando-bernardo-boca-rosa | Boca Rosa |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Fernando-Bernardo-Boca-Rosa.jpeg |
| 3h | stephanie-tardin-loreal-2 | L'Oréal |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Stephanie-Tardin-Loreal.jpeg |
| 3h | stephanie-tardin-loreal | L'Oréal |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Stephanie-Tardin-Loreal.jpeg |
| 3h | fernando-santana-lean-agency-betnacional |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Fernando-Santana-Lean-Agency-Betnacional.jpeg |
| 3h | fernando-santana-lean-agency-betnacional |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Fernando-Santana-Lean-Agency-Betnacional.jpeg |
| 3h | guilherme-monteagudo-jotacom-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Guilherme-Monteagudo-Jotacom.jpeg |
| 3h | guilherme-monteagudo-jotacom |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Guilherme-Monteagudo-Jotacom.jpeg |
| 3h | elaine-monteiro-globo-2 | Globo |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Elaine-Monteiro-Globo.jpeg |
| 3h | elaine-monteiro-globo | Globo |  | https://metakosmos.com.br/wp-content/uploads/2025/07/Elaine-Monteiro-Globo.jpeg |
| 3h | mariana |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/mariana.png |
| 3h | fernando |  |  | https://metakosmos.com.br/wp-content/uploads/2023/09/fernando.jpg |

### Imagens inline (corpo do artigo) (60)

| Score | Slug | Brand | Melhor uso | URL |
|-------|------|-------|------------|-----|
| 5h | woow-workshop-711 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/WooW-Workshop-711-scaled.jpg |
| 5h | fotos-redes-sociais |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/Fotos-Redes-Sociais.jpg |
| 5h | mili_branco | Mili |  | https://metakosmos.com.br/wp-content/uploads/2026/05/mili_branco.png |
| 5h | copra_branco | Copra |  | https://metakosmos.com.br/wp-content/uploads/2026/05/copra_branco.png |
| 5h | chatgpt-image-14-de-mai-de-2026-09_25_56 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/05/ChatGPT-Image-14-de-mai.-de-2026-09_25_56.png |
| 5h | oba_hortifruti_sem_fundo_hd | Oba Hortifruti |  | https://metakosmos.com.br/wp-content/uploads/2026/04/oba_hortifruti_sem_fundo_HD.png |
| 5h | chatgpt-image-2-de-abr-de-2026-11_07_50 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/04/ChatGPT-Image-2-de-abr.-de-2026-11_07_50.png |
| 5h | chatgpt-image-2-de-abr-de-2026-11_04_56 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/04/ChatGPT-Image-2-de-abr.-de-2026-11_04_56.png |
| 5h | chatgpt-image-27-de-mar-de-2026-17_19_34 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-27-de-mar.-de-2026-17_19_34-1.png |
| 5h | chatgpt-image-27-de-mar-de-2026-17_19_34 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-27-de-mar.-de-2026-17_19_34.png |
| 5h | chatgpt-image-27-de-mar-de-2026-08_47_36 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-27-de-mar.-de-2026-08_47_36.png |
| 5h | convertr-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/04/convertr.png |
| 5h | tray-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/04/tray.png |
| 5h | nexaas |  |  | https://metakosmos.com.br/wp-content/uploads/2023/10/LOGOS-2.png |
| 5h | opencart |  |  | https://metakosmos.com.br/wp-content/uploads/2023/10/5-1.png |
| 5h | wake-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/08/wake.png |
| 5h | linx-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2023/10/linx.png |
| 5h | wix |  |  | https://metakosmos.com.br/wp-content/uploads/2023/10/6-1.png |
| 5h | salesforce |  |  | https://metakosmos.com.br/wp-content/uploads/2023/10/8.png |
| 5h | squarespace |  |  | https://metakosmos.com.br/wp-content/uploads/2023/10/7-1.png |
| 5h | 8-9 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/8.png |
| 5h | redley-2 | Redley |  | https://metakosmos.com.br/wp-content/uploads/2023/10/redley.png |
| 5h | boca-rosa | Boca Rosa |  | https://metakosmos.com.br/wp-content/uploads/2024/09/boca-rosa.png |
| 5h | 28-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/28.png |
| 5h | 27-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/27.png |
| 5h | 30-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/30.png |
| 5h | 33-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/33.png |
| 5h | 34-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/34.png |
| 5h | 32-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/32.png |
| 5h | 23-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/23.png |
| 5h | 21-6 |  |  | https://metakosmos.com.br/wp-content/uploads/2024/01/21.png |
| 5h | 20-6 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/20.png |
| 5h | 21-6 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/21.png |
| 5h | 22-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/22.png |
| 5h | 24-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/24.png |
| 5h | 26-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/26.png |
| 5h | 27-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/27.png |
| 5h | chatgpt-image-13-de-mar-de-2026-17_48_13 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-13-de-mar.-de-2026-17_48_13.png |
| 5h | chatgpt-image-13-de-mar-de-2026-17_48_13 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-13-de-mar.-de-2026-17_48_13.jpg |
| 5h | image-10-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/image-10.png |
| 5h | image-9-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/image-9.png |
| 5h | image-8-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/image-8.png |
| 5h | image-7-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/image-7.png |
| 5h | image-6-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/image-6.png |
| 5h | image-5-3 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/image-5.png |
| 5h | render |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/render.jpg |
| 5h | como-aplicar-paginas-de-produto-imersiva |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/Como-aplicar-paginas-de-produto-imersivas-na-pratica.jpg |
| 5h | o-que-sao-paginas-de-produto-imersivas |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/O-que-sao-paginas-de-produto-imersivas.jpg |
| 5h | fooh-5 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/fooh-1.jpg |
| 5h | cases-reais |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/Cases-Reais.jpg |
| 5h | realidade-aumentada-sofda |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/Realidade-Aumentada-sofda.png |
| 5h | fooh-4 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/fooh.jpg |
| 5h | chatgpt-image-4-de-mar-de-2026-08_16_51 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-4-de-mar.-de-2026-08_16_51.png |
| 5h | 4-13 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/4.png |
| 5h | 3-13 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/3.png |
| 5h | 2-13 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/2.png |
| 5h | 1-13 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/1.png |
| 5h | chatgpt-image-2-de-mar-de-2026-11_42_53- |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-2-de-mar.-de-2026-11_42_53-1.png |
| 5h | chatgpt-image-2-de-mar-de-2026-11_42_53 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/03/ChatGPT-Image-2-de-mar.-de-2026-11_42_53.png |
| 5h | fashion-highlight |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/fashion-highlight.png |

### Logos / selos / parceiros (25)

| Score | Slug | Brand | Melhor uso | URL |
|-------|------|-------|------------|-----|
| 5h | aneethun_logo_white_transparente | Aneethun |  | https://metakosmos.com.br/wp-content/uploads/2026/04/Aneethun_logo_white_transparente-scaled.png |
| 5h | freeco_logo_white_transparente | Freeco |  | https://metakosmos.com.br/wp-content/uploads/2026/04/FreeCo_logo_white_transparente.png |
| 5h | logo_branca_transparente |  |  | https://metakosmos.com.br/wp-content/uploads/2026/04/logo_branca_transparente.png |
| 5h | software-logos-desktop |  |  | https://metakosmos.com.br/wp-content/uploads/2025/07/SOFTWARES-LOGO-DESKTOP-scaled.webp |
| 5h | mercado-pago-logo |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/33.png |
| 5h | general-motors-logo | GM |  | https://metakosmos.com.br/wp-content/uploads/2024/09/1.png |
| 5h | zoom-agency-logo |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/5.png |
| 5h | memo-logo |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/3.png |
| 5h | alice-wonders-logo |  |  | https://metakosmos.com.br/wp-content/uploads/2024/09/2.png |
| 5h | partners-desktop-jan26-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/partners-desktop-jan26-1.png |
| 5h | partners-desktop-jan26 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/partners-desktop-jan26.png |
| 5h | logo-beauty-desktop-jan26 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/logo-beauty-desktop-jan26.png |
| 5h | logo-clientes-footer-mobile-jan26 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/logo-clientes-footer-mobile-jan26.png |
| 5h | logo-clientes-footer-desktop-jan26 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/06/logo-clientes-footer-desktop-jan26.png |
| 5h | logo-clientes-jan-2026-desktop-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/logo-clientes-jan-2026-desktop.png |
| 5h | logo-clientes-jan-2026-desktop |  |  | https://metakosmos.com.br/wp-content/uploads/2026/02/logo-clientes-jan-2026-desktop.png |
| 5h | horizontal-logo-shop-the-look-branco-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/HORIZONTAL-LOGO-SHOP-THE-LOOK-BRANCO-scaled.png |
| 5h | horizontal-logo-shop-the-look-branco |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/HORIZONTAL-LOGO-SHOP-THE-LOOK-BRANCO-scaled.png |
| 5h | horizontal-logo-mk-fashio-branco-new-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/HORIZONTAL-LOGO-MK-FASHIO-BRANCO-NEW-scaled.png |
| 5h | horizontal-logo-mk-fashio-branco-new |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/HORIZONTAL-LOGO-MK-FASHIO-BRANCO-NEW-scaled.png |
| 5h | logo-mk-fashio-new-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/LOGO-MK-FASHIO-NEW.png |
| 5h | logo-mk-fashio-new |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/LOGO-MK-FASHIO-NEW.png |
| 5h | logo-shop-the-look-branco-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/LOGO-SHOP-THE-LOOK-BRANCO.png |
| 5h | logo-shop-the-look-branco |  |  | https://metakosmos.com.br/wp-content/uploads/2026/01/LOGO-SHOP-THE-LOOK-BRANCO.png |
| 4h | flexy-logo-2 |  |  | https://metakosmos.com.br/wp-content/uploads/2025/11/FLEXY-LOGO.png |

<!-- AUTO-CATALOG-END -->
