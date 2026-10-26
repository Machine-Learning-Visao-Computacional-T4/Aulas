from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])
mensal = base.groupby("mes")["total"].sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.6))

# Esquerda: o gráfico padrão
ax1.plot(mensal.index, mensal.values)

# Direita: o mesmo gráfico, com o mínimo necessário
ax2.plot(mensal.index, mensal.values, marker="o", color="#3E6B22", linewidth=2, label="Faturamento")
ax2.set_title("Faturamento por mês - 1º semestre de 2025")
ax2.set_xlabel("Mês")
ax2.set_ylabel("Total vendido (R$)")
ax2.grid(alpha=0.3)
ax2.legend()

fig.tight_layout()
fig.savefig(BASE / "antes_depois.png", dpi=120)

print("Faltava: título, rótulos nos eixos com unidade, legenda e uma grade discreta.")
plt.show()
