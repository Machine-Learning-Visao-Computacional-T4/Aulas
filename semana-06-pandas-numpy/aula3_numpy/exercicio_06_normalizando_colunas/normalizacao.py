import numpy as np

notas = np.array([[8.5, 9.0, 7.5],
                  [6.0, 7.5, 5.0],
                  [9.5, 8.0, 9.0],
                  [5.0, 6.0, 4.5]])
alunos = np.array(["Ana", "Bruno", "Carla", "Diego"])

# Min-max por coluna: (x - min) / (max - min) -> valores entre 0 e 1
minimos = notas.min(axis=0)      # shape (3,): um mínimo por coluna
maximos = notas.max(axis=0)
minmax = (notas - minimos) / (maximos - minimos)   # broadcasting: (4, 3) com (3,)

print("Min-max por coluna:")
print(minmax.round(2))
print("Mínimo de cada coluna:", minmax.min(axis=0), "| máximo:", minmax.max(axis=0))

# Z-score por coluna: (x - média) / desvio-padrão
z = (notas - notas.mean(axis=0)) / notas.std(axis=0)

print("\nZ-score por coluna:")
print(z.round(2))
print("Média de cada coluna (perto de 0):", np.abs(z.mean(axis=0)).round(2))
print("Desvio-padrão de cada coluna (perto de 1):", z.std(axis=0).round(2))
