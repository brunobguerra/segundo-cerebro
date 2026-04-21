---
type: "source"
title: "Teoria dos Grafos —Introdução, Definições, Matriz e Lista de Adjacência"
source_type: "clipping"
url: "https://medium.com/@anwarhermuche/teoria-dos-grafos-introdu%C3%A7%C3%A3o-defini%C3%A7%C3%B5es-matriz-e-lista-de-adjac%C3%AAncia-2252d4800a44"
author:
  - "[[Anwar Hermuche]]"
published: 2024-04-02
ingested: "2026-04-21T18:51:11-03:00"
description: "Teoria dos Grafos —Introdução, Definições, Matriz e Lista de Adjacência Fala, pessoal! Hoje, quero falar sobre um conceito que não estamos tão acostumados a ver em Ciência de Dados, mas que …"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*kKGoeR6U4emPSR4w)

Imagem 1

Fala, pessoal!

Hoje, quero falar sobre um conceito que não estamos tão acostumados a ver em Ciência de Dados, mas que é extremamente útil — e bonito — em diversas aplicações: GRAFOS!

Repita comigo: grafos. Não GARFOS.

Ok, chega de piada ruim e vamos começar a discutir um pouco mais sobre essa estrutura de dados.

## Definições Iniciais

Vamos começar dando nome aos bois, como dizia minha professora de matemática. Precisamos falar o que significa cada coisa antes de já partir para explicações mais complexas.

Na Imagem 1, podemos notar que temos algumas bolinhas cinza. Chamamos essas bolinhas de **Vértices** ou **Nós** (**Vertices**, em inglês). Além disso, temos também essas linhas ou setas que ligam os vértices. Chamamos essas linhas ou setas de **Arestas** (**Edges**, em inglês).

Dessa forma, podemos dizer que um grafo é um conjunto de vértices e arestas, onde cada aresta conecta dois vértices. Podemos usar grafos para modelar relacionamentos!

Se uma pessoa X conhece as pessoas Y e Z e a pessoa Y conhece as pessoas X e W, podemos modelar o grafo da seguinte maneira, mostrado na Imagem 2.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*RX4kEUEIsh0V5sxo)

Imagem 2

Agora, voltando na Imagem 1, notou que os grafos (a) e (b) não possuem setas, mas sim linhas sem orientação? Por isso, chamamos de um grafo **não direcionado**. Quando há setas, como no caso dos grafos ( c ) e (d), chamamos de grafo **direcionado** (orientado).

Em um grafo orientado, devemos obrigatoriamente respeitar a direção indicada. Se há uma seta saindo de V1 para V2 (sendo V1 e V2 dois vértices do grafo) e não há uma seta saindo de V2 e indo para V1, não podemos partir de V2 para chegar em V1.

Entretanto, em um grafo não direcionado, se há uma aresta conectando V1 e V2, podemos ir tanto de V1 para V2 quanto de V2 para V1.

### Número máximo de arestas

Há uma relação muito bacana em grafos direcionados que limita o número de arestas com base no número de vértices. Uma relação que envolve um pouco de análise combinatória.

Como eu gosto de explicar o porquê das coisas, vou falar sobre essa relação aqui. Basicamente, temos a relação abaixo, na Imagem 3.

![](https://miro.medium.com/v2/resize:fit:1254/format:webp/1*r7MlO_HAyjuoVtDeb4Hhiw.png)

Imagem 3

Aqui, estamos dizendo que o número de arestas (Edges) é menor ou igual ao número de vértices ao quadrado em um grafo direcionado. E isso é fácil de demonstrar com um pingo de combinatória.

Quantos pares distintos de vértices podemos formar em um grafo de V vértices? Note que, aqui, a ordem importa. Uma tupla (V1, V2) é diferente da tupla (V2, V1). No primeiro caso, temos um caminho que sai de V1 e chega em V2. No segundo caso, temos um caminho que sai de V2 e chega em V1.

Além disso, note que que um grafo pode “sair” e “entrar” nele mesmo! Na Imagem 4, mostrada abaixo, você vê que o vértice 4 possui um loop (ou laço).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*eg5zFvNZw3jB-THg.png)

Imagem 4

Dito tudo isso, podemos calcular o número máximo de arestas vendo as possibilidades de tuplas que temos. Para a primeira posição da tupla, podemos escolher qualquer vértice, logo, temos N possibilidades. Para a segunda posição, também temos N possibilidades, visto que ele pode apontar para ele mesmo (loop).

Logo, temos N\*N = N² arestas no total, chegando na relação da Imagem 3.

## Conceitos Formais

De forma mais formal, um grafo é um par de conjuntos G = (V, A), onde V é um conjunto de vértices e A é um conjunto de arestas. Observe o código abaixo:

```md
# Vértices (Vertices)
V = {v1, v2, v3, v4, v5}

# Arestas (Edges)
A = {(v1, v2), (v1, v4), (v1, v5), (v2, v3), (v3, v5), (v4, v5), (v5, v1)}

# Grafo
G = (V, A)
```

