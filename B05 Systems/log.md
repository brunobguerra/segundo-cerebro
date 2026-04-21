# Log da wiki (append-only)

Formato de cabeçalho (parseável):

- `## [YYYY-MM-DD] ingest | <título curto>`
- `## [YYYY-MM-DD] lint | <resumo>`
- `## [YYYY-MM-DD] query | <tópico>`

---

## [2026-04-21] move | `tools/` → `B03 Resources/tools/`

- `wiki_search.py` e documentação (`README.md`, `CLAUDE.md`, bootstrap) atualizados; default `--root` = três níveis acima do script.

## [2026-04-21] restructure | Layout A/B/C no repositório

- `raw/` e `wiki/` removidos da raiz; conteúdo movido para:
  - `A00 Inbox/clippings/` (ex-`raw/clippings/`)
  - `B03 Resources/{concepts,sources,entities}/`, `B05 Systems/{overview,index,log,meta}/`, `B01 Projects/explorations/`
- Criadas pastas vazias A01–A05, B04, C02–C05 com `README.md`; `C04 Claude Obsidian/README.md` explica o análogo do vídeo.
- Schema: `.cursor/CLAUDE.md`, `.cursor/rules/llm-wiki.mdc`, `B03 Resources/tools/wiki_search.py` atualizados.

## [2026-04-21] meta | Mapeamento pastas A/B/C (Obsidian Ana Jords)

- `B05 Systems/meta/operacao-ia.md`: secção “Esquema de pastas da Ana (A / B / C)” — inbox/processamento vs PARA/systems vs integrações + `C04 Claude Obsidian`; equivalentes no repo.

## [2026-04-21] governance | Três fluxos + papéis (vídeo Ana Jords)

- Referência: [YouTube](https://youtu.be/8NOxb2WV95I)
- Atualizado: `.cursor/CLAUDE.md` (secção *Three workflows*), `README.md`, `raw/README.md`; nova página `B05 Systems/meta/operacao-ia.md`; `B05 Systems/index.md` com secção Meta.
- Intenção: separar cérebro autoral (`raw/`), ambiente da IA (`.cursor/`, tools) e fluxo integrado (`wiki/`) com limites explícitos de autonomia do agente.

## [2026-04-21] ingest | Teoria dos grafos — intro, matriz e lista de adjacência

- Raw: `A00 Inbox/clippings/Teoria dos Grafos —Introdução, Definições, Matriz e Lista de Adjacência.md`
- Wiki pages touched: `B03 Resources/sources/teoria-dos-grafos-intro-matriz-lista-adjacencia.md`, `B03 Resources/concepts/teoria-dos-grafos.md`, `B03 Resources/concepts/grafos-representacoes.md`, `B03 Resources/entities/anwar-hermuche.md`, `B05 Systems/overview.md`, `B05 Systems/index.md`, `B05 Systems/log.md`
- Open questions: parte 2 (DFS/BFS) ainda por ingerir; conferir convenções do teu curso para “caminho” vs repetição de arestas; pequeno lapso A→B vs A→D no texto original.

## [2026-04-21] ingest | Matplotlib e Storytelling com Dados — Pt. II

- Raw: `A00 Inbox/clippings/Matplotlib e Storytelling com Dados 1.md`
- Wiki pages touched: `B03 Resources/sources/matplotlib-storytelling-dados-pt-ii.md`, `B03 Resources/concepts/analise-exploratoria-vs-explanatoria.md`, `B03 Resources/concepts/matplotlib.md`, `B03 Resources/concepts/storytelling-com-dados.md`, `B03 Resources/sources/matplotlib-storytelling-dados-pt-i.md`, `B03 Resources/entities/henrique-w-franco.md`, `B05 Systems/overview.md`, `B05 Systems/index.md`, `B05 Systems/log.md`
- Open questions: checar consistência numérica 2008 vs 2009–2017 ao reproduzir o caso; links externos (Kaggle, Colab, LinkedIn) podem mudar.

## [2026-04-21] ingest | Matplotlib e Storytelling com Dados — Pt. I

- Raw: `A00 Inbox/clippings/Matplotlib e Storytelling com Dados.md`
- Wiki pages touched: `B03 Resources/sources/matplotlib-storytelling-dados-pt-i.md`, `B03 Resources/concepts/matplotlib.md`, `B03 Resources/concepts/storytelling-com-dados.md`, `B03 Resources/entities/henrique-w-franco.md`, `B05 Systems/overview.md`, `B05 Systems/index.md`, `B05 Systems/log.md`
- Open questions: Pt. II (gráfico “antes/depois”) ainda não ingerida; metadados de publicação no Medium vs datas nos comentários — usar URL/clipping como evidência principal.

## [2026-04-21] bootstrap | LLM wiki layout

Repositório inicializado com pastas `raw/`, `wiki/`, ferramenta `tools/wiki_search.py`, e documentação `CLAUDE.md` / regras Cursor.
