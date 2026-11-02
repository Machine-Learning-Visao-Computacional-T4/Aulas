# Exercício 03: Preencher ausentes com critério

**Tipo:** Guiado

## Objetivo
Preencher ausentes numéricos com a mediana do grupo e categóricos com a moda, guardando um indicador.

## O que fazer
1. Leia o arquivo bruto, trate os ausentes disfarçados e remova as duplicatas (como no exercício anterior).
2. Crie a coluna `idade_ausente` antes de preencher `idade_anos`.
3. Preencha `area_m2` e `idade_anos` com a mediana por `tipo`, usando `groupby` e `transform`.
4. Preencha `condicao` com a moda e confira que não restam ausentes nessas colunas.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-1-ausentes-e-duplicatas/exercicio-03-preencher-ausentes/preencher_ausentes.py
```
A solução de referência está em `preencher_ausentes.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
area_m2       0
idade_anos    0
condicao      0
dtype: int64
com idade ausente: 67
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que criar `idade_ausente` antes de preencher e não depois?
- Em que situação a média seria melhor que a mediana? E pior?

## Dicas
- `df.groupby('tipo')[col].transform('median')` devolve uma Series do mesmo tamanho de `df`.
- `mode()` devolve uma Series: pegue o primeiro valor com `[0]`.
