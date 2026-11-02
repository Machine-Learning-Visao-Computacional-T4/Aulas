# Exercício 03 — Hands-on: primeiro olhar

**Tipo:** prática + commit · 15 min

## Objetivo
Aplicar o roteiro inicial de EDA em uma tabela.

## O que fazer
1. Crie `primeiro_olhar.py` lendo `pedidos.csv` e `produtos.csv` e fazendo o `merge`.
2. Mostre `shape`, `head`, `info` e `describe` e escreva, em comentários, **três observações**.
3. Calcule a **proporção de nulos** por coluna e o número de **duplicados**.
4. Liste os valores distintos de `canal`. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_03_primeiro_olhar/primeiro_olhar.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_03_primeiro_olhar/primeiro_olhar.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `primeiro_olhar.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_eda.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
Tamanho: (687, 12)
                            0           1           2
id_pedido                5000        5001        5002
data               2025-01-01  2025-01-02  2025-01-03
id_cliente              113.0       152.0         NaN
id_produto                  3          11          11
qtd                         3           2           1
canal                  Balcão         App      Balcão
avaliacao                 3.0         5.0         5.0
tempo_entrega_min         NaN         NaN         NaN
produto                 Latte     Brownie     Brownie
categoria                Café        Doce        Doce
custo                     3.6         3.1         3.1
preco                    10.5         9.0         9.0
<class 'pandas.DataFrame'>
RangeIndex: 687 entries, 0 to 686
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   id_pedido          687 non-null    int64
 1   data               687 non-null    str
 2   id_cliente         559 non-null    float64
 3   id_produto         687 non-null    int64
 4   qtd                687 non-null    int64
 5   canal              687 non-null    str
 6   avaliacao          571 non-null    float64
 7   tempo_entrega_min  119 non-null    float64
 8   produto            687 non-null    str
 9   categoria          687 non-null    str
 10  custo              687 non-null    float64
 11  preco              687 non-null    float64
dtypes: float64(5), int64(3), str(4)         qtd  avaliacao  tempo_entrega_min  preco
count  687.0      571.0              119.0  687.0
mean     1.8        4.3               43.9    8.6
std      3.1        0.7               71.0    2.6
min     -1.0        2.0               13.0    5.0
25%      1.0        4.0               28.0    6.5
50%      1.0        4.0               33.0    8.5
75%      2.0        5.0               40.0   10.5
max     40.0        5.0              480.0   15.0
                   nulos   pct
id_cliente           128  18.6
avaliacao            116  16.9
tempo_entrega_min    568  82.7
12 linhas duplicadas | 12 ids repetidos
9 variações de canal
canal
Balcão       267
App          211
Delivery     107
APP           21
Balcão        21
balcão        21
 app          21
delivery      10
Delivery       8
Name: count, dtype: int64
```

## Dicas e erros comuns
- `head(3).T` coloca as colunas nas linhas e permite ver todos os campos de uma vez.
- `isna().sum()` conta os ausentes e `isna().mean()` dá a proporção.
- `duplicated()` marca linhas idênticas; `subset="id_pedido"` olha só o id.
- Deveriam ser 3 canais, mas há **9 variações** por causa de maiúsculas, minúsculas e espaços.
