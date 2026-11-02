from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab
import numpy as np

pedidos = pd.read_csv(BASE / "pedidos.csv")

# Colunas do exercício anterior
pedidos["data"] = pd.to_datetime(pedidos["data"])
pedidos["dia_semana"] = pedidos["data"].dt.dayofweek
pedidos["canal"] = pedidos["canal"].str.strip().str.title()

# np.where: duas saídas
pedidos["pedido_grande"] = np.where(pedidos["qtd"] >= 3, "sim", "não")

# np.select: várias regras (vale a primeira verdadeira) + default
condicoes = [
    pedidos["avaliacao"] >= 4,
    pedidos["avaliacao"] == 3,
    pedidos["avaliacao"] <= 2,
]
rotulos = ["satisfeito", "neutro", "insatisfeito"]
pedidos["perfil"] = np.select(condicoes, rotulos, default="sem nota")

# .loc com máscara: altera só algumas linhas
pedidos["taxa_entrega"] = 0.0
pedidos.loc[pedidos["canal"] == "Delivery", "taxa_entrega"] = 4.5

# pd.cut: número vira faixa
pedidos["faixa_tempo"] = pd.cut(
    pedidos["tempo_entrega_min"],
    bins=[0, 20, 30, 45, np.inf],
    labels=["até 20", "21-30", "31-45", "mais de 45"],
)

# isin + np.where
sexta_a_domingo = pedidos["dia_semana"].isin([4, 5, 6])
pedidos["periodo"] = np.where(sexta_a_domingo, "sex-dom", "seg-qui")

for coluna in ["pedido_grande", "perfil", "periodo"]:
    print(pedidos[coluna].value_counts(), "\n")
print(pedidos.groupby("canal")["taxa_entrega"].agg(["min", "max"]), "\n")
print(pedidos["faixa_tempo"].value_counts().sort_index())

# Atenção: qualquer comparação com NaN dá False, por isso quem não tem nota cai no default
print("\nSem avaliação:", pedidos["avaliacao"].isna().sum(), "| 'sem nota':", (pedidos["perfil"] == "sem nota").sum())

# E/OU em Series: & e | com parênteses (nunca and/or)
mask = (pedidos["qtd"] >= 2) & (pedidos["canal"] == "App")
print(mask.sum(), "pedidos com 2+ itens pelo App")
