# Confere as suas previsões: rode depois de preencher a tabela em previsoes.md
expressoes = [
    "10 > 5 and 3 < 1",
    "not (4 == 4)",
    "7 % 2 == 1",
    "2 + 3 * 4 == 20",
    "(2 + 3) * 4 == 20",
    "True or 1 / 0 == 1",
    "False and 1 / 0 == 1",
    "5 > 3 or 2 > 8 and 1 > 2",
    "not True or True",
    "17 // 5 == 3 and 17 % 5 == 2",
]

for i, expressao in enumerate(expressoes, start=1):
    print(i, "|", expressao, "->", eval(expressao))
