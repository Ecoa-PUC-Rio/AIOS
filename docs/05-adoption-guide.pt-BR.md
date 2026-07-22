# 05 — Guia de Adoção

*[English version → 05-adoption-guide.md](05-adoption-guide.md)*

## Pré-requisitos

- **Obsidian** (gratuito) — o vault.
- **Um assistente de IA que leia/escreva no vault** — ex.: Claude Desktop/Cowork com um MCP do Obsidian (como `mcp-obsidian` + plugin Local REST API), ou qualquer agente com acesso à pasta do vault.
- Conectores opcionais: agenda e e-mail (comece read-only — leia antes o doc de segurança).
- Plugins opcionais: [Brain Atlas](https://github.com/colorpulse6/brain-atlas) (visão 3D de cérebro), Dataview, Templater, Tasks, obsidian-git (versione seu cérebro!).

## Setup individual (30–60 min)

1. **Crie um vault** e copie o conteúdo de `vault-template/` para a raiz.
2. **Conecte a IA** ao vault (pasta conectada no Claude Desktop/Cowork, ou um MCP do Obsidian).
3. **Rode a conversa de onboarding**: diga **"onboarding"** — a IA entrevista você (cole CV/LinkedIn, fale dos seus projetos) e rascunha e grava `ME.md`, suas 3–5 áreas e os hubs de projeto, confirmando cada etapa. Você nunca preenche arquivo na mão; o `ME.md` continua sendo o arquivo de maior alavancagem — a entrevista é como ele fica específico.
4. **Confirme o boot**: numa conversa nova, diga "start" → a IA deve ler o `ME.md` e perguntar no que focar.
5. **Agende** o Daily Briefing (manhãs de dia útil) e o Weekly Review (sexta à tarde) no agendador do seu assistente.
6. **Rotina da primeira semana:** capture tudo ("captura: …"), deixe o briefing abrir seu dia, rode a review na sexta. Ajuste as skills — são só markdown.
7. **Cresça o cérebro trabalhando:** decisão nova → nota em `Decisões/` no mesmo dia; pessoa nova em projeto → nota em `People/`; pedido repetido → skill nova.

## Setup para times / ambientes de projeto (o padrão PUC)

A mesma arquitetura, com a identidade deslocada da pessoa para o **projeto**:

| AIOS pessoal | Ambiente de projeto |
|---|---|
| `ME.md` (quem eu sou) | `PROJECT.md` — missão, escopo, stakeholders, marcos, convenções |
| Áreas = contextos de vida | Áreas = subsistemas / frentes / organizações parceiras |
| Daily Briefing | Preparação de standup (tarefas abertas + mudanças de ontem + bloqueios) |
| Weekly Review | Fechamento de sprint / ritual de relatório semanal |
| `People/` | Mapa de stakeholders e time (papéis, alçadas, contatos) |
| `Decisões/` | Registro ADR do projeto (decisões técnicas + de governança) |
| Guardrails | Mesmas regras + restrições de NDA/LGPD do projeto |

Setup: um vault compartilhado por projeto (versionado em git), `CLAUDE.md` apontando para `PROJECT.md`, skills adaptadas aos rituais do time. O assistente de cada membro inicia com a mesma identidade e o mesmo mapa — **o próprio projeto vira o usuário do sistema operacional**.

## Manutenção (o que mantém vivo)

- O **Weekly Review não é opcional** — cérebro sem manutenção perde a confiança rápido.
- Atualize `ME.md`/`PROJECT.md` sempre que um projeto começar, terminar ou mudar de prazo.
- Mantenha o Skill Map honesto: aposente skills que você parou de usar.
- Versione com git. Seu cérebro merece backup.

## FAQ

**Exige Claude?** Não. Qualquer assistente LLM que leia/escreva arquivos ou fale MCP funciona. As convenções são markdown puro.
**Exige Brain Atlas?** Não — é a camada de visualização. Os metadados funcionam só com Dataview/grafo.
**Português ou inglês?** O template do vault vem em pt-BR; traduza à vontade — o framework é agnóstico de idioma.