Abaixo, você vê a representação visual desse grafo.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*155WXvz138qgYNpq)

Imagem 5

### Vizinhança

Com ele, podemos dar algumas definições. A primeira definição é de **relação de vizinhança ou adjacência**. Dois vértices são considerados vizinhos se existe uma aresta que os conecta.

### Passeio, Caminho e Ciclos

Além disso, chamamos de **passeio** (walk) uma trajetória que percorre os vértices e as arestas do grafo, seguindo as conexões entre eles, onde cada aresta na sequência é adjacente à anterior.

Usando o grafo da Imagem 5, um possível passeio seria (V1, V4, V5, V1, V2).

Já um **caminho** (path), é um passeio onde nenhum vértice (ou aresta, depende de algumas definições) se repete. O passeio acima não é um caminho, porque V1 é visitado mais de uma vez.

Se tivermos o passeio (V1, V4, V5, V1), poderíamos denominar de **ciclo**, visto que o vértice de início é o mesmo vértice final. Caso o passeio passasse por todos os vértices do grafo uma única vez (exceto o vértice de início e fim) e fosse um ciclo, chamaríamos de **ciclo hamiltoniano**.

### Grau e Ordem

Alguns conceitos importantes também são o grau e a ordem de um grafo. A ordem é bem tranquila: **é a quantidade de vértices que ele tem**. O grafo da Imagem 5 tem ordem 5, por exemplo, porque possui 5 vértices.

Agora, quando falamos de grau, estamos olhando para cada vértice específico, isto é, falamos o grau do vértice. O grau é **a quantidade de arestas que tocam o vértice.**

Se for um grafo direcionado, falamos **grau de entrada e grau de saída**. O vértice 1 (V1) da Imagem 5 possui 3 graus de saída e 1 grau de entrada, totalizando grau 4 (3 + 1).

Quando temos um laço, como o vértice 4 da imagem 4, temos 2 graus de entrada e 1 de saída, totalizando grau 3 (2 + 1). Isso porque o laço conta como saída e entrada ao mesmo tempo (sai e entra no mesmo vértice).

### Conectividade

Um grafo é dito **conexo** se, para cada par distinto no grafo, existe pelo menos um caminho que os conecta. Note que não necessariamente deve haver uma ARESTA, mas sim um caminho. Ou seja, partindo de um vértice, podemos chegar em todos os outros.

E aí abre margem para duas sub definições: **fortemente e fracamente conexos**.

O grafo direcionado da Imagem 6 é dito **fortemente conexo** porque, partindo de qualquer vértice do grafo, é possível chegar em qualquer outro vértice.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*zcr-00bN6OLc7OZw)

Imagem 6

Já o grafo direcionado da Imagem 7 é dito **fracamente conexo** porque, se ignorarmos a direção das arestas, ele é conexo. Note que não ignorando a direção, não podemos chegar no vértice E partindo do vértice H, por exemplo. Porém, se ignorarmos, ele é conexo.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*rYCSQpPiLkSdFuDO)

Imagem 7

## Casos Particulares

Provavelmente, você notou alguma semelhança dos grafos com um algoritmo bem famoso no mundo da ciência de dados: a árvore de decisão!De forma mais geral, uma árvore é um caso particular de um grafo direcionado. Se aplicarmos uma restrição onde um vértice pode ter no máximo um pai, temos o resultado na Imagem 8.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*mimn82Zjq0J8bt19bZFApA.png)

Imagem 8

Perceba que é uma árvore (pela definição, uma árvore é uma estrutura hierárquica que consiste de vértices conectados por arestas), mas não a árvore de decisão que estamos acostumados a ver como resultado na scikit-learn, como mostra a Imagem 9.

