# Semana 10: Balanceamento de dados

Curso de Machine Learning e Visão Computacional, Turma T4. Dados 100% fictícios (transações do app PagaFácil), sem dados pessoais.

## Como usar
```bash
pip install -r requirements.txt
python aula-1-conceito-e-diagnostico/exercicio-01-diagnostico-de-classes/diagnostico_classes.py
```
Execute sempre os scripts **na raiz** desta pasta, para o caminho `arquivos/...` funcionar. No Colab, instale a biblioteca extra com `!pip install imbalanced-learn`.

## Fio condutor
`transacoes.csv` (10.000 linhas, 185 fraudes = 1,85%) → Aula 1 diagnostica → Aula 2 mostra o impacto no treino → Aula 3 aplica e compara técnicas.

## Exercícios

### Aula 1: Conceito e diagnóstico
- [Diagnóstico de classes](aula-1-conceito-e-diagnostico/exercicio-01-diagnostico-de-classes/README.md) (Guiado)
- [Divisão estratificada e modelo-base](aula-1-conceito-e-diagnostico/exercicio-02-modelo-base/README.md) (Guiado)
- [Matriz de confusão e métricas](aula-1-conceito-e-diagnostico/exercicio-03-lendo-metricas/README.md) (Guiado)
- [Final da Aula 1: função diagnosticar](aula-1-conceito-e-diagnostico/exercicio-04-final-funcao-diagnosticar/README.md) (Final, com Git e Pull Request)

### Aula 2: Impacto no treinamento
- [A regressão logística no conjunto desbalanceado](aula-2-impacto-no-treinamento/exercicio-05-primeiro-modelo/README.md) (Guiado)
- [Probabilidades e limiar de decisão](aula-2-impacto-no-treinamento/exercicio-06-probabilidade-e-limiar/README.md) (Guiado)
- [ROC, PR e outros modelos](aula-2-impacto-no-treinamento/exercicio-07-roc-pr-e-outros-modelos/README.md) (Guiado)
- [Final da Aula 2: avaliação comparativa](aula-2-impacto-no-treinamento/exercicio-08-final-avaliacao-comparativa/README.md) (Final, com Git e Pull Request)

### Aula 3: Técnicas de balanceamento
- [Class_weight na regressão logística](aula-3-tecnicas-de-balanceamento/exercicio-09-class-weight/README.md) (Guiado)
- [Under, over e SMOTE](aula-3-tecnicas-de-balanceamento/exercicio-10-reamostragem/README.md) (Guiado)
- [Vazamento e Pipeline com reamostragem](aula-3-tecnicas-de-balanceamento/exercicio-11-vazamento-e-pipeline/README.md) (Guiado)
- [Final da semana: comparando técnicas](aula-3-tecnicas-de-balanceamento/exercicio-12-final-comparando-tecnicas/README.md) (Final, com Git e Pull Request)

## Regras de ouro da semana
1. Meça o desbalanceamento antes de modelar.
2. Nunca confie só na acurácia: olhe precision, recall, F1 e PR AUC da classe rara.
3. Divida com `stratify` antes de qualquer reamostragem.
4. Balancear só o treino, dentro de um `imblearn.pipeline.Pipeline`.
5. Escolha a técnica e o limiar pelo custo de cada tipo de erro.
