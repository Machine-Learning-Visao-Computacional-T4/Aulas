# Exercício 03 — Hands-on: gráficos básicos

**Tipo:** prática + commit · 15 min

## Objetivo
Criar três gráficos básicos (linha, barra e dispersão) a partir do `pedidos_prontos.csv` e salvar um deles em arquivo.

## O que fazer
1. Crie `grafico_basico.py` (ou uma célula no Colab) lendo `pedidos_prontos.csv`.
2. Faça um gráfico de **linha** da quantidade de pedidos por mês (use `groupby` e `size`).
3. Faça um gráfico de **barras** com o faturamento por canal.
4. Faça uma **dispersão** de `preco` contra `qtd` e comente o que vê.
5. Salve o gráfico de barras com `plt.savefig("canal.png")` **antes** do `plt.show()`. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_03_graficos_basicos/grafico_basico.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_03_graficos_basicos/grafico_basico.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `grafico_basico.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos_prontos.csv`); veja o [guia](../../docs/guia_visualizacao.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
mes
1    118
2    116
3    116
4    102
5    139
6     96
dtype: int64
canal
Delivery    1650.0
App         3731.0
Balcão      5704.0
Name: total, dtype: float64
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Dicas e erros comuns
- `plt.savefig` precisa vir **antes** de `plt.show()`: depois do `show`, a figura é descartada e o arquivo sai em branco.
- Use linha quando o eixo x tem ordem (tempo); `marker="o"` marca cada ponto.
- `alpha=0.5` deixa os pontos transparentes e mostra a sobreposição.
