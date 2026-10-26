# Guia rápido: gráficos com Matplotlib e seaborn

## Instalar e importar
```bash
pip install matplotlib seaborn
```
```python
import matplotlib.pyplot as plt   # "plt" é a convenção
import seaborn as sns             # "sns" é a convenção
```

## Anatomia
| Termo | O que é |
| --- | --- |
| `Figure` | A tela inteira: tamanho, fundo e o conjunto de gráficos |
| `Axes` (`ax`) | Um gráfico dentro da figura, com eixos, título, legenda e os dados |
| `plt.plot(...)` | Estilo rápido: desenha no gráfico atual |
| `ax.plot(...)` | Estilo orientado a objeto: indica em qual gráfico desenhar (necessário com vários gráficos) |

```python
plt.plot([1, 2, 3, 4], [2, 4, 3, 5])
plt.show()          # exibe a figura
```
Para salvar, use `plt.savefig("grafico.png", dpi=150)` **antes** do `plt.show()`.

## Qual gráfico para qual pergunta?
| Pergunta | Gráfico | Função |
| --- | --- | --- |
| Como algo muda ao longo do tempo? | Linha | `plt.plot` |
| Qual grupo é maior ou menor? | Barra | `plt.bar` / `plt.barh` |
| Duas variáveis numéricas se relacionam? | Dispersão | `plt.scatter` |
| Como os valores se distribuem? | Histograma / boxplot | `plt.hist` / `sns.boxplot` |

## Customizar
| O que ajustar | `plt` | `ax` (orientado a objeto) |
| --- | --- | --- |
| Título | `plt.title("...")` | `ax.set_title("...")` |
| Rótulo do eixo x | `plt.xlabel("...")` | `ax.set_xlabel("...")` |
| Limites do eixo y | `plt.ylim(0, 5)` | `ax.set_ylim(0, 5)` |
| Grade e legenda | `plt.grid(); plt.legend()` | `ax.grid(); ax.legend()` |
| Tamanho da figura | `plt.figure(figsize=(8, 4))` | `fig, ax = plt.subplots(figsize=(8, 4))` |

```python
from matplotlib.ticker import FuncFormatter
reais = FuncFormatter(lambda v, _: f"R$ {v:,.0f}".replace(",", "."))
ax.yaxis.set_major_formatter(reais)                 # eixo em reais
ax.annotate("pico", (x, y), xytext=(0, 8), textcoords="offset points", ha="center")
```
O mínimo necessário: **título** que diz o que é, **rótulos nos eixos com unidade** e **legenda** quando há mais de uma série.

## Atalhos e seaborn
| Ferramenta | Quando usar | Ponto forte |
| --- | --- | --- |
| Matplotlib | Controle total de cada detalhe | Flexibilidade |
| `df.plot()` | Olhada rápida em uma tabela ou série | Rapidez |
| seaborn | Gráficos estatísticos com colunas e `hue` | Estilo e simplicidade |

```python
sns.set_theme(style="whitegrid")
sns.barplot(data=base, x="categoria", y="total", estimator="sum", errorbar=None)
sns.lineplot(data=base, x="mes", y="total", hue="canal", estimator="sum", errorbar=None, marker="o")
sns.scatterplot(data=entrega, x="tempo_entrega_min", y="avaliacao", hue="plano", alpha=0.6)
```
O seaborn trabalha com `data=`, `x=` e `y=` usando **nomes de colunas**; `hue` acrescenta uma variável pela cor. A paleta `"colorblind"` evita combinações que quem tem daltonismo não distingue.

## Vários gráficos em uma figura
```python
fig, axes = plt.subplots(2, 2, figsize=(8, 5), layout="constrained")
axes[0, 0].plot(...)                       # axes é uma matriz: axes[linha, coluna]
fig.suptitle("Título geral")

fig, ax = plt.subplot_mosaic([["topo", "topo"], ["esq", "dir"]], layout="constrained")
ax["topo"].plot(...)                       # nomes repetidos ocupam várias células
```
| Tipo | Exemplos | Característica |
| --- | --- | --- |
| Nível de eixo | `barplot`, `lineplot`, `scatterplot`, `histplot` | Desenha em um `ax`; aceita `ax=` |
| Nível de figura | `relplot`, `displot`, `catplot` | Cria a figura; divide por `col=` e `row=`; **não** aceita `ax=` |

## Gráficos honestos
- **Barras começam no zero**: o comprimento da barra representa o valor; cortar o eixo exagera as diferenças.
- **Escolha pela pergunta**: tempo pede linha, comparação pede barra, relação pede dispersão. Evite pizza e 3D.
- **Rotule tudo**: título, unidades, período e legenda.
- **Mostre as exceções**: se há um ponto estranho, sinalize e investigue em vez de esconder ou apagar.

## Uma imagem é um array
```python
img = np.zeros((8, 8), dtype=int)       # matriz 8 x 8: imagem em tons de cinza (0 = preto, 255 = branco)
plt.imshow(img, cmap="gray"); plt.colorbar(); plt.show()
```
O `imshow` desenha uma matriz como imagem: é a base de todo o trabalho em visão computacional.

## No Google Colab
O pandas, o NumPy, o Matplotlib e o seaborn já vêm instalados. Para usar os arquivos de dados de um exercício:
```python
from google.colab import files
enviado = files.upload()      # escolha os arquivos de dados da pasta do exercício
```
Os arquivos enviados ficam em uma pasta **temporária**, apagada ao fim da sessão. Como no Colab não existe `__file__`, os scripts deste repositório usam a pasta atual: basta enviar os dados e executar. Nos notebooks os gráficos aparecem logo abaixo da célula.
