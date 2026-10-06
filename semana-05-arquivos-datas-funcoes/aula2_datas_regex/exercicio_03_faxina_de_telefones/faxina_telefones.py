import csv
import re
from pathlib import Path

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

with open(BASE / "contatos.csv", newline="", encoding="utf-8") as f:
    for contato in csv.DictReader(f):
        original = contato["telefone"]
        so_digitos = re.sub(r"\D", "", original)  # remove tudo que NÃO é dígito
        valido = re.fullmatch(r"\d{11}", so_digitos)  # exatamente 11 dígitos?
        situacao = "válido" if valido else "inválido"
        print(contato["nome"], "|", original, "->", so_digitos, "|", situacao)
