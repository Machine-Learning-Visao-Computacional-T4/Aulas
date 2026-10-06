"""Gera histograma e boxplot de um dataset FICTÍCIO de entregas.

Uso (a partir da raiz do repositório):
    python aula1_problema_dataset/exercicio_03_leia_o_grafico/gerar_graficos.py

Saída:
    graficos_entregas.png (na mesma pasta do script) + estatísticas no terminal.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # permite gerar a imagem mesmo sem janela gráfica
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# 500 entregas "normais"
n = 500
distancia = rng.gamma(shape=3.0, scale=2.0, size=n)  # km, tipicamente 3-10
tempo = 8 + 3.2 * distancia + rng.normal(0, 4, size=n)  # minutos

df = pd.DataFrame({"distancia_km": distancia, "tempo_entrega_min": tempo})

# Problemas plantados de propósito
df.loc[rng.choice(n, 6, replace=False), "tempo_entrega_min"] = rng.uniform(180, 300, 6)  # outliers
df.loc[rng.choice(n, 15, replace=False), "distancia_km"] = 0.0  # distância não registrada

print("Estatísticas do tempo de entrega (min):")
print(df["tempo_entrega_min"].describe().round(1))
print(f"\nMédia:   {df['tempo_entrega_min'].mean():.1f}")
print(f"Mediana: {df['tempo_entrega_min'].median():.1f}")
print(f"\nEntregas com distância = 0: {(df['distancia_km'] == 0).sum()}")

fig, eixos = plt.subplots(1, 3, figsize=(14, 4))

eixos[0].hist(df["tempo_entrega_min"], bins=40, color="#76c043", edgecolor="black")
eixos[0].set_title("Histograma: tempo de entrega (min)")
eixos[0].set_xlabel("minutos")
eixos[0].set_ylabel("quantidade de entregas")

eixos[1].boxplot(df["tempo_entrega_min"])
eixos[1].set_title("Boxplot: tempo de entrega (min)")
eixos[1].set_xticks([])

eixos[2].hist(df["distancia_km"], bins=30, color="#76c043", edgecolor="black")
eixos[2].set_title("Histograma: distância (km)")
eixos[2].set_xlabel("km")

plt.tight_layout()
saida = Path(__file__).with_name("graficos_entregas.png")
plt.savefig(saida, dpi=120)
print(f"\nGráfico salvo em: {saida}")
