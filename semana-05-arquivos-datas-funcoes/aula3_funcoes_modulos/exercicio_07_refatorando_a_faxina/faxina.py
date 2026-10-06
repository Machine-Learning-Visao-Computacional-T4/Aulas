import csv
from pathlib import Path

import limpeza  # nosso módulo (limpeza.py, na mesma pasta)

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

limpas = []

with open(BASE / "sujo.csv", newline="", encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        telefone = limpeza.limpar_telefone(linha["telefone"])
        limpas.append(
            {
                "nome": limpeza.limpar_nome(linha["nome"]),
                "telefone": telefone,
                "data": limpeza.limpar_data(linha["data"]),
                "situacao": "válido" if limpeza.telefone_valido(telefone) else "inválido",
            }
        )

with open(BASE / "limpo.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome", "telefone", "data", "situacao"])
    escritor.writeheader()
    escritor.writerows(limpas)

for linha in limpas:
    print(linha["nome"], "|", linha["telefone"], "|", linha["data"], "|", linha["situacao"])
print("Arquivo limpo.csv gravado.")
