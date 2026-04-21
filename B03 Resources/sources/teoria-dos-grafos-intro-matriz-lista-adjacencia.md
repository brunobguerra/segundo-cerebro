---
title: "Teoria dos grafos — introdução, definições, matriz e lista de adjacência"
slug: teoria-dos-grafos-intro-matriz-lista-adjacencia
type: source
lang: pt-BR
sources:
  - "`A00 Inbox/clippings/Teoria dos Grafos —Introdução, Definições, Matriz e Lista de Adjacência.md`"
updated: 2026-04-21
tags: [data-science, estruturas-de-dados, grafos, algoritmos]
summary: "Medium (Anwar Hermuche): grafos direcionados/não direcionados, formalismo G=(V,A), passeio/caminho/ciclo, grau, conexidade, árvores; grade 0/1; matriz e lista de adjacência; promessa de Pt. II com DFS/BFS."
---

# Teoria dos grafos — introdução, definições, matriz e lista de adjacência

Artigo introdutório em português (Medium), por [[B03 Resources/entities/anwar-hermuche|Anwar Hermuche]], ligando **teoria dos grafos** a usos em ciência de dados (ex.: intuição para árvores de decisão) e às **representações em memória** tratadas nas notas [[B03 Resources/concepts/teoria-dos-grafos|Teoria dos grafos (fundamentos)]] e [[B03 Resources/concepts/grafos-representacoes|Representações de grafos (matriz e lista)]].

## Onde está a fonte

- Clipping: `A00 Inbox/clippings/Teoria dos Grafos —Introdução, Definições, Matriz e Lista de Adjacência.md`
- URL original: [Teoria dos Grafos — Introdução, Definições, Matriz e Lista de Adjacência](https://medium.com/@anwarhermuche/teoria-dos-grafos-introdu%C3%A7%C3%A3o-defini%C3%A7%C3%B5es-matriz-e-lista-de-adjac%C3%AAncia-2252d4800a44) (2024-04-02 no frontmatter do clipping)

## Mapa do conteúdo

1. **Definições visuais** — *Vértices* / *nós*; *arestas*; grafos **não direcionados** vs **direcionados** (orientação importa ou não).
2. **Limite de arestas (direcionado)** — Com laços permitidos e ordem importando nos pares, até **V²** arestas distintas (argumento combinatório do artigo).
3. **Formalismo** — `G = (V, A)` com exemplos de conjuntos de vértices e arestas.
4. **Vizinhança** — Adjacência entre vértices.
5. **Passeio, caminho, ciclo** — *Walk* vs *path* (sem repetição de vértice/aresta conforme definição do texto); **ciclo**; menção a **ciclo hamiltoniano** quando o ciclo visita todos os vértices uma vez (exceto fecho início=fim).
6. **Ordem e grau** — Ordem = \|V\|; grau; em digrafos **grau de entrada** e **grau de saída**; laço contando como entrada e saída no exemplo do autor.
7. **Conectividade** — Grafo **conexo**; em digrafos **fortemente** vs **fracamente** conexo (ignorar direção do grafo subjacente).
8. **Casos particulares** — **Árvore** como grafo direcionado com no máximo um pai; árvore de decisão do scikit-learn como **árvore binária** (≤1 pai, exatamente 2 filhos nos nós internos conforme o texto); *linked lists* como tema futuro.
9. **Representações** — Primeiro uma **matriz 0/1** interpretada como “células livres/bloqueadas” e movimento 4-vizinhança (ponte visual para grafos em grade); depois **matriz de adjacência** e **lista de adjacência** (classe `Vertice` com `vizinhos`).

## Continuação

- O autor anuncia **parte 2** com **DFS e BFS** — ainda não ingerida nesta wiki até novo clipping.

## Nota de leitura crítica

- Num trecho sobre `matriz[0][3]`, o texto associa o índice 3 ao vértice **D**, mas escreve “para **B**” — provável lapso; confiar na convenção linha→origem, coluna→destino e nos rótulos da figura.

## Termos (EN)

- *Graph*, *vertex / node*, *edge*, *directed graph*, *undirected graph*, *loop*, *walk*, *path*, *cycle*, *Hamiltonian cycle*, *degree*, *in-degree*, *out-degree*, *connected*, *strongly connected*, *weakly connected*, *adjacency matrix*, *adjacency list*.

## Ver também

- [[B03 Resources/concepts/teoria-dos-grafos|Teoria dos grafos (fundamentos)]]
- [[B03 Resources/concepts/grafos-representacoes|Representações de grafos (matriz e lista)]]
- [[B03 Resources/entities/anwar-hermuche|Anwar Hermuche]]
