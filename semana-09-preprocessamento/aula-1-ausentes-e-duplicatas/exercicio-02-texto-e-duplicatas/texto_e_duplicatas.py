import pandas as pd
import numpy as np

imoveis = pd.read_csv("arquivos/imoveis_bruto.csv", na_values=["N/D", "?", "s/i"])
print("duplicadas (todas as colunas):", imoveis.duplicated().sum())
print("bairros antes:", imoveis["bairro"].nunique())

imoveis["bairro"] = imoveis["bairro"].str.strip().str.title()
print("bairros depois:", imoveis["bairro"].nunique())

colunas = [c for c in imoveis.columns if c != "id_anuncio"]
print("duplicadas (sem o id):", imoveis.duplicated(subset=colunas).sum())
sem_dup = imoveis.drop_duplicates(subset=colunas)
print(len(imoveis), "->", len(sem_dup))
