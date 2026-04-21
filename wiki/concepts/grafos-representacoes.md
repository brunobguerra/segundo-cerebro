---
title: "Representações de grafos (matriz e lista)"
slug: grafos-representacoes
type: concept
lang: pt-BR
sources:
  - "[[wiki/sources/teoria-dos-grafos-intro-matriz-lista-adjacencia|Teoria dos grafos — introdução, definições, matriz e lista de adjacência]]"
updated: 2026-04-21
tags: [data-science, estruturas-de-dados, grafos, algoritmos, complexidade]
summary: "Matriz 0/1 como grade; matriz de adjacência O(V²) e consulta O(1); lista de adjacência esparsa e exploração de vizinhos."
---

# Representações de grafos (matriz e lista)

Para implementar algoritmos em grafos, precisas de uma **estrutura em memória**. A fonte ingerida contrasta três ideias: uma **matriz binária como “mapa”**, a **matriz de adjacência** e a **lista de adjacência**.

## Termos (EN)

- *Adjacency matrix*, *adjacency list*, *sparse graph*, *dense graph*, *time/space complexity*.

## Grade 0/1 (intuição do artigo)

Uma matriz de **0s e 1s** pode representar células “livres” vs “bloqueadas”; movendo em **4-vizinhança**, obténs um **grafo implícito** cujos vértices são as células `0` e as arestas são passos válidos. Isto **não** é o mesmo significado da matriz de adjacência abaixo — serve como ponte mental entre “matriz” e “grafos”.

## Matriz de adjacência

Para **V** vértices numerados `0 … V-1`, usa-se uma matriz **V × V**:

- Em **digrafo**, `M[i][j] = 1` indica arco **i → j** (convenção da fonte: linha origem, coluna destino).
- Em **não direcionado**, `M[i][j] = M[j][i]` — matriz **simétrica** (no caso binário simples).

**Espaço:** **Θ(V²)** mesmo quando há poucas arestas (grafo **esparso** — muitos zeros).

**Vantagem:** testar se existe arco entre **i** e **j** em **O(1)** tempo.

## Lista de adjacência

Cada vértice mantém a lista dos **vizinhos de saída** (e, se precisares, outra lista para entrada). Em grafos esparsos, **economiza memória** relativamente à matriz densa.

**Vantagem típica:** iterar vizinhos de **v** em **O(grau(v))**, o que acelera muitos traversals (ex.: **BFS/DFS**, anunciados na continuação do artigo original).

## Esboço OO (como no Medium)

```python
class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.vizinhos = []
```

Na prática de produção costuma-se usar `dict`/`list` de listas ou bibliotecas (NetworkX, etc.) — o padrão acima é didático.

## Ver também

- [[wiki/concepts/teoria-dos-grafos|Teoria dos grafos (fundamentos)]]
- [[wiki/sources/teoria-dos-grafos-intro-matriz-lista-adjacencia|Teoria dos grafos — introdução, definições, matriz e lista de adjacência]]
