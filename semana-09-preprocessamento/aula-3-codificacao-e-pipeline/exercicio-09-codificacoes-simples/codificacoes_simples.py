import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

imoveis = pd.read_csv("arquivos/imoveis_tratado.csv")
print(imoveis.select_dtypes(exclude=["number", "bool"]).columns.tolist())

for col in ["aceita_pet", "mobiliado"]:
    imoveis[col + "_num"] = imoveis[col].map({"Não": 0, "Sim": 1})
print(imoveis[["aceita_pet_num", "mobiliado_num"]].isna().sum().sum(), "sem correspondência")

ordem = {"Ruim": 0, "Regular": 1, "Bom": 2, "Ótimo": 3}
imoveis["condicao_num"] = imoveis["condicao"].map(ordem)
enc = OrdinalEncoder(categories=[["Ruim", "Regular", "Bom", "Ótimo"]])
sk = enc.fit_transform(imoveis[["condicao"]]).ravel()
print("map e OrdinalEncoder iguais:", (sk == imoveis["condicao_num"]).all())
print(imoveis["condicao_num"].value_counts().sort_index().to_dict())
