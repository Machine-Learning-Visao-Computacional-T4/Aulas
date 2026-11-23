# Aula 1 - Exercício 4 (Git e Pull Request): arquivo estatistica_amostras.py
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
gerador_aleatorio = np.random.default_rng(seed=42)

umidade_populacao = consumo_campus["umidade_pct"]
medias_das_amostras = pd.Series([umidade_populacao.sample(n=30, random_state=repeticao).mean() for repeticao in range(1000)])
print(f"umidade: desvio das médias = {medias_das_amostras.std():.2f} | erro padrão teórico = {umidade_populacao.std() / np.sqrt(30):.2f}")

amostra_de_ocupacao = consumo_campus["ocupacao_pct"].sample(n=40, random_state=42).to_numpy()
medianas_bootstrap = [np.median(gerador_aleatorio.choice(amostra_de_ocupacao, size=40, replace=True)) for _ in range(2000)]
limite_inferior, limite_superior = np.percentile(medianas_bootstrap, [2.5, 97.5])
print(f"mediana da ocupação (amostra de 40 dias) = {np.median(amostra_de_ocupacao):.1f} | intervalo 95% = [{limite_inferior:.1f}; {limite_superior:.1f}]")

entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(consumo_campus[["temperatura_c"]], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
erro_baseline = mean_absolute_error(consumo_teste, DummyRegressor(strategy="mean").fit(entradas_treino, consumo_treino).predict(entradas_teste))
erro_linear = mean_absolute_error(consumo_teste, LinearRegression().fit(entradas_treino, consumo_treino).predict(entradas_teste))
print(f"baseline = {erro_baseline:.1f} kWh | regressão só com temperatura = {erro_linear:.1f} kWh | redução = {1 - erro_linear / erro_baseline:.1%}")
