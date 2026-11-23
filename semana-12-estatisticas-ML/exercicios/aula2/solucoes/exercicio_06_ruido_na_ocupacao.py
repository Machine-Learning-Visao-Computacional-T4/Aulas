# Aula 2 - Exercício 6: ruído na medição da ocupação
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
gerador_aleatorio = np.random.default_rng(seed=42)
for desvio_do_ruido in [0, 10, 20, 40]:
    treino_ruidoso, teste_ruidoso = entradas_treino.copy(), entradas_teste.copy()
    treino_ruidoso["ocupacao_pct"] += gerador_aleatorio.normal(0, desvio_do_ruido, len(treino_ruidoso))
    teste_ruidoso["ocupacao_pct"] += gerador_aleatorio.normal(0, desvio_do_ruido, len(teste_ruidoso))
    modelo = LinearRegression().fit(treino_ruidoso, consumo_treino)
    erro = mean_absolute_error(consumo_teste, modelo.predict(teste_ruidoso))
    print(f"ruído de {desvio_do_ruido:2d} pontos: coeficiente da ocupação = {modelo.coef_[1]:.2f} | erro no teste = {erro:.1f} kWh")
