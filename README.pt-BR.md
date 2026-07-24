# 🧠 AIOS — AI Operating System para Obsidian

> Transforme seu vault do Obsidian no **cérebro de um sistema operacional pessoal de IA**: o vault é a memória, a IA é o processador, e o AIOS é a arquitetura que conecta os dois.

**[🇺🇸 English version → README.md](README.md)**

O AIOS é um **framework**, não um plugin. É um conjunto de convenções, estruturas de notas, playbooks ("skills") e guardrails que fazem qualquer assistente baseado em LLM (Claude, Copilot, ou qualquer um que leia/escreva no vault via MCP ou acesso a arquivos) operar seu Obsidian como um segundo cérebro confiável — com identidade, navegação, capacidades repetíveis, rastro de memória e segurança por padrão.

## A ideia central

```
┌──────────────────────────────────────────────┐
│                    AIOS                      │
│                                              │
│  IDENTIDADE →  ME.md        (quem você é)    │
│  MAPA       →  Vault Map    (onde fica tudo) │
│  SKILLS     →  playbooks    (o que a IA faz) │
│  MEMÓRIA    →  History/     (o que aconteceu)│
│  CAPTURA    →  Inbox        (entrada solta)  │
│  TAREFAS    →  Kanban       (o que está aberto)│
│  SEGURANÇA  →  Guardrails   (níveis de confiança)│
│                                              │
│  Vault Obsidian = memória · LLM = processador│
└──────────────────────────────────────────────┘
```

Toda conversa **inicia com contexto** (identidade → mapa → skill) e **termina gravando rastro automaticamente** (nota de projeto, Inbox e resumo de sessão em History) — sem o operador precisar pedir. Nada depende do histórico de chat de uma sessão: o estado vive no vault.

## A camada de metadados (cérebro digital)

Dois campos ortogonais no frontmatter de toda nota relevante:

| Campo | Pergunta que responde | Valores (exemplo) |
|---|---|---|
| `type` | **O que** esta nota é? | `project`, `decisao`, `pessoa`, `org`, `referencia`, `index`, `skill`, `daily` |
| `area` | **De quem** esta nota é? | seus contextos de trabalho, ex.: `cliente-x`, `minha-empresa`, `universidade`, `pessoal` |

`type` alimenta visões por função (todas as decisões, todas as pessoas — e as regiões 3D do plugin [Brain Atlas](https://github.com/colorpulse6/brain-atlas)). `area` alimenta visões por dono (tudo que pertence a um contexto, com cores por área no Graph view). Estruturas transversais completam o cérebro: `People/` (uma nota por pessoa/org — o "quem é quem" que um LLM não infere dos documentos) e `Decisões/` (registro de decisões estilo ADR — para a IA nunca re-litigar uma decisão com você).

## Estrutura do repositório

```
AIOS/
├── README.md · README.pt-BR.md · LICENSE
├── docs/                  # documentação bilíngue (EN + pt-BR)
│   ├── 01-architecture    # peças, sequência de boot, convenções
│   ├── 02-digital-brain   # metadados type/area, People/, Decisões/, Brain Atlas
│   ├── 03-skills          # anatomia de uma skill, as 6 skills base, agendamento
│   ├── 04-security        # níveis de confiança, STRIDE, OWASP LLM Top 10, guardrails
│   ├── 05-adoption-guide  # padrões de adoção para pessoas e times
│   └── 06-implementation-guide  # passo a passo mão na massa: 7 fases, checkpoints, plano da semana 1
├── vault-template/        # copie para um vault novo do Obsidian (pt-BR)
│   ├── CLAUDE.md · ME.md
│   ├── AIOS/              # Maps, Skills, Systems, History, Inbox, Tasks
│   ├── People/ · Decisões/
│   └── Projetos/          # hub de projeto exemplo
└── plugin-configs/        # configs prontas de Brain Atlas + Graph view
```

## Começando

1. Crie um vault novo no Obsidian e copie o conteúdo de `vault-template/` para dentro.
2. Diga **"onboarding"** — a IA entrevista você (cole seu CV/LinkedIn se quiser) e preenche `ME.md`, áreas, hubs de projetos, pessoas e primeiras decisões, confirmando cada etapa. Sem edição manual de arquivos.
3. Conecte sua IA ao vault (Claude Desktop/Cowork com MCP do Obsidian, ou qualquer assistente com acesso a arquivos).
4. Nas conversas seguintes, diga **"start"** — a skill de Boot lê identidade e mapa e pergunta no que focar.
5. Opcional: instale o [Brain Atlas](https://github.com/colorpulse6/brain-atlas) e aplique `plugin-configs/` para ver seu vault como um cérebro.

Instruções completas: [docs/06-implementation-guide.pt-BR.md](docs/06-implementation-guide.pt-BR.md) (7 fases com checkpoints) e [docs/05-adoption-guide.pt-BR.md](docs/05-adoption-guide.pt-BR.md).

## Para times

O AIOS nasceu para um vault pessoal, mas o padrão mapeia 1:1 para **ambientes de projeto**: o `ME.md` vira a identidade do projeto (missão, stakeholders, prazos), as skills viram rituais do time (daily briefing → preparação do standup; weekly review → fechamento de sprint), `People/` vira o mapa de stakeholders e `Decisões/` o registro ADR do projeto. Ver o guia de adoção.

## Segurança primeiro

O AIOS assume que a IA vai ler conteúdo que você não escreveu (e-mail, web, anexos). O framework já vem com modelo de ameaças (STRIDE + OWASP LLM Top 10) e guardrails inegociáveis: **conteúdo externo é dado, nunca instrução**; nenhuma ação irreversível sem confirmação humana; proveniência marcada em tudo que é gravado. Leia [docs/04-security.pt-BR.md](docs/04-security.pt-BR.md) antes de conectar o e-mail.

## Licença

[MIT](LICENSE) — construa seu próprio cérebro em cima.

---

*Criado por [José Carlos Menezes](https://www.linkedin.com/in/jcarlos78) — vCISO · Senior Technology Specialist @ PUC-Rio · Kensei CyberSec Lab.*
