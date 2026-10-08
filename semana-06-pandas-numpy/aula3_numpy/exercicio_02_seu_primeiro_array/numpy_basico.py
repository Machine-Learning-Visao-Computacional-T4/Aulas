import numpy as np

# Matriz 3x4 com os valores de 1 a 12
m = np.arange(1, 13).reshape(3, 4)

print(m)
print("shape:", m.shape, "| ndim:", m.ndim, "| size:", m.size)

print("Segunda linha:", m[1])
print("Última coluna:", m[:, -1])
print("Bloco central (linhas 0 a 1, colunas 1 a 2):")
print(m[0:2, 1:3])

# Máscara booleana: m % 2 == 0 gera True/False para cada elemento
pares = m[m % 2 == 0]
print("Valores pares:", pares, "-> quantidade:", pares.size)
