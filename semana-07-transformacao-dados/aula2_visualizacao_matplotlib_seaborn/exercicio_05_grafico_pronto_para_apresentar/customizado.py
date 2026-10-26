from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])

VERDE = "#3E6B22"
CLARO = "#B5C9A5"

por_cat = base.groupby("categoria")["total"].sum().sort_values(ascending=False)
cores = [VERDE if c == por_cat.idxmax() else CLARO for c in por_cat.index]   # destaque no maior

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(por_cat.index, por_cat.values, color=cores)

ax.set_title("Faturamento por categoria - 1º semestre de 2025")
ax.set_xlabel("Categoria")
ax.set_ylabel("Faturamento (R$)")
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"R$ {v:,.0f}".replace(",", ".")))   # eixo em reais
ax.set_ylim(0, por_cat.max() * 1.15)   # barras começam no zero

ax.annotate(f"{por_cat.idxmax()} lidera\nR$ {por_cat.max():,.0f}".replace(",", "."),
            (0, por_cat.max()), xytext=(0, 6), textcoords="offset points", ha="center")

fig.tight_layout()
fig.savefig(BASE / "categoria.png", dpi=150)
print(por_cat.round(0))
print("Imagem categoria.png gravada.")
plt.show()
