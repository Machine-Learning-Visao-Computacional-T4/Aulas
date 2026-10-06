"""Diagnostica underfitting/overfitting a partir dos F1 de treino e validação."""

# (combinação, max_depth, F1 treino, F1 validação)
resultados = [
    ("A", 2, 0.61, 0.59),
    ("B", 4, 0.79, 0.76),
    ("C", 6, 0.87, 0.84),
    ("D", 12, 0.96, 0.77),
    ("E", 25, 1.00, 0.66),
]

print(f"{'Comb.':<6}{'max_depth':>10}{'F1 treino':>11}{'F1 valid.':>11}{'Diferença':>11}")
for comb, prof, f1_treino, f1_valid in resultados:
    print(f"{comb:<6}{prof:>10}{f1_treino:>11.2f}{f1_valid:>11.2f}{f1_treino - f1_valid:>11.2f}")

melhor = max(resultados, key=lambda r: r[3])
maior_diferenca = max(resultados, key=lambda r: r[2] - r[3])

print()
print(f"Melhor F1 de validação: combinação {melhor[0]} (max_depth={melhor[1]}, F1={melhor[3]:.2f})")
print(
    f"Maior diferença treino-validação: combinação {maior_diferenca[0]} "
    f"(diferença de {maior_diferenca[2] - maior_diferenca[3]:.2f})"
)
print()
print("Leitura: F1 baixo nos dois conjuntos = underfitting;")
print("F1 de treino muito acima do de validação = overfitting.")
