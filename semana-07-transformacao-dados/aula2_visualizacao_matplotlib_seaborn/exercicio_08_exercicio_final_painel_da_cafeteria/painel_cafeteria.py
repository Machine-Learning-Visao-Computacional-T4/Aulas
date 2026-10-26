from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab
from matplotlib.ticker import FuncFormatter

VERDE = "#3E6B22"
reais = FuncFormatter(lambda v, _: f"R$ {v:,.0f}".replace(",", "."))


def criar_painel(base):
    """Desenha 4 gráficos em uma figura e devolve a figura."""
    entrega = base.dropna(subset=["tempo_entrega_min", "avaliacao"])
    ordem_cat = base.groupby("categoria")["total"].sum().sort_values(ascending=False).index

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.5), layout="constrained")

    # 1) Como o faturamento mudou mês a mês?  (tempo -> linha)
    ax = axes[0, 0]
    sns.lineplot(data=base, x="mes", y="total", estimator="sum", errorbar=None, marker="o", color=VERDE, ax=ax)
    ax.set(title="Faturamento por mês", xlabel="Mês (2025)", ylabel="Faturamento (R$)")
    ax.yaxis.set_major_formatter(reais)
    pico = base.groupby("mes")["total"].sum()
    ax.set_ylim(0, pico.max() * 1.2)   # abre espaço para a anotação
    ax.annotate("pico: investigar", (pico.idxmax(), pico.max()), xytext=(0, 8), textcoords="offset points", ha="center")

    # 2) Qual categoria vende mais?  (grupos -> barra)
    ax = axes[0, 1]
    sns.barplot(data=base, x="categoria", y="total", estimator="sum", errorbar=None, order=ordem_cat, color=VERDE, ax=ax)
    ax.set(title="Faturamento por categoria", xlabel="Categoria", ylabel="Faturamento (R$)")
    ax.yaxis.set_major_formatter(reais)

    # 3) A nota muda entre canais?  (barra começando no zero: honesto)
    ax = axes[1, 0]
    sns.barplot(data=base, x="canal", y="avaliacao", errorbar=None, color=VERDE, ax=ax)
    ax.set(title="Avaliação média por canal", xlabel="Canal", ylabel="Nota média (1 a 5)", ylim=(0, 5))

    # 4) Quem demora mais recebe nota pior?  (relação -> dispersão)
    ax = axes[1, 1]
    sns.scatterplot(data=entrega, x="tempo_entrega_min", y="avaliacao", alpha=0.5, color=VERDE, ax=ax)
    ax.set(title="Tempo de entrega x nota", xlabel="Tempo de entrega (min)", ylabel="Nota (1 a 5)")
    ax.annotate("480 min: ponto isolado", (480, 4), xytext=(230, 3.4), arrowprops={"arrowstyle": "->"})

    fig.suptitle("Painel da Grão Certo - 1º semestre de 2025")
    return fig


base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])
fig = criar_painel(base)
fig.savefig(BASE / "painel.png", dpi=150)
print("Painel com", len(fig.axes), "gráficos gravado em painel.png")
plt.show()
