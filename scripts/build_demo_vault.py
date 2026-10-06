#!/usr/bin/env python3
"""Build examples/demo-vault: vault-template filled in for a fictional persona.

The demo vault is what the README screenshots are taken from. Everything in it
(people, companies, projects) is invented. Re-run after changing vault-template:

    python3 scripts/build_demo_vault.py
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "vault-template"
OUT = ROOT / "examples" / "demo-vault"

TODAY = "2026-10-06"
YESTERDAY = "2026-10-05"
CREATED = "2026-09-28"

AREAS = {
    "orbita": ("🔴", "Órbita Logística — cliente principal (consultoria de produto e dados)"),
    "estudio": ("🏯", "Estúdio Duarte — minha consultoria: curso, site e newsletter"),
    "mestrado": ("🎓", "Mestrado em Ciência de Dados — UFPE"),
    "pessoal": ("🏠", "Projetos pessoais"),
}

# name -> (area, descrição, meta, prazo, pessoas, decisões, status)
PROJECTS = {
    "Painel de Entregas": (
        "orbita",
        "Painel operacional que mostra atraso de entregas por rota em tempo quase real.",
        "Go-live para as 4 filiais do Nordeste",
        "2026-10-30",
        ["Rafael Nogueira", "Camila Prado", "Diego Antunes"],
        ["DEC-2026-001 — Painel lê só do warehouse", "DEC-2026-003 — Go-live por filial"],
        "Homologação na filial Recife; faltam 2 métricas de SLA.",
    ),
    "Migração do Data Warehouse": (
        "orbita",
        "Saída do banco legado on-premise para um warehouse em nuvem, sem parar a operação.",
        "Tabelas de entregas e frota migradas e validadas",
        "2026-11-28",
        ["Diego Antunes", "Rafael Nogueira", "Helena Sato"],
        ["DEC-2026-001 — Painel lê só do warehouse"],
        "Carga histórica de entregas concluída; frota em validação.",
    ),
    "Curso Dados para PMs": (
        "estudio",
        "Curso ao vivo de 4 semanas ensinando gente de produto a ler e questionar dados.",
        "Turma 1 com 40 alunos",
        "2026-11-17",
        ["Bruno Teixeira", "Lívia Marques"],
        ["DEC-2026-002 — Turma 1 ao vivo, não gravada"],
        "Módulos 1–2 prontos; página de vendas em revisão.",
    ),
    "Site e Newsletter": (
        "estudio",
        "Site do Estúdio e a newsletter quinzenal que alimenta o funil do curso.",
        "1.500 assinantes até o lançamento do curso",
        "2026-11-10",
        ["Lívia Marques"],
        ["DEC-2026-004 — Newsletter quinzenal"],
        "1.120 assinantes; edição #14 agendada.",
    ),
    "Dissertação": (
        "mestrado",
        "Dissertação sobre previsão de atraso em entregas de última milha.",
        "Qualificação aprovada",
        "2026-12-04",
        ["Prof. Otávio Barros", "Helena Sato"],
        [],
        "Capítulo 3 (método) em revisão com o orientador.",
    ),
    "Meia Maratona do Recife": (
        "pessoal",
        "Primeira meia maratona — plano de 12 semanas.",
        "Completar os 21 km abaixo de 2h10",
        "2026-11-22",
        ["Tiago Duarte"],
        [],
        "Semana 6 de 12; longão de 14 km feito no domingo.",
    ),
}

# name -> (papel, organização, projetos, uma linha, como interagir)
PEOPLE = {
    "Rafael Nogueira": ("Diretor de Operações (sponsor)", "Órbita Logística",
                        ["Painel de Entregas", "Migração do Data Warehouse"],
                        "Quem aprova escopo e orçamento na Órbita.",
                        "Direto ao ponto; quer número e data, não processo. Responde melhor por mensagem curta antes das 9h."),
    "Camila Prado": ("Gerente de Produto", "Órbita Logística", ["Painel de Entregas"],
                     "Dona do backlog do painel; meu contato do dia a dia.",
                     "Gosta de protótipo navegável antes de discutir. Reunião semanal às terças."),
    "Diego Antunes": ("Engenheiro de Dados", "Órbita Logística",
                      ["Painel de Entregas", "Migração do Data Warehouse"],
                      "Conhece o banco legado como ninguém.",
                      "Prefere issue escrita a call. Avisar com antecedência sobre janelas de carga."),
    "Bruno Teixeira": ("Co-instrutor do curso", "Estúdio Duarte", ["Curso Dados para PMs"],
                       "Ex-PM de marketplace; divide as aulas ao vivo comigo.",
                       "Informal; alinha tudo por áudio. Não marcar nada às sextas."),
    "Lívia Marques": ("Designer e editora (freelancer)", "Estúdio Duarte",
                      ["Curso Dados para PMs", "Site e Newsletter"],
                      "Cuida da identidade do Estúdio e da diagramação da newsletter.",
                      "Briefing fechado por escrito; 3 dias úteis de prazo mínimo."),
    "Prof. Otávio Barros": ("Orientador", "UFPE", ["Dissertação"],
                            "Orientador do mestrado.",
                            "Formal; enviar texto com 1 semana de antecedência da reunião."),
    "Helena Sato": ("Colega de laboratório", "UFPE", ["Dissertação", "Migração do Data Warehouse"],
                    "Pesquisa séries temporais; revisa meu método e conhece o stack de nuvem.",
                    "Troca rápida por chat; adora revisar código."),
    "Tiago Duarte": ("Irmão e parceiro de treino", "", ["Meia Maratona do Recife"],
                     "Corre comigo aos domingos.",
                     "Combinar longão até quinta."),
}

# name -> (setor, relação, convenções)
ORGS = {
    "Órbita Logística": ("Logística / última milha", "cliente",
                         "Dados de entrega são confidenciais (NDA): nunca sair do ambiente do cliente."),
    "Estúdio Duarte": ("Educação e consultoria", "minha empresa",
                       "Tom da marca: claro, sem jargão, exemplos reais."),
    "UFPE": ("Universidade", "mestrado",
             "Normas ABNT; dados da pesquisa anonimizados."),
}

# id -> (título, projeto, data, uma linha, contexto, opções, decisão, consequências)
DECISIONS = {
    "DEC-2026-001": ("Painel lê só do warehouse", "Painel de Entregas", "2026-09-15",
                     "O painel nunca consulta o banco legado diretamente.",
                     "O banco legado cai sob carga e a migração já está em curso.",
                     ["Ler do legado agora — rápido, mas frágil e descartável",
                      "Ler só do warehouse — depende da migração, mas é definitivo"],
                     "Opção 2, decidida com [[People/Rafael Nogueira|Rafael]] e [[People/Diego Antunes|Diego]].",
                     "O go-live do painel passa a depender da tabela de entregas migrada. Proibido criar consulta ao legado."),
    "DEC-2026-002": ("Turma 1 ao vivo, não gravada", "Curso Dados para PMs", "2026-09-22",
                     "A primeira turma é 100% ao vivo; gravação só a partir da turma 2.",
                     "Dúvida entre vender curso gravado (escala) ou ao vivo (aprendizado sobre o aluno).",
                     ["Gravado — escala, mas sem feedback", "Ao vivo — limita a 40, mas ensina o que ajustar"],
                     "Ao vivo, decidido com [[People/Bruno Teixeira|Bruno]].",
                     "Limite de 40 vagas. Página de vendas não promete acesso vitalício."),
    "DEC-2026-003": ("Go-live por filial", "Painel de Entregas", "2026-09-29",
                     "O painel entra em produção uma filial por semana, começando por Recife.",
                     "Um go-live único nas 4 filiais concentraria risco na semana do prazo.",
                     ["Big bang em 30/10", "Uma filial por semana a partir de 09/10"],
                     "Uma filial por semana, proposta de [[People/Camila Prado|Camila]], aprovada por [[People/Rafael Nogueira|Rafael]].",
                     "Recife 09/10 · Salvador 16/10 · Fortaleza 23/10 · Natal 30/10."),
    "DEC-2026-004": ("Newsletter quinzenal", "Site e Newsletter", "2026-10-01",
                     "A newsletter passa de semanal para quinzenal até o fim do lançamento.",
                     "A cadência semanal competia com a produção do curso.",
                     ["Manter semanal com textos curtos", "Quinzenal com texto completo"],
                     "Quinzenal, decidido com [[People/Lívia Marques|Lívia]].",
                     "Edições às quartas, semanas ímpares. Reavaliar em 2026-12-01."),
}


def fm(**fields):
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines += [f"  - {item}" for item in value]
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines + ["---", ""])


def write(rel, text):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def person_link(name):
    return f"[[People/{name}|{name}]]"


def project_link(name):
    return f"[[Projetos/{name} — Visão Geral|{name}]]"


def dec_link(label):
    dec_id = label.split(" — ")[0]
    return f"[[Decisões/{dec_id} — {DECISIONS[dec_id][0]}|{label}]]"


def build_me():
    by_area = {}
    for name, (area, desc, meta, prazo, *_rest) in PROJECTS.items():
        by_area.setdefault(area, []).append(
            f"**{name}.** {desc} Meta: {meta} · 📅 {prazo}\n→ {project_link(name)}")
    sections = "\n\n".join(
        f"### {AREAS[a][0]} `{a}` — {AREAS[a][1]}\n\n" + "\n\n".join(items)
        for a, items in by_area.items())
    write("ME.md", fm(title="ME — Perfil e Contexto", type="about", created=CREATED,
                      tags=["sobre", "perfil", "moc"]) + f"""
