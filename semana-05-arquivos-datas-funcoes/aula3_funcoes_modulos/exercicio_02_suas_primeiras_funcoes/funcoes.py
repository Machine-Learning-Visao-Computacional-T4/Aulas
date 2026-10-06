def e_bissexto(ano):
    """Devolve True se o ano for bissexto e False se não for."""
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def calcular_imc(peso, altura):
    """Calcula o IMC: peso (kg) dividido pela altura (m) ao quadrado."""
    return peso / (altura ** 2)


for ano in (2000, 1900, 2024, 2023):
    print(ano, "é bissexto?", e_bissexto(ano))

print("IMC de 70 kg e 1,75 m:", round(calcular_imc(70, 1.75), 1))
print("IMC de 90 kg e 1,80 m:", round(calcular_imc(90, 1.80), 1))
