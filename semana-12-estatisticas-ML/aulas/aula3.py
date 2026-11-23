# Semana 12 - Aula 3: Noções intuitivas de erro e desempenho
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeRegressor

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(
    consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
modelo_linear = LinearRegression().fit(entradas_treino, consumo_treino)
previsoes_teste = modelo_linear.predict(entradas_teste)

print("== 1. O erro de cada previsão: o resíduo ==")
tabela_residuos = pd.DataFrame({"real_kwh": consumo_teste.iloc[:5].to_numpy(), "previsto_kwh": previsoes_teste[:5].round(1)})
tabela_residuos["residuo_kwh"] = (tabela_residuos["real_kwh"] - tabela_residuos["previsto_kwh"]).round(1)
print(tabela_residuos)
residuos_teste = consumo_teste.to_numpy() - previsoes_teste
print(f"média dos resíduos (com sinal) = {residuos_teste.mean():+.2f} kWh")
print(f"média dos resíduos em módulo   = {np.abs(residuos_teste).mean():.2f} kWh")

print("\n== 2. MAE, MSE, RMSE, MAPE e R² ==")
erro_absoluto_medio = mean_absolute_error(consumo_teste, previsoes_teste)
erro_quadratico_medio = mean_squared_error(consumo_teste, previsoes_teste)
raiz_do_erro_quadratico = np.sqrt(erro_quadratico_medio)
erro_percentual_medio = mean_absolute_percentage_error(consumo_teste, previsoes_teste)
coeficiente_de_determinacao = r2_score(consumo_teste, previsoes_teste)
print(f"MAE  = {erro_absoluto_medio:.1f} kWh")
print(f"MSE  = {erro_quadratico_medio:.1f} kWh²")
print(f"RMSE = {raiz_do_erro_quadratico:.1f} kWh")
print(f"MAPE = {erro_percentual_medio:.1%}")
print(f"R²   = {coeficiente_de_determinacao:.3f}")
previsoes_com_um_erro_grande = previsoes_teste.copy()
previsoes_com_um_erro_grande[0] += 400
mae_com_erro_grande = mean_absolute_error(consumo_teste, previsoes_com_um_erro_grande)
rmse_com_erro_grande = np.sqrt(mean_squared_error(consumo_teste, previsoes_com_um_erro_grande))
print(f"com UM erro de 400 kWh: MAE = {mae_com_erro_grande:.1f} | RMSE = {rmse_com_erro_grande:.1f}")

print("\n== 3. O R² e o baseline ==")
previsoes_baseline = DummyRegressor(strategy="mean").fit(entradas_treino, consumo_treino).predict(entradas_teste)
soma_erros_modelo = ((consumo_teste - previsoes_teste) ** 2).sum()
soma_erros_baseline = ((consumo_teste - previsoes_baseline) ** 2).sum()
print(f"R² do baseline (sempre a média) = {r2_score(consumo_teste, previsoes_baseline):.3f}")
print(f"R² do modelo = 1 - {soma_erros_modelo:,.0f} / {soma_erros_baseline:,.0f} = {1 - soma_erros_modelo / soma_erros_baseline:.3f}")

print("\n== 4. Treino x teste: subajuste e superajuste ==")
dias_comparaveis = consumo_campus[(consumo_campus["dia_util"] == 1) & (consumo_campus["evento"] == 0) & (consumo_campus["ocupacao_pct"].between(45, 65))]
temperatura_do_recorte = dias_comparaveis[["temperatura_c"]]
consumo_do_recorte = dias_comparaveis["consumo_kwh"]
temperatura_treino, temperatura_teste, consumo_treino_pequeno, consumo_teste_recorte = train_test_split(
    temperatura_do_recorte, consumo_do_recorte, train_size=15, random_state=42)
print(f"dias comparáveis: {len(dias_comparaveis)} | treino = {len(temperatura_treino)} | teste = {len(temperatura_teste)}")
linhas_da_tabela = []
for grau_do_polinomio in [1, 2, 4, 8, 12]:
    modelo_polinomial = make_pipeline(PolynomialFeatures(degree=grau_do_polinomio, include_bias=False), StandardScaler(), LinearRegression())
    modelo_polinomial.fit(temperatura_treino, consumo_treino_pequeno)
    linhas_da_tabela.append({"grau": grau_do_polinomio,
        "erro_treino": mean_absolute_error(consumo_treino_pequeno, modelo_polinomial.predict(temperatura_treino)),
        "erro_teste": mean_absolute_error(consumo_teste_recorte, modelo_polinomial.predict(temperatura_teste))})
tabela_complexidade = pd.DataFrame(linhas_da_tabela)
print(tabela_complexidade.round(1).to_string(index=False))

print("\n== 5. O desempenho também varia: validação cruzada ==")
erros_por_divisao = []
for semente in range(10):
    entradas_a, entradas_b, consumo_a, consumo_b = train_test_split(consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=semente)
    erros_por_divisao.append(mean_absolute_error(consumo_b, LinearRegression().fit(entradas_a, consumo_a).predict(entradas_b)))
print(f"10 divisões treino/teste diferentes: MAE de {min(erros_por_divisao):.1f} a {max(erros_por_divisao):.1f} kWh")
divisor_de_validacao = KFold(n_splits=5, shuffle=True, random_state=42)
modelos_para_comparar = {"baseline (média)": DummyRegressor(strategy="mean"), "regressão linear": LinearRegression(), "árvore (profundidade 4)": DecisionTreeRegressor(max_depth=4, random_state=42)}
for nome_do_modelo, modelo in modelos_para_comparar.items():
    erros = -cross_val_score(modelo, consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], cv=divisor_de_validacao, scoring="neg_mean_absolute_error")
    print(f"{nome_do_modelo:24s} MAE = {erros.mean():5.1f} ± {erros.std():.1f} kWh")

