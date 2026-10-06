---
title: Vault Map
type: map
created: 2026-09-28
tags:
  - aios
  - map
  - navegacao
  - moc
---

# 🗺️ Vault Map

> Mapa de navegação do vault. Serve para qualquer assistente de IA (ou para o operador) localizar contexto rápido: o que existe, onde fica e por onde começar. Perfil em [[ME]].

## Como o vault está organizado

Todo projeto pertence a uma **área** (campo `area:` no frontmatter do hub; cores por área no Graph view):

- 🔴 `orbita` — Órbita Logística — cliente principal (consultoria de produto e dados)
- 🏯 `estudio` — Estúdio Duarte — minha consultoria: curso, site e newsletter
- 🎓 `mestrado` — Mestrado em Ciência de Dados — UFPE
- 🏠 `pessoal` — Projetos pessoais

Comece sempre pelo arquivo de **entrada** listado abaixo — ele linka o resto. `AIOS/` é **sistema** (meta); `People/` e `Decisões/` são transversais.

| Pasta | Área | Tipo | Entrada | Status |
|---|---|---|---|---|
| Projetos/Painel de Entregas | orbita | Projeto | [[Projetos/Painel de Entregas — Visão Geral\|Visão Geral]] | 🟢 Ativo |
| Projetos/Migração do Data Warehouse | orbita | Projeto | [[Projetos/Migração do Data Warehouse — Visão Geral\|Visão Geral]] | 🟢 Ativo |
| Projetos/Curso Dados para PMs | estudio | Projeto | [[Projetos/Curso Dados para PMs — Visão Geral\|Visão Geral]] | 🟢 Ativo |
| Projetos/Site e Newsletter | estudio | Projeto | [[Projetos/Site e Newsletter — Visão Geral\|Visão Geral]] | 🟢 Ativo |
| Projetos/Dissertação | mestrado | Projeto | [[Projetos/Dissertação — Visão Geral\|Visão Geral]] | 🟢 Ativo |
| Projetos/Meia Maratona do Recife | pessoal | Projeto | [[Projetos/Meia Maratona do Recife — Visão Geral\|Visão Geral]] | 🟢 Ativo |
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

*Última atualização: 2026-10-06*
