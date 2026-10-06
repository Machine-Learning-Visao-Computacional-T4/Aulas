# Exercício 02 — Ajuste o hiperparâmetro

**Tipo:** análise de tabela + script

## Cenário
Uma indústria de Santa Catarina quer automatizar a inspeção de peças na linha de produção. A equipe treinou uma **Árvore de Decisão** para classificar as peças como **defeituosa** ou **aprovada**, usando características extraídas das imagens (área, contorno, intensidade de cor etc.). Para escolher a melhor configuração, variaram o hiperparâmetro `max_depth` (profundidade máxima da árvore) e mediram o **F1-score** no conjunto de treino e no de validação.

| Combinação | max_depth | F1 Treino | F1 Validação |
| --- | --- | --- | --- |
| A | 2 | 0,61 | 0,59 |
| B | 4 | 0,79 | 0,76 |
| C | 6 | 0,87 | 0,84 |
| D | 12 | 0,96 | 0,77 |
| E | 25 | 1,00 | 0,66 |

## Perguntas
1. Qual combinação parece sofrer **underfitting**? Por quê?
2. Qual combinação parece sofrer **overfitting**? Por quê?
3. Qual combinação apresenta o **melhor equilíbrio**? Justifique com os números.
4. **(Desafio)** Calcule a diferença entre F1 de treino e de validação para cada combinação. O que essa diferença revela?

## Passo a passo
1. Responda às perguntas 1 a 3 olhando só a tabela, e anote.
2. Rode o script para conferir o desafio:
   ```bash
   python aula3_overfitting_producao/exercicio_02_ajuste_o_hiperparametro/diagnostico.py
   ```
3. Compare com as suas respostas. O que o script confirma? O que você ajustaria?

## Como ler o resultado
- **Underfitting:** F1 baixo no treino **e** na validação (o modelo é simples demais).
- **Overfitting:** F1 muito alto no treino e bem menor na validação (o modelo decorou).
- **Melhor equilíbrio:** maior F1 de **validação**, com diferença pequena entre treino e validação.
