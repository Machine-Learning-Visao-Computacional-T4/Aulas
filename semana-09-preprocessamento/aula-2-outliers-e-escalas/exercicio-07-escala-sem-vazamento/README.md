# Exercício 07: Dividir antes de escalar

**Tipo:** Guiado

## Objetivo
Provar com números que ajustar a escala com todos os dados contamina o teste.

## O que fazer
1. Leia `arquivos/imoveis_tratado.csv` e separe treino e teste (80/20, `random_state=42`).
2. Ajuste um `StandardScaler` com a base inteira e outro só com o treino. Compare as médias de `area_m2`.
3. Aplique `transform` (nunca `fit_transform`) ao teste.
4. Mostre a média da área escalada no treino e no teste e explique a diferença.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-2-outliers-e-escalas/exercicio-07-escala-sem-vazamento/escala_sem_vazamento.py
```
A solução de referência está em `escala_sem_vazamento.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
média com tudo:    [104.28]
média só no treino: [105.38]
média no teste:    99.92
treino escalado: 0.0 | teste escalado: -0.08
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que a média do teste escalado não precisa ser zero?
- O que seria 'vazar' neste exemplo?

## Dicas
- `fit` aprende (média e desvio); `transform` aplica.
- O teste simula dados que ainda não existem.
