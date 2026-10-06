# Exercício 02 — Traduza o problema

**Tipo:** escrita · **Tempo:** 12 min

## Objetivo
Transformar uma frase **vaga** de negócio em uma **pergunta de Machine Learning específica e mensurável**.

## Passo a passo
1. Abra o arquivo [`traduza_o_problema.md`](traduza_o_problema.md). Ele traz frases vagas de exemplo.
2. Para cada frase, reescreva como uma pergunta de ML usando um **verbo de previsão concreto**: *prever, classificar, agrupar, recomendar*.
3. Indique o **tipo de problema**: classificação, regressão, série temporal, recomendação ou clustering.
4. Teste sua tradução com duas perguntas:
   - Ficou específica o suficiente?
   - Dá para saber **que dado seria necessário**?

## Armadilha comum
Manter a resposta vaga ("vamos usar IA para melhorar X"). Se não há um verbo de previsão, ainda não é um problema de ML.

## Exemplo resolvido
| Frase vaga | Pergunta de ML | Tipo | Dados necessários |
| --- | --- | --- | --- |
| "Queremos reduzir o cancelamento de clientes" | Dado o histórico de uso de um cliente, ele vai cancelar nos próximos 30 dias? | Classificação | Histórico de uso, tempo de contrato, chamados de suporte, flag de cancelamento |

> As frases do arquivo ao lado foram preparadas para este repositório; na aula, as frases podem ser outras. Crie as suas também.
