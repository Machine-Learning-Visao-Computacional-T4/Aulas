import csv
from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

# --- Jeito difícil: csv + dicionário + laço (o que você faria na Semana 05) ---
totais = {}
with open(BASE / "vendas.csv", newline="", encoding="utf-8") as f:
    for venda in csv.DictReader(f):
        total = int(venda["quantidade"]) * float(venda["preco"])
        cidade = venda["cidade"]
        if cidade not in totais:
            totais[cidade] = 0
        totais[cidade] += total

print("Jeito difícil (csv + dicionário + laço):")
for cidade, total in sorted(totais.items()):
    print(f"  {cidade}: {total:.1f}")

# --- Com pandas: ler, criar a coluna e agrupar ---
df = pd.read_csv(BASE / "vendas.csv")
df["total"] = df["quantidade"] * df["preco"]
print("\nCom pandas (groupby, que você vai aprender na Aula 2):")
print(df.groupby("cidade")["total"].sum())
