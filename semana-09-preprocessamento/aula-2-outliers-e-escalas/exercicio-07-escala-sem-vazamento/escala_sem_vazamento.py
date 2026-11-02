import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

imoveis = pd.read_csv("arquivos/imoveis_tratado.csv")
treino, teste = train_test_split(imoveis, test_size=0.2, random_state=42)

tudo = StandardScaler().fit(imoveis[["area_m2"]])
so_treino = StandardScaler().fit(treino[["area_m2"]])
print("média com tudo:   ", tudo.mean_.round(2))
print("média só no treino:", so_treino.mean_.round(2))
print("média no teste:   ", teste["area_m2"].mean().round(2))

z_treino = so_treino.transform(treino[["area_m2"]])
z_teste = so_treino.transform(teste[["area_m2"]])
print("treino escalado:", z_treino.mean().round(2), "| teste escalado:", z_teste.mean().round(2))
