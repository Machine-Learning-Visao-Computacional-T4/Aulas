from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

df = pd.read_csv(BASE / "vendas.csv")


def mostrar(titulo, filtro):
    ids = df[filtro]["id"].tolist()
    print(f"{titulo}: {len(ids)} venda(s) (ids {ids})")


# 1) Vendas de Mouse
mostrar("1) Vendas de Mouse", df["produto"] == "Mouse")

# 2) Vendas em Blumenau com quantidade maior que 3 (cada condição entre parênteses, unidas por &)
mostrar("2) Blumenau com quantidade > 3", (df["cidade"] == "Blumenau") & (df["quantidade"] > 3))

# 3) Produtos que NÃO são da categoria Vídeo (~ nega o filtro)
mostrar("3) Fora da categoria Vídeo", ~(df["categoria"] == "Vídeo"))

# 4) Preço entre 100 e 1000 (between inclui as pontas)
mostrar("4) Preço entre 100 e 1000", df["preco"].between(100, 1000))

# 5) Vendas de Joinville OU de Notebook (| significa "ou")
mostrar("5) Joinville ou Notebook", (df["cidade"] == "Joinville") | (df["produto"] == "Notebook"))
