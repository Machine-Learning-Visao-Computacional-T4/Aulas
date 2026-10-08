# Exercício 06 — Exercício final: mini-relatório

**Tipo:** projeto integrador · 20 min · branch + Pull Request

## Objetivo
Consolidar a aula criando um **relatório com pandas** e entregando via **branch e Pull Request**.

## O que fazer
1. Crie a branch `feature/mini-relatorio-pandas` no seu repositório.
2. Escreva `relatorio.py`: leia `vendas.csv`, crie a coluna `total`, filtre as vendas **acima da média de `total`** e grave em `maiores_que_a_media.csv`.
3. Imprima **quantas linhas** passaram no filtro e a **categoria mais frequente** (`value_counts`).
4. Commit, push da branch e **Pull Request** para a `main`, descrevendo o que o código faz.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_pandas_dataframes/exercicio_06_exercicio_final_mini_relatorio/relatorio.py
```

No Windows, se `python` não funcionar, use `py aula1_pandas_dataframes/exercicio_06_exercicio_final_mini_relatorio/relatorio.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `relatorio.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`vendas.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
Média do total: 1807.50
2 vendas acima da média gravadas em maiores_que_a_media.csv
Categoria mais frequente: Periféricos
```

## Dicas e erros comuns
- A média de uma coluna é `df["total"].mean()` e pode ser usada direto dentro do filtro.
- `value_counts().idxmax()` devolve o valor mais frequente de uma coluna.

## Git deste exercício
```bash
git switch -c feature/mini-relatorio-pandas
git add relatorio.py vendas.csv
git commit -m "Adiciona mini-relatório de vendas com pandas"
git push -u origin feature/mini-relatorio-pandas
```
Depois, no GitHub: **Compare & pull request** → descreva o que o programa faz → **Create pull request**.
