from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab
import time

pedidos = pd.read_csv(BASE / "pedidos.csv")

# Tabela grande: os 687 pedidos repetidos 150 vezes
grande = pd.concat([pedidos] * 150, ignore_index=True)

t0 = time.perf_counter()
r1 = grande.apply(lambda linha: linha["qtd"] * 2, axis=1)   # linha a linha
t1 = time.perf_counter()
r2 = grande["qtd"] * 2                                      # vetorizado
t2 = time.perf_counter()

print(f"{len(grande)} linhas")
print(f"apply(axis=1): {t1 - t0:.2f}s | vetorizado: {t2 - t1:.4f}s")
print(f"O vetorizado foi cerca de {(t1 - t0) / (t2 - t1):.0f} vezes mais rápido")
print("Mesmo resultado?", bool((r1 == r2).all()))