print("\n== 6. Onde o modelo erra ==")
analise_de_erros = entradas_teste.copy()
analise_de_erros["residuo"] = residuos_teste
analise_de_erros["faixa_de_temperatura"] = pd.qcut(analise_de_erros["temperatura_c"], q=4)
print(analise_de_erros.groupby("faixa_de_temperatura", observed=True)["residuo"].agg(erro_medio_com_sinal="mean", erro_absoluto=lambda residuos: residuos.abs().mean()).round(1))
print(f"percentil 90 do erro absoluto = {np.percentile(np.abs(residuos_teste), 90):.1f} kWh")

print("\n== 7. Erro e decisão: o custo não é simétrico ==")
custo_por_kwh_subestimado, custo_por_kwh_superestimado = 3.0, 1.0
for margem_de_seguranca in [0, 10, 20, 30, 50]:
    previsoes_com_margem = previsoes_teste + margem_de_seguranca
    falta = np.maximum(consumo_teste.to_numpy() - previsoes_com_margem, 0)
    sobra = np.maximum(previsoes_com_margem - consumo_teste.to_numpy(), 0)
    custo_medio = (custo_por_kwh_subestimado * falta + custo_por_kwh_superestimado * sobra).mean()
    print(f"margem de {margem_de_seguranca:2d} kWh: custo médio = {custo_medio:5.1f} pontos")

figura, eixos = plt.subplots(1, 2, figsize=(11, 3.6))
eixos[0].scatter(previsoes_teste, residuos_teste, s=10, alpha=0.5, color="#3E6B22")
eixos[0].axhline(0, color="#1A1A1A", linestyle="--")
eixos[0].set_title("Resíduos x previsão")
eixos[0].set_xlabel("consumo previsto (kWh)")
eixos[0].set_ylabel("resíduo (kWh)")
eixos[1].plot(tabela_complexidade["grau"], tabela_complexidade["erro_treino"], marker="o", color="#3E6B22", label="treino")
eixos[1].plot(tabela_complexidade["grau"], tabela_complexidade["erro_teste"], marker="o", color="#E0605A", label="teste")
eixos[1].set_title("Complexidade do modelo e erro")
eixos[1].set_xlabel("grau do polinômio")
eixos[1].set_ylabel("erro médio (kWh)")
eixos[1].legend()
figura.tight_layout()
figura.savefig("figuras/a3_erro_desempenho.png", dpi=150)
