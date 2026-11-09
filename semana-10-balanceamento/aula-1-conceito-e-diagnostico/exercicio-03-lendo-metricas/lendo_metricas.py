import pandas as pd
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (classification_report, confusion_matrix,
                             f1_score, precision_score, recall_score)
from sklearn.model_selection import train_test_split

transacoes = pd.read_csv("arquivos/transacoes.csv")
X = transacoes.drop(columns=["id_transacao", "fraude"])
y = transacoes["fraude"]
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42)

base = DummyClassifier(strategy="most_frequent").fit(X_treino, y_treino)
y_prev = base.predict(X_teste)

vn, fp, fn, vp = confusion_matrix(y_teste, y_prev).ravel()
print("VN", vn, "FP", fp, "FN", fn, "VP", vp)
print("precision:", precision_score(y_teste, y_prev, zero_division=0))
print("recall:   ", recall_score(y_teste, y_prev))
print("f1:       ", f1_score(y_teste, y_prev))
print(classification_report(y_teste, y_prev, target_names=["Legítima", "Fraude"], zero_division=0))
print(f"prejuízo: R$ {fn * 800 + fp * 15:,.0f}".replace(",", "."))
