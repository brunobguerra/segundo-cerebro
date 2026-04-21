---
type: "source"
title: "Matplotlib e Storytelling com Dados"
source_type: "clipping"
url: "https://medium.com/data-hackers/matplotlib-e-storytelling-com-dados-pt-i-48c289943d60"
author:
  - "[[Henrique W. Franco]]"
published: 2023-10-23
ingested: "2026-04-21T18:35:50-03:00"
description: "Matplotlib e Storytelling com Dados — Pt. I Uma introdução ao Matplotlib Introdução “Storytelling com Dados”, da autora Cole Nussbaumer, com certeza é um dos principais livros que qualquer …"
tags:
  - "clippings"
---
Get unlimited access to the best of Medium for less than $1/week.[Become a member](https://medium.com/plans?source=upgrade_membership---post_top_nav_upsell-----------------------------------------)

[

Become a member

](https://medium.com/plans?source=upgrade_membership---post_top_nav_upsell-----------------------------------------)

## [Data Hackers](https://medium.com/data-hackers?source=post_page---publication_nav-da79ab871116-48c289943d60---------------------------------------)

[![Data Hackers](https://miro.medium.com/v2/resize:fill:48:48/1*muaTINHqZE4FWSzkfgsO9A.png)](https://medium.com/data-hackers?source=post_page---post_publication_sidebar-da79ab871116-48c289943d60---------------------------------------)

Blog oficial da comunidade Data Hackers

## Uma introdução ao Matplotlib

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*VX9zwHScMuB5aOYd.jpg)

Imagem sobre Matplotlib. Fonte: Ideogram.AI

## Introdução

“Storytelling com Dados”, da autora Cole Nussbaumer, com certeza é um dos principais livros que qualquer profissional de dados (ou alguém que queira entrar na área) deve ler. Lendo essa obra, um dos vários ensinamentos que aprendi está contida na frase abaixo:

> “O nirvana na comunicação com dados é alcançado quando visuais eficazes são combinados com uma narrativa poderosa.”

De fato, acredito que uma visualização eficiente de dados pode transformar um trabalho e facilitar muito o entendimento de uma informação. Sobretudo, quando seu **público é leigo no assunto tratado do gráfico** (conheça seu público sempre!).

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*nItaaMIePSsFTpWBHrtq3A.jpeg)

Capa do livro Storytelling com Dados. Fonte: Amazon

Nesse sentido, quero mostrar como criar gráficos informativos e impactantes, que utilizam conceitos do livro “Storytelling com Dados”, por meio da biblioteca Matplotlib. Se você trabalha com dados ou está iniciando na carreira, já deve ter conhecido essa ferramenta, visto que é uma das principais bibliotecas de código aberto para visualização de dados do Python.

Como o Matplotlib pode parecer um tanto complexo, optei por dividir o artigo sobre Matplotlib e Storytelling com Dados em duas partes:

- **Pt. I: vamos entender melhor como é o funcionamento dessa biblioteca**
- **Pt. II: vamos criar um gráfico com Matplotlib, passo a passo, inspirado nas técnicas apresentadas no “Storytelling com Dados”**

Após essas observações, vamos começar a entender melhor como é o funcionamento dessa ferramenta.

## Matplotlib

A biblioteca Matplotlib, criada por John Hunter em 2003, foi projetada para produzir gráficos semelhantes aos do MATLAB, uma popular linguagem de programação usada para computação numérica.

![](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*gw2NcnIYpiBlFy4le3pF5w.png)

Logo da biblioteca do Matplotlib. Fonte: GitHub — Matplotlib

Não vou entrar em muitos detalhes sobre a história da biblioteca. Todavia, caso queira saber mais, pode verificar esse [Guia do Real Python](https://realpython.com/python-matplotlib-guide/) em que há mais assuntos aprofundados sobre essa ferramenta.

Como citei anteriormente, meu objetivo nessa primeira parte é focar no funcionamento do Matplotlib. Para isso, é fundamental entender a hierarquia dessa biblioteca, as diferenças entre Interface Pyplot e Interface Orientada a Objetos, e, por fim, compreender os elementos da anatomia de uma ‘Figure’.

> Obs.: Apesar de focarmos aqui em uma introdução a essa biblioteca, quero ressaltar a importância de verificar a [documentação do Matplotlib](https://matplotlib.org/). De fato, não se limite a esse artigo, já que a documentação é muito completa e vai te auxiliar em muitos casos!

## Hierarquia do Matplotlib

Ao usar o Matplotlib, é fundamental compreender como essa biblioteca estrutura seus gráficos. Essa estrutura é composta por uma **hierarquia de elementos** que incluem a **“Figure”** (Figura), **“Axes”** (Eixos), **“Axis”** (Eixo) e **“Artist”** (Artista).

Entender essa hierarquia e a função de cada componente é de extrema importância. Desse modo, vou detalhar a seguir os quatro conceitos que são essenciais para construir um gráfico no Matplotlib.

### Figure

- É o espaço global em que todos os elementos do gráfico são dispostos.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*nRbaIEm9XBNM5t1tm6aiZw.png)

Imagem de um ‘Figure’ do Matplotlib. Fonte: Matplotlib — Introduction to Figures

- Pense que a ‘Figure’ é uma ‘lousa’ na qual você vai colocar seus gráficos.

### Axes

- Representa uma área de plotagem dentro de uma ‘Figure’. Cada ‘Axes’ tem seus próprios eixos, rótulos e título.
- De fato, um gráfico individual está contido dentro de um objeto ‘Axes’ (isto é, o ‘Axes’ pode ser considerado um gráfico individual). **Logo, uma ‘Figure’ não é o gráfico em si, já que pode conter um ou mais gráficos.**
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*mWzwRX462O54ns01kCbxTQ.png)

Axes dentro de uma ‘Figure’. Fonte: Axes and subplots

- Pense que os ‘Axes’ são quadros ou telas que podem ser colocados na lousa (‘Figure’).

### Axis

- Refere-se às partes que lidam com a escala e os limites do gráfico, além de gerar os marcadores (ticks) e seus rótulos (ticks labels) — partes em verde na imagem abaixo.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*nF7kSzuwBuKKi6rB.png)

Fonte: Real Python

- Pense que os Axis são réguas e etiquetas que ajudam a medir os gráficos.

### Artist

- Basicamente, **tudo o que é visível em um gráfico no Matplotlib é considerado um “Artist”** (itens em azul), em que inclui os objetos ‘Figure’, ‘Axes’ e ‘Axis’.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*czSppDAKmr00sJdMbFtD7w.png)

