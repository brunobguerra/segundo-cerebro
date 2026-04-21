# segundo-cerebro

Cofre Obsidian/Git com **prefixos A / B / C** (entrada → PARA → integrações), inspirado na organização da [Ana Jords](https://youtu.be/8NOxb2WV95I): **`A*`** captura humana (imutável para o agente), **`B*`** wiki mantida pelo LLM, **`C*`** integrações.

## Start here

1. Abre **`.cursor/CLAUDE.md`** antes de usar um agente neste repo.
2. Coloca novas fontes em **`A00 Inbox/clippings/`** (ver `A00 Inbox/README.md`). O agente **não edita** pastas **A*** nem **C02/C03/C05**.
3. Pede **ingest de uma fonte de cada vez**; revê takeaways antes de autorizar escrita em **`B03`** / **`B05`**.
4. Navega no Obsidian (grafo, backlinks).

## Layout (raiz do vault)

| Prefix | Pastas | Função |
|--------|--------|--------|
| **A** | `A00 Inbox` … `A05 Backlog` | Captura, processamento, âncoras, imagens, daily, backlog — **só tu editas** |
| **B** | `B01 Projects`, `B03 Resources`, `B04 Archives`, `B05 Systems` | PARA + sistemas — **wiki do agente** em `B03`/`B05`/`B01` |
| **C** | `C02 Readwise` … `C05 Excalidraw` | Integrações; **`C04 Claude Obsidian`** = ponteiros / docs locais da IA |

| Destaque | Conteúdo |
|----------|-----------|
| `B03 Resources/` | `sources/`, `concepts/`, `entities/` |
| `B05 Systems/` | `overview.md`, `index.md`, `log.md`, `meta/` |
| `B03 Resources/tools/` | `wiki_search.py` — pesquisa local nos `.md` da wiki |

### Três fluxos (vídeo)

1. **Autoral** — pensamento e fontes em **`A*`** (e notas tuas, ex. `A00 Inbox/permanent/`).
2. **Ambiente da IA** — `.cursor/`, **`C04 Claude Obsidian/`**, skills Cursor.
3. **Integrado** — ingest com confirmação → síntese em **`B03`/`B05`**. Detalhes: [`B05 Systems/meta/operacao-ia.md`](B05 Systems/meta/operacao-ia.md).

## Wiki search (opcional)

Na raiz do repositório (Python 3):

```bash
python "B03 Resources/tools/wiki_search.py" "transformer"
```

Lista caminhos e linhas sob **`B01 Projects/`**, **`B03 Resources/`**, **`B05 Systems/`**.

## Remote

GitHub: [brunobguerra/segundo-cerebro](https://github.com/brunobguerra/segundo-cerebro)
