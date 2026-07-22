# 05 — Adoption Guide

*[Versão em português → 05-adoption-guide.pt-BR.md](05-adoption-guide.pt-BR.md)*

## Prerequisites

- **Obsidian** (free) — the vault.
- **An AI assistant that can read/write the vault** — e.g. Claude Desktop/Cowork with an Obsidian MCP server (such as `mcp-obsidian` + the Local REST API plugin), or any agent with file access to the vault folder.
- Optional connectors: calendar and e-mail (read-only to start — see the security doc first).
- Optional plugins: [Brain Atlas](https://github.com/colorpulse6/brain-atlas) (3D brain view), Dataview, Templater, Tasks, obsidian-git (version your brain!).

## Individual setup (30–60 min)

1. **Create a vault** and copy the contents of `vault-template/` into its root.
2. **Connect the AI** to the vault (Claude Desktop/Cowork connected folder, or an Obsidian MCP).
3. **Run the onboarding conversation**: say **"onboarding"** — the AI interviews you (paste your CV/LinkedIn, talk about your projects) and drafts and writes `ME.md`, your 3–5 areas and the project hubs, confirming each step. You never fill a file by hand; `ME.md` stays the highest-leverage file in the system — the interview is how it gets specific.
4. **Confirm the boot**: in a new conversation, say "start" → the AI should read `ME.md` and ask what to focus on.
5. **Schedule** the Daily Briefing (weekday mornings) and the Weekly Review (Friday afternoon) in your assistant's scheduler.
6. **First week routine:** capture everything ("capture: …"), let the briefing open your day, run the review on Friday. Adjust the skills — they are just markdown.
7. **Grow the brain as you work:** new decision → note in `Decisões/` the same day; new person in a project → note in `People/`; new repeated request → new skill.

## Team / project-environment setup (the PUC pattern)

The same architecture, with the identity shifted from a person to a **project**:

| Personal AIOS | Project environment |
|---|---|
| `ME.md` (who I am) | `PROJECT.md` — mission, scope, stakeholders, milestones, conventions |
| Areas = life contexts | Areas = subsystems / workstreams / partner orgs |
| Daily Briefing | Standup prep (open tasks + yesterday's changes + blockers) |
| Weekly Review | Sprint close / weekly report ritual |
| `People/` | Stakeholder & team map (roles, decision rights, contacts) |
| `Decisões/` | Project ADR log (technical + governance decisions) |
| Guardrails | Same rules + project NDA/LGPD data-handling constraints |

Setup: one shared vault per project (git-versioned), `CLAUDE.md` pointing to `PROJECT.md`, skills adapted to the team's rituals. Each member's assistant boots with the same identity and the same map — **the project itself becomes the operating system's user**.

## Maintenance (what keeps it alive)

- The **Weekly Review is not optional** — an unmaintained brain loses trust fast.
- Update `ME.md`/`PROJECT.md` whenever a project starts, ends or changes deadline.
- Keep the Skill Map honest: retire skills you stopped using.
- Version with git. Your brain deserves backups.

## FAQ

**Does it require Claude?** No. Any LLM assistant that can read/write files or speak MCP works. The conventions are plain markdown.
**Does it require Brain Atlas?** No — it's the visualization layer. The metadata works with Dataview/graph alone.
**Portuguese or English?** The vault template ships in pt-BR; translate freely — the framework is language-agnostic.
