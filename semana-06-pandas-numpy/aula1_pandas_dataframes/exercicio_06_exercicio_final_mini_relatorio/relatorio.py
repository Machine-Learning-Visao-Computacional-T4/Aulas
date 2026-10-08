from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

df = pd.read_csv(BASE / "vendas.csv")
df["total"] = df["quantidade"] * df["preco"]

# Vendas acima da média do total
media_total = df["total"].mean()
maiores = df[df["total"] > media_total]
maiores.to_csv(BASE / "maiores_que_a_media.csv", index=False)

print(f"Média do total: {media_total:.2f}")
print(f"{len(maiores)} vendas acima da média gravadas em maiores_que_a_media.csv")
print("Categoria mais frequente:", df["categoria"].value_counts().idxmax())
