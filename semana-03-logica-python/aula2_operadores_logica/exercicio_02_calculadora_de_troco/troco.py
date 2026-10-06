# Calculadora de troco com // e %
valor_compra = float(input("Valor da compra (R$): "))
valor_pago = float(input("Valor pago em dinheiro (R$): "))

troco = round(valor_pago - valor_compra, 2)

notas_de_10 = int(troco // 10)  # quantas notas de R$ 10 cabem no troco
resto = round(troco % 10, 2)  # o que sobra depois das notas
moedas_de_1 = int(resto // 1)  # quantas moedas de R$ 1 cabem no resto
centavos = round(resto % 1, 2)  # o que sobra depois das moedas de R$ 1

print("Troco total: R$", troco)
print("Notas de R$ 10:", notas_de_10)
print("Moedas de R$ 1:", moedas_de_1)
print("Sobra em centavos: R$", centavos)
