import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


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


def limites_iqr(serie, k=1.5):
    """Devolve os limites inferior e superior pelo método do IQR."""
    q1, q3 = serie.quantile([0.25, 0.75])
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def tratar_erros(df):
    """Remove erros de digitação e marca preços atípicos que são reais."""
    erros = (df["area_m2"] > 2000) | (df["preco"] < 10_000) | (df["quartos"] > 10)
    df = df[~erros].copy()
    baixo, alto = limites_iqr(df["preco"])
    df["preco_atipico"] = (df["preco"] > alto) | (df["preco"] < baixo)
    return df.reset_index(drop=True)


def montar_pipeline():
    """Monta o ColumnTransformer: escala, ordinal, One-Hot e binárias."""
    numericas = ["area_m2", "quartos", "banheiros", "vagas", "idade_anos", "distancia_praia_km"]
    binarias = ["aceita_pet", "mobiliado", "idade_ausente"]
    return ColumnTransformer([
        ("num", StandardScaler(), numericas),
        ("ord", OrdinalEncoder(categories=[["Ruim", "Regular", "Bom", "Ótimo"]]), ["condicao"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["tipo", "bairro"]),
        ("bin", OrdinalEncoder(categories=[["Não", "Sim"], ["Não", "Sim"], [False, True]]), binarias),
    ])


if __name__ == "__main__":
    df = limpar_imoveis("arquivos/imoveis_bruto.csv")
    print("depois da limpeza:", len(df))
    df = tratar_erros(df)
    print("depois dos erros:", len(df))
    X = df.drop(columns=["preco", "id_anuncio", "preco_atipico"])
    y = np.log1p(df["preco"])
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
    print("treino/teste:", X_treino.shape, X_teste.shape)
    prep = montar_pipeline()
    Xt_treino = prep.fit_transform(X_treino)
    Xt_teste = prep.transform(X_teste)
    print("saída:", Xt_treino.shape, Xt_teste.shape)
