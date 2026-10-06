# Exercício 03 — Calcule a partir da matriz de confusão

**Tipo:** cálculo + script

## Objetivo
Calcular **acurácia, precisão, recall e F1-score** a partir de uma matriz de confusão concreta e decidir se o modelo serve para cada cenário.

## Dados da matriz
| | Previsto: positivo | Previsto: negativo |
| --- | --- | --- |
| **Real: positivo** | VP = 40 | FN = 5 |
| **Real: negativo** | FP = 10 | VN = 945 |

## Fórmulas
- Acurácia = (VP + VN) / total
- Precisão = VP / (VP + FP)
- Recall = VP / (VP + FN)
- F1 = 2 × precisão × recall / (precisão + recall)

## Passo a passo
1. **Calcule à mão** (ou na calculadora) as quatro métricas.
2. Rode o script para conferir:
   ```bash
   python aula2_features_metricas/exercicio_03_matriz_de_confusao/metricas.py
   ```
3. Troque os números no topo do script (`VP`, `FP`, `FN`, `VN`) e veja como as métricas mudam.
4. Responda: **esse modelo seria bom para detectar fraude? E para triagem médica? Por quê?**

## Resultado esperado (para os números acima)
Acurácia = 98,5% · Precisão = 80,0% · Recall ≈ 88,9% · F1 ≈ 84,2%.

## Para pensar
A acurácia está altíssima, mas o modelo deixa passar 5 casos positivos e dá 10 alarmes falsos. Qual desses dois erros custa mais em fraude? E em triagem médica?
