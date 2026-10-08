from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

# 1) pandas lê e organiza; to_numpy entrega a matriz de notas ao NumPy
df = pd.read_csv(BASE / "provas.csv")
notas = df[["p1", "p2", "p3"]].to_numpy()

# 2) Média ponderada por broadcasting: pesos (3,) sobre notas (4, 3)
pesos = np.array([0.3, 0.3, 0.4])
df["final"] = (notas * pesos).sum(axis=1).round(2)
df["situacao"] = np.where(df["final"] >= 7, "Aprovado", "Reprovado")

# 3) Z-score de cada prova (também por broadcasting)
z = (notas - notas.mean(axis=0)) / notas.std(axis=0)
df["z_p1"] = z[:, 0].round(2)
df["z_p2"] = z[:, 1].round(2)
df["z_p3"] = z[:, 2].round(2)

# 4) Grava o resultado completo
df.to_csv(BASE / "resultado_provas.csv", index=False)

print(df)
print("Arquivo resultado_provas.csv gravado.")
