from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

print(f"1) Quantas linhas e colunas? {df.shape[0]} x {df.shape[1]}")

print("\n2) Que tipo tem cada coluna?")
print(df.dtypes.to_string())

print("\n3) O que está faltando?")
nulos = df.isna().sum()
print(nulos[nulos > 0].to_string())

print("\n4) Há linhas repetidas?", df.duplicated().sum())

print("\n5) Há valores estranhos? (mínimo e máximo)")
print(df[["qtd", "tempo_entrega_min"]].agg(["min", "max"]))
