import numpy as np

notas = np.array([[8.5, 9.0, 7.5],
                  [6.0, 7.5, 5.0],
                  [9.5, 8.0, 9.0],
                  [5.0, 6.0, 4.5]])
alunos = np.array(["Ana", "Bruno", "Carla", "Diego"])

print("1)", notas[:, 1].max())
print("2)", notas.mean(axis=1).argmin())
print("3)", (notas >= 7).sum(axis=0))
print("4)", np.where(notas < 6, 0, 1)[0])
