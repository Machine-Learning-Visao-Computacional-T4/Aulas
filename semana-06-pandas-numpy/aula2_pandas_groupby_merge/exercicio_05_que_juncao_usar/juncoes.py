from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

clientes = pd.read_csv(BASE / "clientes.csv")
pedidos = pd.read_csv(BASE / "pedidos.csv")

print(f"{len(clientes)} clientes e {len(pedidos)} pedidos\n")

# Quantas linhas cada tipo de junção devolve?
for como in ["inner", "left", "right", "outer"]:
    juncao = pedidos.merge(clientes, on="id_cliente", how=como)
    print(f"{como:<6} -> {len(juncao)} linhas")

# Pedidos sem cliente cadastrado: left + nome ausente
esquerda = pedidos.merge(clientes, on="id_cliente", how="left")
print("\nPedidos sem cliente cadastrado (left + nome ausente):")
print(esquerda[esquerda["nome"].isna()][["id_pedido", "id_cliente", "valor"]])

# Clientes que nunca compraram: right + pedido ausente
direita = pedidos.merge(clientes, on="id_cliente", how="right")
print("\nClientes que nunca compraram (right + pedido ausente):")
print(direita[direita["id_pedido"].isna()][["id_cliente", "nome"]])
