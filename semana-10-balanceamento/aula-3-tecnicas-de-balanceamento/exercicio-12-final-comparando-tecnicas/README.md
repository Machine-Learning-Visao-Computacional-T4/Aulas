# Exercício 12: Final da semana: comparando técnicas

**Tipo:** Final, com Git e Pull Request

## Objetivo
Entregar a comparação completa entre técnicas, com escolha justificada pelo custo.

## O que fazer
1. Crie a branch `feature/comparar-tecnicas-balanceamento`.
2. Crie `balanceamento.py` com a função `resumo` e cinco técnicas em `ImbPipeline`: sem técnica, class_weight, undersampling, oversampling e SMOTE.
3. Treine todas no mesmo treino estratificado e imprima a tabela (precision, recall, F1, PR AUC).
4. Calcule o prejuízo de cada uma (R$ 800 por fraude perdida, R$ 15 por falso alarme) e ordene do menor para o maior.
5. Crie `BALANCEAMENTO.md` com a técnica escolhida, a justificativa e uma frase sobre o que ainda poderia melhorar.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-3-tecnicas-de-balanceamento/exercicio-12-final-comparando-tecnicas/balanceamento.py
```
A solução de referência está em `balanceamento.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
               precision  recall     f1  pr_auc
técnica                                        
sem técnica        0.692   0.196  0.305   0.412
class_weight       0.110   0.848  0.194   0.434
undersampling      0.101   0.848  0.181   0.450
oversampling       0.111   0.848  0.197   0.439
SMOTE              0.113   0.848  0.200   0.412
SMOTE           R$ 10.175
oversampling    R$ 10.265
class_weight    R$ 10.355
undersampling   R$ 10.790
sem técnica     R$ 29.660
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que as diferenças entre as técnicas devem ser interpretadas com cuidado com apenas 46 fraudes no teste?
- O que muda se o falso alarme custar R$ 150 em vez de R$ 15?

## Dicas
- O reamostrador só pode estar dentro do ImbPipeline.
- Rode o script antes de abrir o Pull Request.

## Git deste exercício
```bash
git checkout -b feature/comparar-tecnicas-balanceamento
git add balanceamento.py BALANCEAMENTO.md
git commit -m "feat: comparação de técnicas"
git push -u origin feature/comparar-tecnicas-balanceamento
```
Abra o Pull Request para a `main` pelo GitHub e descreva em duas frases o que o programa faz e quais números você conferiu.
