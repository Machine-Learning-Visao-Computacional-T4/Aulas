import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

imoveis = pd.read_csv("arquivos/imoveis_tratado.csv")
area = imoveis[["area_m2"]]

for nome, esc in [("MinMax", MinMaxScaler()), ("Standard", StandardScaler()), ("Robust", RobustScaler())]:
    z = esc.fit_transform(area)
    print(f"{nome:8s} média {z.mean():6.2f}  desvio {z.std():5.2f}  min {z.min():6.2f}  max {z.max():6.2f}")

manual = (area["area_m2"] - area["area_m2"].mean()) / area["area_m2"].std(ddof=0)
sk = StandardScaler().fit_transform(area).ravel()
print("manual igual ao scikit-learn:", np.allclose(manual, sk))

esc = StandardScaler().fit(area)
volta = esc.inverse_transform(esc.transform(area))
print("inverse_transform recupera o original:", np.allclose(volta, area))
