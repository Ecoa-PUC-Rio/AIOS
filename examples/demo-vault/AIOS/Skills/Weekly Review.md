---
title: Weekly Review
type: skill
scheduled: "17:00 sex"
triggers:
  - "weekly review"
  - "revisão semanal"
  - "fecha a semana"
  - "faxina do kanban"
tags:
  - aios
  - skill
---

# 🧹 Skill — Weekly Review

> Fechamento de sexta: faxina do Kanban, atualização dos mapas e prévia da semana seguinte. Roda sozinho sex 17h; também pode ser chamado a qualquer hora.

## Objetivo

Garantir que o quadro [[AIOS/Tasks/Tarefas|Tarefas]], o [[ME]] e os mapas nunca fiquem desatualizados — e abrir a segunda-feira já com foco.

## Passos

1. **Kanban ([[AIOS/Tasks/Tarefas|Tarefas]]):**
   - Perguntar ao operador (ou inferir do vault/History) o que foi concluído → mover para **Concluído** com `✅ AAAA-MM-DD`.
   - Tarefas com prazo vencido → marcar 🔥 e mover para seção **Vencidas — confirmar status**.
   - Concluídos com mais de 2 semanas → apagar do quadro (o rastro fica no History).
   - Atualizar `updated:` no frontmatter e a linha de **marcos** (dias restantes).
2. **Inbox ([[AIOS/Inbox|Inbox]]):** processar itens em Aberto → virar tarefa no quadro ou nota no projeto; mover para Processado.
3. **Mapas:** se houve mudança de estrutura/projeto na semana, atualizar [[ME]] (seção Projetos Ativos + *última atualização*) e [[AIOS/Maps/Vault Map|Vault Map]].
4. **Prévia:** olhar o calendário da semana seguinte + prazos do quadro → montar "Top 3 da próxima semana".
5. **Registrar** resumo da revisão na nota do dia em `AIOS/History/` (seção `## 🧹 Weekly Review`).

## Formato do resumo (chat + History)

```markdown
## 🧹 Weekly Review — AAAA-MM-DD
- Concluídas na semana: N · Vencidas a confirmar: N · Inbox processada: N
- Mapas atualizados: sim/não (o quê)
- 🎯 Top 3 da próxima semana: 1) … 2) … 3) …
```

## Regras

- Nunca apagar tarefa não concluída sem confirmação; na dúvida, mover para Vencidas 🔥.
- Datas absolutas. Conciso.
- Segurança padrão: [[AIOS/Systems/AIOS — Segurança e Guardrails|Guardrails]].

→ Skill agendada. Ver [[AIOS/Maps/Skill Map|Skill Map]].
