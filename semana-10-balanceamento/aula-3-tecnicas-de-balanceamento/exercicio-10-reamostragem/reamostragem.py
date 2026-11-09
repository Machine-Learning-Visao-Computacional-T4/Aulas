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
from imblearn.under_sampling import RandomUnderSampler

X_prep = prep.fit_transform(X_treino)
print("antes: ", y_treino.value_counts().to_dict())

X_sub, y_sub = RandomUnderSampler(random_state=42).fit_resample(X_prep, y_treino)
print("undersampling:", y_sub.value_counts().to_dict(), X_prep.shape, "->", X_sub.shape)

for estrategia in ["auto", 0.1, 0.5, {0: 600, 1: 139}]:
    _, y_novo = RandomUnderSampler(sampling_strategy=estrategia, random_state=42).fit_resample(X_prep, y_treino)
    print(f"{str(estrategia):18s} -> {y_novo.value_counts().to_dict()}")

X_sup, y_sup = RandomOverSampler(random_state=42).fit_resample(X_prep, y_treino)
print("oversampling:", y_sup.value_counts().to_dict(),
      "| fraudes distintas:", np.unique(X_sup[y_sup == 1], axis=0).shape[0])

X_sm, y_sm = SMOTE(random_state=42).fit_resample(X_prep, y_treino)
print("SMOTE:", y_sm.value_counts().to_dict(),
      "| fraudes distintas:", np.unique(X_sm[y_sm == 1], axis=0).shape[0])
