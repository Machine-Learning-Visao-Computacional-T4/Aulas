import pandas as pd
import numpy as np


def limpar_imoveis(caminho):
    """Lê o CSV bruto e devolve a tabela sem ausentes disfarçados, repetidos e vazios."""
    df = pd.read_csv(caminho, na_values=["N/D", "?", "s/i"])
    df["bairro"] = df["bairro"].str.strip().str.title()
    df["idade_anos"] = df["idade_anos"].replace(-1, np.nan)
    df = df.drop_duplicates(subset=[c for c in df.columns if c != "id_anuncio"])
    df["idade_ausente"] = df["idade_anos"].isna()
    for col in ["area_m2", "idade_anos"]:
        df[col] = df[col].fillna(df.groupby("tipo")[col].transform("median"))
    df["distancia_praia_km"] = df["distancia_praia_km"].fillna(
        df.groupby("bairro")["distancia_praia_km"].transform("median"))
    df["condicao"] = df["condicao"].fillna(df["condicao"].mode()[0])
    return df.reset_index(drop=True)


if __name__ == "__main__":
    limpo = limpar_imoveis("arquivos/imoveis_bruto.csv")
    print(limpo.shape)
    print(limpo.isna().sum().sum(), "ausentes")
    print(limpo.duplicated().sum(), "duplicadas")
    limpo.to_csv("arquivos/imoveis_limpo.csv", index=False)
