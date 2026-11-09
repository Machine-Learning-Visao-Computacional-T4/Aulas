# Exercício 10: Under, over e SMOTE

**Tipo:** Guiado

## Objetivo
Aplicar as três reamostragens do imbalanced-learn e conferir as contagens.

## O que fazer
1. Instale a biblioteca (`pip install imbalanced-learn`) e importe `RandomUnderSampler`, `RandomOverSampler` e `SMOTE`.
2. Pré-processe o treino e aplique cada técnica com `fit_resample`, imprimindo as contagens antes e depois.
3. Teste `sampling_strategy` com 0.1, 0.5 e um dicionário no undersampling.
4. Conte as linhas distintas entre as fraudes depois do oversampling e do SMOTE com `np.unique`.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-3-tecnicas-de-balanceamento/exercicio-10-reamostragem/reamostragem.py
```
A solução de referência está em `reamostragem.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
antes:  {0: 7361, 1: 139}
undersampling: {0: 139, 1: 139} (7500, 10) -> (278, 10)
auto               -> {0: 139, 1: 139}
0.1                -> {0: 1390, 1: 139}
0.5                -> {0: 278, 1: 139}
{0: 600, 1: 139}   -> {0: 600, 1: 139}
oversampling: {0: 7361, 1: 7361} | fraudes distintas: 139
SMOTE: {0: 7361, 1: 7361} | fraudes distintas: 7361
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que o oversampling simples favorece o sobreajuste?
- Quando o undersampling seria uma péssima escolha?

## Dicas
- O nome do pacote é `imblearn`, mas a instalação é `imbalanced-learn`.
- `fit_resample` devolve novos X e y.
