from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")

# 1) O value_counts denuncia a sujeira: 9 grafias para 3 canais
print("Canais antes:", pedidos["canal"].nunique(), "grafias")

# 2) Texto -> data de verdade, e o acessor .dt
pedidos["data"] = pd.to_datetime(pedidos["data"])
pedidos["mes"] = pedidos["data"].dt.month
pedidos["dia_semana"] = pedidos["data"].dt.dayofweek   # 0 = segunda-feira

# 3) Texto padronizado
pedidos["canal"] = pedidos["canal"].str.strip().str.title()
print(pedidos["canal"].value_counts())

# 4) map com dicionário
dias = {0: "seg", 1: "ter", 2: "qua", 3: "qui", 4: "sex", 5: "sab", 6: "dom"}
pedidos["dia"] = pedidos["dia_semana"].map(dias)
print("Dias sem correspondência:", pedidos["dia"].isna().sum())   # map não avisa: confira


# 5) Função própria + apply
def faixa_tempo(minutos):
    if pd.isna(minutos):
        return "sem entrega"
    if minutos <= 30:
        return "rápida"
    return "demorada"


pedidos["faixa_entrega"] = pedidos["tempo_entrega_min"].apply(faixa_tempo)

# 6) lambda: nota de 1 a 5 em percentual (NaN continua NaN)
pedidos["nota_pct"] = pedidos["avaliacao"].apply(lambda n: n * 20)

print(pedidos[["data", "mes", "dia_semana", "dia"]].head(3))
print(pedidos["faixa_entrega"].value_counts())
