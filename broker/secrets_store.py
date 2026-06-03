"""
secrets_store.py — Leitura das credenciais do WordPress no GCP Secret Manager.

O runtime service account do broker tem roles/secretmanager.secretAccessor
APENAS nestes secrets (per-secret IAM, nunca project-level). Os valores sao
lidos em runtime e mantidos so em memoria pelo tempo da requisicao.

Secrets esperados no projeto (mk-ai-first-ops):
  - wordpress-site-url
  - wordpress-username
  - wordpress-password
"""

import os
from functools import lru_cache

from google.cloud import secretmanager

PROJECT_ID = os.environ.get("GCP_PROJECT") or os.environ.get("GOOGLE_CLOUD_PROJECT", "mk-ai-first-ops")

SECRET_NAMES = {
    "WP_SITE_URL": os.environ.get("SECRET_WP_SITE_URL", "wordpress-site-url"),
    "WP_USERNAME": os.environ.get("SECRET_WP_USERNAME", "wordpress-username"),
    "WP_PASSWORD": os.environ.get("SECRET_WP_PASSWORD", "wordpress-password"),
}


@lru_cache(maxsize=1)
def _client():
    return secretmanager.SecretManagerServiceClient()


def _access(secret_name, version="latest"):
    name = f"projects/{PROJECT_ID}/secrets/{secret_name}/versions/{version}"
    resp = _client().access_secret_version(request={"name": name})
    return resp.payload.data.decode("utf-8").strip()


def get_wp_credentials():
    """Retorna {WP_SITE_URL, WP_USERNAME, WP_PASSWORD} lidos do Secret Manager."""
    return {key: _access(secret) for key, secret in SECRET_NAMES.items()}
