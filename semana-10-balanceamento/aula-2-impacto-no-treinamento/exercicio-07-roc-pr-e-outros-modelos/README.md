# Exercício 07: ROC, PR e outros modelos

**Tipo:** Guiado

## Objetivo
Comparar modelos com as métricas certas e ver o sobreajuste da árvore.

## O que fazer
1. Treine uma árvore (`DecisionTreeClassifier(random_state=42)`) e um KNN (`n_neighbors=15`) no mesmo Pipeline de pré-processamento.
2. Mostre o recall da árvore no treino e no teste.
3. Mostre o recall e o número de alertas do KNN.
4. Calcule `roc_auc_score` e `average_precision_score` da regressão logística e compare com a proporção de fraudes.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-2-impacto-no-treinamento/exercicio-07-roc-pr-e-outros-modelos/outros_modelos.py
```
A solução de referência está em `outros_modelos.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
árvore, recall no treino: 1.0
árvore, recall no teste:  0.26
KNN, recall: 0.02 | alertas: 1
ROC AUC: 0.928
PR AUC:  0.412 | aleatório: 0.018
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que a ROC AUC parece tão boa e a PR AUC não?
- Por que o KNN quase não alerta?

## Dicas
- O sobreajuste aparece quando o desempenho no treino é muito maior que no teste.
- A PR AUC de um modelo aleatório é a proporção da classe rara.
