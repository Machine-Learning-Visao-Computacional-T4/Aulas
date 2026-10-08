# Semana 06 — Pandas e NumPy: análise de dados em Python

Material de prática da **Semana 06** do curso *Machine Learning e Visão Computacional* (Turma T4, SC TEC / SENAI). Você passa das listas e dicionários para **tabelas e matrizes de verdade**: carregar dados de várias fontes, limpar, resumir, cruzar tabelas e fazer contas em bloco, sem laços.

Nos slides, esta semana aparece como **Semana 06 — Análise de dados** (pandas e NumPy).

## Aulas e exercícios

| Aula | Tema | Pasta |
| --- | --- | --- |
| 1 | Pandas essencial I: Series, DataFrames, leitura de fontes, seleções e filtros | [aula1_pandas_dataframes](aula1_pandas_dataframes/) |
| 2 | Pandas essencial II: limpeza, `groupby`, `merge` e `pivot` | [aula2_pandas_groupby_merge](aula2_pandas_groupby_merge/) |
| 3 | NumPy: arrays, operações vetorizadas e broadcasting | [aula3_numpy](aula3_numpy/) |

Resumos teóricos em [`docs/guia_pandas.md`](docs/guia_pandas.md) e [`docs/guia_numpy.md`](docs/guia_numpy.md).

## O fio condutor: da tabela ao modelo
Os exercícios finais de cada aula formam uma sequência:
1. **Aula 1:** ler um CSV, filtrar e gerar um relatório ([mini-relatório](aula1_pandas_dataframes/exercicio_06_exercicio_final_mini_relatorio/)).
2. **Aula 2:** limpar, juntar e resumir tabelas ([análise de vendas por cliente](aula2_pandas_groupby_merge/exercicio_07_exercicio_final_analise_de_vendas/)).
3. **Aula 3:** juntar pandas e NumPy em uma única análise ([análise de provas](aula3_numpy/exercicio_07_exercicio_final_analise_de_provas/)).

Tudo o que você preparou (dados limpos, organizados e numéricos) é exatamente o que um modelo de Machine Learning recebe nas próximas semanas.

## Como executar
Esta semana usa bibliotecas externas: **pandas**, **NumPy** e **openpyxl** (para Excel). Instale com:

```bash
git clone https://github.com/Machine-Learning-Visao-Computacional-T4/semana-06-pandas-numpy.git
cd semana-06-pandas-numpy
pip install -r requirements.txt
python aula2_pandas_groupby_merge/exercicio_07_exercicio_final_analise_de_vendas/analise.py
```

No Windows, se `python` ou `pip` não funcionarem, use `py` e `py -m pip`.

Os scripts procuram os arquivos de dados **na mesma pasta do próprio script**, então você pode rodá-los de qualquer lugar. Cada exercício que grava arquivos (`resumo_categorias.csv`, `resultado_provas.csv`...) cria o resultado ao lado do script.

No **Google Colab** o pandas, o NumPy e o openpyxl já vêm instalados: envie os arquivos de dados da pasta do exercício (veja o [guia](docs/guia_pandas.md#no-google-colab)) e cole o script em uma célula.

## Como estudar
1. Leia o `README.md` do exercício.
2. **Tente sozinho**, com seus próprios dados fictícios.
3. Compare com a solução de exemplo.
4. Faça commit e push no **seu** repositório. Use **somente dados fictícios**.

## Observação
Os exemplos foram testados com **pandas 3** e **NumPy 2**. Em versões anteriores (como as do Google Colab), a saída pode ter pequenas diferenças, por exemplo o tipo de colunas de texto aparecer como `object` em vez de `str`. As perguntas dos quizzes foram preparadas para este repositório e podem diferir das usadas na aula ao vivo. Os tempos do exercício "Quem soma mais rápido?" mudam de computador para computador.
