from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])
mensal = base.groupby("mes")["total"].sum()
por_cat = base.groupby("categoria")["total"].sum().sort_values()
por_canal = base.groupby("canal")["total"].sum().sort_values()
nomes_dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
por_dia = base["dia_semana"].value_counts().sort_index()

fig, axes = plt.subplots(2, 2, figsize=(9, 6), layout="constrained")

axes[0, 0].plot(mensal.index, mensal.values, marker="o", color="#3E6B22")
axes[0, 0].set(title="Faturamento por mês", xlabel="Mês (2025)", ylabel="R$")

axes[0, 1].barh(por_cat.index, por_cat.values, color="#78C043")
axes[0, 1].set(title="Faturamento por categoria", xlabel="R$")

axes[1, 0].bar(por_canal.index, por_canal.values, color="#78C043")
axes[1, 0].set(title="Faturamento por canal", ylabel="R$")

axes[1, 1].bar(nomes_dias, por_dia.values, color="#3E6B22")
axes[1, 1].set(title="Pedidos por dia da semana", ylabel="pedidos")

fig.suptitle("Painel da Grão Certo - 1º semestre de 2025")
fig.savefig(BASE / "painel.png", dpi=150)
print("axes tem shape", axes.shape)
print("Imagem painel.png gravada.")
plt.show()
