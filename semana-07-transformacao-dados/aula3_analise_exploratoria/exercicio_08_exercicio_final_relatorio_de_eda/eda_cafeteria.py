from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

pasta = BASE / "graficos"
pasta.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")

# ---- Passo 1: tamanho e tipos ----
print("== 1. Tamanho e tipos ==")
print(df.shape)
print(df.dtypes.to_string())

# ---- Passo 2: ausentes e duplicados ----
print("\n== 2. Ausentes e duplicados ==")
tabela = pd.DataFrame({"nulos": df.isna().sum(), "pct": (df.isna().mean() * 100).round(1)})
print(tabela[tabela["nulos"] > 0])
print(df.duplicated().sum(), "linhas duplicadas")

# ---- Passo 3: categorias ----
print("\n== 3. Categorias ==")
print(df["canal"].nunique(), "grafias de canal")
print(df["canal"].value_counts().head(3))

# Correções essenciais (tipos, texto e período)
df["data"] = pd.to_datetime(df["data"])
df["canal"] = df["canal"].str.strip().str.title()
df["total"] = df["qtd"] * df["preco"]
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.dayofweek
nomes = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
df["dia"] = df["dia_semana"].map(dict(enumerate(nomes)))
print("Canais depois:", df["canal"].nunique())

# ---- Passo 4: números ----
print("\n== 4. Números ==")
print(df[["qtd", "avaliacao", "tempo_entrega_min", "preco"]].describe().round(1))
t = df["tempo_entrega_min"].dropna()
q1, q3 = t.quantile([0.25, 0.75])
limite = q3 + 1.5 * (q3 - q1)
print(f"Regra do IQR: limite {limite:.1f} min | {(df['tempo_entrega_min'] > limite).sum()} pedidos acima")

plt.figure(figsize=(5, 3.6))
sns.boxplot(data=df, x="categoria", y="qtd")
plt.title("Quantidade por categoria")
plt.savefig(pasta / "boxplot_qtd.png", dpi=120)
plt.close()

bom = df[df["tempo_entrega_min"] < 120]
plt.figure(figsize=(5, 3.6))
sns.histplot(bom["tempo_entrega_min"], bins=15)
plt.title("Tempo de entrega (abaixo de 120 min)")
plt.savefig(pasta / "histograma_tempo.png", dpi=120)
plt.close()

# ---- Passo 5: tempo ----
print("\n== 5. Tempo ==")
unicos = df.drop_duplicates()
print(unicos["dia"].value_counts().reindex(nomes).to_string())
por_mes = unicos.groupby(["mes", "categoria"]).size().unstack()
print(por_mes)

plt.figure(figsize=(5, 3.6))
por_mes.plot(marker="o")
plt.ylabel("pedidos")
plt.title("Pedidos por categoria e mês")
plt.savefig(pasta / "pedidos_por_mes.png", dpi=120)
plt.close()

# ---- Passo 6: relações ----
print("\n== 6. Relações ==")
cols = ["qtd", "avaliacao", "tempo_entrega_min", "total"]
r1 = df["tempo_entrega_min"].corr(df["avaliacao"])
r2 = bom["tempo_entrega_min"].corr(bom["avaliacao"])
print(f"Correlação tempo x nota: com os 480 min {r1:.2f} | sem eles {r2:.2f}")

plt.figure(figsize=(5, 3.6))
sns.heatmap(bom[cols].corr(), annot=True, cmap="Greens", vmin=-1, vmax=1)
plt.title("Correlações (tempo abaixo de 120 min)")
plt.savefig(pasta / "heatmap_correlacoes.png", dpi=120, bbox_inches="tight")
plt.close()

# ---- Passo 7: registro dos problemas ----
print("\n== 7. Registro ==")
registro = pd.DataFrame([
    ("Linhas duplicadas", df.duplicated().sum(), "Remover com drop_duplicates()"),
    ("Quantidade inválida (< 1 ou > 10)", ((df["qtd"] < 1) | (df["qtd"] > 10)).sum(), "Investigar com o negócio; excluir do faturamento"),
    ("Tempo de entrega acima de 120 min", (df["tempo_entrega_min"] > 120).sum(), "Tratar como nulo se for código de erro"),
    ("Delivery sem tempo", df.loc[df["canal"] == "Delivery", "tempo_entrega_min"].isna().sum(), "Manter e avisar que faltam dados"),
    ("Pedidos sem cliente", df["id_cliente"].isna().sum(), "Manter: vendas de balcão não identificadas"),
    ("Pedidos sem avaliação", df["avaliacao"].isna().sum(), "Manter; não imputar a nota"),
], columns=["problema", "quantos", "decisao"])
print(registro.to_string(index=False))
registro.to_csv(BASE / "registro_problemas.csv", index=False)
print("Arquivo registro_problemas.csv gravado.")
