from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

df["data"] = pd.to_datetime(df["data"])
df["total"] = df["qtd"] * df["preco"]
df["mes"] = df["data"].dt.month
antes = df.copy()

# Decisões
df = df.drop_duplicates()                                        # duplicados: REMOVER
df["canal"] = df["canal"].str.strip().str.title()                # 9 grafias: CORRIGIR
df.loc[df["tempo_entrega_min"] > 120, "tempo_entrega_min"] = np.nan   # 480 min: parece código de erro -> NaN
validos = df[(df["qtd"] >= 1) & (df["qtd"] <= 10)]               # qtd -1 e 40: EXCLUIR do faturamento (investigar)
# id_cliente ausente no balcão e avaliação ausente: MANTER

resumo = pd.DataFrame({
    "linhas": [len(antes), len(df), len(validos)],
    "faturamento": [antes["total"].sum(), df["total"].sum(), validos["total"].sum()],
    "tempo_max": [antes["tempo_entrega_min"].max(), df["tempo_entrega_min"].max(), validos["tempo_entrega_min"].max()],
}, index=["bruto", "limpo", "limpo e só qtd válida"])
print(resumo.round(1))

mensal = pd.DataFrame({
    "bruto": antes.groupby("mes")["total"].sum(),
    "qtd válida": validos.groupby("mes")["total"].sum(),
}).round(0)
print("\nFaturamento por mês:")
print(mensal)
print("\nCanais depois:", sorted(df["canal"].unique()))
