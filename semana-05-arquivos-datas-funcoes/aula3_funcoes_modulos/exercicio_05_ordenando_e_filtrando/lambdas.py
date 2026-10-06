alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.5},
    {"nome": "Carla", "nota": 7.0},
    {"nome": "Diego", "nota": 5.5},
    {"nome": "Elisa", "nota": 8.2},
]

# Ordena do maior para o menor pela nota
ordenados = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)
print("Do maior para o menor:")
for aluno in ordenados:
    print("-", aluno["nome"], aluno["nota"])

# Filtra só quem tem nota >= 7
aprovados = list(filter(lambda aluno: aluno["nota"] >= 7, alunos))
print("Aprovados:", [aluno["nome"] for aluno in aprovados])
