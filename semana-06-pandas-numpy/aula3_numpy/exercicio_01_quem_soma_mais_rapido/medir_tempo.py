import time

import numpy as np

dados = list(range(1_000_000))
arr = np.array(dados)

# Com laço sobre uma lista Python
t0 = time.perf_counter()
dobro_lista = [x * 2 for x in dados]
t1 = time.perf_counter()

# Com NumPy (operação em bloco)
dobro_arr = arr * 2
t2 = time.perf_counter()

tempo_lista = t1 - t0
tempo_numpy = t2 - t1
print(f"lista: {tempo_lista:.4f}s | numpy: {tempo_numpy:.4f}s")
print(f"O NumPy foi cerca de {tempo_lista / tempo_numpy:.0f} vezes mais rápido nesta máquina.")
