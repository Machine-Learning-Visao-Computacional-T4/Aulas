from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

clientes = pd.read_csv(BASE / "clientes.csv")
pedidos = pd.read_csv(BASE / "pedidos.csv")

# 1) Junta (left: nenhum pedido se perde) e trata o que ficou ausente
base = pedidos.merge(clientes, on="id_cliente", how="left")
base["nome"] = base["nome"].fillna("Cliente não cadastrado")
base["cidade"] = base["cidade"].fillna("Sem cidade")

# 2) Categoria de valor: Alto acima de 500
base["faixa"] = "Baixo"
base.loc[base["valor"] > 500, "faixa"] = "Alto"

# 3) Resumos
total_cidade = base.groupby("cidade")["valor"].sum()
produto_cidade = base.pivot_table(index="produto", columns="cidade",
                                  values="valor", aggfunc="sum", fill_value=0)

total_cidade.to_csv(BASE / "total_por_cidade.csv")
produto_cidade.to_csv(BASE / "produto_por_cidade.csv")

print(base[["id_pedido", "nome", "valor", "faixa"]])
print("\nTotal por cidade:")
print(total_cidade)
print("\nProduto por cidade:")
print(produto_cidade)
