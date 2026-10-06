# Jogo de adivinhação: o computador sorteia um número de 1 a 20
import random

numero_secreto = random.randint(1, 20)
tentativas = 0
acertou = False

print("Adivinhe o número secreto entre 1 e 20!")

while not acertou:
    palpite = int(input("Seu palpite: "))
    tentativas = tentativas + 1

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        acertou = True

print("Parabéns! Você acertou em", tentativas, "tentativas.")
