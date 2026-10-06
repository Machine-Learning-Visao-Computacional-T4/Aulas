import csv
import re
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

limpas = []

with open(BASE / "sujo.csv", newline="", encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        nome = " ".join(linha["nome"].split()).title()  # tira espaços extras e padroniza a caixa
        telefone = re.sub(r"\D", "", linha["telefone"])  # só dígitos
        data = datetime.strptime(linha["data"], "%d/%m/%Y").strftime("%Y-%m-%d")  # AAAA-MM-DD

        # Marca como inválido quem não tem exatamente 11 dígitos
        situacao = "válido" if re.fullmatch(r"\d{11}", telefone) else "inválido"

        limpas.append({"nome": nome, "telefone": telefone, "data": data, "situacao": situacao})

with open(BASE / "limpo.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome", "telefone", "data", "situacao"])
    escritor.writeheader()
    escritor.writerows(limpas)

for linha in limpas:
    print(linha["nome"], "|", linha["telefone"], "|", linha["data"], "|", linha["situacao"])
print("Arquivo limpo.csv gravado.")
