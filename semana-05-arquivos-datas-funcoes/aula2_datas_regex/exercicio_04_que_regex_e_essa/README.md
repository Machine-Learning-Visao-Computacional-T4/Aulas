# Exercício 04 — Que regex é essa?

**Tipo:** leitura de padrões antes de escrevê-los · 12 min

## Objetivo
Praticar a **leitura de padrões de regex** (expressões regulares).

## Os 4 padrões
1. `\d{2}/\d{2}/\d{4}`
2. `[A-Z]{3}-\d{4}`
3. `\w+@\w+\.com`
4. `^\s+|\s+$`

## O que fazer
1. Para cada padrão, escreva **em português** o que ele reconhece e **um exemplo de texto que casa**.
2. Confira as respostas abaixo e discuta os padrões com maior divergência.
3. Feche escrevendo **um exemplo de texto que NÃO casa** com cada padrão.
4. Rode `testar_padroes.py` para ver os padrões funcionando (instruções no final).

<details>
<summary>Ver respostas</summary>

1. Uma **data no formato dd/mm/aaaa** (2 dígitos, barra, 2 dígitos, barra, 4 dígitos). Casa: `25/12/2025`.
2. Uma **placa no formato antigo**: 3 letras maiúsculas, hífen e 4 dígitos. Casa: `ABC-1234`.
3. Um **e-mail simples terminado em `.com`**. Casa: `ana@exemplo.com`.
4. **Espaços no início ou no fim** do texto. Casa: `"  oi  "`.

</details>

## Como executar o teste
```bash
python aula2_datas_regex/exercicio_04_que_regex_e_essa/testar_padroes.py
```
(No Windows, use `py`.)

## Exemplo de execução
```text
Padrão: \d{2}/\d{2}/\d{4}
   casa com '25/12/2025' -> True
   fullmatch em '25-12-2025' -> False
Padrão: [A-Z]{3}-\d{4}
   casa com 'ABC-1234' -> True
   fullmatch em 'abc-1234' -> False
Padrão: \w+@\w+\.com
   casa com 'ana@exemplo.com' -> True
   fullmatch em 'ana@exemplo.com.br' -> False
Padrão: ^\s+|\s+$
   casa com '  texto com espaços  ' -> True
   fullmatch em 'texto sem espaços nas pontas' -> False
```

## Para pensar
- No padrão 3, `ana@exemplo.com.br` casa por inteiro? (Veja a linha `fullmatch` do script.)
- Por que o padrão 4 usa `^` e `$`?
