from pathlib import Path

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab
arquivo = BASE / "diario.txt"

# 1) Modo "w": cria o arquivo e APAGA o que havia antes
with open(arquivo, "w", encoding="utf-8") as f:
    f.write("Hoje comecei a trabalhar com arquivos.\n")
    f.write("Aprendi que o modo w apaga o conteúdo anterior.\n")
    f.write("Estou gostando de ver meus dados virarem arquivos.\n")

# 2) Modo "a": ACRESCENTA ao final, sem apagar
with open(arquivo, "a", encoding="utf-8") as f:
    f.write("Agora estou acrescentando com o modo a.\n")
    f.write("O diário já tem cinco linhas.\n")

# 3) Modo "r": lê e imprime cada linha numerada
with open(arquivo, "r", encoding="utf-8") as f:
    for numero, linha in enumerate(f, start=1):
        print(numero, linha.strip())
