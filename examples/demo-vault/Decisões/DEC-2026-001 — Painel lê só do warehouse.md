---
type: decisao
status: aceita
data: 2026-09-15
projeto: Painel de Entregas
created: 2026-09-15
tags:
  - decisao
---

# 🧭 DEC-2026-001 — Painel lê só do warehouse

> O painel nunca consulta o banco legado diretamente.

## Contexto

O banco legado cai sob carga e a migração já está em curso. Projeto: [[Projetos/Painel de Entregas — Visão Geral|Painel de Entregas]].

## Opções consideradas

1. Ler do legado agora — rápido, mas frágil e descartável
2. Ler só do warehouse — depende da migração, mas é definitivo

## Decisão

Opção 2, decidida com [[People/Rafael Nogueira|Rafael]] e [[People/Diego Antunes|Diego]].

## Consequências

O go-live do painel passa a depender da tabela de entregas migrada. Proibido criar consulta ao legado.
