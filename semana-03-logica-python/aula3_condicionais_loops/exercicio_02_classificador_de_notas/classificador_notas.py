nota = float(input("Digite a nota do aluno: "))

if nota >= 9:
    classificacao = "Excelente"
elif nota >= 7:
    classificacao = "Bom"
elif nota >= 5:
    classificacao = "Regular"
else:
    classificacao = "Insuficiente"

print("Nota", nota, "->", classificacao)
