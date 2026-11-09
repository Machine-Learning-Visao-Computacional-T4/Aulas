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
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

modelo = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))])
modelo.fit(X_treino, y_treino)
print("acurácia no teste:", round(modelo.score(X_teste, y_teste), 3))
y_prev = modelo.predict(X_teste)
print(classification_report(y_teste, y_prev, target_names=["Legítima", "Fraude"]))
print(confusion_matrix(y_teste, y_prev))
# 37 fraudes passaram sem ser detectadas (FN).
