import pandas as pd
import numpy as np

imoveis = pd.read_csv("arquivos/imoveis_limpo.csv")


def limites_iqr(serie, k=1.5):
    q1, q3 = serie.quantile([0.25, 0.75])
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


for col in ["area_m2", "quartos", "idade_anos", "preco"]:
    baixo, alto = limites_iqr(imoveis[col])
    n = ((imoveis[col] < baixo) | (imoveis[col] > alto)).sum()
    print(f"{col:11s} {n:3d} fora de [{baixo:,.0f}; {alto:,.0f}]")

imoveis["preco_m2"] = imoveis["preco"] / imoveis["area_m2"]
suspeitos = imoveis[(imoveis["area_m2"] > 600) | (imoveis["preco"] < 50_000) | (imoveis["quartos"] > 10)]
print(suspeitos[["id_anuncio", "tipo", "area_m2", "quartos", "preco", "preco_m2"]].round(0))

erros = (imoveis["area_m2"] > 2000) | (imoveis["preco"] < 10_000) | (imoveis["quartos"] > 10)
print(erros.sum(), "anúncios com erro de digitação")
