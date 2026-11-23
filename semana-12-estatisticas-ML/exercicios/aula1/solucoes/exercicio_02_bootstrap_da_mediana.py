# Aula 1 - Exercício 2: bootstrap da mediana da ocupação
import numpy as np
import pandas as pd

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
ocupacao_populacao = consumo_campus["ocupacao_pct"]
mediana_real = ocupacao_populacao.median()
gerador_aleatorio = np.random.default_rng(seed=42)

def intervalo_bootstrap_da_mediana(valores_da_amostra, repeticoes=2000):
    medianas = [np.median(gerador_aleatorio.choice(valores_da_amostra, size=len(valores_da_amostra), replace=True)) for _ in range(repeticoes)]
    return np.percentile(medianas, [2.5, 97.5])

amostra_de_40_dias = ocupacao_populacao.sample(n=40, random_state=42).to_numpy()
limite_inferior, limite_superior = intervalo_bootstrap_da_mediana(amostra_de_40_dias)
print(f"mediana real = {mediana_real:.1f} | mediana da amostra = {np.median(amostra_de_40_dias):.1f}")
print(f"intervalo de 95% = [{limite_inferior:.1f}; {limite_superior:.1f}]")

acertos = 0
for semente in range(20):
    amostra = ocupacao_populacao.sample(n=40, random_state=100 + semente).to_numpy()
    inferior, superior = intervalo_bootstrap_da_mediana(amostra, repeticoes=500)
    acertos += inferior <= mediana_real <= superior
print(f"em 20 amostras, o intervalo continha a mediana real em {acertos} casos")
