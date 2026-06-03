#!/usr/bin/env python3
"""
test_publish_equivalence.py — Prova que a versao HOSPEDADA publica igual a V4 do Patrick.

Risco do refactor (local .env -> broker): mudar o que vai pro WordPress.
Este teste dirige os DOIS caminhos com os MESMOS inputs e os MESMOS stubs de rede,
e exige que o payload final enviado a `POST /wp/v2/posts` seja IDENTICO:

  Caminho A (V4 original): tests/v4_reference.py  (copia fiel do wp_publish.py do Patrick)
  Caminho B (hospedado):   scripts/wp_publish.py (cliente) -> broker/wp.py (publish_post)

A rede e neutralizada com stubs identicos nos dois lados (auth, resolve_tags,
find_media), entao a comparacao isola a LOGICA de montagem do post: parse de
metadados, strip de H1/hero, mapping pilar->categoria, tags, featured, Yoast, author.

Roda offline, sem credenciais. Uso:  python tests/test_publish_equivalence.py
"""

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TESTS = REPO / "tests"
FIXTURES = TESTS / "fixtures"
SCRIPTS = REPO / "plugins" / "blog-mk" / "skills" / "blog-mk" / "scripts"
BROKER = REPO / "broker"


def _load(name, path, extra_syspath=None):
    if extra_syspath:
        sys.path.insert(0, str(extra_syspath))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# --- Stubs de rede IDENTICOS para os dois caminhos -------------------------
def stub_tag_ids(_jwt, _env_or_site, tag_names):
    # id deterministico por nome (mesma funcao nos dois lados)
    return [1000 + sum(ord(c) for c in name) for name in (tag_names or [])]


def stub_find_media(_jwt, _env_or_site, source_url):
    return 4242 if source_url else None


def make_capture():
    captured = {}

    def http(method, url, *a, **k):
        body = k.get("body")
        if body is None and len(a) >= 2:
            body = a[1]
        if method == "POST" and url.endswith("/wp/v2/posts"):
            captured["payload"] = body
        # resposta que satisfaz V4 e hospedado
        return 201, {"id": 4701, "status": body.get("status") if isinstance(body, dict) else "draft",
                     "slug": body.get("slug") if isinstance(body, dict) else "",
                     "link": "https://metakosmos.com.br/?p=4701",
                     "meta": (body or {}).get("meta", {})}
    return captured, http


def run_v4(slug, status):
    """Caminho A: V4 original do Patrick."""
    v4 = _load("v4_reference", TESTS / "v4_reference.py")
    v4.OUTPUT_DIR = FIXTURES
    v4.load_env = lambda: {"WP_SITE_URL": "https://metakosmos.com.br",
                           "WP_USERNAME": "x", "WP_PASSWORD": "y"}
    v4.authenticate = lambda env: "JWT"
    v4.resolve_tags = stub_tag_ids
    v4.find_media_by_url = stub_find_media
    captured, http = make_capture()
    v4.http = http
    v4.publish(slug, status=status, dry_run=False)
    return captured["payload"]


def run_hosted(slug, status):
    """Caminho B: cliente hospedado monta payload -> broker wp.publish_post."""
    client = _load("wp_publish_hosted", SCRIPTS / "wp_publish.py", extra_syspath=SCRIPTS)
    client.OUTPUT_DIR = FIXTURES
    payload = client.build_payload(slug, status, None)

    wp = _load("broker_wp", BROKER / "wp.py")
    wp.authenticate = lambda creds: "JWT"
    wp.resolve_tags = stub_tag_ids
    wp.find_media_by_url = stub_find_media
    captured, http = make_capture()
    wp._http = http
    creds = {"WP_SITE_URL": "https://metakosmos.com.br", "WP_USERNAME": "x", "WP_PASSWORD": "y"}
    wp.publish_post(creds, payload)
    return captured["payload"]


def main():
    cases = [
        ("normal-com-hero", "draft"),
        ("pillar-sem-hero", "draft"),
        ("pilar-sem-categoria", "draft"),
        ("normal-com-hero", "publish"),
    ]
    failures = 0
    for slug, status in cases:
        a = run_v4(slug, status)
        b = run_hosted(slug, status)
        if a == b:
            print(f"[OK] {slug} ({status}) — payload identico ao V4")
        else:
            failures += 1
            print(f"[X]  {slug} ({status}) — DIVERGENCIA:")
            keys = sorted(set(a) | set(b))
            for key in keys:
                if a.get(key) != b.get(key):
                    print(f"     campo '{key}':")
                    print(f"        V4:       {a.get(key)!r}")
                    print(f"        hospedado:{b.get(key)!r}")

    print()
    if failures:
        print(f"FALHOU: {failures}/{len(cases)} casos divergiram.")
        sys.exit(1)
    print(f"PASSOU: {len(cases)}/{len(cases)} — a versao hospedada publica identico a V4 do Patrick.")


if __name__ == "__main__":
    main()
