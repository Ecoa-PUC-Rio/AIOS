# Plugin configs

Ready-to-use configurations for the visualization layer of the AIOS digital brain. / Configurações prontas para a camada de visualização do cérebro digital AIOS.

## `brain-atlas.data.json` — [Brain Atlas](https://github.com/colorpulse6/brain-atlas)

Maps the AIOS `type` taxonomy (pt-BR + EN values) to Brain Atlas note kinds, so notes land in the right brain region: projects/decisions → **frontal**, people/orgs → **temporal**, sources → **occipital**, daily notes → **cerebellum**, indexes → **brain stem**, concepts/tools → **parietal**.

**How to apply / Como aplicar:** install Brain Atlas, then merge these keys into `<vault>/.obsidian/plugins/brain-atlas/data.json` (or set the equivalent mappings in the plugin settings UI). Reload Obsidian afterwards. / Instale o Brain Atlas e mescle estas chaves no `data.json` do plugin (ou configure pela UI de settings). Recarregue o Obsidian depois.

## `graph.colorGroups.json` — Obsidian Graph view

Per-area color groups so ownership is visible at a glance in the native graph. Replace the `<pasta-…>` placeholders with your top-level folders (one query per area — `OR` combines multiple folders). / Grupos de cor por área para o dono ficar visível no grafo nativo. Troque os placeholders `<pasta-…>` pelas suas pastas de topo.

**How to apply / Como aplicar:** open Graph view → Groups → create one group per line using the `query` string and pick the color; or merge the `colorGroups` array into `<vault>/.obsidian/graph.json` with Obsidian closed. Suggested palette / paleta sugerida: `#16C79A` · `#E94560` · `#4A90D9` · `#F5A623` · People `#9B59B6` · Decisions `#2ECC71` · AIOS `#95A5A6`.
