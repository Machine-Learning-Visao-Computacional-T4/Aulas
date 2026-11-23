# Aula 3 - Exercício 11: validação cruzada com mais de uma métrica
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_validate
from sklearn.tree import DecisionTreeRegressor

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
divisor_de_validacao = KFold(n_splits=5, shuffle=True, random_state=42)
modelos = {"baseline (média)": DummyRegressor(strategy="mean"), "regressão linear": LinearRegression(), "árvore (profundidade 4)": DecisionTreeRegressor(max_depth=4, random_state=42)}
for nome_do_modelo, modelo in modelos.items():
    resultados = cross_validate(modelo, consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], cv=divisor_de_validacao,
                                scoring={"mae": "neg_mean_absolute_error", "rmse": "neg_root_mean_squared_error", "r2": "r2"})
    print(f"{nome_do_modelo:24s} MAE = {-resultados['test_mae'].mean():5.1f} | RMSE = {-resultados['test_rmse'].mean():5.1f} | R² = {resultados['test_r2'].mean():6.3f} ± {resultados['test_r2'].std():.3f}")
