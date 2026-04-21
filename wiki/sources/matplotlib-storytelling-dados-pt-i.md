---
title: "Matplotlib e Storytelling com Dados — Pt. I"
slug: matplotlib-storytelling-dados-pt-i
type: source
lang: pt-BR
sources:
  - "`raw/clippings/Matplotlib e Storytelling com Dados.md`"
updated: 2026-04-21
tags: [data-science, visualização-de-dados, matplotlib, python]
summary: "Introdução ao Matplotlib (hierarquia Figure/Axes/Axis/Artist), contraste Pyplot vs OO, subplots e subplot_mosaic; prepara Pt. II com técnicas do livro Storytelling com Dados."
---

# Matplotlib e Storytelling com Dados — Pt. I

Artigo em duas partes no blog **Data Hackers** (Medium), por [[wiki/entities/henrique-w-franco|Henrique W. Franco]], conectando [[wiki/concepts/storytelling-com-dados|Storytelling com Dados (livro e princípios)]] com prática em [[wiki/concepts/matplotlib|Matplotlib]].

## Onde está a fonte

- Clipping: `raw/clippings/Matplotlib e Storytelling com Dados.md`
- URL original: [Matplotlib e Storytelling com Dados — Pt. I](https://medium.com/data-hackers/matplotlib-e-storytelling-com-dados-pt-i-48c289943d60) (Medium / Data Hackers, 2023-10-23 no clipping; comentários no final citam datas mais antigas — tratar metadados com cautela)

## Ideias centrais

1. **Narrativa + visual** — O texto ancora no livro de Cole Nussbaumer: visuais eficazes ganham força com narrativa; conhecer o público (especialmente leigos) é parte do desenho do gráfico.
2. **Objetivo da série** — Pt. I explica *como* o Matplotlib funciona; a Pt. II (tutorial com queimadas no Brasil) está resumida em [[wiki/sources/matplotlib-storytelling-dados-pt-ii|Matplotlib e Storytelling com Dados — Pt. II]].
3. **Hierarquia** — [[wiki/concepts/matplotlib|Matplotlib]] organiza o desenho em Figure → Axes → Axis → Artist; uma Figure pode ter vários Axes (ver a nota de conceito).
4. **Pyplot vs OO** — `plt.plot()` cria Figure e Axes implícitos (rápido, menos controle fino). `fig, ax = plt.subplots()` separa instâncias (melhor para subplots e customização); a série usará **OO** na Pt. II.
5. **Subplots** — Grade `nrows`/`ncols` com `axs` como array estilo NumPy ainda é comum no código legado; o artigo destaca `subplot_mosaic()` como layout mais flexível (tamanhos assimétricos, nomes semânticos).
6. **Anatomia** — Referência visual oficial (spines, grid, ticks etc.) será usada na Pt. II para “limpar” o gráfico.

## Termos (EN)

- *Figure*, *Axes* (plural do objeto de plotagem — não confundir com *Axis*), *Artist*, *pyplot*, *object-oriented API*, *subplot mosaic*, *spines*, *ticks*.

## Lacunas / continuação

- O clipping inclui paywall/upsell e rodapé de comentários Medium; o núcleo técnico está nas seções indicadas acima.

## Ver também

- [[wiki/sources/matplotlib-storytelling-dados-pt-ii|Matplotlib e Storytelling com Dados — Pt. II]]
- [[wiki/concepts/matplotlib|Matplotlib]]
- [[wiki/concepts/storytelling-com-dados|Storytelling com Dados (livro e princípios)]]
- [[wiki/entities/henrique-w-franco|Henrique W. Franco]]
