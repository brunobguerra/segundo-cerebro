---
description: 
alwaysApply: true
---

# CLAUDE.md — LLM-maintained wiki (segundo-cerebro)

This repository is a **Karpathy-style “LLM Knowledge Base”** with an **Obsidian vault layout (Ana Jords-style A / B / C prefixes)**: curated **human-only** capture under **`A*`**, compounding **Markdown (+ Mermaid)** under **`B*`**, integrations under **`C*`**, plus `.cursor/` as schema. Follow this file.

**Domain:** studying **data science** and **AI engineering** from articles and videos (and related notes).

---

## Vault layout (prefix groups)

**Human-only for the agent (read sources here; never edit, rename, move, or delete):**

| Prefix | Folder | Role |
|--------|--------|------|
| **A** | `A00 Inbox/` | Capturas para ingest (`clippings/`, opcional `permanent/`); entrada bruta |
| **A** | `A01 Processamento/` | Triagem / notas em preparação |
| **A** | `A02 Anchor Topics/` | Temas âncora / pilares |
| **A** | `A03 Banco de imagens/` | Imagens e anexos referenciados pelos `.md` |
| **A** | `A04 Daily Notes/` | Diário (se usar no mesmo repo) |
| **A** | `A05 Backlog/` | Fila “para depois” |
| **C** | `C02 Readwise/` | Export/sync Readwise |
| **C** | `C03 Books database/` | Notas de livros |
| **C** | `C05 Excalidraw/` | Desenhos |

**Agent-maintained wiki (Markdown + Mermaid):**

| Prefix | Folder | Role |
|--------|--------|------|
| **B** | `B01 Projects/` | Explorações arquivadas (`explorations/`), trabalho com fim |
| **B** | `B03 Resources/` | `sources/`, `concepts/`, `entities/` |
| **B** | `B04 Archives/` | Material inativo movido aqui quando fizeres limpeza |
| **B** | `B05 Systems/` | `overview.md`, `index.md`, `log.md`, `meta/` |

**Ambiente IA (config, não é “wiki”):** `.cursor/` (este arquivo e regras), **`C04 Claude Obsidian/`** (README / ponteiros humanos opcionais), **`B03 Resources/tools/`** (helpers locais).

---

## Architecture (conceptual layers)

1. **Capture (`A*`, parts of `C*`)** — documents **added by the human**. Agents **read only**.
2. **Wiki (`B01`, `B03`, `B05`; optionally `B04`)** — LLM-owned Markdown where allowed above. The human reads; the agent creates/updates pages, links, indexes, and logs.
3. **`CLAUDE.md`** (this file) — conventions + workflows. Co-evolve with the human over time.

Optional: **`B03 Resources/tools/`** — tiny stdlib helpers (e.g. `wiki_search.py`).

---

## Three workflows (human vs integrated vs agent tooling)

