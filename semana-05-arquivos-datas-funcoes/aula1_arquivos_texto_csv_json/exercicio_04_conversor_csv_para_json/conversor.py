import csv
import json
from pathlib import Path

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

# Opcional: aceita o nome do arquivo via input() (Enter usa notas.csv)
nome_arquivo = input("Arquivo CSV (Enter para notas.csv): ") or "notas.csv"

dados = []
with open(BASE / nome_arquivo, newline="", encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        dados.append(
            {
                "nome": linha["nome"],
                "nota1": float(linha["nota1"]),  # converte texto em número
                "nota2": float(linha["nota2"]),
            }
        )

with open(BASE / "dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print(len(dados), "registros convertidos para dados.json")
