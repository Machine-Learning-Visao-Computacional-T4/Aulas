# Exercício 03 — Leia o gráfico

**Tipo:** interpretação + script · **Tempo:** 15 min

## Objetivo
Praticar a leitura de **histogramas e boxplots** para suspeitar de problemas nos dados **antes** de rodar qualquer modelo. Não é para calcular nada: é para desenvolver o "olho treinado".

## Passo a passo
1. Instale as bibliotecas (uma vez), a partir da raiz do repositório: `pip install -r requirements.txt`
2. Gere os gráficos de um dataset **fictício** de entregas:
   ```bash
   python aula1_problema_dataset/exercicio_03_leia_o_grafico/gerar_graficos.py
   ```
   Isso cria o arquivo `graficos_entregas.png` na mesma pasta do script.
3. Abra a imagem e responda, para cada gráfico:
   - Qual é a forma da distribuição (simétrica, torta para um lado, dois "montes")?
   - Há **valores fora do padrão** (outliers)? Onde?
   - Algo parece **impossível ou suspeito**?
4. Responda: **que ação você tomaria?** (investigar o outlier, remover a coluna, corrigir o registro, coletar mais dados...)

## O que o script mostra
O dataset tem 500 entregas fictícias com `tempo_entrega_min` e `distancia_km`. Foram plantados de propósito alguns problemas: poucas entregas com tempos absurdamente altos, e uma pequena parcela de distâncias registradas como `0`. Procure-os nos gráficos.

## Para pensar
- O outlier é um **erro de registro** ou um **caso real raro**? A resposta muda sua ação.
- Média e mediana mudam muito por causa do outlier? (O script imprime as duas.)

> Os dados são gerados por código com semente fixa (`seed=42`), então todo mundo vê os mesmos gráficos. Este dataset é um material criado para este repositório; na aula o gráfico pode ser outro.
