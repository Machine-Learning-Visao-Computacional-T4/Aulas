import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

imoveis = pd.read_csv("arquivos/imoveis_tratado.csv")
dummies = pd.get_dummies(imoveis, columns=["tipo", "bairro"], drop_first=True, dtype=int)
print(imoveis.shape, "->", dummies.shape)

todas = pd.get_dummies(imoveis["tipo"], dtype=int)
print("soma por linha:", todas.sum(axis=1).unique())

oh = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
oh.fit(imoveis[["tipo"]])
print(oh.get_feature_names_out().tolist())
print(oh.transform(pd.DataFrame({"tipo": ["Casa", "Galpão"]})))

# Em produção: OneHotEncoder, porque guarda as categorias do treino e ignora as inéditas.
