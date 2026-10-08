# Exercício 05 — Mãos à obra + commit: explorando as vendas

**Tipo:** prática + commit · 18 min

## Objetivo
Aplicar **leitura, inspeção, filtros e novas colunas** em um dataset completo.

## O que fazer
1. Coloque `vendas.csv` ao lado do seu script e carregue com `read_csv`.
2. Mostre `shape`, as colunas e o `describe` das colunas numéricas.
3. Crie a coluna `total` e responda: quais vendas passam de **R$ 1.000**? Quais são de **Florianópolis ou Blumenau**? Qual é o **produto mais caro**?
4. Salve o resultado de uma das perguntas em um novo CSV com `index=False`; commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_pandas_dataframes/exercicio_05_explorando_as_vendas/exploracao.py
```

No Windows, se `python` não funcionar, use `py aula1_pandas_dataframes/exercicio_05_explorando_as_vendas/exploracao.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `exploracao.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`vendas.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
Linhas e colunas: (8, 6)
Colunas: ['id', 'produto', 'categoria', 'cidade', 'quantidade', 'preco']
       quantidade   preco
count         8.0     8.0
mean          2.5  1145.0
max           5.0  3500.0

Vendas acima de R$ 1.000:
    produto         cidade   total
2   Monitor  Florianópolis  1800.0
3  Notebook       Blumenau  3500.0
7  Notebook      Joinville  7000.0

Vendas de Florianópolis ou Blumenau: 5
Produto mais caro: Notebook

Arquivo vendas_acima_de_1000.csv gravado.
```

## Dicas e erros comuns
- `df["preco"].idxmax()` devolve o **rótulo da linha** do maior preço; use `df.loc[rótulo, "produto"]` para ver o produto.
- Os dados são **fictícios**: podem ir para o GitHub sem problema.
- Extra: troque a ordenação para pegar as 3 menores vendas (`sort_values`).
