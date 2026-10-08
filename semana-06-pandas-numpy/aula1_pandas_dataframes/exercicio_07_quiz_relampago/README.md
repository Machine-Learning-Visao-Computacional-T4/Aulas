# Exercício 07 — Quiz relâmpago: revisão da Aula 1

Cobre Series, DataFrames, leitura de fontes, seleções e filtros.

1. O que `df["a"]` devolve? E `df[["a", "b"]]`?
2. Qual a diferença entre `loc` e `iloc`?
3. Qual função lê uma planilha Excel? Qual parâmetro escolhe a aba?
4. Para que serve `index=False` ao gravar com `to_csv`?
5. O que está errado em `df[df["a"] > 1 and df["b"] < 5]`?
6. O que o método `isin` faz?
7. Qual método mostra as primeiras linhas de um DataFrame? E qual mostra o número de linhas e colunas?
8. O que `value_counts()` devolve?
9. **Preveja a saída:**
   ```python
   import pandas as pd

   s = pd.Series([1, 2, 3], index=["a", "b", "c"])
   print(s["b"], s.sum(), s[s > 1].tolist())
   ```
10. Em um DataFrame com índice 0, 1, 2, 3, 4 e 5, quantas linhas devolvem `df.loc[2:4]` e `df.iloc[2:4]`?

<details>
<summary>Ver respostas</summary>

1. `df["a"]` devolve uma **Series** (uma coluna); `df[["a", "b"]]` devolve um **DataFrame** com as duas colunas.
2. `loc` seleciona por **rótulos** e **inclui** o último da fatia; `iloc` seleciona por **posições** e **exclui** o último.
3. `pd.read_excel`; o parâmetro `sheet_name`.
4. Evita gravar no arquivo uma coluna extra com o **índice** (0, 1, 2...).
5. O `and` não funciona com colunas inteiras. O correto é `df[(df["a"] > 1) & (df["b"] < 5)]`, com **parênteses** e **`&`**.
6. Devolve uma máscara `True/False` indicando se cada valor **está em uma lista** de valores.
7. `head()` mostra as primeiras linhas; `shape` devolve `(linhas, colunas)`.
8. Quantas vezes cada valor aparece, do **mais frequente** para o menos frequente.
9. `2 6 [2, 3]`.
10. `df.loc[2:4]` devolve **3** linhas (2, 3 e 4); `df.iloc[2:4]` devolve **2** linhas (2 e 3).

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
