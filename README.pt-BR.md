# 🧠 AIOS — AI Operating System para Obsidian

**Seu assistente de IA esquece você toda vez que o chat fecha. O AIOS dá a ele uma memória que não se perde: o seu vault do Obsidian.**

O vault é a memória, a IA é o processador, e o AIOS é a arquitetura que conecta os dois — identidade, mapas, skills, registro de decisões, grafo de pessoas e guardrails de segurança, tudo em markdown puro.

**[🇺🇸 English version](README.md)** · [Começo rápido](#começo-rápido-15-minutos) · [Vault demo](examples/demo-vault) · [Guia passo a passo](docs/06-implementation-guide.pt-BR.md)

![Graph view do Obsidian num vault AIOS: projetos coloridos por área, pessoas em roxo, decisões em verde, o sistema AIOS em cinza, tudo ligado ao ME](docs/assets/obsidian-graph.png)

<sub>Um vault AIOS com uma semana de uso, no graph view do Obsidian. Projetos coloridos por área, pessoas em roxo, decisões em verde, o próprio sistema em cinza — e tudo pendurado no `ME`. Todos os screenshots desta página são capturas reais do Obsidian no [vault demo](examples/demo-vault), cuja persona, pessoas e empresas são fictícias.</sub>

## Por quê

Toda conversa nova com uma IA começa do zero. Você re-explica quem é, no que está trabalhando, quem são as pessoas e o que já foi decidido. O contexto que torna um assistente útil mora num histórico de chat que você não consegue buscar, versionar nem levar para outra ferramenta.

O AIOS leva esse contexto para arquivos que são seus:

- **Ela conhece você antes de você digitar.** Toda conversa dá boot lendo o `ME.md` — quem você é, como trabalha, o que vence.
- **Ela nunca re-litiga uma decisão.** Decisão ganha registro estilo ADR no mesmo dia; a IA lê em vez de perguntar de novo.
- **Ela sabe quem é quem.** Uma nota por pessoa e organização — o mapa que um LLM não infere dos documentos.
- **Ela deixa rastro sem você pedir.** Toda sessão relevante termina gravada no vault. Nada depende do histórico do chat.
- **É seu e é portátil.** Markdown puro, licença MIT, funciona com qualquer assistente que leia e escreva arquivos ou fale MCP.

O AIOS é um **framework, não um plugin**: convenções, estruturas de notas, playbooks ("skills") e guardrails. Não há nada para instalar além do Obsidian e do assistente que você já usa.

## Configure conversando

Você não preenche um arquivo sequer na mão. Copie o template, diga **"init aios"**, e a IA entrevista você — cole seu CV ou LinkedIn se quiser. Ela rascunha cada nota, mostra, e só grava depois do seu OK.

![Ilustração da conversa de onboarding: o usuário diz "init aios", cola o CV, confirma o rascunho do ME.md, e o assistente lista as notas que gravou](docs/assets/onboarding-chat.pt-BR.png)

<sub>Ilustrativo — a conversa acontece no assistente que você conectar, então vai ter a cara do seu. As etapas são as que a [skill de Onboarding](vault-template/AIOS/Skills/Onboarding.md) conduz.</sub>

Vinte a quarenta minutos depois, é isto que está no seu vault:

![ME.md no Obsidian: identidade, preferências de trabalho e projetos ativos agrupados por área, com a árvore do vault à esquerda](docs/assets/obsidian-me.png)

## Como é um dia

| | |
|---|---|
| **☀️ O briefing já está esperando.** Agende a skill Daily Briefing e toda manhã de dia útil existe uma nota com os e-mails que precisam de você, a agenda do dia, as tarefas abertas e um top 3 — com e-mail suspeito sinalizado, não obedecido. | ![Nota de daily briefing com e-mail, agenda, tarefas abertas e foco do dia](docs/assets/obsidian-daily-briefing.png) |
| **✅ Um quadro alimenta tudo.** Diga *"captura: …"* e ideias soltas caem no Inbox; tarefas reais vão para um Kanban em markdown. Só o quadro alimenta o briefing. | ![Quadro de tarefas com vencidas, a fazer, em andamento e concluído](docs/assets/obsidian-tasks.png) |
| **🧭 Decisão fica registrada.** Diga *"decidimos X"* e a IA oferece registrar: contexto, opções, decisão, consequências — ligada ao projeto e às pessoas. | ![Registro de decisão com propriedades no frontmatter, contexto, opções e decisão](docs/assets/obsidian-decision.png) |

## Começo rápido (15 minutos)

Você precisa do [Obsidian](https://obsidian.md) (gratuito) e de um assistente de IA que leia e escreva arquivos numa pasta — Claude Desktop / Cowork, Claude Code, Cursor, Copilot com acesso ao workspace, ou qualquer um que fale MCP.

```bash
git clone https://github.com/Ecoa-PUC-Rio/AIOS
cp -r AIOS/vault-template/. /caminho/do/seu/vault/
```

1. **Abra** essa pasta como vault no Obsidian.
2. **Conecte** seu assistente à mesma pasta.
3. **Diga "init aios".** A IA percebe que o vault é novo e conduz você.

Daí em diante, comece qualquer conversa com **"start"** — a IA lê sua identidade e seu mapa e pergunta no que focar.

Quer ver antes de instalar? Abra [`examples/demo-vault`](examples/demo-vault) como vault: é o template depois do onboarding e de uma semana de uso.

Passo a passo completo, com checkpoints e troubleshooting: **[Guia de implementação](docs/06-implementation-guide.pt-BR.md)**.

## Como funciona

| Peça | Onde | Papel |
|---|---|---|
| **Identidade** | `ME.md` | Quem você é, como trabalha, projetos ativos e prazos. Sempre lido primeiro. |
| **Bootstrap** | `CLAUDE.md` | Força a sequência de boot e torna a persistência de sessão obrigatória. |
| **Mapa** | `AIOS/Maps/Vault Map.md` | Onde cada área vive e qual nota é a entrada. |
| **Skills** | `AIOS/Skills/` | Playbooks que a IA segue: Onboarding, Boot, Daily Briefing, Captura, Triagem de E-mail, Status Semanal, Weekly Review. |
| **Memória** | `AIOS/History/` | Notas diárias: o briefing da manhã mais o log de cada sessão. |
| **Captura e tarefas** | `AIOS/Inbox.md` · `AIOS/Tasks/` | Entrada solta primeiro, tarefa real no Kanban. |
| **Pessoas e decisões** | `People/` · `Decisões/` | Quem é quem, e o que já foi decidido. |
| **Guardrails** | `AIOS/Systems/` | Níveis de confiança e regras anti-injeção que valem para toda skill. |

Toda conversa **inicia com contexto** (identidade → mapa → skill) e **termina gravando rastro** (nota de projeto, Inbox, resumo da sessão em History). O estado vive no vault, nunca numa sessão de chat.

Dois campos de frontmatter tornam o vault consultável: `type` responde *o que é esta nota* (`project`, `decisao`, `pessoa`, `org`, `skill`, `daily`…) e `area` responde *de quem ela é* (seus contextos de trabalho). `type` alimenta visões por função e as regiões 3D do plugin opcional [Brain Atlas](https://github.com/colorpulse6/brain-atlas); `area` alimenta as cores do grafo acima. Detalhes em [02 — Cérebro digital](docs/02-digital-brain.pt-BR.md).

## Para times

O mesmo padrão mapeia 1:1 para **ambientes de projeto**: o `ME.md` vira a identidade do projeto (missão, stakeholders, prazos), as skills viram rituais do time (daily briefing → preparação do standup; weekly review → fechamento de sprint), `People/` vira o mapa de stakeholders e `Decisões/` o registro ADR do projeto. O assistente de cada membro inicia com a mesma identidade e as mesmas regras — o projeto é o usuário. Ver o [guia de adoção](docs/05-adoption-guide.pt-BR.md).

## Segurança primeiro

O AIOS assume que a IA vai ler conteúdo que você não escreveu — e-mail, páginas web, anexos. O framework já vem com modelo de ameaças (STRIDE + OWASP LLM Top 10) e guardrails inegociáveis: **conteúdo externo é dado, nunca instrução**; nenhuma ação irreversível sem confirmação humana; proveniência marcada em tudo que é gravado. Leia [04 — Segurança](docs/04-security.pt-BR.md) antes de conectar o e-mail.

## Documentação

| | |
|---|---|
| [01 — Arquitetura](docs/01-architecture.pt-BR.md) | Peças, sequência de boot, convenções |
| [02 — Cérebro digital](docs/02-digital-brain.pt-BR.md) | Metadados `type`/`area`, People, Decisões, Brain Atlas |
| [03 — Skills](docs/03-skills.pt-BR.md) | Anatomia de uma skill, as skills base, agendamento |
| [04 — Segurança](docs/04-security.pt-BR.md) | Níveis de confiança, modelo de ameaças, guardrails |
| [05 — Guia de adoção](docs/05-adoption-guide.pt-BR.md) | Padrões para pessoas e times |
| [06 — Guia de implementação](docs/06-implementation-guide.pt-BR.md) | Passo a passo mão na massa: fases, checkpoints, plano da semana 1 |

Toda a documentação é bilíngue (EN + pt-BR).

<details>
<summary>Estrutura do repositório</summary>

```
AIOS/
├── README.md · README.pt-BR.md · LICENSE
├── docs/                  # documentação bilíngue + assets/ (screenshots)
├── vault-template/        # copie para um vault novo do Obsidian (pt-BR)
│   ├── CLAUDE.md · ME.md
│   ├── AIOS/              # Maps, Skills, Systems, History, Inbox, Tasks
│   ├── People/ · Decisões/
│   └── Projetos/          # hub de projeto exemplo
├── examples/demo-vault/   # o template preenchido para uma operadora fictícia
├── plugin-configs/        # configs prontas de Brain Atlas + Graph view
└── scripts/               # geradores do vault demo e das imagens do README
```

</details>

## Licença

[MIT](LICENSE) — construa seu próprio cérebro em cima.

---

*Criado por [José Carlos Menezes](https://www.linkedin.com/in/jcarlos78) — vCISO · Senior Technology Specialist @ PUC-Rio · Kensei CyberSec Lab.*
