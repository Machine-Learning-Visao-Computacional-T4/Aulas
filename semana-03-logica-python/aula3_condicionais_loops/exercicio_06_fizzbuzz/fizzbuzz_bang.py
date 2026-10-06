# Desafio extra: múltiplos de 7 também imprimem "Bang"
# Os textos se combinam: 21 é múltiplo de 3 e de 7, então vira "FizzBang"
for numero in range(1, 31):
    saida = ""
    if numero % 3 == 0:
        saida = saida + "Fizz"
    if numero % 5 == 0:
        saida = saida + "Buzz"
    if numero % 7 == 0:
        saida = saida + "Bang"

    if saida == "":
        print(numero)
    else:
        print(saida)
