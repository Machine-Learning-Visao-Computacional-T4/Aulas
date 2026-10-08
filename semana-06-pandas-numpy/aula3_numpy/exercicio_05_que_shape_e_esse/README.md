# Exercício 05 — Que shape é esse?

**Tipo:** dinâmica + script · 12 min

## Objetivo
Praticar a **previsão de shapes** em operações com broadcasting.

## O que fazer
1. Para cada operação abaixo, escreva se ela **funciona** e qual é o **shape do resultado**.
2. Rode `shapes.py`, que testa cada caso com arrays de uns (`np.ones`), e confira.
3. Revise a regra: alinhe os shapes pela **direita** e compare; cada par de dimensões precisa ser **igual** ou ter um **1**.

## As 5 operações (soma de dois arrays)
1. `(4, 3)` + `(3,)`
2. `(4, 3)` + `(4,)`
3. `(4, 3)` + `(4, 1)`
4. `(3, 1)` + `(1, 4)`
5. `(2, 3, 4)` + `(4,)`

<details>
<summary>Ver respostas</summary>

1. Funciona: `(4, 3)`.
2. **Erro**: 3 e 4 não são iguais nem 1.
3. Funciona: `(4, 3)`.
4. Funciona: `(3, 4)`.
5. Funciona: `(2, 3, 4)`.

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_numpy/exercicio_05_que_shape_e_esse/shapes.py
```

No Windows, se `python` não funcionar, use `py aula3_numpy/exercicio_05_que_shape_e_esse/shapes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `shapes.py` em uma célula e execute com `Shift + Enter`.

## Exemplo de execução

```text
(4, 3) + (3,) -> funciona, shape (4, 3)
(4, 3) + (4,) -> ERRO (shapes incompatíveis)
(4, 3) + (4, 1) -> funciona, shape (4, 3)
(3, 1) + (1, 4) -> funciona, shape (3, 4)
(2, 3, 4) + (4,) -> funciona, shape (2, 3, 4)
```

## Dicas e erros comuns
- Escreva os shapes um embaixo do outro, **alinhados à direita**: o que sobra à esquerda é esticado.
- Quando der `ValueError: operands could not be broadcast together`, **imprima os shapes** dos dois operandos antes de qualquer outra investigação.
