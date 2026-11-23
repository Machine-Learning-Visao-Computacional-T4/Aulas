# Aula 3 - Exercício 9: calcular as métricas sem o scikit-learn e conferir
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
previsoes = LinearRegression().fit(entradas_treino, consumo_treino).predict(entradas_teste)

consumo_real = consumo_teste.to_numpy()
residuos = consumo_real - previsoes
mae_manual = np.abs(residuos).mean()
mse_manual = (residuos ** 2).mean()
rmse_manual = np.sqrt(mse_manual)
soma_quadrados_do_modelo = (residuos ** 2).sum()
soma_quadrados_total = ((consumo_real - consumo_real.mean()) ** 2).sum()
r2_manual = 1 - soma_quadrados_do_modelo / soma_quadrados_total
print(f"MAE  manual = {mae_manual:.3f} | scikit-learn = {mean_absolute_error(consumo_real, previsoes):.3f}")
print(f"MSE  manual = {mse_manual:.1f} | scikit-learn = {mean_squared_error(consumo_real, previsoes):.1f}")
print(f"RMSE manual = {rmse_manual:.3f}")
print(f"R²   manual = {r2_manual:.4f} | scikit-learn = {r2_score(consumo_real, previsoes):.4f}")
print(f"os valores coincidem? {np.isclose(mae_manual, mean_absolute_error(consumo_real, previsoes)) and np.isclose(r2_manual, r2_score(consumo_real, previsoes))}")
