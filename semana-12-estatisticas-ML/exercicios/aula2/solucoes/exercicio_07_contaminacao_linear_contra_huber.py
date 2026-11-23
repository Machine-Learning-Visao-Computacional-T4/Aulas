# Aula 2 - Exercício 7: quanto contaminar até o modelo linear falhar?
import numpy as np
import pandas as pd
from sklearn.linear_model import HuberRegressor, LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
gerador_aleatorio = np.random.default_rng(seed=42)
print("proporção contaminada | erro linear | erro Huber")
for proporcao in [0.0, 0.01, 0.03, 0.10]:
    consumo_contaminado = consumo_treino.copy()
    quantidade = int(proporcao * len(consumo_contaminado))
    if quantidade:
        posicoes = gerador_aleatorio.choice(len(consumo_contaminado), size=quantidade, replace=False)
        consumo_contaminado.iloc[posicoes] *= 5
    erro_linear = mean_absolute_error(consumo_teste, LinearRegression().fit(entradas_treino, consumo_contaminado).predict(entradas_teste))
    modelo_huber = make_pipeline(StandardScaler(), HuberRegressor(epsilon=1.35, max_iter=1000)).fit(entradas_treino, consumo_contaminado)
    erro_huber = mean_absolute_error(consumo_teste, modelo_huber.predict(entradas_teste))
    print(f"{proporcao:>20.0%} | {erro_linear:11.1f} | {erro_huber:10.1f}")