![](https://miro.medium.com/v2/resize:fit:1280/format:webp/0*eubdNjGqh3V8PQr-.png)

Imagem 9

Note que a árvore de decisão da scikit-learn é um grafo onde cada vértice possui no máximo 1 pai E no exatamente 2 filhos. Isso caracteriza uma árvore binária.

Além das árvores, temos outras estruturas como linked-lists (listas encadeadas) que podem ser representadas por um grafo, mas isso fica para um próximo papo.

## Representações de Um Grafo

Como vou falar aqui da parte prática também, é importantíssimo sabermos como representar um grafo no computador. E já vou adiantar: há diversas maneiras de fazer isso. Entretanto, vou focar em três principais:

- Matrizes
- Matrizes de Adjacência
- Listas de Adjacência

### Matrizes

Bom, acho que todos nós sabemos o que é uma matriz, certo? Só para recapitular, é uma estrutura bidimensional com linhas e colunas. Vou criar uma matriz de 0’s e 1’s com o código em Python abaixo, depois representar isso em uma imagem, na Imagem 10.

```md
# Matriz
matriz = [
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*4yy5bt2DcqdBaZLp.png)

Imagem 10

Aqui, vamos imaginar que todo elemento que for igual a zero está “livre” e todo elemento que for igual a um está “bloqueado”.

“Como assim, Anwar? Bloqueado?”

Sei que pode parecer confuso, então vou dar um exemplo. Note que o caminho verde, seguido pela Imagem 11, é permitido, porque não passa em nenhuma posição bloqueada, ou seja, com algum valor 1.

![](https://miro.medium.com/v2/resize:fit:1296/format:webp/1*sZICbJZ67XvahGMZeNZe-A.png)

Imagem 11

Já na Imagem 12, vemos que esse caminho em vermelho não pode acontecer, visto que estamos passando por um caminho bloqueado!

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NZUzHmuBxI8DXcetHpWfqw.png)

Imagem 12

Aqui, podemos entender que cada elemento pode ser representado por matriz\[i\]\[j\], onde *i* é o índice da linha e *j* é o índice da coluna. Ou seja, o elemento matriz\[3\]\[0\] = 1, visto que o elemento da 4º linha (i + 1 = 3 + 1 = 4) e da 1º coluna (j + 1 = 0 + 1 = 1) é igual a 1.

E o que isso tem a ver com vértices? Ora, pense que cada zero da nossa matriz é um vértice e podemos nos mover para cima, para baixo, para a direita e para a esquerda. Note na Imagem 13 a representação, em forma de um grado não direcionado, da nossa matriz anterior.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*zXDxUcLj3co_K5uFfhibww.png)

Imagem 13

### Matriz de Adjacência

A matriz de adjacência é também, como o próprio nome diz, uma matriz, mas aqui os índices representam os próprios vértices!

Vamos retomar ao exemplo da Imagem 6, mostrada novamente abaixo, com sua matriz de adjacência ao lado direito da Imagem 14. Note que temos 4 vértices, logo nossa matriz terá exatamente 4 linhas e 4 colunas, já que os índices indicam cada um dos vértices.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*AQFrQf51F4mkl1u_ipXqrg.png)

Imagem 14

O que cada 1's e 0's significam agora? Que está “bloqueado” e “livre”? Não. Esqueça isso. Agora, temos um significado muito maior e mais informativo.

Como disse, cada linha e coluna representa um dos nós. Nesse caso, a linha e coluna de índice 0 representam o nó A, a linha e coluna de índice 1 representam o nó B, a linha e coluna de índice 2 representam o nó C e por aí vai.

Quando temos que o elemento da 1º linha (índice 0), que representa o vértice A, e 4º coluna (índice 3), que representa o vértice D, tem o valor igual a 0, significa que não há uma aresta que sai de A e vai para B. Ou seja, o elemento matriz\[0\]\[3\] = 0.

Entretanto, vemos que o elemento matriz\[1\]\[2\] = 1. O que isso significa? Que há uma aresta que sai de B (índice 1 na linha) e chega em C (índice 2 na coluna).

Ou seja, se matriz\[*vi*\]\[*vj*\] = 1, então existe um caminho que sai do vértice *v1* e chega no vértice *vj*.

Note que se o grafo for não direcionado, se existe uma aresta saindo de *vi* para *vj,* então matriz\[*vi*\]\[*vj*\] = 1 e matriz\[*vj*\]\[*vi*\] = 1. Uma curiosidade: a matriz de adjacência, nesse caso, é simétrica.

Porém… como tudo na vida há vantagens e desvantagens, um caso particular onde utilizar a matriz de adjacência não é uma boa opção é quando não temos tantas arestas, visto que teríamos uma matriz com muitos 0’s de forma desnecessária.

De forma mais técnica, temos uma complexidade de espaço O(V²), onde V é o número de vértices. Mas vamos resolver isso.

Uma vantagem de utilizar a matriz de adjacência seria para casos onde a verificação de arestas entre dois vértices for uma operação comum, pois permite o acesso a um tempo constante.

### Lista de Adjacência

A lista de adjacência é uma das formas mais comuns de representarmos um grafo. Basicamente, podemos criar uma classe com dois atributos: valor e vizinhos. Observe o código abaixo:

```md
# Classe para representar um vértice na lista de adjacência
class Vertice:
  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = list()
```

Usando o mesmo grafo da Imagem 6, vamos representá-lo usando, agora, uma lista de adjacência. Note que, na Imagem 15, temos essa representação.

Quando temos poucas arestas, representar dessa forma pode ser muito mais eficiente em termos de espaço de memória, visto que estamos olhando apenas para os vértices que possuem uma ligação. Na matriz de adjacência, tínhamos um espaço na memória guardado até para as conexões que não existiam (quando os elementos eram 0).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*z5Oq31dd8Cw0cek0wNhoGg.png)

Imagem 15

Utilizar a Lista de Adjacência pode ser muito útil quando queremos explorar os vizinhos de um determinado vértice. E faremos muito isso no próximo artigo.

## Conclusão

Aprendemos bastante coisa até aqui!

Espero que tenham gostado e fique tranquilo, porque teremos a parte 2 falando sobre métodos de busca DFS e BFS.

Até já, pessoal.