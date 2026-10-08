# Exercício 02 — Mãos à obra + commit: faxina com pandas

**Tipo:** prática + commit · 18 min

## Objetivo
Refazer a faxina da Semana 05 **com pandas** e comparar o tamanho do código.

## O que fazer
1. Crie `faxina_pandas.py`: leia `contatos_sujos.csv`, **preencha a nota ausente com a média** e **remova as duplicatas**.
2. Padronize **nome** (Title Case, sem espaços extras), **telefone** (só dígitos) e **data** (`to_datetime`).
3. Grave o resultado em `contatos_limpos.csv` com `index=False`.
4. Compare, em um comentário, o número de linhas do código novo com o `faxina.py` da Semana 05. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_pandas_groupby_merge/exercicio_02_faxina_com_pandas/faxina_pandas.py
```

No Windows, se `python` não funcionar, use `py aula2_pandas_groupby_merge/exercicio_02_faxina_com_pandas/faxina_pandas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `faxina_pandas.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`contatos_sujos.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
Média usada para preencher a nota ausente: 8.25
           nome     telefone data_cadastro  nota
0     Ana Souza  48999991234    2025-03-05  8.50
1    Bruno Lima  48988885678    2025-03-18  8.25
2  Carla Mendes  48977770000    2025-04-02  9.00
4   Diego Alves  48966661111    2025-04-10  6.50
Arquivo contatos_limpos.csv gravado.
```

## Dicas e erros comuns
- `fillna` **devolve** uma nova Series: é preciso atribuir de volta (`df["nota"] = df["nota"].fillna(...)`).
- A ordem importa: preenchendo a nota **antes** de remover a duplicata, a média é 8.25; **depois**, é 8.0. Qual é mais correta? Pense: a duplicata é um dado real ou um erro?
- `str.replace` precisa de `regex=True` para entender padrões como `\D` e `\s+`.
