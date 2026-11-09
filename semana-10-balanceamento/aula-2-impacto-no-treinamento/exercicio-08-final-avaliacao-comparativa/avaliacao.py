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
from sklearn.metrics import (accuracy_score, average_precision_score, f1_score,
                             precision_score, recall_score)
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier


def avaliar(modelo, X_teste, y_teste):
    """Devolve as métricas principais para classes desbalanceadas."""
    prev = modelo.predict(X_teste)
    proba = modelo.predict_proba(X_teste)[:, 1]
    return {"acuracia": accuracy_score(y_teste, prev),
            "precision": precision_score(y_teste, prev, zero_division=0),
            "recall": recall_score(y_teste, prev),
            "f1": f1_score(y_teste, prev),
            "pr_auc": average_precision_score(y_teste, proba)}


modelos = {"logística": LogisticRegression(max_iter=1000),
           "árvore": DecisionTreeClassifier(random_state=42),
           "KNN": KNeighborsClassifier(n_neighbors=15)}
pipes = {nome: Pipeline([("prep", prep), ("clf", m)]) for nome, m in modelos.items()}
linhas = {}
for nome, pipe in pipes.items():
    pipe.fit(X_treino, y_treino)
    linhas[nome] = avaliar(pipe, X_teste, y_teste)
print(pd.DataFrame(linhas).T.round(3))

cv = StratifiedKFold(5, shuffle=True, random_state=1)
r = cross_validate(pipes["logística"], X, y, cv=cv, scoring=["recall", "average_precision"])
print("recall médio:", r["test_recall"].mean().round(3))
print("PR AUC média:", r["test_average_precision"].mean().round(3))
