# Aula 2 - Exercício 8 (Git e Pull Request): arquivo dados_e_modelo.py
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import learning_curve, train_test_split
from sklearn.tree import DecisionTreeRegressor

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
consumo_serra = pd.read_csv("arquivos/consumo_campus_serra.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]

print("== curva de aprendizado (erro de validação) ==")
for nome_do_modelo, modelo in {"linear": LinearRegression(), "árvore": DecisionTreeRegressor(max_depth=6, random_state=42)}.items():
    tamanhos, _, erros_validacao = learning_curve(modelo, consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"],
        train_sizes=[0.1, 0.4, 1.0], cv=5, scoring="neg_mean_absolute_error", shuffle=True, random_state=42)
    print(nome_do_modelo, dict(zip(tamanhos.tolist(), (-erros_validacao.mean(axis=1)).round(1).tolist())))

print("\n== ocupação nos dois campi ==")
estatistica_ks, p_valor_ks = stats.ks_2samp(consumo_campus["ocupacao_pct"], consumo_serra["ocupacao_pct"])
print(f"KS = {estatistica_ks:.2f} | p-valor = {p_valor_ks:.2g}")

entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
modelo_linear = LinearRegression().fit(entradas_treino, consumo_treino)
residuos_serra = consumo_serra["consumo_kwh"] - modelo_linear.predict(consumo_serra[colunas_de_entrada])
print(f"viés no campus da serra = {residuos_serra.mean():+.1f} kWh | erro absoluto = {residuos_serra.abs().mean():.1f} kWh")
