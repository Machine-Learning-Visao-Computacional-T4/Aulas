# Exercício 06 — Quiz relâmpago de encerramento

Responda **sem rodar o código**, depois confira.

1. Qual o tipo de retorno de `input()`, mesmo se a pessoa digitar só números?
2. Esse nome de variável é válido: `2_nota`?
3. O que `type(3.14)` retorna?
4. V ou F: em Python, `10 / 2` retorna `5` (inteiro).
5. Qual função transforma o texto `"25"` no número inteiro `25`?
6. O que acontece se você digitar `idade = 18` com um único `=` dentro de uma comparação?
7. Por que uma linha começando com `#` não gera erro, mesmo com texto livre depois dela?
8. Qual erro o Python mostra se você tentar usar uma variável que ainda não foi criada?

<details>
<summary>Ver respostas</summary>

1. Sempre `str` (texto).
2. Não. Nomes de variáveis não podem começar com número.
3. `<class 'float'>`.
4. **Falso.** A divisão com `/` sempre devolve `float`: `10 / 2` é `5.0`.
5. `int("25")`.
6. Um único `=` é **atribuição**, não comparação. O Python mostra um erro (a comparação deve usar `==`).
7. Porque `#` marca um **comentário**: o Python ignora o resto da linha.
8. `NameError`.

</details>
