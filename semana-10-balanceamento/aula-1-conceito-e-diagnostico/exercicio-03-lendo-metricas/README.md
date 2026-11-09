# Exercício 03: Matriz de confusão e métricas

**Tipo:** Guiado

## Objetivo
Calcular VP, FP, FN, VN, precision, recall, F1 e o prejuízo do modelo-base.

## O que fazer
1. Treine o modelo-base e calcule a `confusion_matrix`; extraia VN, FP, FN e VP com `ravel()`.
2. Calcule precision, recall e F1 da classe Fraude com `zero_division=0`.
3. Imprima o `classification_report` com `target_names`.
4. Calcule o prejuízo com R$ 800 por fraude perdida e R$ 15 por falso alarme.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-1-conceito-e-diagnostico/exercicio-03-lendo-metricas/lendo_metricas.py
```
A solução de referência está em `lendo_metricas.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
VN 2454 FP 0 FN 46 VP 0
precision: 0.0
recall:    0.0
f1:        0.0
              precision    recall  f1-score   support

    Legítima       0.98      1.00      0.99      2454
      Fraude       0.00      0.00      0.00        46

    accuracy                           0.98      2500
   macro avg       0.49      0.50      0.50      2500
weighted avg       0.96      0.98      0.97      2500

prejuízo: R$ 36.800
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que o `macro avg` do recall é 0,50?
- Qual métrica você priorizaria para um alerta de incêndio? E para recomendar produtos?

## Dicas
- `confusion_matrix` devolve `[[VN, FP], [FN, VP]]`.
- Sem `zero_division`, o scikit-learn emite um aviso.
