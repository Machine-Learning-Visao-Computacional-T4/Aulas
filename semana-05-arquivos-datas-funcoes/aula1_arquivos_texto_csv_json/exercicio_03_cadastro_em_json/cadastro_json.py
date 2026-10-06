import json
from pathlib import Path

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

contatos = [
    {"nome": "Ana Souza", "telefone": "48999991111", "cidade": "Florianópolis"},
    {"nome": "Bruno Lima", "telefone": "48988882222", "cidade": "São José"},
    {"nome": "Carla Dias", "telefone": "47977773333", "cidade": "Joinville"},
    {"nome": "Diego Alves", "telefone": "48966664444", "cidade": "Florianópolis"},
]

# Grava a lista de dicionários em JSON (ensure_ascii=False mantém os acentos)
with open(BASE / "contatos.json", "w", encoding="utf-8") as f:
    json.dump(contatos, f, indent=2, ensure_ascii=False)

# Lê o arquivo de volta: o JSON vira uma lista de dicionários de novo
with open(BASE / "contatos.json", "r", encoding="utf-8") as f:
    lidos = json.load(f)

cidade = input("Mostrar contatos de qual cidade? ")
for contato in lidos:
    if contato["cidade"] == cidade:
        print(contato["nome"], "|", contato["telefone"])
