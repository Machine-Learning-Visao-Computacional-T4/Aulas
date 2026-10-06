favoritos = ["pizza", "violão", "praia", "cinema", "café"]
print("Lista inicial:", favoritos)

favoritos.append("livros")  # adiciona no final
print("Depois do append:", favoritos)

favoritos.remove("cinema")  # remove pelo valor
print("Depois do remove:", favoritos)

removido = favoritos.pop()  # remove (e devolve) o último item
print("pop removeu:", removido)
print("Depois do pop:", favoritos)

favoritos.sort()  # ordena em ordem alfabética
print("Depois do sort:", favoritos)

print("Primeiro item (índice 0):", favoritos[0])
