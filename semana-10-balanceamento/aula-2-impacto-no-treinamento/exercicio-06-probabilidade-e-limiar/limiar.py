import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

transacoes = pd.read_csv("arquivos/transacoes.csv")
X = transacoes.drop(columns=["id_transacao", "fraude"])
y = transacoes["fraude"]
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numericas = ["valor", "hora", "distancia_residencia_km", "tentativas_24h", "idade_conta_dias"]
prep = ColumnTransformer([("num", StandardScaler(), numericas),
                          ("cat", OneHotEncoder(), ["canal"])], remainder="passthrough")
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.pipeline import Pipeline

modelo = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))]).fit(X_treino, y_treino)
proba = modelo.predict_proba(X_teste)[:, 1]
print("maior probabilidade prevista:", proba.max().round(3))
print("transações acima de 0,5:", (proba > 0.5).sum())

print("limiar precision recall alertas")
for corte in [0.5, 0.3, 0.2, 0.1, 0.05]:
    prev = (proba >= corte).astype(int)
    p, r = precision_score(y_teste, prev), recall_score(y_teste, prev)
    print(f"{corte:6.2f} {p:9.2f} {r:6.2f} {prev.sum():7d}")
# Escolha: 0,10 (80 alertas, dentro do limite de 100), recall 0,57.
