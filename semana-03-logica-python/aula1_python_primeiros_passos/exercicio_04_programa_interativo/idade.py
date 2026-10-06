from datetime import date

ano_atual = date.today().year  # ou escreva o ano atual direto: ano_atual = 2026

nome = input("Qual é o seu nome? ")
ano_nascimento = int(input("Em que ano você nasceu? "))  # input() devolve texto: int() converte

idade = ano_atual - ano_nascimento

print("Olá,", nome + "! Você tem aproximadamente", idade, "anos.")
