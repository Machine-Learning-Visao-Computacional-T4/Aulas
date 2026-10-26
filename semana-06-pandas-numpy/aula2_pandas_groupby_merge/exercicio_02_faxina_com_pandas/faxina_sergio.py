import pandas as pd
sujo = pd.read_csv("contatos_sujos.csv")
print(sujo.shape)
print(sujo.isna().sum())

media  = sujo["nota"].mean()
sujo["nota"] = sujo["nota"].fillna(media)
print(round(media, 2))
print(sujo["nota"].tolist())

sujo["nome"] = (sujo["nome"].str.strip()
                .str.replace(r"\s+", " ", regex=True)
                .str.title())
sujo["telefone"] = sujo["telefone"].str.replace(r"\D", "", regex=True)
print(sujo[["nome", "telefone"]])