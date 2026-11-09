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
from imblearn.under_sampling import RandomUnderSampler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, f1_score, precision_score, recall_score


def montar(*passos, **extra):
    """Pipeline de pré-processamento, etapas extras e regressão logística."""
    return ImbPipeline([("prep", prep), *passos, ("clf", LogisticRegression(max_iter=1000, **extra))])


def resumo(nome, modelo, X_teste, y_teste):
    """Métricas principais de um modelo."""
    prev, proba = modelo.predict(X_teste), modelo.predict_proba(X_teste)[:, 1]
    return {"técnica": nome, "precision": precision_score(y_teste, prev, zero_division=0),
            "recall": recall_score(y_teste, prev), "f1": f1_score(y_teste, prev),
            "pr_auc": average_precision_score(y_teste, proba)}


def prejuizo(y_real, prev):
    """Custo: R$ 800 por fraude perdida e R$ 15 por falso alarme."""
    fn = ((y_real == 1) & (prev == 0)).sum()
    fp = ((y_real == 0) & (prev == 1)).sum()
    return fn * 800 + fp * 15


tecnicas = {
    "sem técnica": montar(),
    "class_weight": montar(class_weight="balanced"),
    "undersampling": montar(("amostra", RandomUnderSampler(random_state=42))),
    "oversampling": montar(("amostra", RandomOverSampler(random_state=42))),
    "SMOTE": montar(("amostra", SMOTE(random_state=42))),
}
linhas, custos = [], {}
for nome, m in tecnicas.items():
    m.fit(X_treino, y_treino)
    linhas.append(resumo(nome, m, X_teste, y_teste))
    custos[nome] = prejuizo(y_teste, m.predict(X_teste))
print(pd.DataFrame(linhas).set_index("técnica").round(3))
for nome, valor in sorted(custos.items(), key=lambda x: x[1]):
    print(f"{nome:15s} R$ {valor:,.0f}".replace(",", "."))
