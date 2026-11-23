# Aula 1 - Exercício 1: amostras de umidade
import numpy as np
import pandas as pd

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
umidade_populacao = consumo_campus["umidade_pct"]
print(f"média da população = {umidade_populacao.mean():.2f} % | desvio padrão = {umidade_populacao.std():.2f}")

for tamanho_da_amostra in [30, 120]:
    medias_das_amostras = pd.Series([umidade_populacao.sample(n=tamanho_da_amostra, random_state=repeticao).mean() for repeticao in range(1000)])
    erro_padrao_teorico = umidade_populacao.std() / np.sqrt(tamanho_da_amostra)
    print(f"n = {tamanho_da_amostra:3d}: desvio das médias = {medias_das_amostras.std():.2f} | erro padrão teórico = {erro_padrao_teorico:.2f}")
