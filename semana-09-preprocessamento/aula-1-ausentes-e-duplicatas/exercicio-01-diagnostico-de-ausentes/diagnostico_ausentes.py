import pandas as pd
import numpy as np

bruto = pd.read_csv("arquivos/imoveis_bruto.csv")
print("shape:", bruto.shape)
print("colunas de texto:", bruto.select_dtypes(exclude="number").columns.tolist())
print(bruto["area_m2"].dtype)

imoveis = pd.read_csv("arquivos/imoveis_bruto.csv", na_values=["N/D", "?", "s/i"])
imoveis["idade_anos"] = imoveis["idade_anos"].replace(-1, np.nan)
ausentes = imoveis.isna().sum()
print(ausentes[ausentes > 0])
print((imoveis["idade_anos"].isna().groupby(imoveis["tipo"]).mean() * 100).round(1))
