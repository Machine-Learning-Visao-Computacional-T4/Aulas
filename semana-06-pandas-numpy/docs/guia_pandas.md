# Guia rápido: pandas

## Instalar e importar
```bash
pip install pandas openpyxl
```
```python
import pandas as pd   # "pd" é a convenção mundial
```
`openpyxl` é necessário para ler e gravar planilhas `.xlsx`.

## Series e DataFrames
| Estrutura | O que é | Exemplo |
| --- | --- | --- |
| **Series** | Uma coluna de valores, com rótulos (índice) | `pd.Series([8.5, 6.0], index=["Ana", "Bruno"])` |
| **DataFrame** | Uma tabela: várias Series (colunas) com o mesmo índice | `pd.DataFrame({"produto": ["Mouse"], "preco": [60.0]})` |

Cada coluna de um DataFrame é uma Series e tem **um único tipo** (`int64`, `float64`, texto, `bool`, `datetime64`). Nas versões mais novas do pandas, o texto aparece como `str`; nas anteriores, como `object`.

## Ler e gravar
| Função | Lê de | Observação |
| --- | --- | --- |
| `pd.read_csv()` | CSV/TXT (e URLs) | `sep=";"`, `decimal=","`, `encoding="latin-1"`, `usecols=[...]`, `parse_dates=[...]` |
| `pd.read_excel()` | planilhas `.xlsx` | `sheet_name="Janeiro"` escolhe a aba |
| `pd.read_json()` | JSON | funciona bem com uma lista de objetos |
| `pd.read_sql()` | banco SQL | recebe a consulta e uma conexão (`sqlite3.connect(...)`) |

Para gravar: `df.to_csv("saida.csv", index=False)`, `df.to_excel(...)`, `df.to_json(..., orient="records", force_ascii=False)`. Use `index=False` para não gravar a coluna de índice.

## Conhecer o dataset
```python
df.shape                 # (linhas, colunas)
df.columns.tolist()      # nomes das colunas
df.head(3)               # primeiras linhas
df.describe()            # resumo estatístico das colunas numéricas
df["cidade"].value_counts()   # contagem de cada valor
```

## Selecionar
| Quero | Código | Devolve |
| --- | --- | --- |
| Uma coluna | `df["preco"]` | Series |
| Várias colunas | `df[["produto", "preco"]]` | DataFrame |
| Por **rótulo** | `df.loc[2:4, ["produto", "preco"]]` | inclui o último (`4`) |
| Por **posição** | `df.iloc[0:3, 1:3]` | exclui o último |

## Filtrar
```python
df[df["preco"] > 500]                                   # uma condição
df[(df["cidade"] == "Joinville") | (df["preco"] > 3000)]  # ou
df[(df["cidade"] == "Blumenau") & (df["quantidade"] > 3)] # e
df[~(df["categoria"] == "Vídeo")]                       # não
df[df["produto"].isin(["Mouse", "Teclado"])]
df[df["preco"].between(100, 1000)]
df[df["produto"].str.contains("tor")]
```
Use `&`, `|` e `~`, sempre com **cada condição entre parênteses**. `and`, `or` e `not` **não funcionam** com colunas.

## Criar e ordenar
```python
df["total"] = df["quantidade"] * df["preco"]      # conta em todas as linhas de uma vez
df.sort_values("total", ascending=False)
```

## Limpar
| Problema | Código |
| --- | --- |
| Ver ausentes | `df.isna().sum()` |
| Remover linhas com ausentes | `df.dropna()` |
| Preencher ausentes | `df["nota"] = df["nota"].fillna(df["nota"].mean())` |
| Linhas repetidas | `df.drop_duplicates()` |
| Espaços e caixa | `df["nome"].str.strip().str.title()` |
| Tirar não dígitos | `df["tel"].str.replace(r"\D", "", regex=True)` |
| Texto em data | `pd.to_datetime(df["data"], format="%d/%m/%Y")` |
| Texto em número | `pd.to_numeric(df["valor"], errors="coerce")` |

`fillna` e companhia **devolvem** um novo resultado: lembre de atribuir de volta.

## groupby: dividir, aplicar, combinar
```python
df.groupby("cidade")["total"].sum()
df.groupby("categoria").agg(vendas=("total", "sum"), itens=("quantidade", "sum"))
df.groupby(["cidade", "categoria"])["total"].sum().reset_index()
```
`reset_index()` transforma o índice (as chaves do grupo) de volta em colunas.

## merge: juntar tabelas
| `how` | Mantém |
| --- | --- |
| `inner` | só as linhas com correspondência nas **duas** tabelas |
| `left` | **todas** as linhas da tabela da esquerda |
| `right` | **todas** as linhas da tabela da direita |
| `outer` | todas as linhas das duas |

```python
pedidos.merge(clientes, on="id_cliente", how="left")
a.merge(b, left_on="codigo", right_on="id")        # chaves com nomes diferentes
```
**Cuidado:** chaves **repetidas** multiplicam linhas (2 x 2 = 4). Confira `len()` antes e depois. `indicator=True` cria a coluna `_merge`, que mostra de onde veio cada linha.

## pivot_table e melt
```python
df.pivot_table(index="cidade", columns="categoria", values="total", aggfunc="sum", fill_value=0)
largo.melt(id_vars="produto", var_name="mes", value_name="qtd")   # largo -> longo
```
`pivot` não agrega e dá erro se houver combinações repetidas; `pivot_table` usa `aggfunc`.

## No Google Colab
O pandas e o openpyxl já vêm instalados. Para usar os arquivos de dados de um exercício:
```python
from google.colab import files
enviado = files.upload()      # escolha os arquivos de dados da pasta do exercício
```
Os arquivos enviados ficam em uma pasta **temporária**, apagada ao fim da sessão. Como no Colab não existe `__file__`, os scripts deste repositório usam a pasta atual: basta enviar os dados e executar.

## Dados fictícios
Em exercícios e portfólio, **use dados inventados**. Nunca suba dados pessoais de verdade para um repositório público.
