from pathlib import Path

import matplotlib.pyplot as plt

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

layouts = {
    "layout_1_largo_no_topo": [["topo", "topo"], ["esq", "dir"]],
    "layout_2_alto_a_esquerda": [["alto", "a"], ["alto", "b"]],   # desafio
}

for nome, desenho in layouts.items():
    fig, ax = plt.subplot_mosaic(desenho, figsize=(5, 3.6), layout="constrained")
    for rotulo, eixo in ax.items():
        eixo.text(0.5, 0.5, rotulo, ha="center", va="center", fontsize=14)
        eixo.set_xticks([])
        eixo.set_yticks([])
    fig.suptitle(nome)
    fig.savefig(BASE / f"{nome}.png", dpi=100)
    print(nome, "->", list(ax))

plt.show()