Anatomia de uma ‘Figure’ do Matplotlib. Fonte: Quick start guide — Matplotlib

- Pense que seria o ‘pincel’ que vamos utilizar para confeccionar todos os elementos visuais, como linhas e formas até rótulos e texto.

Desse modo, espero que tenha entendido que o Matplotlib segue uma hierarquia. Caso esteja um pouco confuso, fique, por enquanto, com essa informação: **uma ‘Figure’ pode ter vários sistemas de ‘Axes’**.

Isso vai ser importante para entender as duas abordagens do Matplotlib para criação de gráficos, as quais serão o foco do nosso próximo tópico.

## Interface Pyplot X Abordagem Orientada a Objetos

Se você já criou gráficos com Python, provavelmente deve ter utilizado essa estrutura abaixo:

```md
plt.plot()
```

Todavia, talvez também já tenha visto esta estrutura abaixo:

```md
fig, ax = plt.subplots()
```

Qual seria a diferença? Basicamente, uma estrutura utiliza a Interface Pyplot, enquanto o outro código é feito na Abordagem Orientada a Objetos.

De forma resumida, ao utilizar a **Interface Pyplot**, por meio do comando **plt.plot**, por exemplo, **cria-se a ‘Figure’ e o sistema de ‘Axes’ ao mesmo tempo**.

