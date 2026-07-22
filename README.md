# 🧠 AIOS — AI Operating System for Obsidian

> Turn your Obsidian vault into the **brain of a personal AI operating system**: the vault is the memory, the AI is the processor, and AIOS is the architecture that connects them.

**[🇧🇷 Versão em português → README.pt-BR.md](README.pt-BR.md)**

AIOS is a **framework**, not a plugin. It is a set of conventions, note structures, playbooks ("skills") and guardrails that make any LLM-based assistant (Claude, Copilot, or anything that can read/write your vault via MCP or file access) operate your Obsidian vault as a reliable second brain — with identity, navigation, repeatable capabilities, memory traces and security by default.

## The core idea

```
┌─────────────────────────────────────────────┐
│                    AIOS                     │
│                                             │
│  IDENTITY   →  ME.md         (who you are)  │
│  MAP        →  Vault Map     (where it is)  │
│  SKILLS     →  playbooks     (what AI does) │
│  MEMORY     →  History/      (what happened)│
│  CAPTURE    →  Inbox         (loose input)  │
│  TASKS      →  Kanban board  (what's open)  │
│  SECURITY   →  Guardrails    (trust tiers)  │
│                                             │
│  Obsidian vault = memory · LLM = processor  │
└─────────────────────────────────────────────┘
```

Every conversation **boots with context** (identity → map → skill) and **ends leaving a trace** (History, Inbox or a project note). Nothing depends on the chat history of a single session: the state lives in the vault.

## The metadata layer (digital brain)

Two orthogonal fields in the frontmatter of every relevant note:

| Field | Question it answers | Values (example) |
|---|---|---|
| `type` | **What** is this note? | `project`, `decisao` (decision), `pessoa` (person), `org`, `referencia` (source), `index`, `skill`, `daily` |
| `area` | **Whose** is this note? | your work contexts, e.g. `client-x`, `my-company`, `university`, `personal` |

`type` powers function views (all decisions, all people — and 3D region views with the [Brain Atlas](https://github.com/colorpulse6/brain-atlas) plugin). `area` powers ownership views (everything belonging to a context, with per-area colors in the Graph view). Cross-cutting structures complete the brain: `People/` (one note per person/org — the "who is who" an LLM cannot infer from documents) and `Decisões/` (ADR-style decision log — so the AI never re-litigates a decision with you).

## Repository layout

```
AIOS/
├── README.md · README.pt-BR.md · LICENSE
├── docs/                  # bilingual documentation (EN + pt-BR)
│   ├── 01-architecture    # pieces, boot sequence, conventions
│   ├── 02-digital-brain   # type/area metadata, People/, Decisions/, Brain Atlas
│   ├── 03-skills          # anatomy of a skill, the 6 core skills, scheduling
│   ├── 04-security        # trust tiers, STRIDE, OWASP LLM Top 10, guardrails
│   ├── 05-adoption-guide  # adoption patterns for individuals and teams
│   └── 06-implementation-guide  # hands-on step-by-step: 7 phases, checkpoints, week-1 plan
├── vault-template/        # copy this into a new Obsidian vault (pt-BR)
│   ├── CLAUDE.md · ME.md
│   ├── AIOS/              # Maps, Skills, Systems, History, Inbox, Tasks
│   ├── People/ · Decisões/
│   └── Projetos/          # example project hub
└── plugin-configs/        # ready-to-use Brain Atlas + Graph view configs
```

## Quickstart

1. Create a new Obsidian vault and copy the contents of `vault-template/` into it.
2. Say **"onboarding"** — the AI interviews you (paste your CV/LinkedIn if you like) and fills in `ME.md`, your areas, project hubs, people and first decisions, confirming each step. No manual file editing.
3. Connect your AI to the vault (Claude Desktop/Cowork with an Obsidian MCP, or any assistant with file access).
4. In later conversations, say **"start"** — the Boot skill reads your identity and map and asks what to focus on.
5. Optional: install [Brain Atlas](https://github.com/colorpulse6/brain-atlas) and apply `plugin-configs/` to see your vault as a brain.

Full instructions: [docs/06-implementation-guide.md](docs/06-implementation-guide.md) (7 phases with checkpoints) and [docs/05-adoption-guide.md](docs/05-adoption-guide.md).

## For teams

AIOS was designed for a personal vault, but the pattern maps 1:1 to **project environments**: `ME.md` becomes the project identity (mission, stakeholders, deadlines), skills become team rituals (daily briefing → standup prep; weekly review → sprint close), `People/` becomes the stakeholder map and `Decisões/` the project ADR log. See the adoption guide.

## Security first

AIOS assumes the AI will read content you did not write (e-mail, web, attachments). The framework ships with a threat model (STRIDE + OWASP LLM Top 10) and non-negotiable guardrails: **external content is data, never instruction**; no irreversible action without human confirmation; provenance tracking on everything written back. Read [docs/04-security.md](docs/04-security.md) before connecting e-mail.

## License

[MIT](LICENSE) — build your own brain on top of it.

---

*Created by [José Carlos Menezes](https://www.linkedin.com/in/jcarlos78) — vCISO · Senior Technology Specialist @ PUC-Rio · Kensei CyberSec Lab.*
