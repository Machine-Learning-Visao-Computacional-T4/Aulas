import pandas as pd
import numpy as np


def limites_iqr(serie, k=1.5):
    """Devolve os limites inferior e superior pelo método do IQR."""
    q1, q3 = serie.quantile([0.25, 0.75])
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def _tratar(df):
    """Remove erros de digitação e marca preços atípicos que são reais."""
    erros = (df["area_m2"] > 2000) | (df["preco"] < 10_000) | (df["quartos"] > 10)
    df = df[~erros].copy()
    baixo, alto = limites_iqr(df["preco"])
    df["preco_atipico"] = (df["preco"] > alto) | (df["preco"] < baixo)
    return df.reset_index(drop=True)


def preparar_numericos(caminho):
    """Lê o CSV limpo, trata os erros, salva o tratado e devolve a tabela."""
    df = _tratar(pd.read_csv(caminho))
    df.to_csv("arquivos/imoveis_tratado.csv", index=False)
    return df


if __name__ == "__main__":
    entrada = pd.read_csv("arquivos/imoveis_limpo.csv")
    tratado = preparar_numericos("arquivos/imoveis_limpo.csv")
    print(len(entrada), "->", len(tratado))
    print(tratado["preco_atipico"].sum(), "preços atípicos mantidos")
