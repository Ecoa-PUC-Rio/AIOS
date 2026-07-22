# 02 — O Cérebro Digital (camada de metadados)

*[English version → 02-digital-brain.md](02-digital-brain.md)*

Pastas respondem "onde fica?". O cérebro precisa de mais duas respostas que pastas não dão: **o que esta nota é?** e **de quem ela é?** O AIOS codifica as duas no frontmatter, para qualquer ferramenta (Dataview, Brain Atlas, Graph view — ou o próprio LLM) fatiar o vault por função ou por dono sem reorganizar uma pasta sequer.

## `type` — o que a nota é (função)

| `type` | Significado | Região no Brain Atlas |
|---|---|---|
| `project` / `projeto` | Hub ou nota de projeto | **Frontal** (executivo) |
| `decisao` / `decision` | Decisão registrada (ADR) | **Frontal** |
| `pessoa` / `person`, `org` | Pessoa ou organização | **Temporal** (social) |
| `referencia` / `source` | Referência externa, paper, norma, repo | **Occipital** (percepção) |
| `daily` | Nota diária / log de briefing | **Cerebelo** (memória temporal) |
| `index` / `map` / `dashboard` | Navegação, MOCs, roteamento | **Tronco cerebral** (routing) |
| `concept` / `tool` (default) | Conceitos, ferramentas, notas de trabalho | **Parietal** (integração) |
| `skill`, `system`, `inbox`, `tasks` | Maquinário do AIOS | — |

Com o plugin [Brain Atlas](https://github.com/colorpulse6/brain-atlas), esses tipos viram literalmente regiões cerebrais (ver `plugin-configs/`). Precedência do plugin: value map do frontmatter → campo `type` → tags → nomes de pasta → default.

## `area` — de quem a nota é (dono)

Defina uma vez seus contextos de trabalho de topo — ex.: `cliente-x`, `minha-empresa`, `universidade`, `pessoal` — e carimbe `area: <x>` (+ tag `#area/<x>`) em todo hub. Regras práticas:

- **Todo projeto tem exatamente um dono.** Conteúdo produzido *para* uma parceria pertence à área da parceria, não a quem produziu.
- Área ≠ região. Região diz o que a nota *é*; área diz *de quem ela é*. São ortogonais por design.
- Pinte o Graph view por área (`plugin-configs/graph.colorGroups.json`) — o dono fica visível de relance, e notas "mal agrupadas" (linkadas entre áreas) deixam de enganar.

## Estruturas transversais

**`People/`** — uma nota por pessoa (`type: pessoa`) e por organização (`People/Orgs/`, `type: org`): papel, org, projetos (wikilinks), contato, como interagir, histórico de interações. Este é o contexto que um LLM *não consegue inferir dos documentos* — quem é quem, quem decide o quê, como falar com cada um. Transforma o vault num CRM leve e povoa a região Temporal.

**`Decisões/`** — registro estilo ADR, uma nota por decisão (`type: decisao`, id `DEC-AAAA-NNN`): contexto → opções → decisão → consequências. Regra de ouro: *decisão que muda nome, escopo, dinheiro ou processo ganha nota no mesmo dia.* ADRs específicos de projeto podem viver dentro do projeto; o índice central linka todos. É o que impede a IA (e você) de re-litigar decisões antigas.

## Por que isso importa para LLMs

Quando o assistente inicia, `ME.md` + mapas dão identidade e navegação; `type`/`area` dão **semântica consultável** ("liste decisões abertas da área X", "quem está envolvido no projeto Y"); People/ e Decisões/ dão **contexto social e histórico**. Resultado: respostas ancoradas no seu estado real, não em suposições.
