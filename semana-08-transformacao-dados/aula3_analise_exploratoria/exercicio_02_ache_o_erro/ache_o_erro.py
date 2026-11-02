from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

colunas = ["qtd", "avaliacao", "tempo_entrega_min", "preco"]
print(df[colunas].describe().round(1))

print("\nQuantidade por pedido:")
print(df["qtd"].value_counts().sort_index())

print("\nImpossível (qtd < 1):", len(df[df["qtd"] < 1]), "pedidos")
print("Suspeito (qtd > 10):  ", len(df[df["qtd"] > 10]), "pedidos")
print("Tempo de entrega máximo:", df["tempo_entrega_min"].max(), "min | mediana:", df["tempo_entrega_min"].median(), "min")
