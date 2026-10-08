# Exercício 08 — Quiz relâmpago: revisão da Aula 2

Cobre limpeza, `groupby`, `merge` e `pivot`.

1. O que `df.isna().sum()` mostra?
2. Por que é preciso **atribuir** o resultado de `fillna` de volta à coluna?
3. Quais são as três etapas do `groupby`?
4. Para que serve `reset_index()` depois de um `groupby`?
5. Qual a diferença entre `how="inner"` e `how="left"`?
6. Duas linhas com a chave 1 de um lado e duas linhas com a chave 1 do outro: quantas linhas o `merge` devolve?
7. Quando o `pivot` dá erro e o `pivot_table` não?
8. O que `melt` faz?
9. **Preveja a saída:**
   ```python
   import pandas as pd

   df = pd.DataFrame({"g": ["a", "b", "a"], "v": [1, 2, 3]})
   print(df.groupby("g")["v"].sum().to_dict())
   ```
10. O que `errors="coerce"` faz em `pd.to_numeric`?

<details>
<summary>Ver respostas</summary>

1. A **quantidade de valores ausentes em cada coluna**.
2. Porque `fillna` **devolve** uma nova Series e não altera a original. Sem atribuir, nada muda no DataFrame.
3. **Dividir** (split) em grupos, **aplicar** uma função (apply) e **combinar** os resultados (combine).
4. Transforma os rótulos do índice (as chaves do grupo) de volta em **colunas comuns**.
5. `inner` mantém só as linhas com correspondência **nas duas** tabelas; `left` mantém **todas as linhas da esquerda**, mesmo sem correspondência.
6. **4** linhas (2 x 2): chaves repetidas multiplicam linhas.
7. Quando alguma combinação de linha e coluna **aparece mais de uma vez**: o `pivot` não sabe agregar, enquanto o `pivot_table` usa `aggfunc`.
8. Converte colunas largas em **formato longo**: as colunas viram linhas (uma coluna de nome e uma de valor).
9. `{'a': 4, 'b': 2}`.
10. Transforma o que **não é número** em `NaN`, em vez de dar erro.

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
