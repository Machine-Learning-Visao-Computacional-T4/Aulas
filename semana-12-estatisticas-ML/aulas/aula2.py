# Semana 12 - Aula 2: O impacto dos dados no comportamento do modelo
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
consumo_serra = pd.read_csv("arquivos/consumo_campus_serra.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(
    consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)

print("== 1. Mais dados, melhor modelo? ==")
tamanhos_do_treino, erros_treino, erros_validacao = learning_curve(
    estimator=DecisionTreeRegressor(max_depth=6, random_state=42), X=consumo_campus[colunas_de_entrada], y=consumo_campus["consumo_kwh"],
    train_sizes=[0.05, 0.1, 0.2, 0.4, 0.7, 1.0], cv=5, scoring="neg_mean_absolute_error", shuffle=True, random_state=42)
tabela_curva = pd.DataFrame({"linhas_no_treino": tamanhos_do_treino, "erro_treino": -erros_treino.mean(axis=1), "erro_validacao": -erros_validacao.mean(axis=1)})
print(tabela_curva.round(1).to_string(index=False))

print("\n== 2. Ruído na medição da entrada ==")
gerador_aleatorio = np.random.default_rng(seed=42)
for desvio_do_ruido in [0, 2, 4, 8]:
    entradas_treino_ruidosas = entradas_treino.copy()
    entradas_teste_ruidosas = entradas_teste.copy()
    entradas_treino_ruidosas["temperatura_c"] += gerador_aleatorio.normal(0, desvio_do_ruido, len(entradas_treino))
    entradas_teste_ruidosas["temperatura_c"] += gerador_aleatorio.normal(0, desvio_do_ruido, len(entradas_teste))
    modelo = LinearRegression().fit(entradas_treino_ruidosas, consumo_treino)
    erro = mean_absolute_error(consumo_teste, modelo.predict(entradas_teste_ruidosas))
    print(f"ruído de {desvio_do_ruido} °C: coeficiente da temperatura = {modelo.coef_[0]:5.2f} | erro no teste = {erro:.1f} kWh")

print("\n== 3. Dados contaminados e modelos robustos ==")
consumo_contaminado = consumo_treino.copy()
posicoes_com_defeito = gerador_aleatorio.choice(len(consumo_contaminado), size=int(0.03 * len(consumo_contaminado)), replace=False)
consumo_contaminado.iloc[posicoes_com_defeito] *= 5
print(f"linhas com leitura defeituosa (x5): {len(posicoes_com_defeito)} de {len(consumo_contaminado)}")
modelos_comparados = {
    "linear, dados limpos": (LinearRegression(), consumo_treino),
    "linear, dados contaminados": (LinearRegression(), consumo_contaminado),
    "Huber, dados contaminados": (make_pipeline(StandardScaler(), HuberRegressor(epsilon=1.35, max_iter=1000)), consumo_contaminado)}
for nome_do_modelo, (modelo, consumo_usado) in modelos_comparados.items():
    modelo.fit(entradas_treino, consumo_usado)
    erro = mean_absolute_error(consumo_teste, modelo.predict(entradas_teste))
    print(f"{nome_do_modelo:28s} erro no teste = {erro:6.1f} kWh")

print("\n== 4. Colunas irrelevantes ==")
entradas_pequenas = entradas_treino.iloc[:60]
consumo_pequeno = consumo_treino.iloc[:60]
for quantidade_colunas_ruido in [0, 10, 30, 50]:
    colunas_ruido_treino = pd.DataFrame(gerador_aleatorio.normal(size=(60, quantidade_colunas_ruido)), index=entradas_pequenas.index).add_prefix("ruido_")
    colunas_ruido_teste = pd.DataFrame(gerador_aleatorio.normal(size=(len(entradas_teste), quantidade_colunas_ruido)), index=entradas_teste.index).add_prefix("ruido_")
    treino_com_ruido = pd.concat([entradas_pequenas, colunas_ruido_treino], axis=1)
    teste_com_ruido = pd.concat([entradas_teste, colunas_ruido_teste], axis=1)
    modelo = LinearRegression().fit(treino_com_ruido, consumo_pequeno)
    erro_treino = mean_absolute_error(consumo_pequeno, modelo.predict(treino_com_ruido))
    erro_teste = mean_absolute_error(consumo_teste, modelo.predict(teste_com_ruido))
    print(f"{quantidade_colunas_ruido:2d} colunas inúteis: erro no treino = {erro_treino:5.1f} | erro no teste = {erro_teste:5.1f}")

print("\n== 5. Quando os dados mudam: deslocamento de distribuição ==")
print(pd.DataFrame({"campus_principal": consumo_campus[["temperatura_c", "ocupacao_pct", "consumo_kwh"]].mean(),
                    "campus_serra": consumo_serra[["temperatura_c", "ocupacao_pct", "consumo_kwh"]].mean()}).round(1))
estatistica_ks, p_valor_ks = stats.ks_2samp(consumo_campus["temperatura_c"], consumo_serra["temperatura_c"])
print(f"teste KS da temperatura: estatística = {estatistica_ks:.2f} | p-valor = {p_valor_ks:.2g}")
modelo_final = LinearRegression().fit(entradas_treino, consumo_treino)
previsoes_serra = modelo_final.predict(consumo_serra[colunas_de_entrada])
residuos_serra = consumo_serra["consumo_kwh"] - previsoes_serra
print(f"erro no teste do campus principal = {mean_absolute_error(consumo_teste, modelo_final.predict(entradas_teste)):.1f} kWh")
print(f"erro no campus da serra           = {mean_absolute_error(consumo_serra['consumo_kwh'], previsoes_serra):.1f} kWh")
print(f"viés (erro médio com sinal)       = {residuos_serra.mean():+.1f} kWh")

figura, eixos = plt.subplots(1, 2, figsize=(11, 3.6))
eixos[0].plot(tabela_curva["linhas_no_treino"], tabela_curva["erro_treino"], marker="o", color="#3E6B22", label="treino")
eixos[0].plot(tabela_curva["linhas_no_treino"], tabela_curva["erro_validacao"], marker="o", color="#E0605A", label="validação")
eixos[0].set_title("Curva de aprendizado (árvore, profundidade 6)")
eixos[0].set_xlabel("linhas usadas no treino")
eixos[0].set_ylabel("erro médio (kWh)")
eixos[0].legend()
eixos[1].hist(consumo_campus["temperatura_c"], bins=30, alpha=0.6, density=True, color="#78C043", label="campus principal")
eixos[1].hist(consumo_serra["temperatura_c"], bins=30, alpha=0.6, density=True, color="#E7B84E", label="campus da serra")
eixos[1].set_title("A temperatura mudou entre os campi")
eixos[1].set_xlabel("temperatura (°C)")
eixos[1].legend()
figura.tight_layout()
figura.savefig("figuras/a2_dados_e_modelo.png", dpi=150)
