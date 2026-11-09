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
from sklearn.metrics import average_precision_score, recall_score, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

arvore = Pipeline([("prep", prep), ("clf", DecisionTreeClassifier(random_state=42))]).fit(X_treino, y_treino)
print("árvore, recall no treino:", round(recall_score(y_treino, arvore.predict(X_treino)), 2))
print("árvore, recall no teste: ", round(recall_score(y_teste, arvore.predict(X_teste)), 2))

knn = Pipeline([("prep", prep), ("clf", KNeighborsClassifier(n_neighbors=15))]).fit(X_treino, y_treino)
print("KNN, recall:", round(recall_score(y_teste, knn.predict(X_teste)), 2), "| alertas:", knn.predict(X_teste).sum())

logistica = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))]).fit(X_treino, y_treino)
proba = logistica.predict_proba(X_teste)[:, 1]
print("ROC AUC:", round(roc_auc_score(y_teste, proba), 3))
print("PR AUC: ", round(average_precision_score(y_teste, proba), 3), "| aleatório:", round(y_teste.mean(), 3))
