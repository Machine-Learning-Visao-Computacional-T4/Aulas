from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

df = pd.read_csv(BASE / "vendas.csv")
df["total"] = df["quantidade"] * df["preco"]

# Uma única chamada produz o resumo completo (nome_da_coluna=(coluna, função))
resumo = df.groupby("categoria").agg(
    total_vendido=("total", "sum"),
    itens=("quantidade", "sum"),
    preco_medio=("preco", "mean"),
)

# Do maior para o menor total
resumo = resumo.sort_values("total_vendido", ascending=False)
resumo.to_csv(BASE / "resumo_categorias.csv")

print(resumo)
print("Arquivo resumo_categorias.csv gravado.")
