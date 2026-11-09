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
from sklearn.metrics import average_precision_score, f1_score, precision_score, recall_score
from sklearn.pipeline import Pipeline
from sklearn.utils.class_weight import compute_class_weight

pesos = compute_class_weight("balanced", classes=np.array([0, 1]), y=y_treino)
print(pesos.round(2))
n = len(y_treino)
print("manual:", round(n / (2 * (y_treino == 0).sum()), 2), round(n / (2 * (y_treino == 1).sum()), 2))

linhas = {}
for nome, cw in [("sem peso", None), ("balanced", "balanced"), ("peso 1:10", {0: 1, 1: 10})]:
    m = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000, class_weight=cw))])
    m.fit(X_treino, y_treino)
    prev, proba = m.predict(X_teste), m.predict_proba(X_teste)[:, 1]
    linhas[nome] = {"precision": precision_score(y_teste, prev, zero_division=0),
                    "recall": recall_score(y_teste, prev), "f1": f1_score(y_teste, prev),
                    "pr_auc": average_precision_score(y_teste, proba)}
print(pd.DataFrame(linhas).T.round(3))
