# Exercício 03 — Qual função de leitura?

**Tipo:** dinâmica + script · 12 min

## Objetivo
Escolher a **função de leitura** (e o **parâmetro** mais importante) para cada fonte de dados.

## O que fazer
1. Veja os 4 cenários abaixo. Para cada um, escreva a **função** do pandas e, se for o caso, o **parâmetro** principal.
2. Confira as respostas e discuta as divergências.
3. Rode o script: ele lê os **mesmos dados** em 5 formatos diferentes (arquivos desta pasta).
4. Feche pensando: o que muda **depois** que o dado virou DataFrame? (Nada: o formato de origem deixa de importar.)

## Os 4 cenários
1. Um **CSV exportado do Excel em português** (separado por `;` e com vírgula decimal).
2. Uma **planilha com 3 abas**, e você quer a aba `Janeiro`.
3. A **resposta de uma API** salva em JSON (uma lista de objetos).
4. Os dados de um sistema que ficam em um **banco SQL**.

<details>
<summary>Ver respostas</summary>

1. `pd.read_csv("arquivo.csv", sep=";", decimal=",")`
2. `pd.read_excel("arquivo.xlsx", sheet_name="Janeiro")`
3. `pd.read_json("arquivo.json")`
4. `pd.read_sql("SELECT ...", conexao)`

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_pandas_dataframes/exercicio_03_qual_funcao_de_leitura/leituras.py
```

No Windows, se `python` não funcionar, use `py aula1_pandas_dataframes/exercicio_03_qual_funcao_de_leitura/leituras.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `leituras.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`vendas.csv`, `vendas_br.csv`, `vendas.xlsx`, `vendas.json`, `loja.db`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
CSV      -> 8 linhas, 6 colunas, soma dos preços = 9160.0
CSV (;)  -> 8 linhas, 6 colunas, soma dos preços = 9160.0
Excel    -> 8 linhas, 6 colunas, soma dos preços = 9160.0
JSON     -> 8 linhas, 6 colunas, soma dos preços = 9160.0
SQL      -> 8 linhas, 6 colunas, soma dos preços = 9160.0

Depois de lido, o formato de origem deixa de importar: é tudo DataFrame.
```

## Dicas e erros comuns
- `read_excel` precisa da biblioteca **openpyxl** (`pip install openpyxl`); no Colab ela já vem instalada.
- Se os acentos saírem quebrados, teste `encoding="latin-1"`; se tudo vier em uma coluna só, o `sep` está errado.
- O arquivo `loja.db` é um banco **SQLite**: o módulo `sqlite3` já faz parte do Python.
