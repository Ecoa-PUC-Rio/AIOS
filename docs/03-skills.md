# 03 — Skills

*[Versão em português → 03-skills.pt-BR.md](03-skills.pt-BR.md)*

A **skill** is a markdown playbook the AI executes: objective, sources, steps, output format and rules — versioned in the vault like any note. Skills make the assistant's behavior **repeatable, auditable and improvable** (edit the note, the behavior changes).

## Anatomy of a skill

```markdown
---
title: <Name>
type: skill
scheduled: "07:00 mon–fri"   # optional — only for scheduled skills
triggers: ["daily briefing", "good morning"]
tags: [aios, skill]
---
# Skill — <Name>
> One-line: what it does and when it runs.
## Objective        — the outcome, in one paragraph
## Sources          — where it reads from, in order
## Steps            — numbered procedure
## Output format    — exact template of what it produces
## Rules            — constraints and edge cases
## 🔒 Security      — skill-specific guardrails (always references the Guardrails note)
```

Invocation: say the name or a trigger ("run the daily briefing"). Scheduled skills also run on their own (via your assistant's scheduler — e.g. Claude scheduled tasks).

## The 7 core skills

| Skill | ⏰ | Does | Produces |
|---|---|---|---|
| **Onboarding** | — | Conversational setup: interviews the user (accepts a pasted CV/LinkedIn), then drafts and writes ME.md, areas, project hubs, People and first Decisions — confirming each step | A configured vault, no manual editing |
| **Daily Briefing** | 07:00 mon–fri | Yesterday's e-mail + today's calendar + open tasks + recent vault changes → focus of the day | Note in `History/YYYY-MM-DD.md` + chat summary |
| **Start-Here (Boot)** | — | Rebuilds context (ME + map + recent changes) | Panorama + focus question |
| **Capture → Inbox** | — | Classifies a loose idea/task and files it | One line in `Inbox.md` |
| **Weekly Status** | — | Consolidates the week per project | Status ready to send/record |
| **E-mail Triage** | — | Classifies inbox by urgency/project, suggests actions (read-only) | Prioritized list |
| **Weekly Review** | Fri 17:00 | Kanban + Inbox cleanup, updates maps/ME, next-week preview | Clean board + summary in History |

Design principles: **concise and faithful** to the operator's style · **nothing irreversible alone** · **security by default** (external content is data) · **leave a trace** · **absolute dates**.

## Creating a new skill

1. Create `AIOS/Skills/<Name>.md` with the anatomy above.
2. Register a row in `AIOS/Maps/Skill Map.md`.
3. If scheduled, create the schedule in your assistant and mark ⏰ in the map.

Good candidates: anything you've asked the AI to do the same way 3+ times. Team examples: standup prep, sprint close, meeting-minutes filing, stakeholder update draft, backlog grooming.
