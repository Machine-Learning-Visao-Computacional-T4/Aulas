from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab
import numpy as np

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")

pedidos["data"] = pd.to_datetime(pedidos["data"])
pedidos["canal"] = pedidos["canal"].str.strip().str.title()
df = pedidos.merge(produtos, on="id_produto", how="left", validate="m:1")
df["total"] = df["qtd"] * df["preco"]

# 1) Nota 5 = "ótimo", o resto = "ok"  ->  duas saídas: np.where
df["destaque"] = np.where(df["avaliacao"] == 5, "ótimo", "ok")
print("1)", df["destaque"].value_counts().to_dict())

# 2) Satisfeito, neutro ou insatisfeito  ->  várias regras: np.select
condicoes = [df["avaliacao"] >= 4, df["avaliacao"] == 3, df["avaliacao"] <= 2]
df["perfil"] = np.select(condicoes, ["satisfeito", "neutro", "insatisfeito"], default="sem nota")
print("2)", df["perfil"].value_counts().to_dict())

# 3) 10% de desconto só nos pedidos do App  ->  alterar só algumas linhas: .loc
df["total_final"] = df["total"]
df.loc[df["canal"] == "App", "total_final"] = df["total"] * 0.9
print("3)", f"total sem desconto: {df['total'].sum():.2f} | com desconto no App: {df['total_final'].sum():.2f}")

# 4) Entrega rápida, média ou lenta  ->  número vira faixa: pd.cut
df["velocidade"] = pd.cut(df["tempo_entrega_min"], bins=[0, 30, 45, np.inf], labels=["rápida", "média", "lenta"])
print("4)", df["velocidade"].value_counts().sort_index().to_dict())

# 5) Pedidos de sábado ou domingo  ->  valor está em uma lista: isin
df["fim_de_semana"] = df["data"].dt.dayofweek.isin([5, 6])
print("5)", df["fim_de_semana"].value_counts().to_dict())

# 6) Trocar o código do produto pelo nome  ->  dicionário: map
nomes = dict(zip(produtos["id_produto"], produtos["produto"]))
df["nome_produto"] = df["id_produto"].map(nomes)
print("6)", df[["id_produto", "nome_produto"]].head(3).values.tolist())
