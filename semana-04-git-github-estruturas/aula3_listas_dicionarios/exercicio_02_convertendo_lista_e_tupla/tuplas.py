dias_favoritos = ("sexta", "sábado", "domingo")
print("Tupla original:", dias_favoritos)

# Tuplas não podem ser alteradas: convertemos para lista, mudamos e voltamos
dias_lista = list(dias_favoritos)
dias_lista.append("quinta")
print("Como lista, com um dia novo:", dias_lista)

dias_favoritos = tuple(dias_lista)
print("De volta a tupla:", dias_favoritos)
print("Tipo final:", type(dias_favoritos))
