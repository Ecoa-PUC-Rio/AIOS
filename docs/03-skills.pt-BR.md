# 03 — Skills

*[English version → 03-skills.md](03-skills.md)*

Uma **skill** é um playbook em markdown que a IA executa: objetivo, fontes, passos, formato de saída e regras — versionado no vault como qualquer nota. Skills tornam o comportamento do assistente **repetível, auditável e melhorável** (edite a nota, o comportamento muda).

## Anatomia de uma skill

```markdown
---
title: <Nome>
type: skill
scheduled: "07:00 seg–sex"   # opcional — só para skills agendadas
triggers: ["daily briefing", "bom dia"]
tags: [aios, skill]
---
# Skill — <Nome>
> Uma linha: o que faz e quando roda.
## Objetivo          — o resultado, em um parágrafo
## Fontes            — de onde lê, em ordem
## Passos            — procedimento numerado
## Formato de saída  — template exato do que produz
## Regras            — restrições e casos de borda
## 🔒 Segurança      — guardrails específicos (sempre referencia a nota de Guardrails)
```

Invocação: pelo nome ou por um gatilho ("roda o daily briefing"). Skills agendadas também rodam sozinhas (pelo agendador do seu assistente — ex.: scheduled tasks do Claude).

## As 6 skills base

| Skill | ⏰ | Faz | Produz |
|---|---|---|---|
| **Daily Briefing** | 07h seg–sex | E-mails de ontem + agenda de hoje + tarefas abertas + mudanças no vault → foco do dia | Nota em `History/AAAA-MM-DD.md` + resumo no chat |
| **Start-Here (Boot)** | — | Reconstrói contexto (ME + mapa + mudanças recentes) | Panorama + pergunta de foco |
| **Captura → Inbox** | — | Classifica ideia/tarefa solta e arquiva | Linha no `Inbox.md` |
| **Status Semanal** | — | Consolida a semana por projeto | Status pronto p/ enviar/registrar |
| **Triagem de E-mail** | — | Classifica a caixa por urgência/projeto, sugere ações (read-only) | Lista priorizada |
| **Weekly Review** | sex 17h | Faxina Kanban + Inbox, atualiza mapas/ME, prévia da semana | Quadro limpo + resumo no History |

Princípios de design: **conciso e fiel** ao estilo do operador · **nada irreversível sozinho** · **segurança por padrão** (conteúdo externo é dado) · **deixar rastro** · **datas absolutas**.

## Criando uma skill nova

1. Crie `AIOS/Skills/<Nome>.md` com a anatomia acima.
2. Registre uma linha no `AIOS/Maps/Skill Map.md`.
3. Se agendada, crie o agendamento no seu assistente e marque ⏰ no mapa.

Bons candidatos: qualquer coisa que você já pediu à IA do mesmo jeito 3+ vezes. Exemplos para times: preparação de standup, fechamento de sprint, arquivamento de atas, rascunho de update para stakeholders, grooming de backlog.
