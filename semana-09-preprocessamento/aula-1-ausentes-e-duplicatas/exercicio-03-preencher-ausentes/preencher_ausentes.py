import pandas as pd
import numpy as np

df = pd.read_csv("arquivos/imoveis_bruto.csv", na_values=["N/D", "?", "s/i"])
df["bairro"] = df["bairro"].str.strip().str.title()
df["idade_anos"] = df["idade_anos"].replace(-1, np.nan)
df = df.drop_duplicates(subset=[c for c in df.columns if c != "id_anuncio"])

df["idade_ausente"] = df["idade_anos"].isna()
for col in ["area_m2", "idade_anos"]:
    df[col] = df[col].fillna(df.groupby("tipo")[col].transform("median"))
df["condicao"] = df["condicao"].fillna(df["condicao"].mode()[0])

print(df[["area_m2", "idade_anos", "condicao"]].isna().sum())
print("com idade ausente:", df["idade_ausente"].sum())