Em contrapartida, na **abordagem OO**, por meio do comando **fig, ax = plt.subplots()**, há **uma variável para a ‘Figure’ e outra para o ‘Axes’**. Isso permite um maior controle no sistema de ‘Axes’ — basicamente **há um maior controle nos gráficos em si**.

Note que, com a OO, podemos trabalhar diretamente com as intâncias ‘Figure’ e Axes, em que vamos poder manipular cada aspecto do gráfico. Para deixar mais claro, olhe novamente como são as linhas de código para criar os gráficos:

```md
# Interface Pyplot
plt.plot() # Note que não há distinção entre 'Figure' e 'Axes'
''' 
Na interface Pyplot, não conseguimos ter um controle entre a 'Figure' e o 
sistema de 'Axes'. Consequentemente, sempre que realizarmos alguma customização,
afetará a 'Figure' de forma geral.
'''

# Orientada a Objetos
fig, ax = plt.subplots() # Aqui, criamos uma variável para 'Figure' e para 'Axes'
''' 
Nesse caso, vamos conseguir uma maior personalização nos 'Axes' (quando
criarmos mais gráficos em uma mesma 'Figure'), já que as diferentes variáveis 
vão permitir um controle mais preciso sobre cada aspecto do gráfico. 
'''
```

Você vai notar que as funções entre essas abordagens são bem parecidas. Afinal, a maioria das funções do Pyplot também existem como métodos da OO. Por exemplo, para criar um gráfico de barras:

- Pyplot → `plt.bar`
- OO → `ax.bar()`

Senão for praticamente igual, vão ter algumas mudanças, como no caso de personalizações nos rótulos dos eixos y e x, em que adicionamos o `.set_`:

- Pyplot → `plt.ylabel` / `plt.xlabel`
- OO → `ax.set_ylabel` / `ax.set_xlabel`

Mas, afinal, qual abordagem escolher?

**Depende! A escolha entre a interface Pyplot e a Orientada a Objetos dependerá das suas necessidades e preferências.** Vou explicar as duas mais detalhadamente nos tópicos seguintes.

### Interface Pyplot

A Interface Pyplot do Matplotlib é uma abordagem mais simples para a criação de gráficos. Ela é acessada por meio do módulo “pyplot” com funções como “plt.plot()” e “plt.xlabel()”.

> Conforme o artigo do [Real Python](https://realpython.com/python-matplotlib-guide/), na Interface Pyplot, funções simples são usadas para adicionar elementos de *plot* (linhas, imagens, textos, entre outras) ao ‘ `**Axes**` **‘ atual, pertencente à '** `**Figure' **` **atual**.

Eu gosto de usar essa interface para **tarefas rápidas de visualização**, pois é mais concisa e requer menos código. Mas saiba que também é possível fazer ótimos gráficos com Pyplot, então avalie o que for melhor para o seu projeto!

Abaixo, veja como é simples criar o gráfico:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*skQFdPBdazKl_nESNH4RrQ.png)

Além disso, podemos adicionar mais alguns detalhes utilizando funções como “plt.xlabel”, “plt.ylabel”, “plt.title” e “plt.legend”. Veja como fica o nosso gráfico na figura abaixo:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6hIZtTvS9Zl1y0LO1pq28g.png)

Há diversas funções Pyplot, as quais você pode conferir [nessa parte da documentação](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html). Todavia, vou listar algumas que são bem comuns de serem utilizadas ao plotar um gráfico:

- `plt.scatter()`: Cria um gráfico de dispersão
- `plt.bar()`: Cria um gráfico de barras
- `plt.hist()`: Cria um histograma
- `plt.boxplot()`: Cria um boxplot (gráficos de caixa)
- `plt.xlabel()`: Define o rótulo do eixo x.
- `plt.ylabel()`: Define o rótulo do eixo y.
- `plt.title()`: Define um título para os eixos.
- `plt.grid()`: Configura as linhas da grade.
- `plt.legend()`: Coloca uma legenda no eixo.
- `plt.show()`: Exibe uma figura.

