=== mK Yoast REST Fields ===
Contributors: metakosmos
Tags: yoast, rest-api, seo
Requires at least: 6.0
Tested up to: 6.7
Stable tag: 1.0.0
Requires PHP: 7.4
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

Expõe os meta fields do Yoast SEO no REST API do WordPress para permitir criação programática de artigos com SEO já preenchido.

== Description ==

Por padrão, o Yoast SEO não registra seus meta fields (`_yoast_wpseo_title`, `_yoast_wpseo_metadesc`, etc.) como visíveis no REST API. Isso impede que ferramentas externas criem posts com SEO já configurado via API.

Este plugin resolve esse problema registrando os principais fields do Yoast como `show_in_rest`, permitindo que ferramentas como a skill blog-mk da metaKosmos criem artigos diretamente via REST API com todos os metadados de SEO preenchidos.

**Fields expostos:**

* Título SEO (_yoast_wpseo_title)
* Meta Description (_yoast_wpseo_metadesc)
* Focus Keyword (_yoast_wpseo_focuskw)
* Canonical URL (_yoast_wpseo_canonical)
* Robots Noindex/Nofollow
* OpenGraph (título, descrição, imagem)
* Twitter Card (título, descrição, imagem)
* Cornerstone (Pillar Page)
* Schema page/article type

**Segurança:** Apenas usuários com capability `edit_posts` podem alterar esses fields via API.

== Installation ==

1. Faça upload da pasta `mk-yoast-rest-fields` para `/wp-content/plugins/`
2. Ative o plugin em "Plugins" no WordPress

Não há configuração necessária. Após ativação, os fields ficam disponíveis no endpoint `/wp-json/wp/v2/posts` via parâmetro `meta`.

== Changelog ==

= 1.0.0 =
* Versão inicial. Registra os fields principais do Yoast SEO no REST API.
