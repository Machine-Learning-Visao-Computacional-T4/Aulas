import pandas as pd
import numpy as np


def diagnosticar(df, alvo):
    """Resume o balanceamento de uma coluna alvo."""
    cont = df[alvo].value_counts()
    return {"classe_majoritaria": int(cont.idxmax()), "classe_minoritaria": int(cont.idxmin()),
            "proporcao_minoritaria": float(round(cont.min() / len(df), 4)),
            "razao": float(round(cont.max() / cont.min(), 1)),
            "acuracia_baseline": float(round(cont.max() / len(df), 4))}


if __name__ == "__main__":
    print(diagnosticar(pd.read_csv("arquivos/transacoes.csv"), "fraude"))
    tres = pd.DataFrame({"classe": [0] * 80 + [1] * 15 + [2] * 5})
    print(diagnosticar(tres, "classe"))
