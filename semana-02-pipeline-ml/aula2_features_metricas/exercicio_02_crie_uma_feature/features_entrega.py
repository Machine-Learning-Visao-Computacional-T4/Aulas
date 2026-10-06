"""Cria features derivadas em um dataset FICTÍCIO de pedidos de entrega."""
import pandas as pd

pedidos = pd.DataFrame(
    {
        "cliente_id": [1, 1, 2, 3, 3, 3, 4, 5],
        "hora_pedido": [12, 20, 19, 8, 13, 21, 3, 18],
        "distancia_km": [2.0, 7.5, 3.2, 1.1, 4.0, 9.0, 12.0, 2.5],
        "valor_pedido": [45.0, 80.0, 30.0, 18.0, 52.0, 110.0, 25.0, 60.0],
        "pedidos_anteriores": [10, 11, 2, 25, 26, 27, 0, 5],
    }
)

print("=== Variáveis brutas ===")
print(pedidos, "\n")

# Feature 1: pedido em horário de pico? (almoço 11-14h ou jantar 18-21h)
pedidos["horario_pico"] = pedidos["hora_pedido"].apply(
    lambda h: 11 <= h <= 14 or 18 <= h <= 21
)

# Feature 2: valor médio por pedido do cliente (olhando o dataset todo, é só um exemplo)
pedidos["valor_medio_cliente"] = pedidos.groupby("cliente_id")["valor_pedido"].transform("mean")

# Feature 3: cliente novo? (nenhum pedido anterior)
pedidos["cliente_novo"] = pedidos["pedidos_anteriores"] == 0

# Feature 4: valor por quilômetro rodado
pedidos["valor_por_km"] = (pedidos["valor_pedido"] / pedidos["distancia_km"]).round(2)

# SUA FEATURE AQUI -------------------------------------------------
# Exemplo de ideia: entrega de madrugada? (hora entre 0 e 5)
# pedidos["madrugada"] = pedidos["hora_pedido"] <= 5
# -------------------------------------------------------------------

print("=== Com features derivadas ===")
print(pedidos.to_string())
