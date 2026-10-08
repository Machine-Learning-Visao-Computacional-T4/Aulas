# pandas_basico.py
# Exercício: primeiros passos com Series e DataFrames.

import pandas as pd

# 1) Series: notas de 4 colegas fictícios (o índice guarda os nomes)
notas = pd.Series([8.5, 6.0, 9.5, 7.0], index=["Ana", "Bruno", "Carla", "Diego"])

print("Notas dos colegas:")
print(notas)
print("Média da turma:", notas.mean())
print("Maior nota:", notas.idxmax(), "com", notas.max())

# 2) DataFrame: 5 filmes a partir de um dicionário de listas
# (as notas são fictícias, só para o exercício)
dados = {
    "titulo": ["Cidade de Deus", "Central do Brasil", "O Auto da Compadecida",
               "Tropa de Elite", "Ainda Estou Aqui"],
    "ano": [2002, 1998, 2000, 2007, 2024],
    "nota": [9.0, 8.5, 9.5, 8.0, 8.8],
}
filmes = pd.DataFrame(dados)

print("\nTabela de filmes:")
print(filmes)

# 3) Uma coluna (devolve uma Series)
print("\nUma coluna:")
print(filmes["titulo"])

# 4) Duas colunas (colchetes duplos: devolve um DataFrame)
print("\nDuas colunas:")
print(filmes[["titulo", "nota"]])

# 5) Tipo (dtype) de cada coluna
# (em versões mais novas do pandas, o texto aparece como "str" em vez de "object")
print("\nTipos das colunas:")
print(filmes.dtypes)