# 👤 ME — Marina Duarte

> Página de entrada do vault. Reúne quem sou, como trabalho e o índice dos projetos ativos. **A IA deve ler esta nota primeiro, sempre.**
>
> fonte: CV colado em {CREATED} + conversa de onboarding

## Quem sou

- **Nome:** Marina Duarte
- **Headline:** Consultora de produto e dados · Estúdio Duarte · mestranda em Ciência de Dados (UFPE)
- **Resumo:** 9 anos entre produto e analytics em logística e marketplaces. Hoje divido a semana entre um cliente grande, meu curso e a dissertação.
- **Local:** Recife, Brasil
- **Idiomas:** português, inglês, espanhol

## Como trabalho (preferências)

- **Tom:** conciso e direto — corta palavra que não muda o ponto.
- **Metodologia:** MVP → validação → escala. Decisão registrada no mesmo dia.
- **Restrições:** dado de cliente nunca sai do ambiente do cliente. Nada enviado em meu nome sem eu ler.
- **Ritmo:** manhãs para trabalho profundo; reuniões só depois das 14h.

## 🚀 Projetos Ativos (por área)

> Todo projeto pertence a exatamente uma área. Índices transversais: [[People/People — Índice|People]] · [[Decisões/Decisões — Índice|Decisões]].

