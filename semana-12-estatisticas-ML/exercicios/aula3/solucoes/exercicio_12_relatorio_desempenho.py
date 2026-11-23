# Aula 3 - Exercício 12 (Git e Pull Request): arquivo relatorio_desempenho.py
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.tree import DecisionTreeRegressor

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
modelo_linear = LinearRegression().fit(entradas_treino, consumo_treino)
previsoes = modelo_linear.predict(entradas_teste)
previsoes_baseline = DummyRegressor(strategy="mean").fit(entradas_treino, consumo_treino).predict(entradas_teste)

print("== métricas no teste ==")
print(f"MAE = {mean_absolute_error(consumo_teste, previsoes):.1f} | RMSE = {np.sqrt(mean_squared_error(consumo_teste, previsoes)):.1f} | MAPE = {mean_absolute_percentage_error(consumo_teste, previsoes):.1%} | R² = {r2_score(consumo_teste, previsoes):.3f}")
print(f"baseline: MAE = {mean_absolute_error(consumo_teste, previsoes_baseline):.1f} | R² = {r2_score(consumo_teste, previsoes_baseline):.3f}")

print("\n== validação cruzada (MAE) ==")
divisor_de_validacao = KFold(n_splits=5, shuffle=True, random_state=42)
for nome_do_modelo, modelo in {"baseline": DummyRegressor(), "regressão": LinearRegression(), "árvore (profundidade 4)": DecisionTreeRegressor(max_depth=4, random_state=42)}.items():
    erros = -cross_val_score(modelo, consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], cv=divisor_de_validacao, scoring="neg_mean_absolute_error")
    print(f"{nome_do_modelo:24s} {erros.mean():5.1f} ± {erros.std():.1f} kWh")

print("\n== erro por tipo de dia ==")
analise = entradas_teste[["dia_util"]].copy()
analise["residuo"] = consumo_teste.to_numpy() - previsoes
print(analise.groupby("dia_util")["residuo"].agg(viés="mean", erro_absoluto=lambda residuos: residuos.abs().mean()).round(1))

print("\n== custo com margem de segurança (faltar custa 5, sobrar custa 1) ==")
consumo_real = consumo_teste.to_numpy()
for margem in [0, 20, 40, 60, 80]:
    com_margem = previsoes + margem
    custo = (5 * np.maximum(consumo_real - com_margem, 0) + 1 * np.maximum(com_margem - consumo_real, 0)).mean()
    print(f"margem de {margem:2d} kWh: custo médio = {custo:5.1f}")
