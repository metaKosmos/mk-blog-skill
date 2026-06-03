<?php
/**
 * Plugin Name:       mK Yoast REST Fields
 * Plugin URI:        https://metakosmos.com.br
 * Description:       Expõe os meta fields do Yoast SEO (título SEO, meta description, focus keyword, canonical, OpenGraph) no REST API. Permite criar e editar artigos via API com SEO já preenchido. Necessário para a skill blog-mk da metaKosmos.
 * Version:           1.0.0
 * Requires at least: 6.0
 * Requires PHP:      7.4
 * Author:            metaKosmos
 * Author URI:        https://metakosmos.com.br
 * License:           GPL-2.0-or-later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       mk-yoast-rest-fields
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Registra os meta fields do Yoast SEO como visíveis no REST API
 * para o post type "post" (artigos do blog).
 *
 * Sem isso, o WordPress ignora silenciosamente os campos
 * _yoast_wpseo_* enviados via REST API durante criação/edição de posts.
 */
add_action('init', function () {

    $yoast_fields = [
        // Campos principais
        '_yoast_wpseo_title'                  => 'string',  // Título SEO
        '_yoast_wpseo_metadesc'               => 'string',  // Meta Description
        '_yoast_wpseo_focuskw'                => 'string',  // Focus Keyword
        '_yoast_wpseo_canonical'              => 'string',  // Canonical URL

        // Robots
        '_yoast_wpseo_meta-robots-noindex'    => 'string',  // 0|1|2
        '_yoast_wpseo_meta-robots-nofollow'   => 'string',  // 0|1

        // OpenGraph (Facebook, WhatsApp, LinkedIn)
        '_yoast_wpseo_opengraph-title'        => 'string',
        '_yoast_wpseo_opengraph-description'  => 'string',
        '_yoast_wpseo_opengraph-image'        => 'string',
        '_yoast_wpseo_opengraph-image-id'     => 'string',

        // Twitter
        '_yoast_wpseo_twitter-title'          => 'string',
        '_yoast_wpseo_twitter-description'    => 'string',
        '_yoast_wpseo_twitter-image'          => 'string',
        '_yoast_wpseo_twitter-image-id'       => 'string',

        // Cornerstone (Pillar Page do Yoast)
        '_yoast_wpseo_is_cornerstone'         => 'string',  // 0|1

        // Schema
        '_yoast_wpseo_schema_page_type'       => 'string',
        '_yoast_wpseo_schema_article_type'    => 'string',
    ];

    $auth_callback = function () {
        return current_user_can('edit_posts');
    };

    foreach ($yoast_fields as $meta_key => $type) {
        register_post_meta('post', $meta_key, [
            'show_in_rest'  => true,
            'single'        => true,
            'type'          => $type,
            'auth_callback' => $auth_callback,
        ]);
    }
}, 20); // prioridade 20 para rodar depois do Yoast registrar seus próprios hooks
