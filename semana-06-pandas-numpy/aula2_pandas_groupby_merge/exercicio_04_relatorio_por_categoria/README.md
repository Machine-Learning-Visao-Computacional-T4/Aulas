# Exercício 04 — Mãos à obra + commit: relatório por categoria

**Tipo:** prática + commit · 15 min

## Objetivo
Produzir um **relatório resumido** com `groupby` e salvá-lo.

## O que fazer
1. Crie `relatorio_categorias.py`, que lê `vendas.csv` e cria a coluna `total`.
2. Use `groupby` com `agg` para calcular, **por categoria**: total vendido, itens vendidos e preço médio.
3. Ordene o resumo pelo total, do maior para o menor, e salve em `resumo_categorias.csv`.
4. Commit e push; confira no GitHub como o CSV aparece.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_pandas_groupby_merge/exercicio_04_relatorio_por_categoria/relatorio_categorias.py
```

No Windows, se `python` não funcionar, use `py aula2_pandas_groupby_merge/exercicio_04_relatorio_por_categoria/relatorio_categorias.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `relatorio_categorias.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`vendas.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
              total_vendido  itens  preco_medio
categoria
Computadores        10500.0      3       3500.0
Vídeo                2700.0      3        900.0
Periféricos          1260.0     14         90.0
Arquivo resumo_categorias.csv gravado.
```

## Dicas e erros comuns
- Cada argumento `nome=(coluna, função)` do `agg` cria uma coluna de resultado com o nome escolhido.
- Extra: repita o relatório **por cidade** e compare os dois resumos.
