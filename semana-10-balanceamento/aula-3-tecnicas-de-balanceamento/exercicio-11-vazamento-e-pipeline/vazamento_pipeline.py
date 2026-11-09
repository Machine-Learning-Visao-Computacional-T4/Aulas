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
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.tree import DecisionTreeClassifier

# Caminho errado: balancear a base inteira antes de dividir.
X_todo = prep.fit_transform(X)
X_bal, y_bal = RandomOverSampler(random_state=42).fit_resample(X_todo, y)
Xa, Xb, ya, yb = train_test_split(X_bal, y_bal, test_size=0.25, random_state=42)
arv = DecisionTreeClassifier(random_state=42).fit(Xa, ya)
print("recall (errado):", round(recall_score(yb, arv.predict(Xb)), 2))

# Caminho certo: dividir antes e balancear só o treino, dentro do pipeline.
certa = ImbPipeline([("prep", prep), ("amostra", RandomOverSampler(random_state=42)),
                     ("clf", DecisionTreeClassifier(random_state=42))])
certa.fit(X_treino, y_treino)
print("recall (certo):", round(recall_score(y_teste, certa.predict(X_teste)), 2))

smote = ImbPipeline([("prep", prep), ("smote", SMOTE(random_state=42)),
                     ("clf", LogisticRegression(max_iter=1000))]).fit(X_treino, y_treino)
prev = smote.predict(X_teste)
print("SMOTE: precision", round(precision_score(y_teste, prev), 3), "| recall", round(recall_score(y_teste, prev), 3))
# O primeiro recall é enganoso: as cópias das fraudes caíram no treino e no teste.
