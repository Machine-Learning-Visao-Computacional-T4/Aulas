import pandas as pd
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split

transacoes = pd.read_csv("arquivos/transacoes.csv")
X = transacoes.drop(columns=["id_transacao", "fraude"])
y = transacoes["fraude"]
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42)
print(X_treino.shape, X_teste.shape)
print("fraudes no treino:", y_treino.sum(), "| no teste:", y_teste.sum())

for semente in [1, 2, 3]:
    _, _, _, y_t = train_test_split(X, y, test_size=0.25, random_state=semente)
    print("semente", semente, "-> fraudes no teste sem stratify:", y_t.sum())

base = DummyClassifier(strategy="most_frequent")
base.fit(X_treino, y_treino)
print("acurácia:", round(base.score(X_teste, y_teste), 3))
print("previsões distintas:", np.unique(base.predict(X_teste)))