This vault follows the split discussed in [Ana Jords — segundo cérebro (Obsidian + IA)](https://youtu.be/8NOxb2WV95I): separate **where you author**, **where the AI operates autonomously**, and **where knowledge multiplies under your approval**.

| Workflow | Locations | Human | Agent |
|----------|-----------|-------|-------|
| **1 — Autorial / study** | `A00`–`A05` (incl. `A00 Inbox/clippings/`), `C02`/`C03`/`C05` como fontes suas | Escreve, deposita fontes, decide o que vale ingerir | **Somente leitura** nas zonas human-only; não substitui o teu julgamento |
| **2 — Ambiente da IA** | `.cursor/`, `C04 Claude Obsidian/` (docs), skills Cursor, `B03 Resources/tools/` | Aprova mudanças de schema | Propõe edits em `.cursor/` e `B03 Resources/tools/` quando pedires |
| **3 — Integrado (multiplicação)** | `B03 Resources/`, `B05 Systems/` (+ `B01 Projects/` quando aplicável) | Confirma takeaways antes do ingest | Autonomia **dentro dos caminhos `B*`** deste schema; **uma fonte nova por ingest** salvo pedido explícito em lote |

**PARA-ish mapping:** *projects/areas* → perguntas em `B05 Systems/overview.md` e `B01 Projects/explorations/`; *resources* → `B03 Resources/`; *archive* → `B04 Archives/` + entradas antigas em `B05 Systems/log.md`; entrada de material → **`A00 Inbox/`** primeiro.

**Trap of accumulation:** volume of notes ≠ insight. Prefer periodic **lint** (on-demand) and human pruning of what deserves to stay linked from `B05 Systems/index.md` and `B05 Systems/overview.md`.

---

## Language convention (bilingual)

- **Body text:** Brazilian Portuguese (**pt-BR**) for explanations, synthesis, and study notes.
- **English** for: YAML **keys**, **slugs**, **folder names**, common field terms (*embedding*, *fine-tuning*, *RAG*, *KV-cache*, …), and **verbatim quotes** from English sources.
- **Titles:** prefer pt-BR; keep paper titles / proper nouns as-is.
- On substantive wiki pages, add a short **“Termos (EN)”** gloss when jargon is dense.

---

## Wiki layout

| Path | Purpose |
|------|---------|
| `B03 Resources/sources/` | One page per ingested source (summary + pointer to path under `A00 Inbox/clippings/` or equivalent) |
| `B03 Resources/concepts/` | Concept pages (definitions, links, tensions) |
| `B03 Resources/entities/` | People, orgs, models, datasets — when useful |
| `B01 Projects/explorations/` | Filed answers / analyses the human wants kept |
| `B05 Systems/overview.md` | Living synthesis (“what we believe so far”) |
| `B05 Systems/index.md` | Content catalog (must be updated after ingests / major queries) |
| `B05 Systems/log.md` | Append-only timeline |

---

## Internal linking (Obsidian-style)

- Use wikilinks: `[[page title]]` or `[[folder/subfolder/page title]]` **without** `.md` extensions (paths may include spaces, e.g. `B03 Resources/concepts/foo`).
- Prefer **stable note titles** matching the `title` frontmatter field.
- Every new page should link **up** to concepts and **sideways** to related pages.
- After adding a source page, update relevant concept pages and `B05 Systems/overview.md` if needed.

---

## Frontmatter (required on new wiki pages)

Not required on `B05 Systems/index.md` / `B05 Systems/log.md` unless helpful.

```yaml
---
title: "<pt-BR title>"
slug: "<ascii-kebab-case>"
type: source|concept|entity|exploration|overview
lang: pt-BR
sources:
  - "[[...]]"   # wikilinks to source pages and/or paths like `A00 Inbox/clippings/...` in backticks if needed
updated: YYYY-MM-DD
tags: [data-science, ai-engineering]
summary: "<one line, pt-BR>"
---
```

- `slug` should match the filename stem when practical (`slug: foo` → `foo.md`).
- `sources` lists evidence backing the page.

---

## Output formats (MVP)

- **Markdown** and **Mermaid** diagrams under **`B01 Projects/`**, **`B03 Resources/`**, **`B05 Systems/`** (not under `A*` / `C02`–`C05` human zones).
- Do **not** add Marp, matplotlib pipelines, or mandatory web-search tooling unless the human asks.

---

## Workflow: Ingest (one source at a time)

**Never** ingest multiple brand-new sources in one pass unless the human explicitly requests batching.

### Steps

1. **Locate** the new source the human points to (typically a single file under `A00 Inbox/clippings/`).
2. **Read** it (if images exist, follow up by reading key images separately when needed).
3. **Propose** to the human: key takeaways, proposed wiki changes (list of pages to create/update), and open questions / uncertainties.
4. **Wait** for human confirmation on emphasis and scope.
5. **Write** the wiki updates (often 5–15 files):  
   - `B03 Resources/sources/<slug>.md`  
   - update/create `B03 Resources/concepts/*` as needed  
   - update/create `B03 Resources/entities/*` if useful  
   - update `B05 Systems/overview.md`  
   - update backlinks across touched pages  
   - update `B05 Systems/index.md`  
   - append `B05 Systems/log.md` with `## [YYYY-MM-DD] ingest | <short title>`

### Log entry template

```markdown
## [2026-04-21] ingest | <short title>

- Fonte: `A00 Inbox/clippings/...`
- Wiki pages touched: ...
- Open questions: ...
```

---

## Workflow: Query / Q&A

1. Use `B05 Systems/index.md` first to find relevant pages; drill into linked notes.
2. Answer with **citations** to wiki pages (`[[...]]`) and source paths (`` `A00 Inbox/clippings/...` ``) when appropriate.
3. If the human wants an answer preserved, create/update a page under `B01 Projects/explorations/` and link it from `B05 Systems/index.md`, then append `B05 Systems/log.md` (`query`).

---

## Workflow: Lint (on-demand only)

Run only when the human asks.

### Checklist

- Contradictions between pages; mark uncertainty or resolve with evidence.
- Stale claims vs newer sources (flag + propose update).
- Orphan pages (no inbound wikilinks).
- Recurring terms missing concept pages.
- Missing cross-links between related notes.
- Broken wikilinks (best-effort detection).
- Duplicate coverage (merge plan).
- Suggest **next questions** and **next sources** to ingest.

Append `B05 Systems/log.md`: `## [YYYY-MM-DD] lint | <one-line summary>` plus bullet findings.

---

## Mermaid

Use fenced blocks:

````markdown
```mermaid
flowchart LR
  A[A00 capture] --> B[B03+B05 wiki]
```
````

---

## Tooling: local wiki search

From repo root:

```bash
python "B03 Resources/tools/wiki_search.py" "<query>"
```

Useful when the wiki grows beyond trivial size. Still keep `B05 Systems/index.md` healthy.

---

## Privacy / safety

Assume **no highly sensitive personal data** in this vault. Do not invent private facts about real people. Never commit secrets or credentials.

---

## Git

Commit wiki changes in coherent chunks with clear messages. Do not commit large binaries unless the human explicitly wants them versioned.

---

## First action for a new session

If the human says “ingest”, identify **exactly one** new source file under `A00 Inbox/` (usually `clippings/`), then follow the ingest workflow. If unclear which file, ask.