{sections}

### ⚙️ Sistema (meta)

- **AIOS** — mapas, skills e schedules ([[AIOS/Systems/AIOS — Como Funciona|como funciona]]).

## 🔗 Atalhos

- [[AIOS/Maps/Vault Map|Vault Map]] · [[AIOS/Maps/Skill Map|Skill Map]] · [[AIOS/Tasks/Tarefas|Tarefas]] · [[AIOS/Inbox|Inbox]]

*Última atualização: {TODAY}*
""")


def build_projects():
    (OUT / "Projetos" / "Projeto Exemplo — Visão Geral.md").unlink()
    for name, (area, desc, meta, prazo, people, decs, status) in PROJECTS.items():
        pessoas = "\n".join(f"- {person_link(p)} — {PEOPLE[p][0]}" for p in people)
        decisoes = "\n".join(f"- {dec_link(d)}" for d in decs) or "- (nenhuma registrada ainda)"
        write(f"Projetos/{name} — Visão Geral.md",
              fm(title=f"{name} — Visão Geral", type="project", area=area, status="ativo",
                 prazo=prazo, created=CREATED, tags=["projeto", f"area/{area}"]) + f"""
# 🚀 {name} — Visão Geral

> Hub do projeto: o que é, meta, prazo, quem participa e onde está cada coisa.

## Contexto

- **O que é:** {desc}
- **Meta:** {meta} · 📅 {prazo}
- **Área (dono):** `{area}` · perfil em [[ME]]

## Pessoas

{pessoas}

## Decisões do projeto

{decisoes}

## Status atual

- {TODAY} — {status}
""")


def build_people():
    for name, (papel, org, projetos, linha, interagir) in PEOPLE.items():
        org_link = f"[[People/Orgs/{org}|{org}]]" if org else "—"
        write(f"People/{name}.md",
              fm(type="pessoa", papel=papel, organizacao=org or "—", created=CREATED,
                 tags=["pessoa"]) + f"""
# 👤 {name}

> {linha}

## Papel e contexto

- **Papel:** {papel}
- **Organização:** {org_link}
- **Projetos:** {" · ".join(project_link(p) for p in projetos)}

## Como interagir

- {interagir}

## Histórico e notas

