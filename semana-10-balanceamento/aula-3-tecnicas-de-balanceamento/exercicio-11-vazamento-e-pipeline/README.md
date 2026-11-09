# Exercício 11: Vazamento e Pipeline com reamostragem

**Tipo:** Guiado

## Objetivo
Provar que balancear antes de dividir gera um resultado ilusório.

## O que fazer
1. Caminho errado: aplique `RandomOverSampler` à base inteira, divida e avalie uma árvore. Anote o recall.
2. Caminho certo: divida primeiro e monte um `imblearn.pipeline.Pipeline` com pré-processamento, `RandomOverSampler` e a árvore.
3. Monte também um pipeline com SMOTE e regressão logística e imprima as métricas.
4. Escreva em comentário por que o primeiro recall é enganoso.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-3-tecnicas-de-balanceamento/exercicio-11-vazamento-e-pipeline/vazamento_pipeline.py
```
A solução de referência está em `vazamento_pipeline.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
recall (errado): 1.0
recall (certo): 0.13
SMOTE: precision 0.113 | recall 0.848
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que o SMOTE também causaria vazamento se aplicado antes de dividir?
- O que o imblearn Pipeline faz no `predict`?

## Dicas
- Importe o Pipeline do imblearn com um apelido para não confundir.
- O teste nunca é reamostrado.
