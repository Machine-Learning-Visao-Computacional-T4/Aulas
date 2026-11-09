# Exercício 06: Probabilidades e limiar de decisão

**Tipo:** Guiado

## Objetivo
Testar vários limiares e observar o troca-troca entre precision e recall.

## O que fazer
1. Treine o modelo do exercício anterior e obtenha `proba = modelo.predict_proba(X_teste)[:, 1]`.
2. Mostre quantas transações passam de 0,5 e a maior probabilidade prevista.
3. Com um laço, teste os limiares 0,5; 0,3; 0,2; 0,1 e 0,05 e imprima precision, recall e número de alertas.
4. Escolha um limiar para uma equipe que revisa no máximo 100 alertas e justifique em comentário.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-2-impacto-no-treinamento/exercicio-06-probabilidade-e-limiar/limiar.py
```
A solução de referência está em `limiar.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
maior probabilidade prevista: 0.963
transações acima de 0,5: 13
limiar precision recall alertas
  0.50      0.69   0.20      13
  0.30      0.71   0.37      24
  0.20      0.49   0.43      41
  0.10      0.33   0.57      80
  0.05      0.20   0.65     153
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Existe um limiar perfeito? De quem é a decisão de escolhê-lo?
- O que muda se a equipe puder revisar 200 alertas?

## Dicas
- `predict_proba` devolve duas colunas: P(legítima) e P(fraude).
- `(proba >= corte).astype(int)` transforma probabilidade em classe.
