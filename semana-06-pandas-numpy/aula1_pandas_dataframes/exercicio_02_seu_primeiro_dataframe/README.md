# Exercício 02 — Mãos à obra + commit: seu primeiro DataFrame

**Tipo:** prática + commit · 15 min

## Objetivo
Construir **Series** e **DataFrames** do zero e explorar suas partes.

## O que fazer
1. Crie `pandas_basico.py` e importe pandas como `pd`.
2. Crie uma **Series** com as notas de 4 colegas fictícios e calcule a **média** e **quem tem a maior nota**.
3. Crie um **DataFrame** de 5 filmes (`titulo`, `ano`, `nota`) a partir de um **dicionário de listas**.
4. Imprima **uma coluna** e depois **duas colunas**; mostre o **dtype** de cada coluna; faça commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_pandas_dataframes/exercicio_02_seu_primeiro_dataframe/pandas_basico.py
```

No Windows, se `python` não funcionar, use `py aula1_pandas_dataframes/exercicio_02_seu_primeiro_dataframe/pandas_basico.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `pandas_basico.py` em uma célula e execute com `Shift + Enter`.

## Exemplo de execução

```text
Notas dos colegas:
Ana      8.5
Bruno    6.0
Carla    9.5
Diego    7.0
dtype: float64
Média da turma: 7.75
Maior nota: Carla com 9.5

Tabela de filmes:
                  titulo   ano  nota
0         Cidade de Deus  2002   9.0
1      Central do Brasil  1998   8.5
2  O Auto da Compadecida  2000   9.5
3         Tropa de Elite  2007   8.0
4       Ainda Estou Aqui  2024   8.8

Uma coluna:
0           Cidade de Deus
1        Central do Brasil
2    O Auto da Compadecida
3           Tropa de Elite
4         Ainda Estou Aqui
Name: titulo, dtype: str

Duas colunas:
                  titulo  nota
0         Cidade de Deus   9.0
1      Central do Brasil   8.5
2  O Auto da Compadecida   9.5
3         Tropa de Elite   8.0
4       Ainda Estou Aqui   8.8

Tipos das colunas:
titulo        str
ano         int64
nota      float64
dtype: object
```

## Dicas e erros comuns
- `filmes["titulo"]` (colchetes simples) devolve uma **Series**; `filmes[["titulo", "nota"]]` (colchetes duplos) devolve um **DataFrame**.
- Em versões mais novas do pandas, a coluna de texto aparece com o tipo `str`; em versões anteriores (e no Colab), como `object`. É só diferença de versão.
- Extra: adicione uma coluna `decada` calculada a partir de `ano` (`filmes["ano"] // 10 * 10`).
