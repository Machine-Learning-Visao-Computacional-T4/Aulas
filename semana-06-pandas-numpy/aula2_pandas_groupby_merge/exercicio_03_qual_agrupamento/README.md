# Exercício 03 — Qual agrupamento?

**Tipo:** dinâmica + script · 12 min

## Objetivo
Traduzir **perguntas de negócio** em `groupby`.

## O que fazer
1. Para cada pergunta, escreva a linha de código (coluna de agrupamento, coluna calculada e função). Considere `df` lido de `vendas.csv`, já com a coluna `total`.
2. Rode o script e confira os números.
3. Discuta qual pergunta exigiu mais cuidado (a última, que usa `max`).

## As 4 perguntas
1. **Total** vendido por produto.
2. **Preço médio** por categoria.
3. **Quantidade de vendas** por cidade.
4. **Maior venda** em cada cidade.

<details>
<summary>Ver respostas</summary>

```python
df.groupby("produto")["total"].sum()
df.groupby("categoria")["preco"].mean()
df.groupby("cidade").size()
df.groupby("cidade")["total"].max()
```

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_pandas_groupby_merge/exercicio_03_qual_agrupamento/agrupamentos.py
```

No Windows, se `python` não funcionar, use `py aula2_pandas_groupby_merge/exercicio_03_qual_agrupamento/agrupamentos.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `agrupamentos.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`vendas.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
1) Total vendido por produto:
produto
Monitor      2700.0
Mouse         420.0
Notebook    10500.0
Teclado       840.0
Name: total, dtype: float64

2) Preço médio por categoria:
categoria
Computadores    3500.0
Periféricos       90.0
Vídeo            900.0
Name: preco, dtype: float64

3) Quantidade de vendas por cidade:
cidade
Blumenau         2
Florianópolis    3
Joinville        3
dtype: int64

4) Maior venda em cada cidade:
cidade
Blumenau         3500.0
Florianópolis    1800.0
Joinville        7000.0
Name: total, dtype: float64
```

## Dicas e erros comuns
- O `groupby` **divide** a tabela em grupos, **aplica** uma função a cada grupo e **combina** os resultados.
- `size()` conta as linhas de cada grupo; `count()` contaria só os valores não ausentes de uma coluna.
