from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])
mensal = base.groupby("mes")["total"].sum()
por_categoria = base.groupby("categoria")["total"].sum().sort_values()
entrega = base.dropna(subset=["tempo_entrega_min", "avaliacao"])

# Pergunta 1: mudança no tempo -> LINHA
plt.figure(figsize=(5, 3.6))
plt.plot(mensal.index, mensal.values, marker="o")
plt.title("Como o faturamento mudou mês a mês?")
plt.savefig(BASE / "pergunta1_linha.png", dpi=100)

# Pergunta 2: comparação entre grupos -> BARRA
plt.figure(figsize=(5, 3.6))
plt.barh(por_categoria.index, por_categoria.values)
plt.title("Qual categoria vende mais?")
plt.savefig(BASE / "pergunta2_barra.png", dpi=100)

# Pergunta 3: relação entre duas variáveis numéricas -> DISPERSÃO
plt.figure(figsize=(5, 3.6))
plt.scatter(entrega["tempo_entrega_min"], entrega["avaliacao"], alpha=0.5)
plt.title("Quem demora mais recebe nota pior?")
plt.savefig(BASE / "pergunta3_dispersao.png", dpi=100)

print("Pergunta 1 -> linha (tempo tem ordem). Mês de maior faturamento:", mensal.idxmax())
print("Pergunta 2 -> barra (comparar grupos). Categoria líder:", por_categoria.idxmax())
print("Pergunta 3 -> dispersão (duas variáveis numéricas).", len(entrega), "entregas com nota")
plt.show()
