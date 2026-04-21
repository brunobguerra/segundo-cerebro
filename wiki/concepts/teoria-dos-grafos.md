---
title: "Teoria dos grafos (fundamentos)"
slug: teoria-dos-grafos
type: concept
lang: pt-BR
sources:
  - "[[wiki/sources/teoria-dos-grafos-intro-matriz-lista-adjacencia|Teoria dos grafos — introdução, definições, matriz e lista de adjacência]]"
updated: 2026-04-21
tags: [data-science, estruturas-de-dados, grafos, algoritmos]
summary: "G=(V,A), grafos direcionados/não direcionados, passeio/caminho/ciclo, grau, conexidade forte/fraca, árvores e ligação com ML."
---

# Teoria dos grafos (fundamentos)

Um **grafo** modela **objetos** (*vértices* / *nós*) e **relações** (*arestas* / *arcos*). É base para redes sociais, rotas, compiladores, **árvores** em ML e muitos algoritmos clássicos.

## Termos (EN)

- *Graph*, *vertex*, *edge*, *directed / undirected*, *loop*, *walk*, *path*, *cycle*, *Hamiltonian cycle*, *order*, *degree*, *in-degree*, *out-degree*, *connected*, *strongly / weakly connected*, *tree*, *binary tree*.

## Formalismo

Um grafo costuma ser denotado **G = (V, A)**, com **V** conjunto de vértices e **A** conjunto de arestas (pares ordenados em digrafos; em não direcionados costuma-se tratar aresta como par não ordenado, conforme o livro/texto que estiveres a seguir).

## Direcionado vs não direcionado

- **Não direcionado:** aresta liga os dois sentidos.
- **Direcionado (*digraph*):** respeitar a seta; ausência de arco inverso impede ir “de volta” só porque existe o caminho de ida.

## Limite simples (digrafo com laços)

Se a ordem dos extremos importa e **laços** (arco de um vértice para si) são permitidos, há no máximo **|V|²** arcos distintos (pares ordenados, incluindo (v,v)).

## Vizinhança

Dois vértices são **adjacentes** (*vizinhos*) se existe aresta/arco entre eles (respeitando orientação no caso direcionado).

## Passeio, caminho e ciclo

- **Passeio (*walk*):** sequência de vértices em que cada passo segue uma aresta disponível; vértices podem repetir-se.
- **Caminho (*path*):** passeio **sem repetir vértices** (em algumas definições também se exige não repetir arestas — alinhar com o teu curso).
- **Ciclo:** passeio fechado (início = fim); **ciclo hamiltoniano** visita todos os vértices uma vez antes de fechar (definição informal alinhada à fonte ingerida).

## Ordem e grau

- **Ordem** do grafo: número de vértices (|V|).
- **Grau:** número de arestas incidentes (definição varia com laços e direção). Em digrafos: **grau de entrada** e **grau de saída** por vértice.

## Conexidade

- **Conexo (não direcionado):** existe caminho entre qualquer par de vértices.
- **Digrafo fortemente conexo:** caminho dirigido de qualquer vértice a qualquer outro.
- **Digrafo fracamente conexo:** o grafo **subjacente** sem direção é conexo, mas nem todos os pares são alcançáveis respeitando só as setas.

## Árvores e ciência de dados

Em **matemática discreta**, *árvore* costuma significar grafo **conexo e acíclico**; o artigo ingerido enfatiza outra vista útil em ML: grafo **hierárquico** em que cada vértice tem **no máximo um pai** (árvore enraizada como digrafo “de cima para baixo”). Árvores de decisão (ex.: scikit-learn) aparecem na fonte como caso especial com restrições de **fan-out** (texto cita **árvore binária** com até dois filhos por nó interno).

## Ver também

- [[wiki/concepts/grafos-representacoes|Representações de grafos (matriz e lista)]]
- [[wiki/sources/teoria-dos-grafos-intro-matriz-lista-adjacencia|Teoria dos grafos — introdução, definições, matriz e lista de adjacência]]
