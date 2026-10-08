import numpy as np

# Cada caso: (shape do primeiro array, shape do segundo array)
casos = [
    ((4, 3), (3,)),
    ((4, 3), (4,)),
    ((4, 3), (4, 1)),
    ((3, 1), (1, 4)),
    ((2, 3, 4), (4,)),
]

for a, b in casos:
    # try/except ainda não foi visto no curso: aqui ele só captura o erro
    # de shapes incompatíveis para o programa continuar com o próximo caso.
    try:
        resultado = np.ones(a) + np.ones(b)
        print(f"{a} + {b} -> funciona, shape {resultado.shape}")
    except ValueError:
        print(f"{a} + {b} -> ERRO (shapes incompatíveis)")
