from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab
import numpy as np


def preparar_pedidos(pedidos, produtos, clientes):
    """Recebe as 3 tabelas brutas e devolve a tabela pronta, sem alterar as originais."""
    return (
        pedidos
        # 1) tipos e texto: data vira data, canal padronizado
        .assign(data=lambda d: pd.to_datetime(d["data"]),
                canal=lambda d: d["canal"].str.strip().str.title())
        # 2) partes da data
        .assign(mes=lambda d: d["data"].dt.month,
                dia_semana=lambda d: d["data"].dt.dayofweek)
        # 3) junções seguras: nenhuma linha pode aparecer ou sumir
        .merge(produtos, on="id_produto", how="left", validate="m:1")
        .merge(clientes, on="id_cliente", how="left", validate="m:1")
        # 4) contas entre colunas
        .assign(total=lambda d: d["qtd"] * d["preco"],
                lucro=lambda d: d["qtd"] * (d["preco"] - d["custo"]))
        # 5) classificações
        .assign(pedido_grande=lambda d: np.where(d["qtd"] >= 3, "sim", "não"),
                perfil=lambda d: np.select(
                    [d["avaliacao"] >= 4, d["avaliacao"] == 3, d["avaliacao"] <= 2],
                    ["satisfeito", "neutro", "insatisfeito"],
                    default="sem nota"))
    )


pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
clientes = pd.read_csv(BASE / "clientes.csv")

pronto = preparar_pedidos(pedidos, produtos, clientes)
assert len(pronto) == len(pedidos), "o pipeline não pode criar nem perder linhas"

pronto.to_csv(BASE / "pedidos_prontos.csv", index=False)

print(pronto.shape)
print(pronto[["id_pedido", "canal", "produto", "plano", "total", "perfil"]].head(3))
print("Faturamento bruto:", round(pronto["total"].sum(), 2), "| lucro bruto:", round(pronto["lucro"].sum(), 2))
print("Arquivo pedidos_prontos.csv gravado.")
