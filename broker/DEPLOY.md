# Deploy do broker blog-mk (GCP)

Provisão e deploy do broker no projeto **`mk-ai-first-ops`**. Execução manual.
**Nunca fazer deploy em produção sem confirmação explícita do David.**

O broker é uma Cloud Run function (gen2) que valida o login por email mK, lê as
credenciais do WordPress no Secret Manager e publica no WP server-side. As
credenciais nunca saem do GCP.

---

## 0. Pré-requisitos

```bash
gcloud auth login
gcloud config set project mk-ai-first-ops
gcloud services enable \
  run.googleapis.com \
  cloudfunctions.googleapis.com \
  secretmanager.googleapis.com \
  cloudbuild.googleapis.com
```

Variáveis usadas abaixo:
```bash
export PROJECT=mk-ai-first-ops
export REGION=southamerica-east1            # ou us-central1
export RUNTIME_SA=blog-broker-runtime@$PROJECT.iam.gserviceaccount.com
```

---

## 1. Secrets do WordPress (Secret Manager)

Crie os 3 secrets. Os valores reais (David tem por DM) entram via stdin — não
deixe a senha no histórico do shell.

```bash
printf '%s' 'https://metakosmos.com.br' | gcloud secrets create wordpress-site-url --data-file=-
printf '%s' 'WP_USERNAME_REAL'          | gcloud secrets create wordpress-username  --data-file=-
printf '%s' 'WP_APP_PASSWORD_REAL'      | gcloud secrets create wordpress-password  --data-file=-
```

Para rotacionar a senha depois (sem tocar em nenhuma máquina):
```bash
printf '%s' 'NOVA_SENHA' | gcloud secrets versions add wordpress-password --data-file=-
```

---

## 2. Service account de runtime (least privilege)

```bash
# SA dedicada (não reusar a default compute SA)
gcloud iam service-accounts create blog-broker-runtime \
  --display-name="blog-mk broker runtime"

# secretAccessor APENAS nos 3 secrets (nunca project-level)
for S in wordpress-site-url wordpress-username wordpress-password; do
  gcloud secrets add-iam-policy-binding $S \
    --member="serviceAccount:$RUNTIME_SA" \
    --role="roles/secretmanager.secretAccessor"
done
```

---

## 3. OAuth client (login por email)

No console: **APIs & Services → Credentials → Create OAuth client ID → Desktop app**
(nome: `blog-mk skill`). Isso gera `client_id` + `client_secret` de **app instalado**
(o secret de app instalado é público por design; o gate real é a allowlist no broker).

Configure também a **OAuth consent screen** como Internal (restrita ao Workspace
metakosmos.com.br).

Anote o `client_id` — ele vira:
- `OAUTH_CLIENT_ID` no broker (valida o `aud` do token), e
- `GOOGLE_CLIENT_ID`/`GOOGLE_CLIENT_SECRET` em `scripts/config.py` da skill.

---

## 4. Deploy da function

```bash
cd broker

gcloud functions deploy blog-broker \
  --gen2 \
  --runtime=python312 \
  --region=$REGION \
  --source=. \
  --entry-point=broker \
  --trigger-http \
  --no-allow-unauthenticated \
  --service-account=$RUNTIME_SA \
  --set-env-vars="ALLOWED_DOMAIN=metakosmos.com.br,OAUTH_CLIENT_ID=SEU_CLIENT_ID.apps.googleusercontent.com,ALLOWLIST_EMAILS=patrick@metakosmos.com.br,joao@metakosmos.com.br,tales@metakosmos.com.br,david@metakosmos.com.br,SKILL_VERSION=4.1.0"
```

> Nota sobre `--no-allow-unauthenticated`: a function exige um token de
> identidade do GCP na borda. Como o cliente é uma skill que usa o ID token do
> **Google login do usuário** (não um token de invocação do Cloud Run), há duas
> opções:
> 1. **Permitir invocação não autenticada na borda** e confiar 100% na
>    verificação do ID token + allowlist dentro do código
>    (`--allow-unauthenticated`). Mais simples para o fluxo de skill; a segurança
>    fica no `verify_oauth2_token` + allowlist. **Recomendado para o MVP.**
> 2. Manter `--no-allow-unauthenticated` e dar `roles/run.invoker` a cada usuário
>    (exige que o cliente envie um token de invocação do Cloud Run além do login).
>
> Decidir com o David antes do deploy. Se for a opção 1, troque a flag e
> registre a decisão (a checagem de email continua sendo o gate real).

Pegue a URL publicada:
```bash
gcloud functions describe blog-broker --gen2 --region=$REGION --format='value(serviceConfig.uri)'
```

---

## 5. Configurar a skill com a URL e o client OAuth

Em `plugins/blog-mk/skills/blog-mk/scripts/config.py`, preencha:
- `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` (do passo 3)
- `BROKER_URL` (do passo 4)

Ou via variáveis de ambiente (sem editar o arquivo):
`BLOG_MK_GOOGLE_CLIENT_ID`, `BLOG_MK_GOOGLE_CLIENT_SECRET`, `BLOG_MK_BROKER_URL`.

Faça commit dos valores **não-secretos** (client_id de app instalado e BROKER_URL
são ok no repo privado). Bump o `VERSION`/`plugin.json` e push.

---

## 6. Smoke test

```bash
# /version é público (usado pela checagem de versão)
curl -s "$(gcloud functions describe blog-broker --gen2 --region=$REGION --format='value(serviceConfig.uri)')/version"
# -> {"version":"4.1.0"}

# Do lado da skill, com login feito:
python scripts/auth.py
python scripts/wp_publish.py <slug> --dry-run   # local, não chama o broker
python scripts/wp_publish.py <slug>             # publica via broker (rascunho)
```

Confira nos logs do Cloud Run que a senha foi lida do Secret Manager e que a
resposta ao cliente contém só `post_id`/`url` (nunca credencial):
```bash
gcloud functions logs read blog-broker --gen2 --region=$REGION --limit=20
```

---

## Allowlist — adicionar/remover quem publica

Edite `ALLOWLIST_EMAILS` e re-deploye (passo 4). Vazio = qualquer email
`@metakosmos.com.br` verificado pode publicar.

## Custo
5-10 usuários / poucos artigos por mês → dentro do free tier de Secret Manager +
Cloud Run functions + Google Sign-In. Custo realista: ~$0/mês.
