# Exercício 08 — Exercício final: relatório de EDA

**Tipo:** projeto integrador · branch + Pull Request · 25 min

## Objetivo
Aplicar o roteiro de EDA a `pedidos.csv` e entregar um **relatório** por Pull Request.

## O que fazer
1. Crie a branch `feature/eda-cafeteria`.
2. Escreva `eda_cafeteria.py` seguindo os **sete passos do roteiro**, com pelo menos **três gráficos** salvos.
3. Crie `RELATORIO_EDA.md` com a tabela de problemas (problema, quantidade, decisão) e **três frases de achados** do negócio.
4. Commit e push da branch.
5. Abra um Pull Request para a `main` explicando **o que você encontrou e o que ainda não sabe**.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_08_exercicio_final_relatorio_de_eda/eda_cafeteria.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_08_exercicio_final_relatorio_de_eda/eda_cafeteria.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `eda_cafeteria.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_eda.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
== 1. Tamanho e tipos ==
(687, 12)
id_pedido              int64
data                     str
id_cliente           float64
id_produto             int64
qtd                    int64
canal                    str
avaliacao            float64
tempo_entrega_min    float64
produto                  str
categoria                str
custo                float64
preco                float64

== 2. Ausentes e duplicados ==
                   nulos   pct
id_cliente           128  18.6
avaliacao            116  16.9
tempo_entrega_min    568  82.7
12 linhas duplicadas

== 3. Categorias ==
9 grafias de canal
canal
Balcão      267
App         211
Delivery    107
Name: count, dtype: int64
Canais depois: 3

== 4. Números ==
         qtd  avaliacao  tempo_entrega_min  preco
count  687.0      571.0              119.0  687.0
mean     1.8        4.3               43.9    8.6
std      3.1        0.7               71.0    2.6
min     -1.0        2.0               13.0    5.0
25%      1.0        4.0               28.0    6.5
50%      1.0        4.0               33.0    8.5
75%      2.0        5.0               40.0   10.5
max     40.0        5.0              480.0   15.0
Regra do IQR: limite 58.0 min | 3 pedidos acima

== 5. Tempo ==
dia
seg     77
ter     63
qua     69
qui     66
sex    116
sab    135
dom    149
categoria  Bebida Gelada  Café  Doce  Salgado
mes
1                     14    78    11       13
2                     23    51    17       22
3                     28    47    21       19
4                     28    44    11       16
5                     39    42    24       32
6                     29    25    16       25

== 6. Relações ==
Correlação tempo x nota: com os 480 min 0.03 | sem eles -0.15

== 7. Registro ==
                         problema  quantos                                          decisao
                Linhas duplicadas       12                    Remover com drop_duplicates()
Quantidade inválida (< 1 ou > 10)        7 Investigar com o negócio; excluir do faturamento
Tempo de entrega acima de 120 min        3           Tratar como nulo se for código de erro
               Delivery sem tempo        6                 Manter e avisar que faltam dados
              Pedidos sem cliente      128       Manter: vendas de balcão não identificadas
            Pedidos sem avaliação      116                       Manter; não imputar a nota
Arquivo registro_problemas.csv gravado.
```

Os gráficos são salvos ao lado do script; se quiser vê-los na tela, acrescente `plt.show()` ao final (no Colab/notebook eles aparecem logo abaixo da célula). O relatório de exemplo está em [`RELATORIO_EDA.md`](RELATORIO_EDA.md).

## Dicas e erros comuns
- Roteiro de EDA em sete passos: 1) tamanho e tipos; 2) ausentes e duplicados; 3) categorias; 4) números; 5) tempo; 6) relações; 7) registro.
- Correlação **não** é causa: a relação fraca entre tempo e nota é uma pista, não uma conclusão.
- No relatório, cada achado deve ter um **número** e uma **decisão sugerida**.

## Git deste exercício
```bash
git switch -c feature/eda-cafeteria
git add eda_cafeteria.py RELATORIO_EDA.md graficos/ pedidos.csv produtos.csv registro_problemas.csv
git commit -m "Adiciona EDA da cafeteria e relatório"
git push -u origin feature/eda-cafeteria
```
Depois, no GitHub: **Compare & pull request** → descreva o que o programa faz → **Create pull request**.
