# Skill Blog mK — Guia de instalação

Esta skill faz o Claude escrever artigos no tom do blog da metaKosmos e publicar
como **rascunho** no nosso WordPress. Você só conversa com o Claude; ele cuida do resto.
As senhas do blog **não ficam na sua máquina** — você entra com seu email mK e pronto.

Tempo: ~5 minutos, uma vez só.

---

## Antes de começar (pré-requisitos)

1. **Um destes apps:**
   - **Claude Desktop** (recomendado para quem não usa terminal) — baixe em claude.ai/download
   - **Claude Code** (terminal)
   - **Claude Cowork**
2. **Python 3** instalado (no Mac geralmente já vem; se não, baixe em python.org).
3. **Seu email `@metakosmos.com.br`** precisa estar na lista de quem pode publicar
   (hoje: David, Patrick, João, Tales). Se não estiver, peça ao David para incluir.

Não precisa de conta no GitHub: o repositório é público, então o comando de
instalação funciona direto.

---

## Passo 1 — Instalar a skill (uma vez)

No Claude (Code, Desktop ou Cowork), digite estes dois comandos, um de cada vez:

```
/plugin marketplace add metaKosmos/mk-blog-skill
```
```
/plugin install blog-mk@mk-skills
```

Pronto, a skill `blog-mk` está instalada.

---

## Passo 2 — Primeira vez: login com seu email mK

Simplesmente peça ao Claude:

> **"Quero publicar um artigo de teste no blog. Faz meu login primeiro."**

O Claude vai preparar tudo e **abrir uma aba no navegador** "Entrar com Google".
Escolha sua conta **@metakosmos.com.br** e autorize. Só isso.

(Por baixo: ele instala um pacotinho `certifi` e guarda só o seu token de login —
nenhuma senha do blog fica com você.)

---

## Passo 3 — Usar no dia a dia

Converse normalmente com o Claude. Exemplos:

> "Escreve um artigo sobre provador virtual no tom do blog mK."

> "Reescreve esse texto no estilo mK: [cola o texto]"

> "Publica esse artigo como rascunho no blog."

O artigo **sempre entra como rascunho** — alguém revisa no WordPress antes de ir ao ar.
O Claude te devolve o link do rascunho no fim.

---

## Se algo der errado

- **"Acesso negado / 403"** ao publicar → seu login expirou ou seu email não está
  liberado. Peça ao Claude: "refaz meu login do blog". Se persistir, fale com o David
  para confirmar seu email na lista.
- **Erro de certificado / SSL** → peça ao Claude: "roda o setup da skill do blog".
- **O comando `/plugin` não encontra o repositório** → confira se digitou exatamente
  `metaKosmos/mk-blog-skill` (com o K maiúsculo em Kosmos). O repo é público, não
  precisa de conta no GitHub.

---

## Atualizações

Automático. O `setup.sh` já liga a atualização automática, então quando o Patrick
ou o David melhorarem a skill, você recebe sozinho no próximo uso (Claude
Desktop/Code/Cowork). Não precisa fazer nada.

Se por algum motivo a skill avisar que há versão nova (ex: você usa via upload no
claude.ai web, que não tem auto-update), é só rodar:
```
/plugin marketplace update mk-skills
```
