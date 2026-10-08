from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

sujo = pd.read_csv(BASE / "contatos_sujos.csv")

# 1) Nota ausente -> média; linhas repetidas -> removidas
media = sujo["nota"].mean()
sujo["nota"] = sujo["nota"].fillna(media)
sujo = sujo.drop_duplicates()
print(f"Média usada para preencher a nota ausente: {media:.2f}")

# 2) Nome: sem espaços extras e em Title Case; telefone: só dígitos
sujo["nome"] = (sujo["nome"].str.strip()
                .str.replace(r"\s+", " ", regex=True)
                .str.title())
sujo["telefone"] = sujo["telefone"].str.replace(r"\D", "", regex=True)

# 3) Data: texto dd/mm/aaaa -> data de verdade
sujo["data_cadastro"] = pd.to_datetime(sujo["data_cadastro"], format="%d/%m/%Y")

# 4) Grava o resultado (index=False: sem a coluna de índice)
sujo.to_csv(BASE / "contatos_limpos.csv", index=False)

print(sujo)
print("Arquivo contatos_limpos.csv gravado.")
