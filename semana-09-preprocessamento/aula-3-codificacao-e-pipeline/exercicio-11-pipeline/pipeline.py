import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

imoveis = pd.read_csv("arquivos/imoveis_tratado.csv")
X = imoveis.drop(columns=["preco", "id_anuncio", "preco_atipico"])
y = np.log1p(imoveis["preco"])
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_treino.shape, X_teste.shape)


def montar_prep():
    """Monta o ColumnTransformer: escala, ordinal, One-Hot e binárias."""
    numericas = ["area_m2", "quartos", "banheiros", "vagas", "idade_anos", "distancia_praia_km"]
    binarias = ["aceita_pet", "mobiliado", "idade_ausente"]
    return ColumnTransformer([
        ("num", StandardScaler(), numericas),
        ("ord", OrdinalEncoder(categories=[["Ruim", "Regular", "Bom", "Ótimo"]]), ["condicao"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["tipo", "bairro"]),
        ("bin", OrdinalEncoder(categories=[["Não", "Sim"], ["Não", "Sim"], [False, True]]), binarias),
    ])

prep = montar_prep()
Xt_treino = prep.fit_transform(X_treino)
Xt_teste = prep.transform(X_teste)
print(Xt_treino.shape, "|", Xt_teste.shape)

modelo = Pipeline([("prep", montar_prep()), ("regressao", LinearRegression())])
modelo.fit(X_treino, y_treino)
print("R2 no teste:", round(modelo.score(X_teste, y_teste), 3))
