---
title: "Matplotlib e Storytelling com Dados — Pt. II"
slug: matplotlib-storytelling-dados-pt-ii
type: source
lang: pt-BR
sources:
  - "`A00 Inbox/clippings/Matplotlib e Storytelling com Dados 1.md`"
updated: 2026-04-21
tags: [data-science, visualização-de-dados, matplotlib, python, storytelling]
summary: "Tutorial OO no Matplotlib: dataset Kaggle de queimadas, seis lições de Storytelling com Dados, gráfico de linhas do exploratório ao explanatório (antes/depois) e sequência de slides."
---

# Matplotlib e Storytelling com Dados — Pt. II

Continuação direta da [[B03 Resources/sources/matplotlib-storytelling-dados-pt-i|Matplotlib e Storytelling com Dados — Pt. I]], por [[B03 Resources/entities/henrique-w-franco|Henrique W. Franco]] (Medium / **Data Hackers**): parte **prática** de um gráfico de linhas com técnicas do livro [[B03 Resources/concepts/storytelling-com-dados|Storytelling com Dados (livro e princípios)]].

## Onde está a fonte

- Clipping: `A00 Inbox/clippings/Matplotlib e Storytelling com Dados 1.md`
- URL original: [Matplotlib e Storytelling com Dados — Pt. II](https://medium.com/data-hackers/matplotlib-e-storytelling-com-dados-pt-ii-35e0da269a1e)

## Enquadramento narrativo (contexto)

- **Público fictício:** ministro do Meio Ambiente; **pergunta de negócio:** evolução dos **registros de queimadas** nas florestas brasileiras ao longo dos anos.
- **Dados:** [Forest Fires in Brazil](https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil/data) (Kaggle); notebook Colab linkado no Medium; agregação com Pandas (`groupby('year')['number'].sum()` etc.).
- **Disciplina central:** não apresentar [[B03 Resources/concepts/analise-exploratoria-vs-explanatoria|análise exploratória]] no lugar da **explanatória** quando o objetivo é comunicar uma mensagem.

## As seis lições (estrutura do artigo)

O texto organiza o tutorial segundo seis eixos do livro de Cole Nussbaumer:

1. **Entenda o contexto** — quem é o público e o que precisa saber ou fazer.
2. **Escolha uma apresentação visual adequada** — para série temporal de contagens ao longo dos anos, **gráfico de linhas** (barras também podem servir, “depende”).
3. **Elimine a saturação** — reduzir *carga cognitiva*; retirar o que ocupa espaço sem aumentar entendimento (referência a *WTF Visualizations* como antiexemplos).
4. **Foque a atenção onde você deseja** — *pre-attentive attributes* (cor, tamanho, etc.); no caso, destaque pós-2008 com cor mais forte, `linewidth` maior, `ax.axvspan` com transparência.
5. **Pense como um designer** — *affordance*, **acessibilidade** (simplicidade; tempo limitado do decisor), **estética**, **aceitação**; título/subtítulo com `ax.text` e `transform=ax.transAxes`; anotações com `scatter` + `annotate`; opcionalmente omitir *yticks* para evitar redundância com rótulos nos pontos; rodapé com fonte (Dados Abertos / Governo Federal, via metadados do dataset no Kaggle).
6. **Conte uma história** — sequência de slides: situar o problema → pico em 2003 → declínio → **ênfase no aumento após 2008** → gráfico final completo.

## Técnicas Matplotlib destacadas (OO)

Resumo alinhado à nota [[B03 Resources/concepts/matplotlib|Matplotlib]]:

- `fig, ax = plt.subplots(figsize=..., dpi=...)`
- Linha inicial com Pyplot só para “ver” a série; refinamento em OO.
- Decluttering: `ax.grid(False)`, `ax.spines['top'/'right'].set_visible(False)`, cores discretas nos *spines* restantes, `ax.tick_params`, `ax.set_xticks` para mostrar todos os anos.
- Ênfase: dois segmentos de `ax.plot` (cinza vs azul), `linewidth`, `ax.axvspan(..., alpha=...)`.
- Paleta fixa em constantes hex (inspirada nas cores que Cole usa); menção a **daltonismo** (evitar vermelho/verde sem redundância; azul como cor de destaque); alternativa com `cycler` + colormap do Matplotlib.
- Texto posicionado com `transform=ax.transAxes` (coordenadas 0–1); `plt.tight_layout()`.

## Antes e depois

O artigo fecha com contraste explícito entre o primeiro `plt.plot` “cru” e o gráfico final explanatório — mesma ideia prometida já na Pt. I.

## Termos (EN)

- *Exploratory vs explanatory analysis*, *cognitive load*, *saturation / decluttering*, *pre-attentive attributes*, *affordance*, *accessibility*, *colorblind-safe palette*, *transAxes*, *axvspan*, *annotate*.

## Incertezas / edição

- Pequenas divergências de redação entre trechos do subtítulo (“2008”, “2009–2017”) e o rótulo em negrito no texto embutido do gráfico — tratar números com o CSV e com revisão humana se for reproduzir o caso.

## Ver também

- [[B03 Resources/sources/matplotlib-storytelling-dados-pt-i|Matplotlib e Storytelling com Dados — Pt. I]]
- [[B03 Resources/concepts/matplotlib|Matplotlib]]
- [[B03 Resources/concepts/storytelling-com-dados|Storytelling com Dados (livro e princípios)]]
- [[B03 Resources/concepts/analise-exploratoria-vs-explanatoria|Análise exploratória vs explanatória]]
