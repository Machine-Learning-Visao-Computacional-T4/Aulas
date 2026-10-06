# Exercício 05 — Preveja a saída

**Tipo:** leitura de código + conferência · 15 min

## Objetivo
Praticar a **leitura de código com loops e condicionais**, prevendo o resultado **antes** de executar.

## O que fazer
1. Leia os 4 trechos abaixo. **Não rode ainda.**
2. Escreva, ao lado de cada um, qual será a saída impressa.
3. Rode `trechos.py` (instruções no final) e compare.
4. Discuta com a turma os trechos em que houve mais divergência.

**Trecho A**
```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
```

**Trecho B**
```python
n = 0
while n < 10:
    n += 3
    if n == 6:
        break
    print(n)
```

**Trecho C**
```python
total = 0
for i in range(1, 5):
    if i == 3:
        continue
    total += i
print(total)
```

**Trecho D**
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

## Como executar
```bash
python aula3_condicionais_loops/exercicio_05_preveja_a_saida/trechos.py
```
(No Windows, use `py` no lugar de `python`.) No Colab, cole o conteúdo de `trechos.py` numa célula.

<details>
<summary>Ver respostas</summary>

- **A:** `1`, `3`, `5` (o `continue` pula os pares).
- **B:** só `3`. Quando `n` chega a 6, o `break` encerra o loop **antes** do `print`.
- **C:** `7` (1 + 2 + 4; o 3 foi pulado).
- **D:** seis linhas: `0 0`, `0 1`, `1 0`, `1 1`, `2 0`, `2 1`.

</details>

> Os 4 trechos foram preparados para este repositório; os da aula podem ser outros.
