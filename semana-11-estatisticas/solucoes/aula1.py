# Semana 11 - Aula 1: Estatística descritiva
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

dias = pd.read_csv("arquivos/dias.csv", parse_dates=["data"])
viagens = pd.read_csv("arquivos/viagens.csv")

print("== 1. Primeiro olhar ==")
print(dias.shape, viagens.shape)
print(dias[["data", "temperatura_c", "chuva_mm", "alugueis"]].head(3))

print("\n== 2. Medidas de tendência central ==")
alugueis_por_dia = dias["alugueis"]
print(f"média   = {alugueis_por_dia.mean():.1f}")
print(f"mediana = {alugueis_por_dia.median():.1f}")
print(f"moda    = {dias['dia_semana'].mode()[0]} (dia da semana mais frequente)")
duracoes = viagens["duracao_min"]
print(f"duração: média = {duracoes.mean():.1f} min | mediana = {duracoes.median():.1f} min")

print("\n== 3. Dispersão: variância, desvio padrão, amplitude ==")
print(f"variância (pandas, ddof=1) = {alugueis_por_dia.var():.1f}")
print(f"variância (NumPy, ddof=0)  = {np.var(alugueis_por_dia):.1f}")
print(f"desvio padrão (ddof=1)     = {alugueis_por_dia.std():.1f}")
print(f"amplitude = {alugueis_por_dia.max() - alugueis_por_dia.min()}")
coeficiente_variacao_alugueis = alugueis_por_dia.std() / alugueis_por_dia.mean() * 100
coeficiente_variacao_temperatura = dias["temperatura_c"].std() / dias["temperatura_c"].mean() * 100
print(f"coeficiente de variação = {coeficiente_variacao_alugueis:.1f}%")
print("CV de temperatura vs alugueis:",
      round(coeficiente_variacao_temperatura, 1), "%",
      round(coeficiente_variacao_alugueis, 1), "%")

print("\n== 4. Quartis e IQR ==")
primeiro_quartil, mediana, terceiro_quartil = alugueis_por_dia.quantile([0.25, 0.5, 0.75])
amplitude_interquartil = terceiro_quartil - primeiro_quartil
print(f"Q1={primeiro_quartil:.0f}  Q2={mediana:.0f}  Q3={terceiro_quartil:.0f}  IQR={amplitude_interquartil:.0f}")
print(alugueis_por_dia.quantile([0.05, 0.95]).round(0).to_dict())

print("\n== 5. describe() e agg() ==")
print(dias[["temperatura_c", "chuva_mm", "alugueis"]].describe().round(2))
print(dias[["chuva_mm", "alugueis"]].agg(["mean", "median", "std", "skew", "kurt"]).round(2))

print("\n== 6. Estatísticas por grupo ==")
dias["fim_semana"] = dias["dia_semana"] >= 5
print(dias.groupby("fim_semana")["alugueis"].agg(["count", "mean", "median", "std"]).round(1))
print(viagens.groupby("bicicleta")["duracao_min"].agg(["mean", "median", "std"]).round(1))

print("\n== 7. Outliers pela regra do IQR ==")
primeiro_quartil_duracao, terceiro_quartil_duracao = duracoes.quantile([0.25, 0.75])
limite_superior = terceiro_quartil_duracao + 1.5 * (terceiro_quartil_duracao - primeiro_quartil_duracao)
viagens_atipicas = viagens[duracoes > limite_superior]
print(f"limite superior = {limite_superior:.1f} min | viagens acima: {len(viagens_atipicas)} ({len(viagens_atipicas)/len(viagens):.1%})")
print(f"maior duração = {duracoes.max():.0f} min ({duracoes.max()/60:.1f} h)")
duracoes_sem_atipicas = duracoes[duracoes <= limite_superior]
print("média sem os outliers:", round(duracoes_sem_atipicas.mean(), 1),
      "| mediana sem:", round(duracoes_sem_atipicas.median(), 1))

figura, eixos = plt.subplots(1, 3, figsize=(12, 3.6))
sns.boxplot(y=dias["alugueis"], ax=eixos[0], color="#3FB950"); eixos[0].set_title("Aluguéis por dia")
sns.boxplot(y=viagens["duracao_min"], ax=eixos[1], color="#3FB950"); eixos[1].set_title("Duração (min)")
sns.boxplot(data=dias, x="fim_semana", y="alugueis", ax=eixos[2], palette=["#8B949E", "#3FB950"], hue="fim_semana", legend=False)
eixos[2].set_title("Fim de semana?")
plt.tight_layout(); plt.savefig("figuras/a1_boxplots.png", dpi=120)
print("\nok")
