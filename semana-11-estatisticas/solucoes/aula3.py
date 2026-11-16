# Semana 11 - Aula 3: Correlação, variância e interpretação estatística de datasets
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

dias = pd.read_csv("arquivos/dias.csv")
viagens = pd.read_csv("arquivos/viagens.csv")

print("== 1. Covariância x correlação ==")
print("covariância(temperatura, aluguéis) =", round(dias["temperatura_c"].cov(dias["alugueis"]), 1), " (depende da unidade)")
print("correlação (temperatura, aluguéis) =", round(dias["temperatura_c"].corr(dias["alugueis"]), 3), " (sempre entre -1 e 1)")
temperatura_fahrenheit = dias["temperatura_c"] * 9 / 5 + 32
print("covariância com temperatura em °F  =", round(temperatura_fahrenheit.cov(dias["alugueis"]), 1))
print("correlação com temperatura em °F   =", round(temperatura_fahrenheit.corr(dias["alugueis"]), 3))

print("\n== 2. Pearson x Spearman ==")
pearson_chuva = dias["chuva_mm"].corr(dias["alugueis"], method="pearson")
spearman_chuva = dias["chuva_mm"].corr(dias["alugueis"], method="spearman")
print(f"chuva x aluguéis: Pearson = {pearson_chuva:.3f} | Spearman = {spearman_chuva:.3f}")
pearson_distancia = viagens["distancia_km"].corr(viagens["duracao_min"], method="pearson")
spearman_distancia = viagens["distancia_km"].corr(viagens["duracao_min"], method="spearman")
print(f"distância x duração: Pearson = {pearson_distancia:.3f} | Spearman = {spearman_distancia:.3f}  (outliers derrubam o Pearson)")
coeficiente_pearson, p_valor = stats.pearsonr(dias["temperatura_c"], dias["alugueis"])
print(f"pearsonr temperatura x aluguéis: r = {coeficiente_pearson:.3f}, p-valor = {p_valor:.2g}")

print("\n== 3. Matriz de correlação ==")
colunas_clima = ["temperatura_c", "sensacao_termica_c", "umidade_pct", "vento_kmh", "chuva_mm", "alugueis"]
matriz_correlacao = dias[colunas_clima].corr()
print(matriz_correlacao.round(2))
print("\ncorrelação de cada variável com o alvo:")
print(matriz_correlacao["alugueis"].drop("alugueis").sort_values(key=abs, ascending=False).round(2))

print("\n== 4. Multicolinearidade e VIF ==")
atributos_clima = dias[["temperatura_c", "sensacao_termica_c", "umidade_pct", "vento_kmh", "chuva_mm"]]
def calcular_vif(atributos):
    vif_por_coluna = {}
    for coluna in atributos.columns:
        demais_colunas = atributos.drop(columns=coluna)
        r_quadrado = LinearRegression().fit(demais_colunas, atributos[coluna]).score(demais_colunas, atributos[coluna])
        vif_por_coluna[coluna] = 1 / (1 - r_quadrado)
    return pd.Series(vif_por_coluna).round(1)
print("VIF com as duas temperaturas:\n", calcular_vif(atributos_clima))
print("\nVIF sem sensacao_termica_c:\n", calcular_vif(atributos_clima.drop(columns="sensacao_termica_c")))

print("\n== 5. Variância como filtro de atributos ==")
dias["fim_semana"] = (dias["dia_semana"] >= 5).astype(int)
atributos_candidatos = dias[["temperatura_c", "umidade_pct", "vento_kmh", "chuva_mm", "feriado", "fim_semana"]]
print("variâncias brutas:\n", atributos_candidatos.var().round(2))
atributos_padronizados = pd.DataFrame(StandardScaler().fit_transform(atributos_candidatos),
                                      columns=atributos_candidatos.columns)
print("\nvariâncias após padronização:", atributos_padronizados.var().round(2).unique())
filtro_variancia = VarianceThreshold(threshold=0.05).fit(atributos_candidatos)
print("\nVarianceThreshold(0.05) mantém:", list(atributos_candidatos.columns[filtro_variancia.get_support()]))
print("descartadas:", list(atributos_candidatos.columns[~filtro_variancia.get_support()]))

print("\n== 6. Correlação não é causa: o papel da estação do ano ==")
dias_de_verao = dias["mes"].isin([12, 1, 2])
print("temperatura x aluguéis (ano todo):", round(dias["temperatura_c"].corr(dias["alugueis"]), 3))
print("temperatura x aluguéis (só verão):",
      round(dias.loc[dias_de_verao, "temperatura_c"].corr(dias.loc[dias_de_verao, "alugueis"]), 3))
print("umidade x aluguéis:", round(dias["umidade_pct"].corr(dias["alugueis"]), 3),
      "| mas umidade x temperatura:", round(dias["umidade_pct"].corr(dias["temperatura_c"]), 3))
# correlação parcial: remove (via regressão) o efeito da temperatura das duas variáveis
temperatura = dias[["temperatura_c"]]
residuo_umidade = dias["umidade_pct"] - LinearRegression().fit(temperatura, dias["umidade_pct"]).predict(temperatura)
residuo_alugueis = dias["alugueis"] - LinearRegression().fit(temperatura, dias["alugueis"]).predict(temperatura)
print("umidade x aluguéis, descontada a temperatura:", round(residuo_umidade.corr(residuo_alugueis), 3), "(praticamente some)")

print("\n== 7. Paradoxo de Simpson ==")
print("nota x valor (todas as viagens):", round(viagens["nota"].corr(viagens["valor_rs"]), 3))
print(viagens.groupby("bicicleta").apply(lambda grupo: grupo["nota"].corr(grupo["valor_rs"]), include_groups=False).round(3))
print(viagens.groupby("bicicleta")[["valor_rs", "nota"]].mean().round(2))

print("\n== 8. Checklist: função de resumo estatístico ==")
def resumo_estatistico(tabela):
    colunas_numericas = tabela.select_dtypes("number")
    resultado = pd.DataFrame({
        "media": colunas_numericas.mean(), "mediana": colunas_numericas.median(),
        "desvio": colunas_numericas.std(),
        "cv_%": colunas_numericas.std() / colunas_numericas.mean() * 100,
        "skew": colunas_numericas.skew(),
        "ausentes_%": tabela[colunas_numericas.columns].isna().mean() * 100,
    }).round(2)
    resultado["alerta"] = np.where(resultado["skew"].abs() > 1, "assimétrica", "")
    return resultado
print(resumo_estatistico(viagens.drop(columns="id_viagem")))

figura, eixos = plt.subplots(1, 3, figsize=(15, 4.4))
sns.heatmap(matriz_correlacao, annot=True, fmt=".2f", cmap="RdYlGn", center=0, ax=eixos[0], cbar=False)
eixos[0].set_title("Matriz de correlação"); eixos[0].tick_params(axis="x", rotation=45)
sns.scatterplot(data=dias, x="temperatura_c", y="alugueis", hue="fim_semana", ax=eixos[1], palette=["#8B949E", "#3FB950"])
eixos[1].set_title("Temperatura x aluguéis")
sns.scatterplot(data=viagens.sample(1200, random_state=1), x="valor_rs", y="nota", hue="bicicleta", alpha=.5, ax=eixos[2])
sns.regplot(data=viagens, x="valor_rs", y="nota", scatter=False, color="black", ax=eixos[2], line_kws={"lw": 1.5})
eixos[2].set_title("Simpson: geral (preta) x por grupo")
plt.tight_layout(); plt.savefig("figuras/a3_correlacao.png", dpi=110)
print("\nok")
