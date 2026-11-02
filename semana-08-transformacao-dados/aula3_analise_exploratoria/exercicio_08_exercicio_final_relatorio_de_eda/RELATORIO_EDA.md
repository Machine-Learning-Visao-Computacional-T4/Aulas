# Relatório de EDA — Cafeteria Grão Certo

Exploração dos **687 pedidos** de janeiro a junho de 2025 (`pedidos.csv` + `produtos.csv`), antes de qualquer modelo. Dados fictícios.

## Problemas encontrados

| Problema | Quantos | Decisão sugerida |
| --- | --- | --- |
| Linhas duplicadas | 12 | Remover com `drop_duplicates()` |
| Quantidade inválida (-1 ou 40) | 7 | Investigar com o negócio; excluir da análise de faturamento |
| Tempo de entrega de 480 min | 3 | Tratar como nulo se for código de erro |
| Delivery sem tempo | 6 | Manter e avisar que faltam dados |
| Pedido sem cliente | 128 | Manter: são vendas de balcão não identificadas |
| Pedido sem avaliação | 116 | Manter; não imputar a nota |
| Canal com 9 grafias | 9 → 3 | Corrigir com `.str.strip().str.title()` |

## Achados do negócio

1. **Sexta a domingo concentram 59% dos pedidos** (sem duplicados): vale pensar a escala de equipe e o estoque em torno do fim de semana.
2. **O Café perde pedidos (78 em janeiro para 25 em junho) enquanto a Bebida Gelada sobe (14 para 29)**. Hipótese: o calor aumenta o consumo de bebidas geladas. É hipótese, não conclusão.
3. **O pico de março (R$ 2.638) está inflado por pedidos de 40 unidades**: sem eles, março cai para R$ 1.658. Antes de comemorar o pico, é preciso confirmar com o negócio se esses pedidos são reais.

## O que eu ainda não sei

- Os **480 minutos** são um código de erro do sistema ou entregas reais? O valor se repete 3 vezes, o que sugere erro.
- Os pedidos de **40 unidades** são encomendas grandes legítimas ou erro de digitação?
- Por que **82,7%** dos pedidos não têm tempo de entrega? Só o Delivery registra o tempo; os 6 deliveries sem tempo merecem atenção.
- A relação entre tempo de entrega e nota é fraca (correlação -0,15 sem os 480 min): é preciso mais dados antes de afirmar que entregas lentas pioram a avaliação.
