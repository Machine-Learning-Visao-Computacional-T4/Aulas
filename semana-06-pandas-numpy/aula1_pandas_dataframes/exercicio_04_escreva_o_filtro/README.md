# Exercício 04 — Escreva o filtro

**Tipo:** dinâmica + script · 12 min

## Objetivo
Traduzir perguntas em português para **filtros do pandas**.

## O que fazer
1. Para cada pergunta abaixo, escreva a **linha de código** do filtro (sem rodar). Considere o DataFrame `df` lido de `vendas.csv`.
2. Rode o script e compare com as suas respostas.
3. Discuta os erros mais comuns: `=` no lugar de `==`, `and` no lugar de `&`, parênteses esquecidos.

## As 5 perguntas
1. Vendas de **Mouse**.
2. Vendas em **Blumenau** com **quantidade maior que 3**.
3. Produtos que **não** são da categoria **Vídeo**.
4. Preço **entre 100 e 1000**.
5. Vendas de **Joinville OU** de **Notebook**.

<details>
<summary>Ver respostas</summary>

```python
df[df["produto"] == "Mouse"]
df[(df["cidade"] == "Blumenau") & (df["quantidade"] > 3)]
df[~(df["categoria"] == "Vídeo")]
df[df["preco"].between(100, 1000)]
df[(df["cidade"] == "Joinville") | (df["produto"] == "Notebook")]
```

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_pandas_dataframes/exercicio_04_escreva_o_filtro/filtros.py
```

No Windows, se `python` não funcionar, use `py aula1_pandas_dataframes/exercicio_04_escreva_o_filtro/filtros.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `filtros.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`vendas.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
1) Vendas de Mouse: 2 venda(s) (ids [2, 5])
2) Blumenau com quantidade > 3: 1 venda(s) (ids [7])
3) Fora da categoria Vídeo: 6 venda(s) (ids [1, 2, 4, 5, 7, 8])
4) Preço entre 100 e 1000: 4 venda(s) (ids [1, 3, 6, 7])
5) Joinville ou Notebook: 4 venda(s) (ids [2, 4, 6, 8])
```

## Dicas e erros comuns
- Use `&` (e), `|` (ou) e `~` (não), sempre com **cada condição entre parênteses**.
- `and` e `or` não funcionam com colunas: o pandas avisa que "o valor de verdade de uma Series é ambíguo".
