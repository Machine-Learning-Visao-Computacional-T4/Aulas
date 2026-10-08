# Exercício 03 — Preveja a saída

**Tipo:** dinâmica + script · 12 min

## Objetivo
Treinar a **leitura de código vetorizado** antes de executá-lo.

## O que fazer
1. Considere a matriz de notas abaixo (4 alunos, 3 provas) e os 4 trechos. Escreva o **valor esperado** (e o **shape**) de cada um, **sem rodar**.
2. Rode `trechos.py` e compare.
3. Discuta os erros mais comuns, principalmente trocas de `axis`.

## A matriz e os 4 trechos
```python
import numpy as np

notas = np.array([[8.5, 9.0, 7.5],
                  [6.0, 7.5, 5.0],
                  [9.5, 8.0, 9.0],
                  [5.0, 6.0, 4.5]])

1) notas[:, 1].max()
2) notas.mean(axis=1).argmin()
3) (notas >= 7).sum(axis=0)
4) np.where(notas < 6, 0, 1)[0]
```

<details>
<summary>Ver respostas</summary>

1. `9.0` (a maior nota da segunda prova).
2. `3` (Diego, o aluno de índice 3, tem a menor média).
3. `[2 3 2]` (quantas notas >= 7 em cada prova, contando por coluna).
4. `[1 1 1]` (a primeira linha não tem nenhuma nota abaixo de 6).

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_numpy/exercicio_03_preveja_a_saida/trechos.py
```

No Windows, se `python` não funcionar, use `py aula3_numpy/exercicio_03_preveja_a_saida/trechos.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `trechos.py` em uma célula e execute com `Shift + Enter`.

## Exemplo de execução

```text
1) 9.0
2) 3
3) [2 3 2]
4) [1 1 1]
```

## Dicas e erros comuns
- `axis=0` produz **um valor por coluna**; `axis=1` produz **um valor por linha**. Confira sempre o **shape** do resultado.
- `argmin` e `argmax` devolvem a **posição** do menor e do maior valor, e não o valor.
