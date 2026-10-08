# Exercício 02 — Mãos à obra + commit: seu primeiro array

**Tipo:** prática + commit · 15 min

## Objetivo
Criar e explorar **arrays e matrizes**.

## O que fazer
1. Crie `numpy_basico.py` e importe NumPy como `np`.
2. Crie uma matriz **3x4** com os valores de 1 a 12 usando `arange` e `reshape`; mostre `shape`, `ndim` e `size`.
3. Selecione a **segunda linha**, a **última coluna** e o **bloco central** (linhas 0 a 1, colunas 1 a 2).
4. Use uma **máscara** para listar os valores **pares** e contar quantos são; commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_numpy/exercicio_02_seu_primeiro_array/numpy_basico.py
```

No Windows, se `python` não funcionar, use `py aula3_numpy/exercicio_02_seu_primeiro_array/numpy_basico.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `numpy_basico.py` em uma célula e execute com `Shift + Enter`.

## Exemplo de execução

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
shape: (3, 4) | ndim: 2 | size: 12
Segunda linha: [5 6 7 8]
Última coluna: [ 4  8 12]
Bloco central (linhas 0 a 1, colunas 1 a 2):
[[2 3]
 [6 7]]
Valores pares: [ 2  4  6  8 10 12] -> quantidade: 6
```

## Dicas e erros comuns
- `m % 2 == 0` gera a máscara dos pares: os operadores também são **vetorizados**.
- Em arrays, a fatia final é **exclusiva**, como nas listas: `m[0:2, 1:3]` pega as linhas 0 e 1 e as colunas 1 e 2.
