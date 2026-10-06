# Mini-programa: calculadora de gorjeta

conta = float(input("Valor da conta (R$): "))
percentual = float(input("Percentual de gorjeta (%): "))

# Calcula a gorjeta e o total
gorjeta = conta * percentual / 100
total = conta + gorjeta

print("Gorjeta de", percentual, "% sobre R$", conta, "= R$", round(gorjeta, 2))
print("Total a pagar: R$", round(total, 2))
