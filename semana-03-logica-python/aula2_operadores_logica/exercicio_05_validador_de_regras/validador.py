# Validador de regras combinadas: aprovado se nota >= 7 E frequência >= 75%
nota = float(input("Nota final: "))
frequencia = float(input("Frequência (%): "))

aprovado = nota >= 7 and frequencia >= 75

print("Nota:", nota, "| Frequência:", frequencia, "%")
print("Aprovado?", aprovado)
