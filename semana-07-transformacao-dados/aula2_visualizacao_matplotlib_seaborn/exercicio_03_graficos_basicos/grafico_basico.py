from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])

# 1) Linha: quantidade de pedidos por mês
pedidos_mes = base.groupby("mes").size()
print(pedidos_mes)
plt.figure(figsize=(5, 3.6))
plt.plot(pedidos_mes.index, pedidos_mes.values, marker="o")
plt.title("Pedidos por mês")

# 2) Barras: faturamento por canal
por_canal = base.groupby("canal")["total"].sum().sort_values()
print(por_canal.round(0))
plt.figure(figsize=(5, 3.6))
plt.barh(por_canal.index, por_canal.values)
plt.title("Faturamento por canal")
plt.savefig(BASE / "canal.png")   # salvar ANTES do plt.show()

# 3) Dispersão: preço x quantidade
plt.figure(figsize=(5, 3.6))
plt.scatter(base["preco"], base["qtd"], alpha=0.5)
plt.title("Preço x quantidade")
# O que vejo? O preço só assume 12 valores (um por produto), então os pontos formam colunas;
# e há pedidos isolados lá em cima, com 40 unidades.

plt.show()
