import csv
from pathlib import Path

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

resultados = []

# Lê notas.csv com DictReader: cada linha vira um dicionário
with open(BASE / "notas.csv", newline="", encoding="utf-8") as f:
    for aluno in csv.DictReader(f):
        nota1 = float(aluno["nota1"])  # o CSV traz tudo como texto: converter!
        nota2 = float(aluno["nota2"])
        media = (nota1 + nota2) / 2
        situacao = "Aprovado" if media >= 7 else "Reprovado"
        resultados.append({"nome": aluno["nome"], "media": round(media, 2), "situacao": situacao})

# Extra: ordena pela média, da maior para a menor
resultados.sort(key=lambda r: r["media"], reverse=True)

# Grava resultado.csv com DictWriter
with open(BASE / "resultado.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome", "media", "situacao"])
    escritor.writeheader()
    escritor.writerows(resultados)

for r in resultados:
    print(r["nome"], "|", r["media"], "|", r["situacao"])
print("Arquivo resultado.csv gravado.")
