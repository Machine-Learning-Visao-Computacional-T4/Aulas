from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

df = pd.read_csv(BASE / "vendas.csv")
df["total"] = df["quantidade"] * df["preco"]

print("1) Total vendido por produto:")
print(df.groupby("produto")["total"].sum())

print("\n2) Preço médio por categoria:")
print(df.groupby("categoria")["preco"].mean())

print("\n3) Quantidade de vendas por cidade:")
print(df.groupby("cidade").size())

print("\n4) Maior venda em cada cidade:")
print(df.groupby("cidade")["total"].max())
