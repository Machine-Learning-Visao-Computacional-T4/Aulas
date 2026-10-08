from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

sujo = pd.read_csv(BASE / "contatos_sujos.csv")

print("Linhas e colunas:", sujo.shape)

print("\nValores ausentes por coluna:")
print(sujo.isna().sum())

print("\nLinhas duplicadas:", sujo.duplicated().sum())

print("\nNomes como estão (repare nos espaços e na caixa):")
print(sujo["nome"].tolist())

print("\nTelefones como estão (sem padrão):")
print(sujo["telefone"].tolist())

print("\nDatas ainda são texto, por exemplo:", sujo["data_cadastro"].iloc[0])
