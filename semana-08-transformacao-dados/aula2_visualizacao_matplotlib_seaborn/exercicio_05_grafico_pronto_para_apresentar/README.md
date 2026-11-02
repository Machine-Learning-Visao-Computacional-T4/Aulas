# Exercício 05 — Hands-on: gráfico pronto para apresentar

**Tipo:** prática + commit · 15 min

## Objetivo
Customizar um gráfico até ele poder ser mostrado a um gestor.

## O que fazer
1. Crie `customizado.py` com um gráfico de barras do faturamento por categoria (seaborn ou Matplotlib).
2. Acrescente título, rótulos com unidade, cor institucional e eixo em reais com `FuncFormatter`.
3. Destaque a barra de maior valor com cor diferente ou `annotate`.
4. Salve como `categoria.png` com `dpi=150`. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_05_grafico_pronto_para_apresentar/customizado.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_05_grafico_pronto_para_apresentar/customizado.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `customizado.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos_prontos.csv`); veja o [guia](../../docs/guia_visualizacao.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
categoria
Café             3902.0
Salgado          2678.0
Bebida Gelada    2318.0
Doce             2187.0
Name: total, dtype: float64
Imagem categoria.png gravada.
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Dicas e erros comuns
- `FuncFormatter` formata os rótulos do eixo como moeda; `annotate` marca o destaque; `set_ylim` abre espaço para o texto.
- Barras sempre começam no **zero**: cortar o eixo exagera as diferenças.
