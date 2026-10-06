from datetime import date, datetime

texto = input("Data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(texto, "%d/%m/%Y").date()  # texto -> data

hoje = date.today()

# Idade aproximada: dias vividos divididos por 365
idade = (hoje - nascimento).days // 365

# Dia da semana: weekday() devolve 0 (segunda) a 6 (domingo)
dias_da_semana = {
    0: "segunda-feira",
    1: "terça-feira",
    2: "quarta-feira",
    3: "quinta-feira",
    4: "sexta-feira",
    5: "sábado",
    6: "domingo",
}
dia_semana = dias_da_semana[nascimento.weekday()]

# Dias que faltam para o próximo Natal
natal = date(hoje.year, 12, 25)
if hoje > natal:
    natal = date(hoje.year + 1, 12, 25)
dias_para_natal = (natal - hoje).days

print("Você tem aproximadamente", idade, "anos.")
print("Você nasceu em uma", dia_semana + ".")
print("Faltam", dias_para_natal, "dias para o próximo Natal.")
