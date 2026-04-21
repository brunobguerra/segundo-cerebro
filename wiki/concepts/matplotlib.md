---
title: "Matplotlib"
slug: matplotlib
type: concept
lang: pt-BR
sources:
  - "[[wiki/sources/matplotlib-storytelling-dados-pt-i|Matplotlib e Storytelling com Dados — Pt. I]]"
  - "[[wiki/sources/matplotlib-storytelling-dados-pt-ii|Matplotlib e Storytelling com Dados — Pt. II]]"
updated: 2026-04-21
tags: [data-science, visualização-de-dados, python]
summary: "Biblioteca Python de visualização: hierarquia Figure/Axes/Axis/Artist, API pyplot vs OO, subplots/mosaic, decluttering e ênfase no eixo OO."
---

# Matplotlib

Biblioteca de visualização em Python (inspirada em gráficos estilo MATLAB), útil para exploração e para gráficos publicáveis quando combinada com bom desenho visual e narrativa — ver [[wiki/concepts/storytelling-com-dados|Storytelling com Dados (livro e princípios)]] e as fontes [[wiki/sources/matplotlib-storytelling-dados-pt-i|Pt. I]] / [[wiki/sources/matplotlib-storytelling-dados-pt-ii|Pt. II]] da série Data Hackers.

## Termos (EN)

- *Matplotlib*, *pyplot*, *Figure*, *Axes*, *Axis*, *Artist*, *subplots*, *subplot_mosaic*, *spines*, *tick labels*, *transAxes*, *axvspan*, *annotate*.

## Hierarquia (objeto mental)

### Figure

Espaço global (“lousa”) onde elementos do gráfico são dispostos. **Não** é sinônimo de “um gráfico”: uma Figure pode conter vários gráficos.

### Axes

Área de plotagem dentro de uma Figure, com eixos, rótulos e título próprios. Na prática, **um gráfico** costuma corresponder a um objeto Axes.

### Axis

Parte que cuida de escala, limites, *ticks* e *tick labels* de um eixo.

### Artist

Tudo que é **visível** no gráfico é Artist (incluindo Figure, Axes e Axis, além de linhas, texto, etc.) — metáfora do “pincel”.

## Pyplot versus API orientada a objetos (OO)

| Aspecto | Pyplot (`plt.*`) | OO (`fig, ax = plt.subplots()`) |
|--------|-------------------|----------------------------------|
| Figure / Axes | Implícitos, “atuais” | Referências explícitas `fig`, `ax` |
| Controle | Customizações afetam o estado global da figura atual | Controle por instância, melhor com vários Axes |
| Uso sugerido no artigo ingerido | Explorações rápidas | Figuras com vários painéis e personalização fina |

Muitas funções têm paralelo: `plt.bar` / `ax.bar`, `plt.xlabel` / `ax.set_xlabel`, etc.

## Vários gráficos na mesma Figure

- `plt.subplots(nrows=..., ncols=...)` devolve um array de Axes (indexação estilo NumPy).
- `fig.subplot_mosaic(layout)` (strings com letras por célula) permite layouts irregulares e nomes estáveis (`mosaic['A']`, …), com menos cerimônia que grades apenas numéricas.

Documentação oficial: [matplotlib.org](https://matplotlib.org/).

## Decluttering e ênfase (API OO)

Padrões úteis quando o objetivo é um gráfico **explanatório** (não só EDA rápida), como na [[wiki/sources/matplotlib-storytelling-dados-pt-ii|Pt. II]] da série citada:

- **Grade e moldura:** `ax.grid(False)`; esconder *spines* com `ax.spines[...].set_visible(False)` ou `ax.set_frame_on(False)` quando fizer sentido; colorir discretamente as *spines* que restarem.
- **Ticks e rótulos:** `ax.tick_params`, `ax.set_xticks` / `labels` para controlar densidade (ex.: todos os anos em uma série longa).
- **Destaque temporal:** `ax.axvspan(xmin, xmax, alpha=...)` para “acercar” visualmente um período.
- **Série segmentada:** vários `ax.plot` com cor e `linewidth` diferentes por período; `ax.scatter` + `ax.annotate` para marcar poucos anos-chave.
- **Texto fora do sistema de dados:** `ax.text(..., transform=ax.transAxes)` para título, subtítulo, caixas de interpretação e rodapé de fonte; `plt.tight_layout()` para evitar cortes.

## Ver também

- [[wiki/concepts/storytelling-com-dados|Storytelling com Dados (livro e princípios)]]
- [[wiki/concepts/analise-exploratoria-vs-explanatoria|Análise exploratória vs explanatória]]
- [[wiki/sources/matplotlib-storytelling-dados-pt-i|Matplotlib e Storytelling com Dados — Pt. I]]
- [[wiki/sources/matplotlib-storytelling-dados-pt-ii|Matplotlib e Storytelling com Dados — Pt. II]]
