from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

df = pd.read_csv(BASE / "vendas.csv")

# 1) Conhecendo o dataset
print("Linhas e colunas:", df.shape)
print("Colunas:", df.columns.tolist())
resumo = df[["quantidade", "preco"]].describe()
print(resumo.loc[["count", "mean", "max"]])

# 2) Nova coluna calculada
df["total"] = df["quantidade"] * df["preco"]

# 3) Perguntas
acima = df[df["total"] > 1000]
print("\nVendas acima de R$ 1.000:")
print(acima[["produto", "cidade", "total"]])

filtro = df["cidade"].isin(["Florianópolis", "Blumenau"])
print("\nVendas de Florianópolis ou Blumenau:", len(df[filtro]))

linha_mais_cara = df["preco"].idxmax()
print("Produto mais caro:", df.loc[linha_mais_cara, "produto"])

# 4) Salvando uma das respostas (index=False evita a coluna de índice no arquivo)
acima.to_csv(BASE / "vendas_acima_de_1000.csv", index=False)
print("\nArquivo vendas_acima_de_1000.csv gravado.")
