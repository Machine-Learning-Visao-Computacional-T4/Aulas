# Exercício 03 — Ache o bug

**Tipo:** leitura de código · 12 min

## Objetivo
Praticar a leitura de funções e **identificar os erros mais comuns**.

## O que fazer
Cada trecho abaixo tem **um erro**. Escreva qual é o erro e como você corrigiria. **Só depois** rode e veja a mensagem.

**Trecho 1**
```python
def dobro(n):
    print(n * 2)

resultado = dobro(5)
print("resultado =", resultado)
```

**Trecho 2**
```python
def somar(a, b)
    return a + b
```

**Trecho 3**
```python
print(saudacao("Ana"))

def saudacao(nome):
    return "Olá, " + nome
```

<details>
<summary>Ver respostas</summary>

1. **`print` em vez de `return`.** A função mostra o valor na tela, mas **devolve `None`**. Saída real:
   ```text
   10
   resultado = None
   ```
   É o erro mais difícil de perceber, porque **não gera erro**: o programa roda, só que com `None` no lugar do valor. Correção: `return n * 2`.
2. **Faltam os dois-pontos** depois do `def`. Mensagem: `SyntaxError: expected ':'`. Correção: `def somar(a, b):`.
3. **Chamada antes da definição.** O Python lê de cima para baixo, então a função ainda não existe. Mensagem: `NameError: name 'saudacao' is not defined`. Correção: definir a função **antes** de usá-la.

</details>

As versões corrigidas estão em [`bugs_corrigidos.py`](bugs_corrigidos.py).

## Como executar as versões corrigidas
```bash
python aula3_funcoes_modulos/exercicio_03_ache_o_bug/bugs_corrigidos.py
```
(No Windows, use `py`.)

## Para pensar
Qual dos três é o mais difícil de perceber? Por quê?

> Os trechos acima foram preparados para este repositório, seguindo os três tipos de erro do exercício.
