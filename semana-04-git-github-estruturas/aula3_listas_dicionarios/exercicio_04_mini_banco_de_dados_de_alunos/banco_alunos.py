alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.5},
    {"nome": "Carla", "nota": 7.0},
    {"nome": "Diego", "nota": 5.5},
    {"nome": "Elisa", "nota": 8.2},
]

aprovados = 0  # contador

print("Alunos aprovados (nota >= 7):")
for aluno in alunos:
    if aluno["nota"] >= 7:
        print("-", aluno["nome"], "| nota:", aluno["nota"])
        aprovados += 1

print("Total de aprovados:", aprovados)
