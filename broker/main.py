"""
main.py — Broker blog-mk (Cloud Run function, gen2).

Fluxo:
  1. Recebe POST com Authorization: Bearer <google_id_token>.
  2. Valida o ID token (assinatura Google) e confere email/dominio na allowlist.
  3. Le as credenciais do WordPress no Secret Manager (runtime SA, per-secret IAM).
  4. Executa a operacao no WP (publish/seo/sync-assets) server-side.
  5. Retorna so o resultado (post id/url). A credencial nunca sai do GCP.

Endpoints (por path):
  GET  /version       -> versao publicada da skill (publico, p/ checagem de versao)
  POST /publish       -> cria/atualiza post (rascunho por padrao)
  POST /seo           -> batch de atualizacoes Yoast
  POST /sync-assets   -> devolve media/posts/pages crus do WP

Deploy: ver broker/DEPLOY.md (NAO fazer deploy sem confirmacao do David).
"""

import json
import os
import re

import functions_framework
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token as google_id_token

import wp
from secrets_store import get_wp_credentials

# === Config (env vars do deploy) ===
# OAuth client id do app instalado — o ID token do usuario deve ter este 'aud'.
ALLOWED_AUDIENCE = os.environ.get("OAUTH_CLIENT_ID", "")
# Client secret do app instalado (Desktop) — servido ao cliente via /oauth-config
# para NAO ficar no repo (que e publico). Secret de Desktop e publico por design;
# o gate real e a allowlist abaixo.
OAUTH_CLIENT_SECRET = os.environ.get("OAUTH_CLIENT_SECRET", "")
ALLOWED_DOMAIN = os.environ.get("ALLOWED_DOMAIN", "metakosmos.com.br")
# Allowlist de emails (separados por virgula OU ponto-e-virgula). Vazio = aceita
# qualquer email verificado do dominio. (`;` evita conflito com o delimitador de
# --set-env-vars do gcloud, que usa virgula entre variaveis.)
ALLOWLIST = {
    e.strip().lower()
    for e in re.split(r"[,;]", os.environ.get("ALLOWLIST_EMAILS", ""))
    if e.strip()
}
SKILL_VERSION = os.environ.get("SKILL_VERSION", "4.1.0")

_request_adapter = google_requests.Request()


def _json(body, status=200):
    return (json.dumps(body, ensure_ascii=False), status,
            {"Content-Type": "application/json; charset=utf-8"})


def _verify_caller(request):
    """Valida o ID token e retorna o email autorizado, ou levanta PermissionError."""
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        raise PermissionError("Token ausente. Faca login com 'python scripts/auth.py'.")
    token = auth.split(" ", 1)[1]

    try:
        # Verifica assinatura. Se ALLOWED_AUDIENCE definido, confere o 'aud'.
        claims = google_id_token.verify_oauth2_token(
            token, _request_adapter, ALLOWED_AUDIENCE or None
        )
    except Exception as e:
        raise PermissionError(f"Token invalido: {e}")

    email = (claims.get("email") or "").lower()
    email_verified = claims.get("email_verified", False)
    hd = claims.get("hd")

    if not email or not email_verified:
        raise PermissionError("Email nao verificado no token.")

    domain_ok = (hd == ALLOWED_DOMAIN) or email.endswith("@" + ALLOWED_DOMAIN)
    if not domain_ok:
        raise PermissionError(f"Email {email} nao e do dominio {ALLOWED_DOMAIN}.")

    if ALLOWLIST and email not in ALLOWLIST:
        raise PermissionError(f"Email {email} nao esta na allowlist de publicacao.")

    return email


@functions_framework.http
def broker(request):
    path = request.path.rstrip("/") or "/"

    # Endpoint publico de versao (sem auth) — para a checagem de versao da skill.
    if path == "/version" and request.method == "GET":
        return _json({"version": SKILL_VERSION})

    # Config publica do OAuth client (client_id + client_secret de Desktop, que e
    # publico por design). Servido aqui para nao ficar no repo publico da skill.
    if path == "/oauth-config" and request.method == "GET":
        return _json({"client_id": ALLOWED_AUDIENCE, "client_secret": OAUTH_CLIENT_SECRET})

    if request.method != "POST":
        return _json({"error": "metodo nao suportado"}, 405)

    # Autenticacao + allowlist
    try:
        caller = _verify_caller(request)
    except PermissionError as e:
        return _json({"error": str(e)}, 403)

    try:
        payload = request.get_json(silent=True) or {}
    except Exception:
        payload = {}

    # Credenciais do WP (Secret Manager) — so apos passar na autenticacao
    try:
        creds = get_wp_credentials()
    except Exception as e:
        return _json({"error": f"falha ao ler credenciais: {e}"}, 500)

    try:
        if path == "/publish":
            result = wp.publish_post(creds, payload)
            print(f"[publish] {caller} -> post {result.get('post_id')} ({result.get('status')})")
            return _json(result)

        if path == "/seo":
            result = wp.update_seo(creds, payload.get("updates", []))
            print(f"[seo] {caller} -> {len(result.get('results', []))} updates")
            return _json(result)

        if path == "/sync-assets":
            result = wp.sync_assets(creds)
            print(f"[sync-assets] {caller} -> {len(result.get('media', []))} media")
            return _json(result)

        return _json({"error": f"rota desconhecida: {path}"}, 404)

    except Exception as e:
        print(f"[error] {caller} {path}: {e}")
        return _json({"error": str(e)}, 502)
