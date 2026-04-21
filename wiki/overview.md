---
title: "Visão geral — ciência de dados e engenharia de IA"
slug: overview
type: overview
lang: pt-BR
sources:
  - "[[wiki/sources/matplotlib-storytelling-dados-pt-i|Matplotlib e Storytelling com Dados — Pt. I]]"
  - "[[wiki/sources/matplotlib-storytelling-dados-pt-ii|Matplotlib e Storytelling com Dados — Pt. II]]"
  - "[[wiki/sources/teoria-dos-grafos-intro-matriz-lista-adjacencia|Teoria dos grafos — introdução, definições, matriz e lista de adjacência]]"
updated: 2026-04-21
tags: [data-science, ai-engineering]
summary: "Ponto de entrada: síntese acumulativa do que a wiki já cobre (atualizar após ingestões)."
---

# Visão geral

Página **viva** de síntese. Após cada ingestão, o agente deve revisar se esta visão geral precisa de ajustes (novos temas, conexões, lacunas).

## Termos (EN)

- *Data science*, *machine learning*, *LLM*, *RAG*, *evals*, *training*, *inference* — usar conforme convenção em `CLAUDE.md` (pt-BR + termos EN quando for o vocabulário usual do campo).

## O que já entrou na wiki

- **Visualização e narrativa** — A comunicação com dados melhora quando [[wiki/concepts/storytelling-com-dados|storytelling]] (audiência, clareza, ênfase) encontra ferramentas como [[wiki/concepts/matplotlib|Matplotlib]]: na [[wiki/sources/matplotlib-storytelling-dados-pt-i|Pt. I]], hierarquia Figure/Axes, *pyplot* vs OO e `subplot_mosaic`; na [[wiki/sources/matplotlib-storytelling-dados-pt-ii|Pt. II]], fluxo **exploratório → explanatório** ([[wiki/concepts/analise-exploratoria-vs-explanatoria|conceito]]), decluttering (*spines*, grade, *ticks*), ênfase com cor/tamanho/`axvspan`, texto com `transAxes` e sequência de “história” para apresentação.
- **Grafos (bases)** — A fonte [[wiki/sources/teoria-dos-grafos-intro-matriz-lista-adjacencia|Teoria dos grafos — introdução…]] resume **G = (V, A)**, digrafos vs não direcionados, passeio/caminho/ciclo, graus, conexidade forte/fraca e ligação com **árvores**; em [[wiki/concepts/grafos-representacoes|representações]], contrasta **matriz de adjacência** (Θ(V²), teste de arco O(1)) com **lista de adjacência** (melhor em grafos esparsos). Continuação prometida pelo autor: **DFS/BFS**.

## Próximos passos

- Ingerir a **parte 2** do fio de grafos (DFS/BFS) quando o clipping estiver em `raw/`.
- Acrescentar outras fontes sobre *evals*, modelagem e engenharia de IA conforme seu roteiro de estudo.
