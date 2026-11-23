# Aula 2 - Exercício 5: qual modelo precisa de mais dados?
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve
from sklearn.tree import DecisionTreeRegressor

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
modelos = {"regressão linear": LinearRegression(), "árvore (profundidade 6)": DecisionTreeRegressor(max_depth=6, random_state=42)}
for nome_do_modelo, modelo in modelos.items():
    tamanhos, erros_treino, erros_validacao = learning_curve(modelo, consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"],
        train_sizes=[0.05, 0.2, 0.5, 1.0], cv=5, scoring="neg_mean_absolute_error", shuffle=True, random_state=42)
    tabela = pd.DataFrame({"linhas": tamanhos, "erro_treino": -erros_treino.mean(axis=1), "erro_validacao": -erros_validacao.mean(axis=1)})
    tabela["lacuna"] = tabela["erro_validacao"] - tabela["erro_treino"]
    print(f"--- {nome_do_modelo}")
    print(tabela.round(1).to_string(index=False))
