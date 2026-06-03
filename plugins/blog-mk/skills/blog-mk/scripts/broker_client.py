#!/usr/bin/env python3
"""
broker_client.py — Cliente fino do broker blog-mk.

Encapsula as chamadas HTTP ao broker (Cloud Run), sempre autenticadas com o
ID token do usuario (obtido via auth.get_id_token()). O broker valida o
email/dominio, le as credenciais do WordPress no GCP Secret Manager e executa
a operacao server-side. Nenhuma credencial do WordPress passa por aqui.

So depende da stdlib (urllib).
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from auth import get_id_token  # noqa: E402
from config import BROKER_URL, ssl_context  # noqa: E402


class BrokerError(Exception):
    """Erro retornado pelo broker (HTTP != 2xx) ou de rede."""


def _call(path, payload):
    url = f"{BROKER_URL}{path}"
    token = get_id_token()
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "blog-mk-skill/4.1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl_context()) as r:
            data = r.read().decode("utf-8")
            return json.loads(data) if data else {}
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode("utf-8"))
        except Exception:
            err = {"error": "resposta nao-JSON do broker"}
        if e.code in (401, 403):
            raise BrokerError(
                f"Acesso negado pelo broker ({e.code}): "
                f"{err.get('error', 'email nao autorizado')}. "
                f"Confirme que voce esta logado com a conta @metakosmos.com.br "
                f"autorizada (rode: python scripts/auth.py --status)."
            )
        raise BrokerError(f"Broker retornou {e.code}: {json.dumps(err, ensure_ascii=False)[:500]}")
    except urllib.error.URLError as e:
        raise BrokerError(
            f"Nao foi possivel contatar o broker em {BROKER_URL}: {e}. "
            f"Verifique BLOG_MK_BROKER_URL/config.py."
        )


def publish(payload):
    """
    Publica um artigo. O broker faz auth no WP, resolve tags/categoria/featured
    image e cria o post.

    payload esperado:
      {
        "title": str, "slug": str, "status": "draft"|"publish"|"pending",
        "content": str (HTML Gutenberg ja com strip de H1/hero),
        "tag_names": [str], "pilar": int|None, "is_pillar_page": bool,
        "hero_url": str|None,
        "yoast": {title, metadesc, focuskw, is_cornerstone},
        "update_id": int|None
      }
    Retorna: { "post_id", "url", "edit_url", "status", "yoast_persisted" }
    """
    return _call("/publish", payload)


def update_seo(updates):
    """Batch de atualizacoes de SEO/Yoast. updates = lista de {id, title?, metadesc?, featured_media?}."""
    return _call("/seo", {"updates": updates})


def sync_assets():
    """Dispara a sincronizacao da media library (operacao de manutencao)."""
    return _call("/sync-assets", {})


def version():
    """Retorna a versao publicada da skill, segundo o broker (para a checagem de versao)."""
    import urllib.request as _u
    try:
        with _u.urlopen(f"{BROKER_URL}/version", timeout=10, context=ssl_context()) as r:
            return json.loads(r.read().decode("utf-8")).get("version")
    except Exception:
        return None
