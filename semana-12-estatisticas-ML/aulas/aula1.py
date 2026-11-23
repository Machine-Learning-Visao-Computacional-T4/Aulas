# Semana 12 - Aula 1: A estatística como lente para dados e modelos
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv", parse_dates=["data"])
gerador_aleatorio = np.random.default_rng(seed=42)

print("== 1. Os dados do campus ==")
print(consumo_campus.shape)
print(consumo_campus[["data", "temperatura_c", "ocupacao_pct", "dia_util", "consumo_kwh"]].head(3))
print(consumo_campus["consumo_kwh"].describe().round(1))

print("\n== 2. População e amostra ==")
consumo_populacao = consumo_campus["consumo_kwh"]
media_populacao = consumo_populacao.mean()
amostra_de_30_dias = consumo_populacao.sample(n=30, random_state=42)
print(f"média da população (730 dias) = {media_populacao:.1f} kWh")
print(f"média de UMA amostra de 30 dias = {amostra_de_30_dias.mean():.1f} kWh")
medias_das_amostras = [consumo_populacao.sample(n=30, random_state=repeticao).mean() for repeticao in range(1000)]
medias_das_amostras = pd.Series(medias_das_amostras)
print(f"1000 amostras: média das médias = {medias_das_amostras.mean():.1f} | desvio das médias = {medias_das_amostras.std():.1f}")
erro_padrao_teorico = consumo_populacao.std() / np.sqrt(30)
print(f"erro padrão teórico (desvio / raiz de 30) = {erro_padrao_teorico:.1f}")

print("\n== 3. Incerteza da estimativa: bootstrap ==")
valores_da_amostra = amostra_de_30_dias.to_numpy()
medias_bootstrap = [gerador_aleatorio.choice(valores_da_amostra, size=30, replace=True).mean() for repeticao in range(2000)]
limite_inferior, limite_superior = np.percentile(medias_bootstrap, [2.5, 97.5])
print(f"média estimada = {valores_da_amostra.mean():.1f} kWh")
print(f"intervalo de 95% (bootstrap) = [{limite_inferior:.1f}; {limite_superior:.1f}]")
print(f"a média real {media_populacao:.1f} está dentro do intervalo? {limite_inferior <= media_populacao <= limite_superior}")

print("\n== 4. Sinal e ruído ==")
consumo_por_tipo_de_dia = consumo_campus.groupby("dia_util")["consumo_kwh"].agg(["mean", "std", "count"]).round(1)
print(consumo_por_tipo_de_dia)
faixa_de_temperatura = pd.qcut(consumo_campus["temperatura_c"], q=4)
print(consumo_campus.groupby(faixa_de_temperatura, observed=True)["consumo_kwh"].agg(["mean", "std"]).round(1))

print("\n== 5. Aprender é estimar ==")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(
    consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
modelo_linear = LinearRegression()
modelo_linear.fit(entradas_treino, consumo_treino)
print(f"intercepto = {modelo_linear.intercept_:.1f}")
for nome_coluna, coeficiente in zip(colunas_de_entrada, modelo_linear.coef_):
    print(f"{nome_coluna:15s} coeficiente = {coeficiente:6.2f}")
dia_novo = pd.DataFrame({"temperatura_c": [28.0], "ocupacao_pct": [80], "dia_util": [1], "evento": [0]})
print(f"previsão para o dia novo = {modelo_linear.predict(dia_novo)[0]:.1f} kWh")

print("\n== 6. O baseline estatístico ==")
modelo_baseline = DummyRegressor(strategy="mean")
modelo_baseline.fit(entradas_treino, consumo_treino)
erro_baseline = mean_absolute_error(consumo_teste, modelo_baseline.predict(entradas_teste))
erro_modelo = mean_absolute_error(consumo_teste, modelo_linear.predict(entradas_teste))
print(f"baseline (sempre a média = {modelo_baseline.constant_[0][0]:.1f} kWh): erro médio = {erro_baseline:.1f} kWh")
print(f"regressão linear: erro médio = {erro_modelo:.1f} kWh")
print(f"redução do erro = {1 - erro_modelo / erro_baseline:.1%}")

print("\n== 7. O modelo como média condicional ==")
dias_parecidos = consumo_campus[(consumo_campus["temperatura_c"].between(26, 30)) & (consumo_campus["ocupacao_pct"].between(70, 90))
                                & (consumo_campus["dia_util"] == 1) & (consumo_campus["evento"] == 0)]
print(f"dias parecidos com o dia novo: {len(dias_parecidos)}")
print(f"média real desses dias = {dias_parecidos['consumo_kwh'].mean():.1f} kWh")
print(f"previsão do modelo       = {modelo_linear.predict(dia_novo)[0]:.1f} kWh")

figura, eixos = plt.subplots(1, 2, figsize=(11, 3.6))
eixos[0].hist(medias_das_amostras, bins=30, color="#78C043", edgecolor="white")
eixos[0].axvline(media_populacao, color="#1A1A1A", linestyle="--", label="média da população")
eixos[0].set_title("Médias de 1000 amostras de 30 dias")
eixos[0].set_xlabel("média da amostra (kWh)")
eixos[0].legend()
eixos[1].scatter(consumo_campus["temperatura_c"], consumo_campus["consumo_kwh"], s=8, alpha=0.4, color="#3E6B22")
eixos[1].set_title("Consumo e temperatura: sinal + ruído")
eixos[1].set_xlabel("temperatura (°C)")
eixos[1].set_ylabel("consumo (kWh)")
figura.tight_layout()
figura.savefig("figuras/a1_amostragem.png", dpi=150)
