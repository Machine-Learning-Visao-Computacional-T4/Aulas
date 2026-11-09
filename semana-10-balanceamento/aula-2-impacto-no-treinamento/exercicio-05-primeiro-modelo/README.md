# Exercício 05: A regressão logística no conjunto desbalanceado

**Tipo:** Guiado

## Objetivo
Treinar o primeiro modelo e ler o que a acurácia esconde.

## O que fazer
1. Faça a divisão estratificada e monte o `ColumnTransformer` do projeto.
2. Treine um `Pipeline` com `LogisticRegression(max_iter=1000)`.
3. Imprima a acurácia, o `classification_report` e a matriz de confusão.
4. Escreva em comentário quantas fraudes passaram sem ser detectadas.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-2-impacto-no-treinamento/exercicio-05-primeiro-modelo/primeiro_modelo.py
```
A solução de referência está em `primeiro_modelo.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
acurácia no teste: 0.984
              precision    recall  f1-score   support

    Legítima       0.99      1.00      0.99      2454
      Fraude       0.69      0.20      0.31        46

    accuracy                           0.98      2500
   macro avg       0.84      0.60      0.65      2500
weighted avg       0.98      0.98      0.98      2500

[[2450    4]
 [  37    9]]
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que a acurácia ficou acima do modelo-base mesmo com recall tão baixo?
- O que o Pipeline garante em relação ao vazamento?

## Dicas
- Passe o Pipeline inteiro ao `fit`: o pré-processamento é aprendido só no treino.
- Olhe sempre a linha da classe Fraude no relatório.