- {CREATED} — nota criada no onboarding
""")
    for name, (setor, relacao, conv) in ORGS.items():
        membros = [p for p, v in PEOPLE.items() if v[1] == name]
        projetos = sorted({proj for p in membros for proj in PEOPLE[p][2]})
        write(f"People/Orgs/{name}.md",
              fm(type="org", setor=setor, relacao=relacao, created=CREATED, tags=["org"]) + f"""
# 🏢 {name}

> {setor} — {relacao}.

## Relação

- **Tipo:** {relacao}
- **Projetos:** {" · ".join(project_link(p) for p in projetos)}

## Pessoas

{chr(10).join(f"- {person_link(p)} — {PEOPLE[p][0]}" for p in membros)}

## Convenções

- {conv}
""")
    por_projeto = "\n\n".join(
        f"### {project_link(name)}\n" + "\n".join(
            f"- {person_link(p)} — {PEOPLE[p][0]}" for p in data[4])
        for name, data in PROJECTS.items())
    orgs = "\n".join(f"- [[People/Orgs/{o}|{o}]] — {v[1]}" for o, v in ORGS.items())
    write("People/People — Índice.md",
          fm(type="index", created=CREATED, tags=["index", "pessoa", "moc"]) + f"""
# 👥 People — Índice

> Pessoas e organizações do ecossistema, cruzando projetos. Template: [[People/_Template Pessoa|_Template Pessoa]].

## Por projeto

{por_projeto}

## Organizações

{orgs}
""")


def build_decisions():
    rows = []
    for dec_id, (titulo, projeto, data, linha, contexto, opcoes, decisao, conseq) in DECISIONS.items():
        note = f"{dec_id} — {titulo}"
        rows.append(f"| {dec_id} | [[Decisões/{note}\\|{titulo}]] | {project_link(projeto).replace('|', chr(92) + '|')} | {data} | ✅ |")
        write(f"Decisões/{note}.md",
              fm(type="decisao", status="aceita", data=data, projeto=projeto, created=data,
                 tags=["decisao"]) + f"""
# 🧭 {note}

> {linha}

## Contexto

{contexto} Projeto: {project_link(projeto)}.

## Opções consideradas

{chr(10).join(f"{i}. {o}" for i, o in enumerate(opcoes, 1))}

## Decisão

{decisao}

## Consequências

{conseq}
""")
    write("Decisões/Decisões — Índice.md",
          fm(type="index", created=CREATED, tags=["index", "decisao", "moc"]) + f"""
# 🧭 Decisões — Índice

> Registro central de decisões (ADR-style). Uma nota por decisão, numeração DEC-AAAA-NNN. Template: [[Decisões/_Template Decisão|_Template Decisão]].
>
> **Regra de ouro:** decisão que muda nome, escopo, dinheiro ou processo → ganha nota aqui no mesmo dia.

## Decisões registradas

| # | Decisão | Projeto | Data | Status |
|---|---|---|---|---|
{chr(10).join(rows)}

## Backlog (decisões a registrar)

- [ ] Preço da turma 2 do curso
""")


def build_system():
    write("AIOS/Tasks/Tarefas.md",
          fm(title="Tarefas", type="tasks", created=CREATED, updated=TODAY,
             tags=["aios", "tasks", "kanban"]) + f"""
# ✅ Tarefas

> Quadro central de tarefas do AIOS. Tudo que está em **A Fazer** e **Em Andamento** entra no [[AIOS/Skills/Daily Briefing|Daily Briefing]].
>
> **Formato:** `- [ ] (🔴/🟡/🟢) #projeto · texto · 📅 AAAA-MM-DD`

**Marcos:** Painel — go-live Recife 📅 2026-10-09 · Curso — abertura de vendas 📅 2026-10-20 · Mestrado — qualificação 📅 2026-12-04

## 🔥 Vencidas — confirmar status

- [ ] 🔴 #mestrado · Enviar capítulo 3 ao [[People/Prof. Otávio Barros|Prof. Otávio]] · 📅 2026-10-02

## 🟦 A Fazer

- [ ] 🔴 #painel · Fechar as 2 métricas de SLA com a [[People/Camila Prado|Camila]] · 📅 2026-10-07
- [ ] 🔴 #curso · Revisar página de vendas com a [[People/Lívia Marques|Lívia]] · 📅 2026-10-08
- [ ] 🟡 #warehouse · Validar tabela de frota com o [[People/Diego Antunes|Diego]] · 📅 2026-10-13
- [ ] 🟡 #newsletter · Escrever a edição #15 · 📅 2026-10-19
- [ ] 🟢 #pessoal · Inscrição na meia maratona · 📅 2026-10-15