No entanto, a **simplicidade dessas funções vem com algumas limitações em termos de personalização avançada**. Por exemplo, criar subplots ou figuras com vários ‘Axes’ pode ser complicado com Pyplot.Desse modo, acredito que precisemos de um maior controle sobre a customização das visualizações de dados, por isso **utilizaremos a Abordagem Orientada a Objetos para criar os gráficos inspirados no livro “Storytelling com Dados”**. Nesse sentido, vale a pena dar uma atenção maior para o próximo tópico.

### Interface Orientada a Objetos (OO)

A Abordagem Orientada a Objetos (OO) no Matplotlib oferece um nível mais avançado de controle e personalização. Ela envolve a **criação explícita de objetos “Figure” (Figura) e “Axes” (Eixos)** e, em seguida, a chamada de métodos nesses objetos para adicionar elementos ao gráfico.

**Se essa parte ficou confusa, acalme-se: eu também demorei para entender o funcionamento dessa abordagem!** Mas, resumindo, vou exemplificar o parágrafo acima com essa estrutura:

```md
fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(x, y)
```

Para entender melhor a estrutura do código acima, vamos detalhar cada parte:

- `**fig**` → variável que é uma instância da ‘Figure’ → permite controlar a aparência e as configurações da ‘Figure’ em que o gráfico será exibido
- `**ax**` → variável que é uma instância do ‘Axes’ → o ‘Axes’ é a área dentro da ‘Figure’ em que o gráfico real será plotado
- `**‘plt.subplots()**` → permite criar uma ‘Figure’ com um ou mais ‘Axes’ em uma única chamada
- `**figsize=(12, 10)**` → é uma configuração da ‘Figure’ (a parte mais externa)→ define o tamanho geral da figura
- `**ax.bar(x, y)**` → é uma operação realizada no ‘Axes’ que cria o gráfico de barras dentro da ‘Figure’

De fato, essa abordagem pode exigir um pouco mais de código. No entanto, como citei anteriormente, ela é ideal para criação de gráficos mais complexos e altamente personalizados.

Para facilitar o entendimento, vou utilizar o mesmo gráfico feito anteriormente com Pyplot, mas agora usando a Interface Orientada a Objetos.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_uCtdc5ZGgr86jVbN5KRtA.png)

Agora você deve estar se perguntando algo assim: “ ***as duas abordagens são parecidas, por que vou utilizar essa mais ‘complexa’?***”

Basicamente, porque ela é muito útil para ter um **maior controle dos ‘Axes’ (dos gráficos em si) dentro de uma ‘Figure’**. Por exemplo, imagine que você queira criar mais de um gráfico na mesma ‘Figure’. Abaixo, vou dar um exemplo disso:

```md
import matplotlib.pyplot as plt

anos = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
vendas_anuais = [45, 50, 58, 63, 70, 72, 76, 80, 85, 90, 95]
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
quantidades = [30, 42, 38, 55, 48]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# Gráfico 1 - Linha
axs[0].plot(anos, vendas_anuais, marker='o', color='blue', label='Vendas Anuais')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Vendas (em milhões de reais)')
axs[0].set_title('Evolução das Vendas Anuais')
axs[0].legend()

# Gráfico 2 - Barras
axs[1].bar(produtos, quantidades, color='green')
axs[1].set_xlabel('Produto')
axs[1].set_ylabel('Quantidade de Vendas')
axs[1].set_title('Quantidade de Vendas por Produto')

plt.tight_layout()
plt.show()
```

Resultado do código acima:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4Ut7XjXxydiXo3Oy7gUN2g.png)

Gráficos resultantes do código anterior. Fonte: Autor.

Nesse caso, criamos uma variável ‘axs’, que será um **array do Numpy**. Não vou entrar em muitos detalhes sobre essa biblioteca, mas recomendo pesquisar sobre essa ferramenta no Google ou, até mesmo, no ChatGPT. Saiba que, basicamente:

