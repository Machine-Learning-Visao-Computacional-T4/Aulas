from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

clientes = pd.read_csv(BASE / "clientes.csv")
pedidos = pd.read_csv(BASE / "pedidos.csv")

# 1) merge left + nome ausente = pedidos "órfãos"
esquerda = pedidos.merge(clientes, on="id_cliente", how="left")
orfaos = esquerda[esquerda["nome"].isna()]
print("Pedidos sem cliente cadastrado:")
print(orfaos[["id_pedido", "valor"]])

# 2) merge inner + groupby: quantidade e valor total por cidade do cliente
base = pedidos.merge(clientes, on="id_cliente", how="inner")
resumo = base.groupby("cidade")["valor"].agg(["count", "sum"])
resumo.to_csv(BASE / "resumo_cidades.csv")

print("\nResumo por cidade:")
print(resumo)
print("Arquivo resumo_cidades.csv gravado.")