## 🟨 Em Andamento

- [ ] 🔴 #painel · Homologação na filial Recife · 📅 2026-10-09
- [ ] 🟡 #curso · Gravar abertura do módulo 3 com o [[People/Bruno Teixeira|Bruno]]

## 🟩 Concluído

- [x] 🔴 #warehouse · Carga histórica de entregas · ✅ 2026-10-02
- [x] 🟡 #newsletter · Agendar a edição #14 · ✅ 2026-10-05

---
> Quadro lido pelo [[AIOS/Skills/Daily Briefing|Daily Briefing]] (seção "Tarefas em aberto").
""")
    write("AIOS/Inbox.md",
          fm(title="Inbox", type="inbox", created=CREATED, tags=["aios", "inbox"]) + f"""
# 📥 Inbox

> Captura rápida de ideias e tarefas soltas. Alimentado pela skill [[AIOS/Skills/Captura para Inbox|Captura → Inbox]].

## Aberto

- [ ] {TODAY} · #curso · (ideia) · estudo de caso do módulo 4 usando o painel da Órbita, anonimizado → {project_link("Curso Dados para PMs")}
- [ ] {YESTERDAY} · #painel · (tarefa) · perguntar ao Rafael quem cobre a operação em Natal no go-live → {project_link("Painel de Entregas")}
- [ ] {YESTERDAY} · #pessoal · (lembrete) · trocar o tênis antes do longão de 16 km

## Processado

- [x] 2026-10-01 · #newsletter · (decisão) · cadência quinzenal → [[Decisões/DEC-2026-004 — Newsletter quinzenal|DEC-2026-004]]
""")
    write(f"AIOS/History/{TODAY}.md",
          fm(title=f"Daily Briefing — {TODAY}", type="daily", created=TODAY,
             tags=["aios", "daily"]) + f"""
# ☀️ {TODAY}

## 📥 E-mail (precisa de mim)

- [[People/Camila Prado|Camila]] — "SLA: falta definir 'entrega atrasada'" — responder antes da reunião das 14h
- [[People/Prof. Otávio Barros|Prof. Otávio]] — "Capítulo 3?" — enviar hoje (venceu em 02/10)
- ⚠️ suspeito — "URGENTE: confirme seus dados de acesso" — remetente desconhecido, ignorado

## 📅 Hoje na agenda

- 14:00 — Semanal do Painel — Camila, Diego
- 16:30 — Alinhamento do módulo 3 — Bruno

## ✅ Tarefas em aberto

- 🔥 🔴 #mestrado — Enviar capítulo 3 ao Prof. Otávio — 📅 2026-10-02 (vencida)
- 🔴 #painel — Fechar as 2 métricas de SLA — 📅 2026-10-07
- 🔴 #painel — Homologação na filial Recife — 📅 2026-10-09
- 🔴 #curso — Revisar página de vendas — 📅 2026-10-08
- 🟡 #warehouse — Validar tabela de frota — 📅 2026-10-13

## 🟢 Ontem (o que avançou)

- {project_link("Site e Newsletter")} — edição #14 agendada
- {project_link("Painel de Entregas")} — roteiro de homologação revisado

## 🎯 Foco de hoje (top 3)

1. Enviar o capítulo 3 — está vencido e trava a qualificação.
2. Levar uma definição de "entrega atrasada" para a reunião das 14h.
3. Página de vendas: comentários para a Lívia até o fim do dia.

## ⏱️ Prazos no radar

- {project_link("Painel de Entregas")} — go-live Recife 2026-10-09 — 3 dias
- {project_link("Curso Dados para PMs")} — abertura de vendas 2026-10-20 — 14 dias
- {project_link("Dissertação")} — qualificação 2026-12-04 — 59 dias

## 📝 Sessões

- 09:40 — Rascunho da definição de SLA para o painel; gravado em {project_link("Painel de Entregas")}.
""")
    write(f"AIOS/History/{YESTERDAY}.md",
          fm(title=f"Daily Briefing — {YESTERDAY}", type="daily", created=YESTERDAY,
             tags=["aios", "daily"]) + f"""
# ☀️ {YESTERDAY}

## 🎯 Foco de hoje (top 3)

1. Agendar a edição #14 da newsletter.
2. Revisar o roteiro de homologação do painel.
3. Longão de 14 km registrado.

## 📝 Sessões

