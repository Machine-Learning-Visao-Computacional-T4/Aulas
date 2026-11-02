# Exercício 07 — Hands-on: painel com subplots

**Tipo:** prática + commit · 15 min

## Objetivo
Montar uma figura com três ou mais gráficos organizados com subplots.

## O que fazer
1. Crie `painel.py` com `plt.subplots(2, 2)` ou `subplot_mosaic`.
2. Coloque faturamento por mês, por categoria e por canal em eixos diferentes (use o 4º espaço para outro gráfico).
3. Dê título a cada `ax` e um título geral com `fig.suptitle`.
4. Salve como `painel.png`. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_07_painel_com_subplots/painel.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_07_painel_com_subplots/painel.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `painel.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos_prontos.csv`); veja o [guia](../../docs/guia_visualizacao.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
axes tem shape (2, 2)
Imagem painel.png gravada.
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Dicas e erros comuns
- Com várias figuras, não dá mais para usar `plt.plot`: use `ax.plot`, `ax.set_title`... para dizer **em qual gráfico** desenhar.
- `layout="constrained"` (ou `fig.tight_layout()`) evita sobreposição de títulos e rótulos.
- `axes[linha, coluna]`: com `plt.subplots(2, 2)` o `axes` é uma matriz.
