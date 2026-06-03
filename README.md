# mK Blog Skill

Skill do Claude que gera artigos no tom editorial da metaKosmos e publica como
rascunho no blog. Distribuída como **plugin do Claude** via marketplace no GitHub.

As credenciais do WordPress **não ficam na máquina de ninguém**: a publicação passa
por um broker no Google Cloud, liberado por **login com email `@metakosmos.com.br`**.

---

## Quem usa / qual app

| Você usa... | Como instalar |
|---|---|
| **Claude Code** (terminal) | Plugin marketplace (abaixo) — instalação + atualização automática |
| **Claude Desktop / Cowork** (sem terminal) | **Mesmo** plugin marketplace — recomendado para quem não usa terminal |
| **claude.ai** (web) | Fallback: upload manual do zip da skill em *Customize → Skills* (precisa "Code execution" ligado). Sem atualização automática. |

Recomendação: se você não usa o terminal, use o **Claude Desktop** ou o **Cowork** —
eles pegam a mesma instalação por marketplace e recebem as atualizações sozinhos.

---

## Instalação (Claude Code / Desktop / Cowork)

1. Adicione o marketplace (uma vez):
   ```
   /plugin marketplace add metaKosmos/mk-blog-skill
   ```
2. Instale o plugin:
   ```
   /plugin install blog-mk@mk-skills
   ```
3. Configure e faça login (uma vez):
   ```bash
   bash scripts/setup.sh
   ```
   Vai abrir o navegador — entre com sua conta **@metakosmos.com.br**.

Pronto. A skill aparece como `blog-mk` (e `/blog-mk` quando invocada).

---

## Como usar

Escreva no chat, por exemplo:
- "escreve um artigo sobre provador virtual no tom do blog mK"
- "reescreve esse texto no estilo mK"
- "publica o slug `provador-virtual-futuro-ecommerce` como rascunho"

Ou via CLI:
```bash
python scripts/auth.py                          # login (uma vez)
python scripts/wp_publish.py --list             # lista artigos prontos em output/
python scripts/wp_publish.py <slug> --dry-run    # confere sem publicar
python scripts/wp_publish.py <slug>             # publica como rascunho
```

O post sempre entra como **rascunho** para revisão humana antes de ir ao ar.

---

## Como funciona (resumo)

```
Você (Claude + skill)
  ├─ Claude escreve o artigo lendo SKILL.md + referências   (no seu app)
  └─ scripts/wp_publish.py monta o payload e chama o broker  (com seu login)
        │  Authorization: Bearer <token do seu email mK>
        ▼
Broker (Google Cloud, projeto mk-ai-first-ops)
  ├─ valida seu email/allowlist
  ├─ lê as credenciais do WordPress no Secret Manager
  └─ publica no WordPress e devolve o link        ← a senha nunca sai do GCP
```

A senha do WordPress fica **só** no Secret Manager do GCP. Sua máquina guarda
apenas o token do seu login (`~/.blog-mk-auth.json`), nunca uma credencial do WP.

---

## Estrutura do repositório

```
mk-blog-skill/                          # este repo = marketplace "mk-skills"
├── .claude-plugin/marketplace.json     # manifesto do marketplace
├── plugins/blog-mk/
│   ├── .claude-plugin/plugin.json      # manifesto do plugin (version)
│   └── skills/blog-mk/
│       ├── SKILL.md                    # instruções do redator (o que o Claude lê)
│       ├── VERSION                     # versão publicada (checagem de atualização)
│       ├── references/                 # style DNA, anti-IA, mKases, GEO/AEO, etc.
│       ├── scripts/                    # clientes finos (auth, publish, sync, ...)
│       └── wp-plugin/                  # plugin WP que expõe campos Yoast no REST
└── broker/                             # serviço no GCP (não vai para a máquina do usuário)
    ├── main.py  wp.py  secrets_store.py
    ├── requirements.txt
    └── DEPLOY.md                       # como provisionar/deployar (mantenedor)
```

---

## Para o mantenedor (Patrick / David)

### Publicar uma atualização da skill
1. Edite o que precisar em `plugins/blog-mk/skills/blog-mk/`.
2. **Bump da versão** em dois lugares (mesmo número):
   - `plugins/blog-mk/.claude-plugin/plugin.json` → `version`
   - `plugins/blog-mk/skills/blog-mk/VERSION`
3. `git commit` + `git push`.
4. Quem usa Claude Code/Desktop/Cowork recebe no próximo uso (ou roda
   `/plugin marketplace update mk-skills`). Quem subiu manual no claude.ai vê o
   aviso de versão e re-sobe o zip.

### Broker (GCP)
O broker vive no projeto `mk-ai-first-ops`. Provisão e deploy: ver
[`broker/DEPLOY.md`](broker/DEPLOY.md). **Nunca** fazer deploy em produção sem
confirmação do David.

Allowlist de quem pode publicar: variável `ALLOWLIST_EMAILS` no deploy do broker.
Inicial: Patrick, João, Tales, David.
