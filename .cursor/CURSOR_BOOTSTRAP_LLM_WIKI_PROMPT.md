# Cursor bootstrap prompt — LLM-maintained wiki (Karpathy-style)

**How to use:** Paste everything below the horizontal rule into a new Cursor agent chat in the repository root (`segundo-cerebro`). The agent must execute the work in-repo (create files/folders), not only describe the plan.

---

## Agent instructions (paste from here)

You are setting up a **personal LLM-maintained research wiki** for studying **data science** and **AI engineering**, inspired by the “LLM Knowledge Bases / LLM Wiki” pattern: immutable sources in `raw/`, compounding knowledge in `wiki/`, and a schema doc that turns the agent into a disciplined maintainer.

### Non-negotiables

1. **Directory model**
   - `raw/`: **immutable** curated sources (articles, papers, notes, transcripts, images). The agent **must not edit, rename, move, or delete** anything under `raw/`. Only the human adds material here (e.g. Obsidian Web Clipper exports, downloaded attachments under `raw/assets/`).
   - `wiki/`: **LLM-owned** markdown knowledge base. The human reads; the agent writes and maintains structure, links, indexes, and logs.
   - Optional helper code: `tools/` for small, dependency-light utilities (see Search tool below).

2. **Bilingual convention (Portuguese + English)**
   - Default voice: **Brazilian Portuguese (pt-BR)** for explanations, synthesis, and teaching notes.
   - **English** for: file slugs / folder names, YAML keys, standard technical terms when they are the field’s common vocabulary (e.g. *embedding*, *backpropagation*, *RAG*, *KV-cache*), and **verbatim quotes** from English sources.
   - Titles: prefer **pt-BR**, but keep recognizable English proper nouns and paper titles as-is.
   - At the top of substantive wiki pages, include a short **“Termos (EN)”** line or mini-gloss when heavy English jargon appears.

3. **Ingest workflow: one source at a time**
   - Never batch-ingest multiple new sources in one pass unless the human explicitly asks.
   - For each ingest: read the source → propose key takeaways and open questions → **wait for human confirmation on emphasis** → then update the wiki (often 5–15 files touched): source page, concept/entity pages, backlinks, `wiki/index.md`, append `wiki/log.md`.

4. **Lint: on-demand only**
   - Run “wiki health checks” only when the human requests linting.
   - Typical checks: contradictions, stale claims vs newer sources, orphan pages, missing concept pages for recurring terms, missing cross-links, broken internal links, duplicate coverage, and “next questions / next sources” suggestions.

5. **Output formats (MVP)**
   - **Markdown + Mermaid** in `wiki/` (and filed outputs under something like `wiki/explorations/` when appropriate).
   - **Do not** add Marp decks, matplotlib pipelines, or web search dependencies in this MVP unless the human later asks.

6. **Privacy**
   - Assume **no sensitive personal data**; still avoid inventing private facts about real people. Do not store credentials in-repo.

### Governance files (proposed best setup)

Create **all** of the following (names matter for ecosystem compatibility):

- **`CLAUDE.md`** (capital **CLAUDE**): canonical “schema” — architecture, conventions, workflows (ingest / query / lint), frontmatter spec, linking rules, and how `index.md` + `log.md` must be maintained. This is the single source of truth for behavior.
- **`.cursor/rules/llm-wiki.mdc`**: Cursor rule that mirrors `CLAUDE.md` policies (immutability of `raw/`, wiki ownership, bilingual rules, one-by-one ingest, on-demand lint, markdown+mermaid MVP). Keep it concise but enforceable.
- **`AGENTS.md`**: short pointer document (“Read `CLAUDE.md` first; same rules apply”) for other agent tools that look for `AGENTS.md`.

### Repository hygiene

- Initialize or preserve **git** usage. Add a sensible **`.gitignore`** (Python caches, virtualenvs, OS junk, Obsidian workspace noise if needed — but **do not** ignore the whole `.obsidian/` if the vault lives here; prefer ignoring only large caches if present).
- Add a minimal **`README.md`** at repo root explaining: what `raw/` vs `wiki/` are, Obsidian as viewer, and “open `CLAUDE.md` before working with the agent.”
- Add **`raw/README.md`** explaining how the human should drop sources and that agents must not modify `raw/`.

### Wiki structure (create empty scaffolding + seed files)

Create folders:

- `raw/assets/` (for local images/attachments referenced by clipped markdown)
- `wiki/sources/`
- `wiki/concepts/`
- `wiki/entities/` (people, orgs, models, datasets — only when useful)
- `wiki/explorations/` (answers/analyses the human wants filed back)

Seed files:

- `wiki/index.md`: start with a categorized outline and links; include instructions to the agent that it must update this file after every ingest and after major queries that create new pages.
- `wiki/log.md`: append-only timeline. Each entry starts with a parseable heading like `## [YYYY-MM-DD] ingest | <short title>` or `## [YYYY-MM-DD] lint | summary` or `## [YYYY-MM-DD] query | <topic>`.

### Frontmatter (required on new wiki pages)

Use YAML at the top of wiki pages (not required on `index.md` / `log.md` unless useful):

```yaml
---
title: "<pt-BR title>"
slug: "<ascii-kebab-case>"
type: source|concept|entity|exploration|overview
lang: pt-BR
sources:
  - "[[<link to wiki source page or raw path note>]]"
updated: YYYY-MM-DD
tags: [data-science, ai-engineering]
summary: "<one line, pt-BR>"
---
```

Rules:

- `slug` matches filename without `.md` where possible.
- `sources` lists what raw/wiki evidence backs the page.
- Internal links use Obsidian-style `[[...]]` **without** file extensions, pointing to wiki page titles or explicit paths consistent with your chosen convention (document the convention in `CLAUDE.md`).

### Linking and page quality rules

- Prefer dense internal links: every new page should link “up” to concepts and “sideways” to related pages.
- When integrating a new source, update **overview/synthesis** pages if your wiki uses them (create `wiki/overview.md` if missing).
- Keep claims grounded: if uncertain, label uncertainty explicitly and propose what evidence would resolve it (do not present guesses as facts).

### Search tool (recommended MVP)

Add **`tools/wiki_search.py`** (stdlib only): CLI that searches `wiki/**/*.md` for a query string (case-insensitive), prints paths + a few matching lines. No external dependencies. Document usage at the bottom of `README.md` and mention in `CLAUDE.md` as an optional agent tool for larger wikis.

### What to deliver in one pass

1. Create the folder tree and seed markdown files (`wiki/index.md`, `wiki/log.md`, `raw/README.md`, root `README.md`).
2. Write **`CLAUDE.md`** comprehensively (this prompt’s rules + expanded operational detail).
3. Write **`.cursor/rules/llm-wiki.mdc`** with `alwaysApply: true` (or equivalent) so Cursor agents inherit it.
4. Write **`AGENTS.md`**.
5. Add **`.gitignore`** and **`tools/wiki_search.py`**.
6. If `git` has no commits yet, make an initial commit with message: `chore: bootstrap llm-maintained wiki layout`.

### Git remote (optional)

If no `origin` is configured and the human uses GitHub, they may add: `https://github.com/brunobguerra/segundo-cerebro` — do not force network operations; only suggest commands if appropriate.

### Style

- Be concrete and operational in `CLAUDE.md` (checklists, examples of log lines, examples of ingest confirmation prompts).
- Do not create placeholder “Lorem ipsum” wiki articles; only scaffolding + index/log seeds.

**Start now:** implement the repository layout and files exactly as specified, then summarize what you created and where the human should begin (first ingest).

---

## End of agent instructions
