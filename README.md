# segundo-cerebro

Personal **LLM-maintained research wiki** for **data science** and **AI engineering** (articles, papers, videos). Pattern: immutable sources in `raw/`, compounding notes in `wiki/`, Obsidian as the reader.

## Start here

1. Open **`CLAUDE.md`** before using an AI agent in this repo.
2. Drop new sources under **`raw/`** (see `raw/README.md`). Do not let the agent edit `raw/`.
3. Ask the agent to **ingest one source at a time**; review takeaways before it writes to `wiki/`.
4. Browse **`wiki/`** in Obsidian (graph, backlinks).

## Layout

| Path | Role |
|------|------|
| `raw/` | Curated sources (you add; agents read-only) |
| `wiki/` | LLM-written markdown wiki + `index.md` + `log.md` |
| `tools/` | Small helpers (e.g. local wiki search) |

## Wiki search (optional)

From the repository root (Python 3):

```bash
python tools/wiki_search.py "transformer"
```

Prints matching paths and a few lines per hit under `wiki/**/*.md`.

## Remote

GitHub: [brunobguerra/segundo-cerebro](https://github.com/brunobguerra/segundo-cerebro)
