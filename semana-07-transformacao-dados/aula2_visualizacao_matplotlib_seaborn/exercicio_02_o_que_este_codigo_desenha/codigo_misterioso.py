from pathlib import Path

import matplotlib.pyplot as plt

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

rotulos = ["A", "B", "C"]
valores = [3, 7, 5]

maior = rotulos[valores.index(max(valores))]
print(f"{len(valores)} barras | a mais alta é a {maior} ({max(valores)}) | a mais baixa vale {min(valores)}")

plt.figure(figsize=(4, 3))
plt.bar(rotulos, valores)
plt.title("plt.bar: barras verticais")
plt.savefig(BASE / "barras_verticais.png", dpi=100)

plt.figure(figsize=(4, 3))
plt.barh(rotulos, valores)
plt.title("plt.barh: barras horizontais")
plt.savefig(BASE / "barras_horizontais.png", dpi=100)

plt.show()
