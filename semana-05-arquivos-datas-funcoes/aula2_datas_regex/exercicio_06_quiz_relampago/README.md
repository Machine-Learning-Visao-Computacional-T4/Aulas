# Exercício 06 — Quiz relâmpago: datetime e regex

1. O que `strptime` faz?
2. E o `strftime`? Qual a diferença entre os dois?
3. O que `\d+` casa?
4. Qual a diferença entre `\d` e `\D`?
5. Qual formato de data **ordena corretamente como texto**?
6. Qual a diferença entre `re.search` e `re.fullmatch`?
7. **Preveja a saída:** `re.sub(r"\D", "", "(48) 9-1234")`
8. Por que `%Y` e `%y` não são iguais?

<details>
<summary>Ver respostas</summary>

1. Converte **texto em data** (`str` → `datetime`), usando um formato.
2. `strftime` faz o caminho contrário: **data em texto**, no formato que você escolher. *p*arse (`strp`) lê; *f*ormat (`strf`) escreve.
3. Um ou mais dígitos seguidos (`42`, `2025`...).
4. `\d` casa **um dígito**; `\D` casa **qualquer coisa que não seja dígito**.
5. **AAAA-MM-DD** (ano-mês-dia).
6. `search` procura o padrão **em qualquer parte** do texto; `fullmatch` exige que o texto **inteiro** case.
7. `'4891234'` (a regex remove tudo que não é dígito).
8. `%Y` é o ano com 4 dígitos (2025); `%y` com 2 dígitos (25).

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
