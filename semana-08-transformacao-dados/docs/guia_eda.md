# Guia rápido: análise exploratória de dados (EDA)

## O que é e por que fazer
Examinar os dados com tabelas e gráficos para entender sua **estrutura, padrões e problemas** antes de qualquer modelo. Modelos de machine learning aprendem o que está nos dados, **inclusive os erros**: dado ruim vira resultado ruim.

Na exploração, cada gráfico responde a uma pergunta; não precisa de capricho, precisa de rapidez. Termine cada gráfico em uma frase: **o que vi e o que farei**.

## Roteiro em sete passos
| # | Passo | Ferramentas |
| --- | --- | --- |
| 1 | Tamanho e tipos | `shape`, `head(3).T`, `info()` |
| 2 | Ausentes e duplicados | `isna().sum()`, `isna().mean()`, `duplicated()` |
| 3 | Categorias | `value_counts()`, `nunique()` |
| 4 | Números | `describe()`, boxplot, regra do IQR |
| 5 | Tempo | contagem por mês e dia da semana, `groupby(...).size().unstack()` |
| 6 | Relações | `corr()`, `heatmap`, dispersão |
| 7 | Registro | tabela de problemas com número e decisão |

## Primeiro olhar
```python
df.shape
df.head(3).T                         # todas as colunas de uma vez
df.info()                            # tipos e contagem de não nulos
df.describe()                        # procure o que não faz sentido: mínimo, máximo, média x mediana
nulos = pd.DataFrame({"nulos": df.isna().sum(), "pct": (df.isna().mean() * 100).round(1)})
df.duplicated().sum()                # linhas idênticas
df.duplicated(subset="id_pedido").sum()
```
- **Impossível** (quantidade -1) é diferente de **suspeito** (quantidade 40): o primeiro é erro; o segundo precisa de uma regra de negócio.
- Média muito acima da mediana é pista de valores extremos.

## Gráficos de exploração
| Pergunta | Gráfico |
| --- | --- |
| Como os valores se distribuem? | `sns.histplot`, `sns.boxplot` |
| Quantos há em cada categoria? | `sns.countplot` |
| Como algo evolui no tempo? | `df.plot()` / linha |
| Duas variáveis se relacionam? | `sns.scatterplot`, `sns.regplot` |
| Visão geral das correlações? | `sns.heatmap(df.corr(), annot=True)` |

Um extremo estica o eixo e esmaga o que importa: compare o gráfico **com e sem** ele, e registre o corte como uma decisão.

## Outliers: a regra de 1,5 x IQR
```python
q1, q3 = t.quantile([0.25, 0.75])
limite = q3 + 1.5 * (q3 - q1)
fora = df[df["tempo"] > limite]
```
O limite superior de valores normais é `Q3 + 1,5 × (Q3 − Q1)`. Valores repetidos (como vários 480) sugerem **código de erro**, não medição real.

## Correlação, com cautela
- `df[cols].corr()` mede o quanto duas colunas se movem juntas, de -1 a 1.
- Alta correlação **construída** (como `qtd` e `total = qtd × preço`) não é descoberta.
- Um outlier pode mudar o sinal e o tamanho da correlação: calcule **com e sem**.
- Correlação **não** é causa.
- **Quarteto de Anscombe:** quatro conjuntos com a mesma média, variância e correlação, mas formas totalmente diferentes. Sempre olhe o gráfico.

## Ausentes que significam algo
Compare os nulos **por grupo** (`df.groupby("canal")[col].agg(lambda s: s.isna().mean())`): um `id_cliente` ausente só no balcão tem sentido (cliente não identificado); uma avaliação ausente em todos os canais parece aleatória.

## Remover, corrigir ou manter?
| Problema | Decisão típica |
| --- | --- |
| Linhas duplicadas | Remover com `drop_duplicates()` |
| Quantidade inválida | Investigar com o negócio; excluir da análise de faturamento |
| Tempo repetido suspeito (480 min) | Tratar como nulo se for código de erro |
| Ausente com sentido (cliente no balcão) | Manter |
| Avaliação ausente | Manter; não imputar a nota |
| Grafias diferentes | Corrigir com `.str.strip().str.title()` |

**Toda decisão deve ser registrada** (problema, quantidade, decisão) e, se possível, validada com quem conhece o negócio.

## Registro dos problemas
```python
registro = pd.Series({
    "linhas duplicadas": df.duplicated().sum(),
    "qtd inválida (<1 ou >10)": ((df.qtd < 1) | (df.qtd > 10)).sum(),
    "tempo acima de 120 min": (df.tempo_entrega_min > 120).sum(),
})
```
É o ponto de partida do relatório de EDA: uma tabela com o problema, a quantidade e a decisão sugerida, mais três frases de achados do negócio e o que você ainda **não** sabe.

## No Google Colab
O pandas, o NumPy, o Matplotlib e o seaborn já vêm instalados. Para usar os arquivos de dados de um exercício:
```python
from google.colab import files
enviado = files.upload()      # escolha os arquivos de dados da pasta do exercício
```
Os arquivos enviados ficam em uma pasta **temporária**, apagada ao fim da sessão. Como no Colab não existe `__file__`, os scripts deste repositório usam a pasta atual: basta enviar os dados e executar. Nos notebooks os gráficos aparecem logo abaixo da célula.
