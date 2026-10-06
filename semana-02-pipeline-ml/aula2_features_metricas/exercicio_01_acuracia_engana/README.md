# Exercício 01 — Por que a acurácia sozinha pode enganar

**Tipo:** discussão + script

## Objetivo
Sentir, antes de aprender os nomes formais, por que "acertar 99% das vezes" pode não significar nada.

## Cenário
> Um modelo detecta uma doença muito rara, que afeta **1 em cada 1.000 pessoas**. Ele acerta **99%** das vezes. Ele é um bom modelo?

## Passo a passo
1. Responda **sim ou não**, antes de ler qualquer coisa a mais.
2. Escreva: *"o que eu precisaria saber para responder com confiança?"*
3. Só depois, rode o script que testa um "modelo preguiçoso":
   ```bash
   python aula2_features_metricas/exercicio_01_acuracia_engana/acuracia_engana.py
   ```
4. Compare o resultado com a sua resposta do passo 1.

## O que o script faz
Cria 100.000 pessoas fictícias (1 em cada 1.000 doente) e avalia um "modelo" que **sempre responde "não tem a doença"**. Veja a acurácia dele e quantos doentes ele encontra.

## Para pensar
- Se um modelo que não faz nada acerta 99,9%, o que significa "99%" nesse cenário?
- Que outra pergunta você faria além de "quanto ele acerta"? (Spoiler: *dos doentes, quantos ele encontra?* Isso é o **recall**, que você calcula no Exercício 03.)
