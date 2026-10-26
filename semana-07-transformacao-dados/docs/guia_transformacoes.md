# Guia rápido: transformar dados com pandas

## Instalar e importar
```bash
pip install pandas numpy
```
```python
import pandas as pd
import numpy as np
```

## Qual ferramenta para transformar uma coluna?
Escolha a mais simples que resolve, nesta ordem.

| Situação | Ferramenta | Exemplo |
| --- | --- | --- |
| Conta com números | Operação vetorizada | `df["qtd"] * 2` |
| Limpar ou padronizar texto | Métodos `.str` | `s.str.strip().str.title()` |
| Extrair partes de datas | Métodos `.dt` | `s.dt.month`, `s.dt.dayofweek` |
| Trocar valores por um dicionário | `.map(dicionário)` | `s.map({0: "seg"})` |
| Regra própria, caso a caso | `.apply(função)` | `s.apply(faixa_tempo)` |
| Último recurso | `.apply(axis=1)` | linha a linha (lentíssimo) |

Em uma tabela de ~100 mil linhas, o `apply(axis=1)` foi centenas de vezes mais lento que a operação direta na coluna.

## Datas e texto
```python
df["data"] = pd.to_datetime(df["data"])      # texto -> data de verdade
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.dayofweek   # 0 = segunda-feira
df["canal"] = df["canal"].str.strip().str.title()
df["canal"].value_counts()                   # denuncia grafias diferentes
```
`map` com chave inexistente vira `NaN` **sem aviso**: confira com `isna()`.

## Função própria
```python
def faixa_tempo(minutos):
    if pd.isna(minutos):          # trate o ausente antes de comparar
        return "sem entrega"
    return "rápida" if minutos <= 30 else "demorada"

df["faixa"] = df["tempo_entrega_min"].apply(faixa_tempo)
df["nota_pct"] = df["avaliacao"].apply(lambda n: n * 20)   # lambda: função de uma linha
```

## Decidir valores com regras
| Situação | Ferramenta | Observação |
| --- | --- | --- |
| Duas saídas | `np.where(cond, a, b)` | if/else em bloco |
| Várias regras em ordem | `np.select(condições, rótulos, default=...)` | vale a 1ª condição verdadeira |
| Alterar só algumas linhas | `df.loc[máscara, coluna] = valor` | altera a tabela original |
| Número vira faixa | `pd.cut(s, bins=[...], labels=[...])` | `pd.qcut` usa quantis |
| Valor está em uma lista | `s.isin([...])`, `s.between(a, b)` | geram a máscara |

```python
df["perfil"] = np.select([df["nota"] >= 4, df["nota"] == 3], ["satisfeito", "neutro"], default="sem nota")
df["faixa"] = pd.cut(df["tempo"], bins=[0, 20, 30, 45, np.inf], labels=["até 20", "21-30", "31-45", "mais de 45"])
```
- Em Series use `&`, `|` e `~`, **cada condição entre parênteses**. `and`, `or` e `not` dão `ValueError: The truth value of a Series is ambiguous`.
- Qualquer comparação com `NaN` dá `False` (`np.nan >= 4` é `False`): decida o que fazer com os ausentes.

## Juntar tabelas
| Operação | Liga por | Efeito | Use quando |
| --- | --- | --- | --- |
| `pd.concat([a, b])` | nada (mesmas colunas) | mais linhas | empilhar meses ou filiais |
| `pd.concat([a, b], axis=1)` | índice | mais colunas | tabelas com o mesmo índice e ordem |
| `a.merge(b, on="chave")` | colunas-chave | mais colunas | tabelas diferentes com chave comum |
| `a.join(b)` | índice | mais colunas | a chave já é o índice |

```python
base = pedidos.merge(produtos, on="id_produto", how="left", validate="m:1")
pedidos.merge(cat, left_on="id_produto", right_on="cod")          # chaves com nomes diferentes
pedidos.merge(clientes, on="id_cliente", how="left", indicator=True)   # coluna _merge: both / left_only / right_only
```
- `validate="m:1"` afirma que a chave é única na tabela da direita; se não for, o pandas dá `MergeError` em vez de multiplicar linhas em silêncio.
- Compare **sempre** `len()` antes e depois do merge. `how="inner"` descarta sem avisar; `how="left"` preserva a tabela da esquerda. A pergunta de negócio decide.
- `pd.concat` **não avisa** quando as colunas têm nomes diferentes: cria as duas e preenche com `NaN`. Padronize os nomes antes de empilhar.

## Pipeline reutilizável
```python
def preparar(pedidos, produtos, clientes):
    return (
        pedidos
        .assign(data=lambda d: pd.to_datetime(d["data"]),
                canal=lambda d: d["canal"].str.strip().str.title())
        .merge(produtos, on="id_produto", how="left", validate="m:1")
        .merge(clientes, on="id_cliente", how="left", validate="m:1")
        .assign(total=lambda d: d["qtd"] * d["preco"])
    )
```
Cada `.assign` cria colunas **sem alterar** a tabela original e cada `.merge` junta uma tabela, em sequência. A função roda do zero e dá sempre o mesmo resultado.

Para gravar o resultado: `pronto.to_csv("pedidos_prontos.csv", index=False)`.

## No Google Colab
O pandas, o NumPy, o Matplotlib e o seaborn já vêm instalados. Para usar os arquivos de dados de um exercício:
```python
from google.colab import files
enviado = files.upload()      # escolha os arquivos de dados da pasta do exercício
```
Os arquivos enviados ficam em uma pasta **temporária**, apagada ao fim da sessão. Como no Colab não existe `__file__`, os scripts deste repositório usam a pasta atual: basta enviar os dados e executar. Nos notebooks os gráficos aparecem logo abaixo da célula.