- 10:15 — Edição #14 revisada e agendada → {project_link("Site e Newsletter")}.
- 15:30 — Roteiro de homologação revisado com a Camila → {project_link("Painel de Entregas")}.
- 18:05 — Captura: dúvida sobre cobertura em Natal → [[AIOS/Inbox|Inbox]].
""")

    vault_map = (OUT / "AIOS/Maps/Vault Map.md").read_text(encoding="utf-8")
    start = vault_map.index("Cada pasta no topo")
    end = vault_map.index("## 👥 People")
    areas = "\n".join(f"- {emoji} `{a}` — {desc}" for a, (emoji, desc) in AREAS.items())
    rows = "\n".join(
        f"| Projetos/{name} | {data[0]} | Projeto | [[Projetos/{name} — Visão Geral\\|Visão Geral]] | 🟢 Ativo |"
        for name, data in PROJECTS.items())
    vault_map = vault_map[:start] + f"""Todo projeto pertence a uma **área** (campo `area:` no frontmatter do hub; cores por área no Graph view):

{areas}

Comece sempre pelo arquivo de **entrada** listado abaixo — ele linka o resto. `AIOS/` é **sistema** (meta); `People/` e `Decisões/` são transversais.

| Pasta | Área | Tipo | Entrada | Status |
|---|---|---|---|---|
{rows}
| People | transversal | Pessoas & Orgs | [[People/People — Índice\\|Índice]] | 🟢 |
| Decisões | transversal | Registro ADR | [[Decisões/Decisões — Índice\\|Índice]] | 🟢 |
| AIOS | ⚙️ sistema | Sistema | [[AIOS/Maps/Vault Map\\|Vault Map]] · [[AIOS/Maps/Skill Map\\|Skill Map]] | Meta |

""" + vault_map[end:]
    write("AIOS/Maps/Vault Map.md", vault_map)

    for path in OUT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "AAAA-MM-DD" in text and not path.name.startswith("_Template") and "Skills" not in path.parts:
            text = text.replace("created: AAAA-MM-DD", f"created: {CREATED}")
            text = text.replace("*Última atualização: AAAA-MM-DD*", f"*Última atualização: {TODAY}*")
            path.write_text(text, encoding="utf-8")


def build_obsidian_config():
    colors = {"orbita": 0xE94560, "estudio": 0x16C79A, "mestrado": 0x4A90D9, "pessoal": 0xF5A623}
    groups = [{"query": f"tag:#area/{a}", "color": {"a": 1, "rgb": rgb}} for a, rgb in colors.items()]
    groups += [
        {"query": "path:People", "color": {"a": 1, "rgb": 0x9B59B6}},
        {"query": "path:Decisões", "color": {"a": 1, "rgb": 0x2ECC71}},
        {"query": "path:AIOS", "color": {"a": 1, "rgb": 0x95A5A6}},
    ]
    config = OUT / ".obsidian"
    config.mkdir(exist_ok=True)
    (config / "graph.json").write_text(json.dumps({
        "colorGroups": groups, "showTags": False, "showAttachments": False,
        "showOrphans": False, "hideUnresolved": True, "showArrow": False, "close": True,
        "search": "-file:_Template -file:README", "textFadeMultiplier": -1.2,
        "nodeSizeMultiplier": 1.35, "lineSizeMultiplier": 1.1,
        "centerStrength": 0.45, "repelStrength": 12, "linkStrength": 1, "linkDistance": 180,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (config / "app.json").write_text(json.dumps({"showInlineTitle": False}, indent=2) + "\n")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT)
    build_me()
    build_projects()
    build_people()
    build_decisions()
    build_system()
    build_obsidian_config()
    write("README.md", """# Demo vault

A filled-in copy of [`vault-template/`](../../vault-template) for a **fictional** operator (Marina Duarte — every person, company and project here is invented). It is what the screenshots in the main README are taken from, and what a vault looks like right after the onboarding conversation plus a week of use.

Open this folder as a vault in Obsidian to explore it, or point your AI assistant at it and say **"start"**.

Generated by [`scripts/build_demo_vault.py`](../../scripts/build_demo_vault.py) — edit the script, not these files.

---

Cópia preenchida do `vault-template/` para uma operadora **fictícia** (todas as pessoas, empresas e projetos são inventados). É a fonte dos screenshots do README. Abra esta pasta como vault no Obsidian, ou conecte sua IA e diga **"start"**.
""")
    print(f"demo vault written to {OUT.relative_to(ROOT)} ({len(list(OUT.rglob('*.md')))} notes)")


if __name__ == "__main__":
    main()
