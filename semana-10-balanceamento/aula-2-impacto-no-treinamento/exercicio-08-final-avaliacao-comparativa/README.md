# Exercício 08: Final da Aula 2: avaliação comparativa

**Tipo:** Final, com Git e Pull Request

## Objetivo
Entregar um script que compara três modelos com métricas apropriadas e validação estratificada.

## O que fazer
1. Crie a branch `feature/avaliar-modelos-desbalanceados`.
2. Crie `avaliacao.py` com `avaliar(modelo, X_teste, y_teste)`, que devolve acurácia, precision, recall, F1 e PR AUC.
3. Treine regressão logística, árvore e KNN no mesmo pré-processamento e imprima uma tabela comparativa com pandas.
4. Faça uma validação cruzada estratificada de 5 partes da regressão logística com `recall` e `average_precision`.
5. Crie `AVALIACAO.md` com uma frase por modelo explicando o que a acurácia esconde.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-2-impacto-no-treinamento/exercicio-08-final-avaliacao-comparativa/avaliacao.py
```
A solução de referência está em `avaliacao.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
           acuracia  precision  recall     f1  pr_auc
logística     0.984      0.692   0.196  0.305   0.412
árvore        0.968      0.211   0.261  0.233   0.069
KNN           0.982      1.000   0.022  0.043   0.254
recall médio: 0.27
PR AUC média: 0.476
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- O que cada modelo tem de 'bom' só na acurácia?
- Por que o desvio da validação cruzada é importante?

## Dicas
- Passe o Pipeline inteiro à validação cruzada.
- Use um dicionário de modelos para evitar código repetido.

## Git deste exercício
```bash
git checkout -b feature/avaliar-modelos-desbalanceados
git add avaliacao.py AVALIACAO.md
git commit -m "feat: avaliação comparativa"
git push -u origin feature/avaliar-modelos-desbalanceados
```
Abra o Pull Request para a `main` pelo GitHub e descreva em duas frases o que o programa faz e quais números você conferiu.