- O Numpy é a base de bibliotecas como Pandas e Matplotlib;
- Para personalizar os gráficos, podemos acessá-los como acessamos posições de um array multidimensional do Numpy.

Isto é, o axs\[0\] pode ser utilizado para acessar o primeiro gráfico, axs\[0, 1\] para acessar o segundo, caso tenha mais de dois, e assim por diante. Veja a figura abaixo para compreender melhor:

![](https://miro.medium.com/v2/resize:fit:1268/format:webp/1*Fwj_gR0DlATP9GkA-2Elyw.png)

Figura com 4 Axes, em que são acessados pelo array do Numpy. Fonte: Complex and semantic figure composition (subplot\_mosaic)

No entanto, essa forma acima, com array em Numpy, é um pouco mais antiga. Quis explicar essa forma pois há muitos códigos por aí que ainda utilizam essa estrutura.

Por isso, vamos deixar as coisas mais interessantes, pois agora **quero apresentar um sistema que pode ser mais flexível: o** [**Mosaico**](https://matplotlib.org/stable/users/explain/axes/mosaic.html). Por meio do método `subplot_mosaic()`, é possível criar vários gráficos com pouco código.

Dê uma olhada no código abaixo.

```md
import matplotlib.pyplot as plt

mosaico = """
    AB
    CD
    """
fig = plt.figure()
axs = fig.subplot_mosaic(mosaico)
plt.show()

# Nesse caso, o código acima substitui essa linha -> fig, ax = plt.subplots()
```

Nesse caso, vou listar o que está acontecendo:

- Definimos a variável `mosaico`, a qual recebe strings e define a organização dos subplots na figura. Cada letra representa a posição de um subplot
- Na parte `fig = plt.figure()`, cria-se uma variável para plotar a ‘Figure’
- O trecho `axs = fig.subplot_mosaic(mosaico)` é responsável por criar e organizar os eixos (gráficos) dentro da figura de acordo com o layout definido pela string `mosaico`
- Por fim, `plt.show()` vai exibir a figura com a organização definida

Assim, a figura resultante do código acima será essa:

![](https://miro.medium.com/v2/resize:fit:1276/format:webp/1*nved2xU9Oh-_4LeAUN5gQg.png)

Gráfico feito com a estrutura de mosaico. Fonte: Complex and semantic figure composition (subplot\_mosaic)

O mais legal dessa abordagem é que facilita quando os gráficos não precisam ser do mesmo tamanho, pois podemos definir o quanto uma visualização gráfica ocupará na ‘Figure’ na variável mosaico. Veja o exemplo abaixo:

```md
import matplotlib.pyplot as plt
import pandas as pd

data = {'day': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00],
        'size': [2, 3, 2, 2, 4, 2, 1]}

df = pd.DataFrame(data)

# Usando Mosaico
fig = plt.figure(constrained_layout=True, figsize=(10, 6))
mosaic = fig.subplot_mosaic('''
                            AB
                            AC
                            DD
                            ''')

# Gráfico A - Linha
mosaic['A'].bar(df.day, df.tip, color='coral')
mosaic['A'].set_xlabel('Dia da Semana')
mosaic['A'].set_ylabel('Gorjeta')
mosaic['A'].set_title('Gorjetas por Dia')

# Gráfico B - Boxplot
mosaic['B'].boxplot(df.total_bill, patch_artist=True)
mosaic['B'].set_title('Valor Total da Conta')

# Gráfico C - Dispersão
mosaic['C'].scatter(df.total_bill, df.tip, color='forestgreen')
mosaic['C'].set_xlabel('Valor Total da Conta')
mosaic['C'].set_ylabel('Gorjeta')
mosaic['C'].set_title('Dispersão: Valor Total da Conta vs. Gorjeta')

# Gráfico D - Linha
mosaic['D'].plot(df.day, df.tip, color='purple')
mosaic['D'].set_xlabel('Dia da Semana')
mosaic['D'].set_ylabel('Gorjeta')
mosaic['D'].set_title('Gorjetas por Dia')

plt.show()
```

E o resultado é esse:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Yk1GIqjKLsqJztw98QOtfw.png)

Gráficos usando Mosaico resultados do código anterior. Fonte: Autor

Para complementar essa leitura sobre o Mosaico, recomendo ler o artigo do

[Gustavo Santos](https://medium.com/u/4429d99b1245?source=post_page---user_mention--48c289943d60---------------------------------------)

— “ [Visualizações sofisticadas com subplots em mosaico](https://medium.com/data-hackers/visualiza%C3%A7%C3%B5es-sofisticadas-com-subplots-em-mosaico-ed2a07b8ce16) ”.

Enfim, acredito que você já tenha notado a variedade de personalizações que podemos fazer com essa interface.

Portanto, reforço que a **Abordagem Orientada a Objetos fornece uma maior flexibilidade sobre seus gráficos**. Ela é mais adequada quando você deseja **criar vários gráficos em uma única figura** ou para a **criação de visualizações mais personalizadas**.

## Anatomia de uma ‘Figure’ no Matplotlib

Antes de finalizar o artigo, quero que você visualize essa imagem abaixo. Ela vai ser muito útil no artigo “Matplotlib e Storytelling — Pt. II”, pois trata da anatomia de uma ‘Figure’ da biblioteca Matplotlib.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wXmtRnECv_6qUvtOUIWQag.png)

Anatomia de uma ‘Figure’ do Matplotlib. Fonte: Quick start guide — Matplotlib

Note que cada parte da imagem mostra os componentes de um gráfico do Matplotlib. Por exemplo, os ‘Spines’ (‘espinhas’) podem ser personalizados pelo ax.spines e o Grids (linhas de grade) podem ser personalizados pelo ax.grid.

No próximo artigo, você vai entender melhor como personalizar esses componentes. Afinal, já dando um ‘spoiler’, é necessário retirar ou mexer em vários desses elementos para deixar o gráfico “mais limpo” e, consequentemente, torná-lo mais fácil de ser visualizado.

## Considerações Finais

Espero que tenha compreendido um pouco melhor o funcionamento do Matplotlib. Todavia, eu o incentivo a ler outros conteúdos para se aprofundar um pouco mais nessa biblioteca. Desse modo, como recomendação, vou deixar abaixo as fontes que utilizei para escrever esse artigo.

Agora que vocêcompreendeu um pouco mais sobre o funcionamento do Matplotlib, vou te dar mais um spoiler do que iremos fazer no artigo “Matplotlib e Storytelling com Dados — Pt. II”:

![](https://miro.medium.com/v2/format:webp/1*YE6qWm_X1Tu59VH-4NbXYA.png)

Antes e depois do nosso gráfico sobre os registros de queimadas no Brasil ao longo dos anos. Fonte: Autor.

Espero que tenha gostado do artigo! Aguardo sua leitura do Matplotlib e Storytelling com Dados — Pt. II.

## Responses (3)

Bruno Guerra

What are your thoughts?

```c
Excelente explicação, Henrique. Sou iniciante e tive pouco contato com o matplotlib ainda, mas lendo o seu texto eu consegui entender vários aspectos que ainda estavam "ocultos" na minha percepção.Obrigado por compartilhar conhecimento. Sigo ansioso…
```

1

```c
Parabéns pelo artigo, Henrique! Uma pergunta: atualmente utilizo o Power BI para a criação de visualizações em painéis e relatórios. O bacana desta ferramenta da Microsoft é sua facilidade para importar, modelar e criar visuais dinâmicos. Pelo que…
```

```c
Obrigado por deixara explicação tão simples e tão rica ao mesmo tempo. Trabalho com dados, mas sei muito pouco sobre a visualização deles. E isso facilitou de mais! Parabéns!
```

Jun 27, 2021

Jun 24, 2024

[View list](https://medium.com/@guerra.bruno/list/reading-list?source=post_page---list_recirc--48c289943d60-----------predefined%3Aba35701959d5%3AREADING_LIST----------------------------)