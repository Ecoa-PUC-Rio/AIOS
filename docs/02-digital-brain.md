# 02 — The Digital Brain (metadata layer)

*[Versão em português → 02-digital-brain.pt-BR.md](02-digital-brain.pt-BR.md)*

Folders answer "where is it?". The brain needs two more answers that folders can't give: **what is this note?** and **whose is it?** AIOS encodes both in frontmatter, so any tool (Dataview, Brain Atlas, the Graph view — or the LLM itself) can slice the vault by function or by ownership without reorganizing a single folder.

## `type` — what the note is (function)

| `type` | Meaning | Brain Atlas region |
|---|---|---|
| `project` / `projeto` | Project hub or project note | **Frontal** (executive) |
| `decisao` / `decision` | A recorded decision (ADR) | **Frontal** |
| `pessoa` / `person`, `org` | A person or organization | **Temporal** (social) |
| `referencia` / `source` | External reference, paper, standard, repo | **Occipital** (perception) |
| `daily` | Daily note / briefing log | **Cerebellum** (temporal memory) |
| `index` / `map` / `dashboard` | Navigation, MOCs, routing | **Brain stem** (routing) |
| `concept` / `tool` (default) | Concepts, tools, working notes | **Parietal** (integration) |
| `skill`, `system`, `inbox`, `tasks` | AIOS machinery | — |

With the [Brain Atlas](https://github.com/colorpulse6/brain-atlas) plugin, these kinds literally render as brain regions (see `plugin-configs/`). Precedence used by the plugin: frontmatter value map → `type` key → tags → folder names → default.

## `area` — whose the note is (ownership)

Define your top-level work contexts once — e.g. `client-x`, `my-company`, `university`, `personal` — and stamp `area: <x>` (+ tag `#area/<x>`) on every hub. Rules of thumb:

- **Every project has exactly one owner area.** Content produced *for* a partnership belongs to the partnership's area, not to whoever produced it.
- Area ≠ region. Region says what the note *is*; area says *who it belongs to*. They are orthogonal by design.
- Color the Graph view by area (`plugin-configs/graph.colorGroups.json`) — ownership becomes visible at a glance, and mis-clustered notes (linked across areas) stop being misleading.

## Cross-cutting structures

**`People/`** — one note per person (`type: pessoa`) and per organization (`People/Orgs/`, `type: org`): role, org, projects (wikilinked), contact, how to interact, interaction history. This is the context an LLM *cannot infer from documents* — who is who, who decides what, how to talk to each one. It turns the vault into a lightweight CRM and populates the Temporal region.

**`Decisões/`** (Decisions) — ADR-style log, one note per decision (`type: decisao`, id `DEC-YYYY-NNN`): context → options → decision → consequences. Golden rule: *a decision that changes name, scope, money or process gets a note the same day.* Project-specific ADRs may live inside the project; the central index links them. This is what stops the AI (and you) from re-litigating old decisions.

## Why this matters for LLMs

When an assistant boots, `ME.md` + maps give it identity and navigation; `type`/`area` give it **queryable semantics** ("list open decisions of area X", "who is involved in project Y"); People/ and Decisions/ give it **social and historical context**. The result: answers grounded in your actual state, not guesses.
