import numpy as np

notas = np.array([[8.5, 9.0, 7.5],
                  [6.0, 7.5, 5.0],
                  [9.5, 8.0, 9.0],
                  [5.0, 6.0, 4.5]])
alunos = np.array(["Ana", "Bruno", "Carla", "Diego"])

# Sem nenhum laço para calcular: tudo em blocos
media_aluno = notas.mean(axis=1).round(2)   # axis=1: uma média por LINHA (aluno)
media_prova = notas.mean(axis=0).round(2)   # axis=0: uma média por COLUNA (prova)
situacao = np.where(media_aluno >= 7, "Aprovado", "Reprovado")

# O laço abaixo é só para imprimir
for nome, media, sit in zip(alunos, media_aluno, situacao):
    print(nome, "|", media, "|", sit)

print("Média de cada prova:", media_prova)
print("Maior média:", alunos[media_aluno.argmax()], "com", media_aluno.max())
