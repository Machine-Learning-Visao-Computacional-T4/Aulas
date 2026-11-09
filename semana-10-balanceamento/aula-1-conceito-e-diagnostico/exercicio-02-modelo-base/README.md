# Exercício 02: Divisão estratificada e modelo-base

**Tipo:** Guiado

## Objetivo
Dividir com `stratify` e criar o piso de acurácia com o DummyClassifier.

## O que fazer
1. Separe `X` (sem `id_transacao` e `fraude`) e `y`.
2. Divida em treino e teste (25%, `stratify=y`, `random_state=42`) e mostre quantas fraudes há em cada parte.
3. Repita a divisão sem `stratify` com as sementes 1, 2 e 3 e compare as fraudes no teste.
4. Treine um `DummyClassifier(strategy='most_frequent')` e imprima a acurácia e as classes previstas.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-1-conceito-e-diagnostico/exercicio-02-modelo-base/modelo_base.py
```
A solução de referência está em `modelo_base.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
(7500, 8) (2500, 8)
fraudes no treino: 139 | no teste: 46
semente 1 -> fraudes no teste sem stratify: 49
semente 2 -> fraudes no teste sem stratify: 57
semente 3 -> fraudes no teste sem stratify: 42
acurácia: 0.982
previsões distintas: [0]
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- O que significa uma acurácia de 0,982 neste conjunto?
- Qual estratégia do DummyClassifier daria a pior acurácia, e por quê?

## Dicas
- A ordem do retorno é `X_treino, X_teste, y_treino, y_teste`.
- `np.unique` confirma quais classes o modelo-base prevê.
