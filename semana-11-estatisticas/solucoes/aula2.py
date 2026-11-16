# Semana 11 - Aula 2: Distribuição de dados
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

dias = pd.read_csv("arquivos/dias.csv")
viagens = pd.read_csv("arquivos/viagens.csv")
alugueis_por_dia = dias["alugueis"]
duracoes = viagens["duracao_min"]

print("== 1. Forma da distribuição: assimetria e curtose ==")
for nome_coluna, serie in [("alugueis", alugueis_por_dia), ("temperatura_c", dias["temperatura_c"]),
                           ("duracao_min", duracoes), ("chuva_mm", dias["chuva_mm"])]:
    print(f"{nome_coluna:14s} skew={serie.skew():6.2f}  curtose={serie.kurt():6.2f}")

print("\n== 2. Histograma em tabela: pd.cut + value_counts ==")
faixas_alugueis = pd.cut(alugueis_por_dia, bins=[0, 200, 300, 400, 500, 600, 700, 900])
print(faixas_alugueis.value_counts().sort_index())

print("\n== 3. Regra empírica 68-95-99,7 ==")
media_alugueis, desvio_alugueis = alugueis_por_dia.mean(), alugueis_por_dia.std()
for numero_desvios in (1, 2, 3):
    limite_inferior = media_alugueis - numero_desvios * desvio_alugueis
    limite_superior = media_alugueis + numero_desvios * desvio_alugueis
    proporcao_dentro = ((alugueis_por_dia >= limite_inferior) & (alugueis_por_dia <= limite_superior)).mean()
    print(f"dentro de ±{numero_desvios} desvio(s): {proporcao_dentro:.1%}")

print("\n== 4. Escore z ==")
escore_z = (alugueis_por_dia - media_alugueis) / desvio_alugueis
print(escore_z.describe().round(2)[["mean", "std", "min", "max"]])
indice_mais_extremo = escore_z.abs().idxmax()
print("dia mais extremo:", dias.loc[indice_mais_extremo, "data"], "| z =", round(escore_z[indice_mais_extremo], 2))
print("dias com |z| > 2:", int((escore_z.abs() > 2).sum()))

print("\n== 5. Teste de normalidade (Shapiro-Wilk) ==")
for nome_coluna, amostra in [("alugueis", alugueis_por_dia), ("duracao_min", duracoes.sample(500, random_state=1))]:
    estatistica_w, p_valor = stats.shapiro(amostra)
    print(f"{nome_coluna:12s} W={estatistica_w:.3f}  p={p_valor:.4g}  ->",
          "compatível com normal" if p_valor > 0.05 else "NÃO normal")

print("\n== 6. Transformação logarítmica ==")
print(f"duracao_min   skew = {duracoes.skew():.2f}")
print(f"log1p(duracao) skew = {np.log1p(duracoes).skew():.2f}")
print(f"chuva_mm      skew = {dias['chuva_mm'].skew():.2f}")
print(f"log1p(chuva)  skew = {np.log1p(dias['chuva_mm']).skew():.2f}  (muitos zeros: a transformação ajuda pouco)")
print("% de dias sem chuva:", round((dias["chuva_mm"] == 0).mean() * 100, 1), "%")

print("\n== 7. Teorema Central do Limite (simulação) ==")
gerador_aleatorio = np.random.default_rng(0)
tamanho_amostra = 30
sementes = gerador_aleatorio.integers(0, 10**6, 1000)
medias_das_amostras = [duracoes.sample(tamanho_amostra, random_state=int(semente)).mean() for semente in sementes]
print(f"população: média={duracoes.mean():.1f}  skew={duracoes.skew():.2f}")
print(f"1000 médias de amostras (n={tamanho_amostra}): média={np.mean(medias_das_amostras):.1f}  "
      f"desvio={np.std(medias_das_amostras):.2f}  skew={stats.skew(medias_das_amostras):.2f}")
print(f"erro padrão teórico = {duracoes.std() / np.sqrt(tamanho_amostra):.2f}")

print("\n== 8. Percentis e ECDF ==")
print("percentis da duração:", duracoes.quantile([.5, .9, .95, .99]).round(1).to_dict())
print(f"P(duração <= 30 min) = {(duracoes <= 30).mean():.1%}")

figura, eixos = plt.subplots(2, 3, figsize=(13, 7))
sns.histplot(alugueis_por_dia, kde=True, ax=eixos[0, 0], color="#3FB950"); eixos[0, 0].set_title("Aluguéis/dia (≈ normal)")
sns.histplot(duracoes, bins=60, ax=eixos[0, 1], color="#3FB950"); eixos[0, 1].set_title("Duração (assimétrica à direita)")
sns.histplot(np.log1p(duracoes), kde=True, ax=eixos[0, 2], color="#3FB950"); eixos[0, 2].set_title("log1p(duração)")
stats.probplot(alugueis_por_dia, dist="norm", plot=eixos[1, 0]); eixos[1, 0].set_title("QQ-plot aluguéis")
stats.probplot(duracoes, dist="norm", plot=eixos[1, 1]); eixos[1, 1].set_title("QQ-plot duração")
sns.histplot(medias_das_amostras, kde=True, ax=eixos[1, 2], color="#3FB950"); eixos[1, 2].set_title("Médias (n=30): TCL")
plt.tight_layout(); plt.savefig("figuras/a2_distribuicoes.png", dpi=110)
print("\nok")
