from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
quarteto = [(x, y1), (x, y2), (x, y3), (x4, y4)]

print("conjunto | média de y | variância de y | correlação")
for i, (a, b) in enumerate(quarteto, 1):
    r = np.corrcoef(a, b)[0, 1].round(3)
    print(f"{i:>8} | {np.mean(b):>10.2f} | {np.var(b, ddof=1):>14.2f} | {r}")

fig, axes = plt.subplots(2, 2, figsize=(5.4, 4.2), sharex=True, sharey=True)
for ax, (a, b) in zip(axes.flat, quarteto):
    ax.scatter(a, b)
fig.tight_layout()
fig.savefig(BASE / "anscombe.png", dpi=120)
