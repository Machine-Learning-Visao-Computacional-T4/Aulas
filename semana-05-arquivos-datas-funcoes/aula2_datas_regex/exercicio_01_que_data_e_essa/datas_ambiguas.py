from datetime import datetime

texto = "03/04/2025"

como_brasil = datetime.strptime(texto, "%d/%m/%Y")   # dia/mês/ano
como_eua = datetime.strptime(texto, "%m/%d/%Y")      # mês/dia/ano

print("Lendo como dia/mês/ano (Brasil):", como_brasil.strftime("%d de %B de %Y"))
print("Lendo como mês/dia/ano (EUA):   ", como_eua.strftime("%d de %B de %Y"))
print()
print("Em ordem de texto, o formato AAAA-MM-DD ordena corretamente:")
print(como_brasil.strftime("%Y-%m-%d"), "<", datetime(2025, 12, 1).strftime("%Y-%m-%d"))
