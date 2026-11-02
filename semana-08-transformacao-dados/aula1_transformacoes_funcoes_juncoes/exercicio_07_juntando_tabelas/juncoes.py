from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
clientes = pd.read_csv(BASE / "clientes.csv")
print(pedidos.shape, produtos.shape, clientes.shape)

# 1) pedidos + produtos: cada produto aparece uma vez (muitos pedidos para um produto)
base = pedidos.merge(produtos, on="id_produto", how="left", validate="m:1")
print(pedidos.shape, "->", base.shape)

# 2) + clientes: left mantém todos os pedidos; indicator mostra quem achou par
base = base.merge(clientes, on="id_cliente", how="left", validate="m:1", indicator=True)
print(base["_merge"].value_counts())
print(pedidos["id_cliente"].isna().sum(), "pedidos sem cliente (balcão não identificado)")

# 3) inner x left: conte as linhas
print("left:", len(pedidos.merge(clientes, on="id_cliente", how="left")),
      "| inner:", len(pedidos.merge(clientes, on="id_cliente", how="inner")))

# 4) Com preço e custo ao lado de cada pedido, total e lucro são contas entre colunas
base["total"] = base["qtd"] * base["preco"]
base["lucro"] = base["qtd"] * (base["preco"] - base["custo"])
print(base[["produto", "qtd", "preco", "total", "lucro"]].head(3))
print(base.groupby("categoria")["lucro"].sum().round(0))

# Extra: o que acontece quando a chave se repete e não há validate
duplicado = pd.concat([produtos, produtos.head(2)])
print("\nSem validate:", len(pedidos), "->", len(pedidos.merge(duplicado, on="id_produto")), "linhas")
