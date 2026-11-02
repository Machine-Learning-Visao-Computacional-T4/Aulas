# Exercício 09 — Quiz relâmpago: revisão da Aula 1

Cobre as 4 partes da aula: funções em colunas, condicionais, junções e pipeline.

1. Qual a ordem de preferência entre operação vetorizada, `.str`/`.dt`, `map` e `apply`? Por quê?
2. O que `pd.Series([0, 9]).map({0: "seg"})` devolve?
3. Qual o número do dia da semana de uma segunda-feira no `.dt.dayofweek`?
4. Qual a diferença entre `np.where` e `np.select`?
5. O que acontece com `NaN` em uma comparação como `np.nan >= 4`? Que cuidado isso exige?
6. Por que `(df["qtd"] >= 2) and (df["canal"] == "App")` dá erro?
7. O que `pd.cut(t, bins=[0, 20, 30, 45, np.inf], labels=[...])` faz?
8. Qual a diferença entre `concat` e `merge`?
9. O que `validate="m:1"` garante, e por que isso importa?
10. **Preveja a saída:**
   ```python
   import pandas as pd

   print(pd.Series([3, 8]).apply(lambda x: x * 2 if x > 5 else x).tolist())
   ```
11. Por que organizar as etapas em uma função como `preparar_pedidos`?

<details>
<summary>Ver respostas</summary>

1. Vetorizada, depois `.str` e `.dt`, depois `map` e por último `apply` (e `apply(axis=1)` só se nada resolver). As primeiras são as mais rápidas e as mais legíveis.
2. `[seg, NaN]`: a chave 9 não existe no dicionário e vira `NaN` **sem aviso**. Confira com `isna()`.
3. **0** (domingo é 6).
4. O `np.where` decide entre **duas** saídas (if/else em bloco); o `np.select` aceita **várias** regras em ordem (vale a primeira verdadeira) e um `default`.
5. Dá `False`. Por isso quem tem avaliação ausente cai no `default` do `np.select`; é preciso decidir o que fazer com eles para não virarem "insatisfeito" por acidente.
6. Porque `and` pergunta se a coluna **inteira** é verdadeira, o que é ambíguo. Em Series use `&`, `|` e `~`, com cada condição entre parênteses.
7. Transforma números em categorias usando os limites (`bins`) e os nomes (`labels`): `(0, 20]`, `(20, 30]`, `(30, 45]` e `(45, inf]`.
8. `concat` **empilha** tabelas de mesma estrutura (mais linhas) ou cola lado a lado pelo índice; `merge` **liga** tabelas diferentes por uma chave comum (mais colunas).
9. Que a chave é **única** na tabela da direita (muitos pedidos para um produto). Se não for, o pandas interrompe com erro em vez de multiplicar linhas em silêncio e inflar os totais.
10. `[3, 16]`: o 3 não passa de 5 e fica como está; o 8 é dobrado.
11. O processo fica **reprodutível** (roda do zero e dá sempre o mesmo resultado), não altera as tabelas de entrada e pode ser reaproveitado pelas próximas etapas (gráficos e análise).

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
