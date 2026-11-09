# Exercício 09: Class_weight na regressão logística

**Tipo:** Guiado

## Objetivo
Comparar o modelo sem e com pesos de classe.

## O que fazer
1. Calcule os pesos com `compute_class_weight('balanced', ...)` e confira a conta manual.
2. Treine a regressão logística sem peso e com `class_weight='balanced'`.
3. Teste também `class_weight={0: 1, 1: 10}`.
4. Imprima uma tabela com precision, recall, F1 e PR AUC das três configurações.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-3-tecnicas-de-balanceamento/exercicio-09-class-weight/class_weight.py
```
A solução de referência está em `class_weight.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
[ 0.51 26.98]
manual: 0.51 26.98
           precision  recall     f1  pr_auc
sem peso       0.692   0.196  0.305   0.412
balanced       0.110   0.848  0.194   0.434
peso 1:10      0.302   0.565  0.394   0.416
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que a PR AUC quase não muda com o class_weight?
- Como escolher entre 'balanced' e 1:10?

## Dicas
- O peso 'balanced' é n_linhas / (n_classes × linhas da classe).
- O dicionário de pesos permite doses intermediárias.
