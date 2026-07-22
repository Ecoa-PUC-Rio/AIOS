---
title: Vault Map
type: map
created: AAAA-MM-DD
tags:
  - aios
  - map
  - navegacao
  - moc
---

# 🗺️ Vault Map

> Mapa de navegação do vault. Serve para qualquer assistente de IA (ou para o operador) localizar contexto rápido: o que existe, onde fica e por onde começar. Perfil em [[ME]].

## Como o vault está organizado

Cada pasta no topo é um **contexto de trabalho**, e todo projeto pertence a uma **área** (campo `area:` no frontmatter do hub; cores por área no Graph view). Defina as suas — exemplo:

- 🔴 `<area-1>` — <ex.: cliente principal>
- 🏯 `<area-2>` — <ex.: minha empresa/marca>
- 🎓 `<area-3>` — <ex.: universidade/emprego>
- 🏠 `pessoal` — projetos pessoais

Comece sempre pelo arquivo de **entrada** (Índice / Hub / Visão Geral / MOC) listado abaixo — ele linka o resto. `AIOS/` é **sistema** (meta); `People/` e `Decisões/` são transversais.

| Pasta | Área | Tipo | Entrada | Status |
|---|---|---|---|---|
| Projetos/ (exemplo) | <area-1> | Projeto | [[Projetos/Projeto Exemplo — Visão Geral\|Visão Geral]] | 🟢 Ativo |
| People | transversal | Pessoas & Orgs | [[People/People — Índice\|Índice]] | 🟢 |
| Decisões | transversal | Registro ADR | [[Decisões/Decisões — Índice\|Índice]] | 🟢 |
| AIOS | ⚙️ sistema | Sistema | [[AIOS/Maps/Vault Map\|Vault Map]] · [[AIOS/Maps/Skill Map\|Skill Map]] | Meta |

## 👥 People

Pessoas e organizações cruzando projetos (`type: pessoa` / `type: org`) — camada "quem é quem" do vault.

- **Entrada:** [[People/People — Índice|People — Índice]] · Template: [[People/_Template Pessoa|_Template Pessoa]]
- Orgs em `People/Orgs/`.

## 🧭 Decisões

Registro central de decisões ADR-style (`type: decisao`, numeração DEC-AAAA-NNN).

- **Entrada:** [[Decisões/Decisões — Índice|Decisões — Índice]] · Template: [[Decisões/_Template Decisão|_Template Decisão]]
- ADRs específicos de projeto podem viver dentro do projeto; o índice linka todos.

## 🤖 AIOS

Sistema operacional pessoal de IA. Como funciona: [[AIOS/Systems/AIOS — Como Funciona|AIOS — Como Funciona]].

- **Maps:** [[AIOS/Maps/Vault Map|Vault Map]] (este) · [[AIOS/Maps/Skill Map|Skill Map]] (catálogo de skills).
- **Segurança:** [[AIOS/Systems/AIOS — Segurança e Guardrails|Segurança e Guardrails]] (anti prompt-injection/poisoning).
- **Skills** (`AIOS/Skills/`): Daily Briefing ⏰ · Start-Here (Boot) · Captura → Inbox · Status Semanal · Triagem de E-mail · Weekly Review ⏰.
- **History** (`AIOS/History/`): notas diárias do Daily Briefing (template `_Template Diário`).
- **Tarefas:** [[AIOS/Tasks/Tarefas|Tarefas]] (quadro Kanban; as abertas entram no Daily Briefing).
- **Captura:** [[AIOS/Inbox|Inbox]].

## Raiz do vault

- [[ME]] — perfil e contexto (ler primeiro).
- [[CLAUDE.md]] — bootstrap da IA.

*Última atualização: AAAA-MM-DD*
