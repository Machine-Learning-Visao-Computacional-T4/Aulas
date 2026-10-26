# Exercício 06 — Monte o layout

**Tipo:** dinâmica + script · 6 min

## Objetivo
Traduzir um desenho de painel em código de `subplot_mosaic`.

## O que fazer
1. Observe o desenho 1: um gráfico **largo no topo** e dois menores embaixo. Escreva a lista do `subplot_mosaic` correspondente.
2. Compare com a resposta: `[["topo", "topo"], ["esq", "dir"]]`.
3. **Desafio (desenho 2):** um gráfico **alto à esquerda** e dois empilhados à direita.
4. Rode o script para ver os dois layouts.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_06_monte_o_layout/layouts.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_06_monte_o_layout/layouts.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `layouts.py` em uma célula e execute com `Shift + Enter`. Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
layout_1_largo_no_topo -> ['topo', 'esq', 'dir']
layout_2_alto_a_esquerda -> ['alto', 'a', 'b']
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Dicas e erros comuns
- No `subplot_mosaic`, repetir um nome na lista faz o gráfico **ocupar várias células**.
- Depois você acessa cada gráfico pelo nome (`ax["topo"]`), o que deixa o código legível.
