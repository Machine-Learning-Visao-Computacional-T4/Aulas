# Exercício 06: MinMax, padronização e RobustScaler

**Tipo:** Guiado

## Objetivo
Comparar três escalas e ver como um valor extremo distorce cada uma.

## O que fazer
1. Leia `arquivos/imoveis_tratado.csv` e escolha a coluna `area_m2`.
2. Aplique `MinMaxScaler`, `StandardScaler` e `RobustScaler` e mostre média, desvio, mínimo e máximo de cada resultado.
3. Calcule a padronização à mão e confirme que bate com o `StandardScaler` (atenção ao `ddof`).
4. Aplique `inverse_transform` e confirme que volta ao valor original.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-2-outliers-e-escalas/exercicio-06-escalas/escalas.py
```
A solução de referência está em `escalas.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
MinMax   média   0.14  desvio  0.11  min   0.00  max   1.00
Standard média  -0.00  desvio  1.00  min  -1.22  max   7.69
Robust   média   0.23  desvio  0.82  min  -0.78  max   6.55
manual igual ao scikit-learn: True
inverse_transform recupera o original: True
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que o MinMax sofre mais com um valor extremo do que o RobustScaler?
- Por que o pandas e o NumPy dão desvios diferentes por padrão?

## Dicas
- `std(ddof=0)` divide por n; o padrão do pandas divide por n-1.
- O `StandardScaler` usa ddof=0.
