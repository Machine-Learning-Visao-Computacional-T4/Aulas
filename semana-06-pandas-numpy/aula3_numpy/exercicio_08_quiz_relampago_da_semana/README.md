# Exercício 08 — Quiz relâmpago: revisão da Semana 06

Cobre as 3 aulas da semana (DataFrames e filtros; `groupby`, `merge` e `pivot`; arrays, vetorização e broadcasting).

1. Qual a diferença entre `[1, 2] * 2` e `np.array([1, 2]) * 2`?
2. Qual o shape de `notas.mean(axis=0)` quando `notas` tem shape `(4, 3)`?
3. O que é **broadcasting**?
4. A soma de arrays com shapes `(4, 3)` e `(4,)` funciona? Por quê?
5. Para que serve `np.newaxis`?
6. Por que `np.array([250], dtype=np.uint8) + 10` não dá 260?
7. O que faz `np.where(condição, a, b)`?
8. Qual a diferença entre `max()` e `argmax()`?
9. **Preveja a saída:**
   ```python
   import numpy as np

   print(np.arange(6).reshape(2, 3).sum(axis=1))
   ```
10. Em uma análise com pandas e NumPy, qual biblioteca você usa para **ler o CSV** e qual para a **conta em bloco** sobre a matriz de notas?

<details>
<summary>Ver respostas</summary>

1. Na lista, `*` **repete** a lista (`[1, 2, 1, 2]`); no array, `*` **multiplica cada elemento** (`[2 4]`).
2. `(3,)`: `axis=0` elimina o 4 e deixa um valor por coluna.
3. O conjunto de regras que permite ao NumPy operar arrays de **formatos diferentes**, "esticando" o menor para combinar com o maior.
4. **Não.** Alinhados pela direita, comparam-se 3 e 4, que não são iguais nem 1: `ValueError`.
5. Insere uma **dimensão de tamanho 1**, por exemplo transformando `(4,)` em `(4, 1)` para o broadcasting funcionar por linha.
6. O tipo `uint8` guarda só de 0 a 255: o resultado "dá a volta" e vira **4** (260 - 256), sem aviso. É o estouro de valor.
7. É um **if/else vetorizado**: devolve `a` onde a condição é verdadeira e `b` onde é falsa.
8. `max()` devolve o **maior valor**; `argmax()` devolve a **posição** desse valor.
9. `[ 3 12]` (soma de cada linha: 0+1+2 e 3+4+5).
10. **pandas** para ler e organizar a tabela (`read_csv`); **NumPy** para a conta em bloco (`to_numpy` e operações vetorizadas).

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
