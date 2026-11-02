# Exercício 02 — Ache o erro

**Tipo:** dinâmica + script · 8 min

## Objetivo
Praticar a leitura de `describe` e `value_counts` em busca de inconsistências.

## O que fazer
1. Rode o script e observe a saída do `describe` e a de `value_counts` da quantidade.
2. Escreva o valor que considera **impossível** e o que considera **suspeito**.
3. Discuta a diferença: **-1 é impossível; 40 é possível, mas improvável** para um pedido de balcão.
4. Pergunte qual regra de negócio permitiria decidir sozinho.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_02_ache_o_erro/ache_o_erro.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_02_ache_o_erro/ache_o_erro.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `ache_o_erro.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_eda.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
         qtd  avaliacao  tempo_entrega_min  preco
count  687.0      571.0              119.0  687.0
mean     1.8        4.3               43.9    8.6
std      3.1        0.7               71.0    2.6
min     -1.0        2.0               13.0    5.0
25%      1.0        4.0               28.0    6.5
50%      1.0        4.0               33.0    8.5
75%      2.0        5.0               40.0   10.5
max     40.0        5.0              480.0   15.0

Quantidade por pedido:
qtd
-1       3
 1     403
 2     172
 3      72
 4      33
 40      4
Name: count, dtype: int64

Impossível (qtd < 1): 3 pedidos
Suspeito (qtd > 10):   4 pedidos
Tempo de entrega máximo: 480.0 min | mediana: 33.0 min
```

## Dicas e erros comuns
- Procure o que não faz sentido: quantidade mínima -1 (impossível), quantidade máxima 40 (muito acima da mediana de 1) e tempo máximo de 480 minutos (média bem acima da mediana).
- Média muito diferente da mediana é pista de valores extremos.
