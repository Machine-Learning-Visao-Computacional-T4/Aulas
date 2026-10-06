# Exercício 08 — Quiz relâmpago: revisão do módulo de Python

Cobre as 3 aulas (variáveis e tipos, operadores e lógica, condicionais e loops). Responda sem rodar o código; depois confira.

1. Qual o tipo de `input()`, mesmo que a pessoa digite `42`?
2. O que `17 // 5` e `17 % 5` retornam?
3. Qual a diferença entre `=` e `==`?
4. Qual o resultado de `True and False or True`?
5. Quando usar `while` em vez de `for`?
6. O que `range(1, 6)` gera?
7. Para que serve o `break`? E o `continue`?
8. **Preveja a saída:**
   ```python
   for i in range(3):
       print(i * 2)
   ```
9. **Preveja a saída:**
   ```python
   x = 10
   if x > 5 and x < 8:
       print("A")
   elif x > 5:
       print("B")
   else:
       print("C")
   ```
10. Por que o teste do número 15 vem primeiro no FizzBuzz?

<details>
<summary>Ver respostas</summary>

1. `str` (texto).
2. `3` e `2`.
3. `=` atribui um valor; `==` compara.
4. `True` (o `and` é avaliado antes: `False`; depois `False or True` é `True`).
5. Quando não se sabe antecipadamente quantas repetições serão necessárias (ex.: pedir a senha até acertar).
6. `1, 2, 3, 4, 5`.
7. `break` encerra o loop; `continue` pula para a próxima repetição.
8. `0`, `2`, `4`.
9. `B`.
10. Porque 15 é múltiplo de 3 **e** de 5; se testasse 3 antes, nunca chegaria no "FizzBuzz".

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
