---
type: "source"
title: "Matplotlib e Storytelling com Dados"
source_type: "clipping"
url: "https://medium.com/data-hackers/matplotlib-e-storytelling-com-dados-pt-ii-35e0da269a1e"
author:
  - "[[Henrique W. Franco]]"
published: 2023-10-24
ingested: "2026-04-21T18:40:22-03:00"
description: "“” is published by Henrique W. Franco in Data Hackers."
tags:
  - "clippings"
---
Get unlimited access to the best of Medium for less than $1/week.[Become a member](https://medium.com/plans?source=upgrade_membership---post_top_nav_upsell-----------------------------------------)

[

Become a member

](https://medium.com/plans?source=upgrade_membership---post_top_nav_upsell-----------------------------------------)

## [Data Hackers](https://medium.com/data-hackers?source=post_page---publication_nav-da79ab871116-35e0da269a1e---------------------------------------)

[![Data Hackers](https://miro.medium.com/v2/resize:fill:48:48/1*muaTINHqZE4FWSzkfgsO9A.png)](https://medium.com/data-hackers?source=post_page---post_publication_sidebar-da79ab871116-35e0da269a1e---------------------------------------)

Blog oficial da comunidade Data Hackers

## Um guia para criar gráficos no Matplotlib usando técnicas do livro “Storytelling com Dados”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Kfw1NCzlaiAyMOEl.jpg)

Storytelling com Dados Cyberpunk. Fonte: Ideogram.AI

## Introdução

Na primeira parte ([Matplotlib e Storytelling com Dados — Pt. I](https://medium.com/data-hackers/matplotlib-e-storytelling-com-dados-pt-i-48c289943d60)), compreendemos como funciona o Matplotlib. Entendemos como funciona a hierarquia dessa biblioteca, quais são as diferenças entre Interface Pyplot e Interface Orientada a Objetos, e, também, verificamos alguns elementos da anatomia de uma ‘Figure’.

**Agora, vamos focar na parte prática: como utilizar o Matplotlib para fazer gráficos informativos e impactantes.** Vamos utilizar técnicas do livro “Storytelling com Dados” para tornar a nossa visualização de dados mais interessante.

Em seu livro, Cole Nussbaumer nos fornece orientações para melhorar a comunicação visual com dados por meio de seis lições importantes:

- **1\. Entenda o contexto**
- **2\. Escolha uma apresentação visual adequada**
- **3\. Elimine a saturação**
- **4\. Foque a atenção onde você deseja**
- **5\. Pense como um designer**
- **6\. Conte uma história**

Desse modo, os tópicos desse artigo serão divididos conforme as lições acima.

> Obviamente, não vou conseguir transmitir todos os ensinamentos que o livro traz, já que meu intuito é dar um panorama de como utilizar o Matplotlib para incrementar seus gráficos. Então, não preciso nem dizer que recomendo fortemente a leitura do livro, né?! 😅

### Orientações Gerais

Vou utilizar a **Abordagem Orientada a Objetos** do Matplotlib, pois eu acredito que seja melhor para as nossas personalizações. No entanto, caso queira utilizar a Interface Pyplot, fique à vontade, já que ela é ótima também.

Como prática, até recomendo você transformar os códigos que utilizarmos aqui para fazer pela Interface Pyplot!

### Fonte dos Dados

Todos os dados usados aqui foram obtidos a partir do [Kaggle](https://www.kaggle.com/). Para baixar o dataset, vá no link abaixo:

- [Forest Fires in Brazil](https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil/data)
![](https://miro.medium.com/v2/resize:fit:1252/format:webp/0*szjqWgj0cBqSQ792)

Queimadas no meio ambiente. Fonte: Freepik.

Além disso, pode acessar o notebook no Google Colab com os códigos que vamos utilizar no link abaixo:

- [Matplotlib e Storytelling com Dados — Google Colab](https://colab.research.google.com/drive/1ypv0uXUwPUnztVho3tOuL-KQAwj9hj7-?usp=sharing)

Agora, vamos iniciar a construção do nosso gráfico com Matplotlib conforme ensinamentos retirados do livro “Storytelling com Dados”.

## 1\. Entenda o contexto

Nessa primeira lição, Cole cita duas perguntas fundamentais que devem ser respondidas para contar uma história com dados:

- Quem é seu público?
- O que ele precisa saber ou fazer?

De fato, como vamos mostrar uma informação se nem sabemos para quem vamos apresentar?

Desse modo, nesse artigo vamos imaginar que iremos **apresentar uma visualização gráfica para o Ministro do Meio Ambiente** (sim, vamos elevar nosso trabalho para apresentar para um ministro! 😅), **o qual quer saber a evolução do registro de queimadas nas florestas brasileiras ao longo dos anos**.

![](https://miro.medium.com/v2/resize:fit:1252/format:webp/0*j6rR6XO15-EhaKRU.jpg)

Imagem do nosso “Ministro” fictício. Fonte: Freepik.

Para isso, vamos realizar uma exploração dos dados para, posteriormente, apresentar uma explanação acerca das informações! **Você sabe que não podemos apenas jogar um monte de dados para o ministro, né?**

Se a sua resposta foi um ‘não!’ para a pergunta acima, vou deixar essa dica: **não podemos apresentar uma análise exploratória em vez de uma explanatória.**

Como assim? Veja abaixo a diferença entre as análises:

- **Análise Exploratória** → descobrir/compreender os dados
- **Análise Explanatória** → mostrar/explicar as informações

Vou deixar abaixo o link de um post que fiz no LinkedIn explicando melhor a diferença desses conceitos (que são enfatizados no “Storytelling com Dados”). E, lendo esse artigo, **você vai ver a diferença de um gráfico exploratório e um explanatório!**

- [**Post LinkedIn**](https://www.linkedin.com/feed/update/urn:li:activity:7117106984750845952/) **—** Análise Exploratória x Análise Explanatória

Depois dessas orientações, vamos iniciar nossa **análise exploratória**.

Primeiramente, vamos verificar como é o nosso dataset. Para isso, utilizaremos as bibliotecas Pandas e Matplolib para analisar os dados. Pode ser necessário instalar as bibliotecas antes de usá-las, caso não esteja usando o Jupyter Notebook ou o Google Colab.

Instale-as, se necessário, conforme os comandos abaixo:

```md
pip3 install pandas
pip3 install matplotlib
```

Como qualquer biblioteca, elas precisam ser importadas para funcionar no seu notebook. Você pode fazer isso pelo seguinte comando:

```md
# Bibliotecas para Manipulação de Dados
import pandas as pd
import numpy as np

# Biblioteca para Visualização de Dados
import matplotlib.pyplot as plt
```

Com as bibliotecas importadas, vamos pegar o dataset e analisá-lo:

```md
df = pd.read_csv('amazon.csv', encoding='latin1')
df
```

Como podemos ver abaixo, é um conjunto de dados simples, que possui apenas 6454 linhas e 5 colunas:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*6aYDK2yeZJmALvIj.png)

Dataset Forest Fires in Brazil. Fonte: Autor

Como podemos ver, há duas variáveis interessantes para a nossa análise da **evolução do registro de queimadas ao longo dos anos:**

- `year`
- `number`

Desse modo, vou utilizar o método `.groupby` do Pandas, que agrupa determinados valores — no caso, os anos (`year`)— e depois soma o número de queimadas (`number`), conforme cada ano, pelo método `.sum()`.

Como os números estão em decimal, optei por transformá-los em inteiro pelo método `.astype(int)`. Com isso, foi criado uma nova coluna para os números inteiros.

```md
# Agrupar os dados por ano e somar número de queimadas
queimadas_ano = df.groupby('year')['number'].sum().reset_index()

# Nova coluna com números de queimadas arredondados
queimadas_ano['int_number'] = queimadas_ano['number'].astype(int)
display(queimadas_ano)
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*QGoO_PkTU40dX-ZI.png)

Tabela criada por meio do código acima. Fonte: Autor.

Após essa análise exploratória básica, estamos prontos para a próxima etapa: escolher o gráfico adequado.

## 2\. Escolha uma apresentação visual adequada

Nessa seção, devemos entender qual é a melhor maneira de mostrar os dados que vamos comunicar. Visto que vamos apresentar a **evolução do registro de queimadas ao longo dos anos**, vou optar por utilizar o gráfico de linhas.

> *De acordo com Cole, os gráficos de linhas são usados para registrar dados contínuos, os quais estão em alguma unidade de tempo: dias, meses, trimestres ou anos.*

> Obs.: Na análise que estamos realizando, eu preferi utilizar o gráfico de linhas, mas os gráficos de barras também podem ser uma opção. Nesse sentido, tudo DEPENDE do que você quer mostrar.

Sendo assim, para plotar o gráfico, vamos utilizar a Interface Pyplot (explicada no artigo [Matplotlib e Storytelling com Dados — Pt. I](https://medium.com/data-hackers/matplotlib-e-storytelling-com-dados-pt-i-48c289943d60)), só para entender como será nossa visualização gráfica:

```md
anos = queimadas_ano['year']
queimadas = queimadas_ano['int_number']

plt.plot(anos, queimadas)

plt.show()
```

E o resultado é esse:

![](https://miro.medium.com/v2/resize:fit:1164/format:webp/0*4Cy7aZZpLlGyo8if.png)

Primeiro gráfico de linha de registros de queimadas no Brasil ao longo dos anos. Fonte: Autor.

Podemos notar, inicialmente, que há um aumento dos registros de queimadas ao longo dos anos. Todavia, **o gráfico está longe de ser a melhor visualização possível para ser apresentado**. Por isso, vamos à próxima etapa: eliminar a saturação.

## 3\. Elimine a saturação

***A saturação é sua inimiga!***

Essa frase é o título de um dos capítulos do “Storytelling com Dados”. Conforme explicado por Cole, nós ***devemos nos preocupar com a carga cognitiva transmitida ao nosso público*** — em outras palavras, o esforço mental exigido que o Ministro vai ter para aprender as informações contidas no gráfico.

> *De fato, o cérebro humano possui uma quantidade finita desse poder de processamento mental. Portanto, precisamos reduzir a saturação — eliminar os elementos visuais que ocupam espaço físico, mas não aumentam o entendimento.*

Quer entender melhor isso? O site “ [WTF Visualizations](https://viz.wtf/) ” possui diversas visualizações de dados ruins (na verdade, terríveis!) que podem servir de inspiração para o que **NÃO FAZER** nas suas análises. Veja esse lindo gráfico de pizza com uma saturação absurda:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*d9rORFvZxWASreB7)

Gráfico de pizza para nunca ser utilizado! Fonte: WTF Visualizations

Com o Matplotlib, vamos retirar tudo que for desnessário do nosso gráfico com esse único objetivo: **DESTACAR OS DADOS**!

Desse modo, você se lembra da Abordagem Orientada a Objetos e da anatomia de uma ‘Figure’? Agora vamos utilizar esses conceitos, por isso recomendo abrir o outro [artigo](https://medium.com/data-hackers/matplotlib-e-storytelling-com-dados-pt-i-48c289943d60) e deixar na parte “Anatomia de uma Figure no Matplotlib”.

Em primeiro lugar, vamos pegar o código com Pyplot e vamos transformar para OO:

```md
# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(14, 7), dpi=72)

# Criar o gráfico de linha
ax.plot(queimadas_ano['year'], queimadas_ano['int_number'], color=AZUL1, linewidth=4) # ax.plot(x, y)
# Exibir o gráfico
plt.show()
```

Nesse caso, já defini o comprimento e largura da Figure com `figsize=(14, 7)`. Por sua vez, o parâmetro `dpi=72` especifica a resolução da imagem em pontos por polegada, controlando a nitidez do gráfico.

Além disso, no `ax.plot`, já inseri a cor (vou detalhar melhor abaixo) e a largura da linha (também vou explicar melhor abaixo). Após isso, usamos o comando `plt.show()` para exibir o gráfico. Logo, ficou assim:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*haMM-5-H8uxQ-woD.png)

Gráfico resultante do código acima. Fonte: Autor.

Agora, vou usar alguns métodos que eu geralmente utilizo nos meus gráficos. Nesse sentido, essa parte acaba se tornando um Ctrl + C / Ctrl + V nas outras visualizações que faço com Matplotlib.

```md
# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(14, 7), dpi=72)

# Criar o gráfico de linha
ax.plot(queimadas_ano['year'], queimadas_ano['int_number'], color=AZUL1, linewidth=4)

# Remover grid
ax.grid(False)

# Remover linhas
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Definir cores das linhas
ax.spines['bottom'].set_color(CINZA5)
ax.spines['left'].set_color(CINZA5)

# Configurar rótulos do eixo y
ax.set_ylabel('Registros de Queimadas', color=CINZA5, fontsize=12, fontweight='bold')

# Definir cor cinza dos valores dos eixos x e y
ax.tick_params(axis='x', colors=CINZA5, labelsize=12)
ax.tick_params(axis='y', colors=CINZA5, labelsize=12)

# Forçar anos eixo x
ax.set_xticks(ticks=anos, labels=anos)

plt.show()
```

Vou detalhar os métodos que usei aqui:

- `ax.grid(False)` → Remover as linhas de grade. Embora no nosso plot original não tivessem essas linhas, recomendo sempre retirá-las.
- `ax.spines[].set_visible(False)` → Remover as linhas laterais. Se quiser remover todas, pode utilizar o método `ax.set_frame_on(False)`. Senão, só utilizar `bottom` (embaixo), `top` (acima), `left ` (esquerda), `right ` (direita) para remover alguma das linhas.
- `ax.spines[].set_color(CINZA5)` → Definir as cores. Pode utilizar também `bottom` (embaixo), `top` (acima), `left ` (esquerda), `right ` (direita). Vamos detalhar melhor sobre cores mais abaixo no artigo.
- `ax.set_ylabel()` → Definir o nome do eixo. Isso é necessário para entender o que a linha se trata.
- `ax.tick_params(axis=, colors=CINZA5, labelsize=12)` → Definir a cor e tamanho dos valores dos eixos x e y.
- `ax.set_xticks(ticks=anos, labels=anos)` → Por padrão, o Matplotlib não coloca todos os valores no eixo x. Assim, esse comando “força” a colocar todos os anos nesse eixo.

O resultado será esse:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*iovut3aOO6wscdu4.png)

Gráfico resultante do código acima. Fonte: Autor.

Aos poucos retiramos algumas saturações do gráfico, mas vamos continuar com esse processo nos próximos passos. Agora, vamos chamar a atenção para os dados.

## 4\. Foque a atenção onde você deseja

Antes de iniciar as orientações sobre essa seção, quero que você conte rapidamente quantos números 3 aparecem na sequência.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*NC2B3ws9-e45bi8w.png)

Explicação sobre atributos pré-atentivos. Fonte: Storytelling com Dados.

A resposta é: 6. Agora, repita o exercício de contagem do número 3.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*KTuFJktg5hp3K1GK.png)

Explicação sobre atributos pré-atentivos utilizando cores. Fonte: Storytelling com Dados.

Acho que ficou mais fácil de identificar que a resposta é 6, né?!

Como é explicado por Cole, a cor é um dos vários atributos pré-atentivos para serem utilizados no gráfico a fim de chamar a atenção.

> *Isto é, se usados estrategicamente, os atributos pré-atentivos permitem que nosso público veja o que queremos antes mesmo que saiba o que está vendo!*

Abaixo, vou deixar uma imagem de elementos que podem ajudar na atração da visualização de dados.

![](https://miro.medium.com/v2/resize:fit:1268/format:webp/0*Sp0jBx5qhKw16YIb.png)

Atributos pré-atentivos. Fonte: Storytelling com Dados.

Depois dessas explicações, vamos iniciar com um dos elementos de destaque que eu mais gosto: cor (tonalidade).

## Cor

Para as cores, eu sempre utilizo essas que estão no código abaixo. São cores que Cole utiliza em seus gráficos também!

```md
# Definições de cores -> todas estão numa escala de mais escura para mais clara
CINZA1, CINZA2, CINZA3 = '#231F20', '#414040', '#555655'
CINZA4, CINZA5, CINZA6 = '#646369', '#76787B', '#828282'
CINZA7, CINZA8, CINZA9 = '#929497', '#A6A6A5', '#BFBEBE'
AZUL1, AZUL2, AZUL3, AZUL4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
VERMELHO1, VERMELHO2, VERMELHO3, VERMELHO4, VERMELHO5 = '#DB0527', '#E23652', '#ED8293', '#F4B4BE', '#FBE6E9'
VERDE1, VERDE2 = '#0C8040', '#9ABB59'
LARANJA1 = '#F79747'
AMARELO1, AMARELO2, AMARELO3, AMARELO4, AMARELO5 = '#FFC700', '#FFCC19', '#FFEB51', '#FFE37F', '#FFEEB2'
BRANCO = '#FFFFFF'
```

No entanto, você pode optar por outras. Por exemplo, a própria documentação do Matplotlib possui uma [seção dedicada só para cores](https://matplotlib.org/stable/users/explain/colors/colormaps.html).

![](https://miro.medium.com/v2/resize:fit:1256/format:webp/0*Ir5n6THGLgCqsFUE.png)

Paleta de cores disponível no Matplotlib. Fonte: Choosing Colormaps in Matplotlib

Se preferir, vou deixar abaixo uma linha de código para escolher a paleta de cor e, também, vou colocar a [documentação do Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html) para pegar a paleta.

```md
import matplotlib.pyplot as plt
from cycler import cycler
```
```md
cores = plt.get_cmap('Pastel2').colors # Pegar mapa de cores
ciclo_cores = cycler('color', cores) # Associar paleta a um ciclo de cores
plt.rc('axes', prop_cycle=ciclo_cores) # rc -> sempre que criar eixos -> usar ciclo
```

Para **chamar a atenção**, eu gosto de utilizar o **AZUL**. Como disse Cole, além de imprimir bem em preto e branco, **evita-se problemas com daltonismo**!

> *Segundo Cole, aproximadamente 8% dos homens e metade disso de mulheres são daltônicos.*

Pessoas daltônicas geralmente possuem a **dificuldade de distinguir entre tons vermelho e verde**. Nesse sentido, é bom evitar essas cores.Veja a imagem abaixo. Na esquerda, como é enxergado por uma pessoa sem daltonismo. No lado direito, como uma pessoa daltônica visualiza.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*-rdyzTE5o1diKi8m.png)

Imagem comparando como uma pessoa sem daltonismo visualiza uma imagem (lado esquerdo) e como um indivíduo daltônico enxerga (lado direito). Fonte: Vischeck

Contudo, se for necessário utilizá-las, certifique-se de adicionar algum indício visual. Por exemplo, um sinal de + para verde (pois é associado a cores positivas) e um sinal de — para cor vermelha (visto que é relacionado à redução ou a coisas negativas).

Agora, vamos para o nosso gráfico. Eu notei que houve uma ascensão após o ano de 2008 de registros de queimadas e, portanto, queria focar nisso. Logo, vamos dividir os plots das linhas (`ax.plot`) em dois grupos:

```md
# Dividir os dados em dois segmentos
dados_1998_2008 = queimadas_ano[(queimadas_ano['year'] >= 1998) & (queimadas_ano['year'] <= 2008)]
dados_2008_2017 = queimadas_ano[(queimadas_ano['year'] >= 2008) & (queimadas_ano['year'] <= 2017)]

# Criar o gráfico de linha para cada segmento com cores diferentes
ax.plot(dados_1998_2008['year'], dados_1998_2008['int_number'], color=CINZA7)
ax.plot(dados_2008_2017['year'], dados_2008_2017['int_number'], color=AZUL1)
```

Nesse caso, definimos até 2008 com uma cor cinza e o restante dos anos com azul. Além disso, vamos definir outro elemento: tamanho das linhas.

## Tamanho

O tamanho também é um ótimo aliado para direcionar a atenção do público. Nesse sentido, vamos definir, por meio do parâmetro `linewidth` a largura das linhas.

```md
dados_1998_2008 = queimadas_ano[(queimadas_ano['year'] >= 1998) & (queimadas_ano['year'] <= 2008)]
dados_2008_2017 = queimadas_ano[(queimadas_ano['year'] >= 2008) & (queimadas_ano['year'] <= 2017)]

ax.plot(dados_1998_2008['year'], dados_1998_2008['int_number'], 
        color=CINZA7, 
        linewidth=2) # Largura 2
ax.plot(dados_2008_2017['year'], dados_2008_2017['int_number'], 
        color=AZUL1, 
        linewidth=4) # Largura 2
```

## Acercamento

Por fim, para dar um maior destaque, vou realizar um “acercamento” entre os anos de 2008 e 2017. Para isso, vamos utilizar o método `ax.axvspan`. O parâmetro `alpha ` indica a transparência da área de foco.

```md
fig, ax = plt.subplots(figsize=(14, 7), dpi=72)

dados_1998_2008 = queimadas_ano[(queimadas_ano['year'] >= 1998) & (queimadas_ano['year'] <= 2008)]
dados_2008_2017 = queimadas_ano[(queimadas_ano['year'] >= 2008) & (queimadas_ano['year'] <= 2017)]

ax.plot(dados_1998_2008['year'], dados_1998_2008['int_number'], 
        color=CINZA7, 
        linewidth=2)
ax.plot(dados_2008_2017['year'], dados_2008_2017['int_number'], 
        color=AZUL1, 
        linewidth=4) 

# Definir área para foco
ax.axvspan(2008, 2017, color=CINZA4, alpha=0.15) # alpha -> transparência
```

Por fim, vamos juntar todo o código e verificar como está ficando nosso gráfico:

```md
# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(14, 7), dpi=72)

# Dividir os dados em dois segmentos
dados_1998_2008 = queimadas_ano[(queimadas_ano['year'] >= 1998) & (queimadas_ano['year'] <= 2008)]
dados_2008_2017 = queimadas_ano[(queimadas_ano['year'] >= 2008) & (queimadas_ano['year'] <= 2017)]

# Criar o gráfico de linha para cada segmento com cores diferentes
ax.plot(dados_1998_2008['year'], dados_1998_2008['int_number'], color=CINZA7, linewidth=2)
ax.plot(dados_2008_2017['year'], dados_2008_2017['int_number'], color=AZUL1, linewidth=4)

# Definir área para foco
ax.axvspan(2008, 2017, color=CINZA4, alpha=0.15)

# Remover grid
ax.grid(False)

# Remover linhas
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Definir cores das linhas
ax.spines['bottom'].set_color(CINZA5)
ax.spines['left'].set_color(CINZA5)

# Configurar rótulos do eixo y
ax.set_ylabel('Registros de Queimadas', color=CINZA5, fontsize=12, fontweight='bold')

# Definir cor cinza dos valores dos eixos x e y
ax.tick_params(axis='x', colors=CINZA5, labelsize=12)
ax.tick_params(axis='y', colors=CINZA5, labelsize=12)

# Forçar anos eixo x
ax.set_xticks(ticks=anos, labels=anos)

plt.show()
```

Resultado do código acima:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*kyTVoXa_-dSML4jI.png)

Gráfico resultante do código acima. Fonte: Autor.

Agora, estamos chegando na reta final, em que vamos fazer os últimos detalhes do gráfico, como adicionar legendas, títulos e fonte.

## 5\. Pense como um designer

Ao pensar como um designer, Cole expõe quatro estratégias para serem consideradas ao criar uma visualização de dados:

- **Affordance** → aspectos inerentes ao design que tornam óbvio como o produto deve ser usado

Por exemplo, um botão permite ser pressionado. Essa característica sugere como interagir com o objeto. Quando affordances suficientes estão presentes, o bom design desaparece e você nem percebe.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*rxYTdbT6syDDRwlH)

Exemplo de Affordance: botão. Fonte: Giphy

No nosso gráfico, estamos aos poucos mostrando como queremos que ele seja interpretado (focando após 2008, mudança das linhas, etc).

- **Acessibilidade** → designs devem ser úteis para pessoas com diversas habilidades

**Resumidademente: não complique demais!** Quanto mais complexa a visualização de dados, maior será a percepção pelo público de que a compreensão demandará mais tempo, diminuindo, assim, a probabilidade de interesse em interpretá-la.

> Afinal, pense no nosso exemplo, quanto tempo você acha que um Ministro do Meio Ambiente possui para analisar um gráfico?!

Nesse tópico, vamos colocar títulos, legendas e qualquer item que possa auxiliar na compreensão do nosso gráfico.

- **Estética** → atenção à estética mostra um respeito geral por seu trabalho e seu público

Precisamos aumentar a tolerância do público a problemas de design, tornando os visuais esteticamente atraentes.

Nesse caso, acredito que estamos fazendo um bom trabalho! Então não vou entrar em muitos detalhes.

- **Aceitação** → para o design ser eficiente, precisa ser aceito pelo público

É necessário que a visualização que estamos apresentando seja aceita pelas pessoas. Afinal, muitos são resistentes às modificações, pois é um fato da natureza humana a maioria dos indivíduos sentir certo grau de desconforto com mudanças.

![](https://miro.medium.com/v2/resize:fit:1252/format:webp/0*6NV-ftKWFyp92r5P)

Imagem de apresentação de relatório. Fonte: Freepik.

Além disso, embora estejamos fingindo que vamos apresentar um gráfico para o Ministro do Meio Ambiente, o meu público é você, leitor! **Por isso, se tiver sugestões de melhorias, entre em contato comigo no LinkedIn.**

Agora, após essa introdução, vamos voltar ao nosso gráfico. Primeiramente, quero destacar valores de queimadas em 4 anos:

- 1998 → acho bom destacar o primeiro ano com registros
- 2003 -> foi o pico de queimadas
- 2008 -> apresentou o menor registro no declínio pós 2003
- 2017 -> quero mostrar o último registro (infelizmente, o dataset só vai até esse ano, mas seria legal mostrar como está atualmente).

Para colocar os valores, vamos fazer uma coisa um pouquinho mais avançada.

```md
for ano, queimada in zip(anos, queimadas):
    if ano in [1998, 2003]:
        ax.scatter(ano, queimada, s=50, color=CINZA7)
        ax.annotate(queimada, 
                    xy=(ano, queimada), 
                    xytext=(8, 0), 
                    textcoords='offset points',
                    color=CINZA7,
                    fontsize=12)
    elif ano in [2008, 2017]:
        ax.scatter(ano, queimada, s=100, color=AZUL1)
        ax.annotate(queimada, 
                    xy=(ano, queimada), 
                    xytext=(8, 0), 
                    textcoords='offset points',
                    color=AZUL1,
                    fontsize=14)
```

Neste código, estamos percorrendo a coluna dos anos (`ano`) e valores de queimadas (`queimada`) usando um loop `for`. A função `zip` é utilizada para combinar as duas variáveis, `anos` e `queimadas` (basicamente vai “juntar” cada ano com seu número, por exemplo, vai fazer isso (1998, 20013)).

Para cada par de valores ano-queimada:

1. O código verifica se o ano está na lista `[1998, 2003]` ou `[2008, 2017]` usando condicionais `if` e `elif`.
2. Se o ano estiver em `[1998, 2003]`, ele cria um gráfico de dispersão (`ax.scatter`) com tamanho `s=50`, usando a cor `CINZA7`. Em seguida, adiciona um rótulo (`ax.annotate`) no ponto com o valor de queimadas, utilizando coordenadas `xy` para a posição do rótulo. O argumento `xytext` define a posição do texto relativo ao ponto, `textcoords` define as coordenadas do texto em relação ao ponto (valor vai ficar sempre um pouco ao lado), a cor do texto é definida como `CINZA7` e o tamanho da fonte é definido como `fontsize=12`.
3. Se o ano estiver em `[2008, 2017]`, ele cria um ponto de dispersão com tamanho `s=100`, usando a cor `AZUL1`. Em seguida, adiciona um rótulo no ponto com o valor da queimada, da mesma forma que no caso anterior, mas com uma cor diferente e um tamanho de fonte maior.

> Ok, isso pode ser uma parte mais complicadinha. Mas, resumindo, vamos percorrer as colunas ano e queimadas ao mesmo tempo, colocando o registro de queimadas apenas nos anos que quereremos (estamos utilizando o gráfico de dispersão para isso).

Além disso, visto que destacamos alguns anos, vou omitir o eixo y para evitar a inclusão de informação redundante (lembra de reduzir a saturação, certo?!). Todavia, fique à vontade para optar por deixar ou não.

```md
# Remover yticks do eixo y
ax.set_yticks([])
```

Vou deixar os ticks (os ‘tracinhos’) acima dos anos, pois acho que vai ficar melhor. No entanto, se quiser retirar, pode usar o comando:

- `ax.tick_params(bottom=False)`

Por fim, deixei por último uma das partes que acho mais trabalhosas do Matplotlib: **inserir textos nos gráficos**.

> *Conforme Cole, o uso cuidadoso de texto ajuda a garantir que sua visualização de dados seja acessível. O texto tem várias funções na comunicação com dados: utilize-o para legendar, apresentar, explicar, reforçar, destacar, recomendar e contar uma história.*

Desse modo, primeiramente vamos colocar o título. Se quiser, você pode utilizar o `ax.set_title()` ou `plt.title()` para criá-lo. Todavia, acho melhor utilizar o `ax.text` (há a opção `ax.annotate` também).

```md
# Título
ax.text(-0.02, 1.22,'Focos de Queimadas nas Florestas Brasileiras entre 1998 e 2017',
        fontsize=25,
        color=CINZA3,
        fontweight='bold',
        transform=ax.transAxes)
```

No código acima, quero destacar essa linha: `transform=ax.transAxes`. Por quê? Simplesmente pois é um processo meio trabalhoso acertar o posicionamento preciso de textos no Matplotlib (sim, é tentativa e erro, até verificar a melhor disposição).

Desse modo, a linha `transform=ax.transAxes` vai especificar o sistema de coordenadas, em que os valores típicos variam de 0 a 1 ao longo do gráfico. Gosto de utilizá-lo pois facilita encontrar o posicionamento adequado dos textos.

Deixa detalhar melhor abaixo:

- Coordenada (0,1): será o canto superior esquerdo do gráfico
- Coordenada (0,0): será o canto inferior esquerdo do gráfico
- Coordenada (1,1): será o canto superior direito do gráfico
- Coordenada (1,0): será o canto inferior direito do gráfico
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*dOUGI_MINhBcdvaj.png)

Explicação sobre sistema de coordenadas no Matplotlib. Fonte: Autor.

**Embora Cole não ache bom destacar tanto o título do gráfico, eu optei por deixá-lo em negrito.** Avalie se você prefere destacar mais o título ou não!

Além disso, resolvi colocar um subtítulo explicando melhor a situação. Todavia, isso não é obrigatório, ok?!

```md
# Subtítulo
ax.text(-0.02, 1.1,'O pico de queimadas ocorreu em 2003, tendo um declínio após esse ano. Contudo, '
                    'entre 2009 e 2017, houve um aumento nos\nfocos de queimadas. '
                    'Nesse sentido, o monitoramento e ações preventivas são ' 
                    'cruciais para preservar nossos ecossistemas.',
        fontsize=14,
        color=CINZA5,
        transform=ax.transAxes)
```

Agora, vamos colocar as legendas dentro do gráfico para direcionar a interpretação do nosso gráfico pelo Ministro do Meio Ambiente.

```md
# Legendas
ax.text(0.02, 0.62,'$\\bf 1998-2003$: nesse período,\nobservou-se um crescimento\n'
                    'progressivo nos registros de\n'
                    'queimadas, atingindo seu pico\n'
                    'em 2003, com um aumento\n'
                    'expressivo de 113% em\n'
                    'comparação a 1998.',
        fontsize=11.5,
        color=CINZA4,
        transform=ax.transAxes)

# Legendas
ax.text(0.26, 0.15,'$\\bf 2004-2008$: porém, após o pico em\n2003, nota-se que houve' 
                  ' um declínio\nacentuado de queimadas nas\n'
                  'florestas brasileiras.',
        fontsize=11.5,
        color=CINZA4,
        transform=ax.transAxes)

# Legendas
ax.text(0.54, 0.2,'$\\bf 2009-2017$: após 2008, o número de queimadas\n' 
                  'aumentou novamente. Isso revela a importância de um\n'
                  'monitoramento contínuo a essa questão ambiental.',
        fontsize=12.5,
        color=AZUL1,
        transform=ax.transAxes)
```

> Obs.: As nossas legendas estão um pouco vagas. Recomendo você explorar mais os dados e buscar notícias sobre o aumento e diminuição de queimadas ao longo dos anos, além de verificar quais biomas sofreram mais com essa questão ambiental.

Por fim, vamos colocar a fonte do nosso gráfico no rodapé. No Kaggle, o autor obteve os dados no site [Dados Abertos](https://dados.gov.br/) do Governo Federal, por isso coloquei-o como nossa fonte.

```md
# Rodapé para a fonte
ax.text(-0.02, -0.15,'Fonte: Dados Abertos - Governo Federal',
        fontsize=12,
        color=CINZA5,
        transform=ax.transAxes)
```

Agora, vamos visualizar nosso gráfico? Verifique após o código abaixo:

```md
# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(14, 7), dpi=72)

# Dividir os dados em dois segmentos
dados_1998_2008 = queimadas_ano[(queimadas_ano['year'] >= 1998) & (queimadas_ano['year'] <= 2008)]
dados_2008_2017 = queimadas_ano[(queimadas_ano['year'] >= 2008) & (queimadas_ano['year'] <= 2017)]

# Gráfico de linha para cada segmento com cores diferentes
ax.plot(dados_1998_2008['year'], dados_1998_2008['int_number'], color=CINZA7, linewidth=2)
ax.plot(dados_2008_2017['year'], dados_2008_2017['int_number'], color=AZUL1, linewidth=4)

# Remover grid
ax.grid(False)

# Remover linhas
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)

# Definir cores das linhas
ax.spines['left'].set_color(CINZA5)
ax.spines['bottom'].set_color(CINZA5)

# Configurar rótulos do eixo y
ax.set_ylabel('Registros de Queimadas', color=CINZA5, fontsize=12, fontweight='bold')

# Definir cor cinza dos valores do eixo x
ax.tick_params(axis='x', colors=CINZA5, labelsize=12)

# Definir comprimento eixo y
ax.set_ylim(15000, 45000)

# Remover yticks do eixo y
ax.set_yticks([])

# Forçar anos eixo x
ax.set_xticks(ticks=anos, labels=anos)

# Definir área para foco
ax.axvspan(2008, 2017, color=CINZA4, alpha=0.15)

# Rótulos
for ano, queimada in zip(anos, queimadas):
    if ano in [1998, 2003]:
        ax.scatter(ano, queimada, s=50, color=CINZA7)
        ax.annotate(queimada, 
                    xy=(ano, queimada), 
                    xytext=(8, 0), 
                    textcoords='offset points',
                    color=CINZA7,
                    fontsize=12)
    elif ano in [2008, 2017]:
        ax.scatter(ano, queimada, s=100, color=AZUL1)
        ax.annotate(queimada, 
                    xy=(ano, queimada), 
                    xytext=(8, 0), 
                    textcoords='offset points',
                    color=AZUL1,
                    fontsize=14)

# Título / Subtítulo / Legendas
ax.text(-0.02, 1.22,'Focos de Queimadas nas Florestas Brasileiras entre 1998 e 2017',
        fontsize=25,
        color=CINZA3,
        fontweight='bold',
        transform=ax.transAxes)

# Subtítulo
ax.text(-0.02, 1.1,'O pico de queimadas ocorreu em 2003, tendo um declínio após esse ano. Contudo, '
                    'entre 2008 e 2017, houve um aumento nos\nfocos de queimadas. '
                    'Nesse sentido, o monitoramento e ações preventivas são ' 
                    'cruciais para preservar nossos ecossistemas.',
        fontsize=14,
        color=CINZA5,
        transform=ax.transAxes)

# Legendas
ax.text(0.02, 0.62,'$\\bf 1998-2003$: nesse período,\nobservou-se um crescimento\n'
                    'progressivo nos registros de\n'
                    'queimadas, atingindo seu pico\n'
                    'em 2003, com um aumento\n'
                    'expressivo de 113% em\n'
                    'comparação a 1998.',
        fontsize=11.5,
        color=CINZA4,
        transform=ax.transAxes)

# Legendas
ax.text(0.26, 0.15,'$\\bf 2004-2008$: porém, após o pico em\n2003, nota-se que houve' 
                  ' um declínio\nacentuado de queimadas nas\n'
                  'florestas brasileiras.',
        fontsize=11.5,
        color=CINZA4,
        transform=ax.transAxes)

# Legendas
ax.text(0.54, 0.2,'$\\bf 2009-2017$: após 2008, o número de queimadas\n' 
                  'aumentou novamente. Isso revela a importância de um\n'
                  'monitoramento contínuo a essa questão ambiental.',
        fontsize=12.5,
        color=AZUL1,
        transform=ax.transAxes)

# Rodapé para a fonte
ax.text(-0.02, -0.15,'Fonte: Dados Abertos - Governo Federal',
        fontsize=12,
        color=CINZA5,
        transform=ax.transAxes)

# Ajustar espaço entre os plots
plt.tight_layout()

# Exibir o gráfico
plt.show()
```

Resultado:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*T5ZslQN_PMfKHMFX9lSsBw.png)

Gráfico final. Fonte: Autor.

Gostou do nosso resultado? Acha que o Ministro do Meio Ambiente vai entender a importância de monitorar as queimadas nas florestas brasileiras?

Compare o antes e depois do nosso gráfico! Veja a importância de transformar sua análise exploratória em uma explanatória:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YE6qWm_X1Tu59VH-4NbXYA.png)

Antes e depois do nosso gráfico sobre os registros de queimadas no Brasil ao longo dos anos. Fonte: Autor.

Esse é o nosso resultado final, mas, se fôssemos realizar uma apresentação para o Ministro, por que não contarmos uma história?

Vamos à última parte do nosso artigo!

## 6\. Conte uma história

Como já mencionamos, o Ministro do Meio Ambiente deve ser uma pessoa meio ocupada, certo? E se tivéssemos apenas cinco minutos para apresentar os nossos resultados?

A sequência a seguir ilustra um caminho que poderíamos realizar para destacar nossos achados.

Primeiro, vamos situar o Ministro sobre o problema. Podemos explicar que as queimadas são um problema ambiental relevante no país e que vamos demonstrar isso com dados!

Nesse sentido, vamos destacar o pico de queimadas no ano de 2003.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*q0Iztk4l1wLWjOBiBKmvnQ.png)

Pico de queimadas em 2003. Fonte: Autor.

Após isso, vamos mostrar que houve um declínio desse problema ambiental.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*i1NSNXav-5h7YWK2k62PIA.png)

Declínio de queimadas após 2003. Fonte: Autor.

Depois de relatar o declínio, **vamos chamar atenção do nosso público para o que achamos importante: o aumento de queimadas após 2008**. Isso é importante para alertar o Ministro que as queimadas são um assunto extremamente relevante no cenário nacional.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nXXcqvW9RYrUXNhZJiqttA.png)

Destaque para o aumento de queimadas após 2008. Fonte: Autor.

Agora que ele visualizou um panorama, vamos colocar os números e as outras informações.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*T5ZslQN_PMfKHMFX9lSsBw.png)

Gráfico final. Fonte: Autor.

Esse é o gráfico que vamos entregar ou deixar no slide final. **Note que conseguimos focar a atenção do Ministro para tomar medidas para mitigar esse problema.**

Contudo, embora nossa análise tenha focado no aumento de queimadas entre 2009 e 2017, não necessariamente poderíamos ter focado nesse período. Por exemplo, poderíamos ter chamado a atenção para o elevado aumento até 2003.

Outra abordagem viável seria analisar a redução das queimadas entre 2003 e 2008. Nesse caso, seria legal investigar as razões por trás desse declínio, o que poderia nos levar a recomendar a implementação de programas de monitoramento florestal mais eficazes.

> *Por isso, não há uma forma correta para fazer uma apresentação visual com seus dados. Isso que é legal do Storytelling, já que você decide a história que vai contar!*

## Considerações Finais

Agora, chegou a sua vez. Por que não pegar esse mesmo dataset e verificar quais foram os estados mais atingidos? Ou quais são os meses que possuem o maior número de queimadas?

Ou, se preferir, escolha um outro conjunto de dados e faça uma análise parecida! Não se limite, use sua criatividade e os conhecimentos adquiridos nos dois artigos!

Espero ter ajudado a aprimorar suas técnicas de Storytelling e DataViz.

Estou sempre à disposição para trocarmos experiências!

## Responses (1)

Bruno Guerra

What are your thoughts?

```c
Uau!! Uma verdadeira aula em formato de post! Adorei a explicação e o contexto. Eu sabia que valeria a pena esperar para ler a segunda parte. Vou experimentar fazer e o colocar o aprendizado em prática. Obrigado Henrique. Parabéns pela postagem. Sensacional 🚀✨
```

3

Jun 27, 2021

Jun 24, 2024

[View list](https://medium.com/@guerra.bruno/list/reading-list?source=post_page---list_recirc--35e0da269a1e-----------predefined%3Aba35701959d5%3AREADING_LIST----------------------------)