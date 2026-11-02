from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

df["data"] = pd.to_datetime(df["data"])
nomes = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
df["dia"] = df["data"].dt.dayofweek.map(dict(enumerate(nomes)))
unicos = df.drop_duplicates()

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(10, 7), layout="constrained")

sns.boxplot(data=df, x="categoria", y="qtd", ax=axes[0, 0])
axes[0, 0].set_title("Há valores extremos na quantidade? (boxplot)")

sns.countplot(data=pedidos, y="canal", ax=axes[0, 1])
axes[0, 1].set_title("Os canais estão padronizados? (countplot)")

sns.countplot(data=unicos, x="dia", order=nomes, ax=axes[1, 0])
axes[1, 0].set_title("Em que dia vendemos mais? (countplot)")

sns.scatterplot(data=df, x="tempo_entrega_min", y="avaliacao", alpha=0.5, ax=axes[1, 1])
axes[1, 1].set_title("A nota muda com o tempo? (dispersão)")

fig.savefig(BASE / "respostas.png", dpi=120)
print("Pedidos de domingo (sem duplicados):", (unicos["dia"] == "dom").sum())
print("Variações de canal no arquivo bruto:", pedidos["canal"].nunique())
