import re

# (padrão, um texto que casa, um texto que NÃO casa)
padroes = [
    (r"\d{2}/\d{2}/\d{4}", "25/12/2025", "25-12-2025"),
    (r"[A-Z]{3}-\d{4}", "ABC-1234", "abc-1234"),
    (r"\w+@\w+\.com", "ana@exemplo.com", "ana@exemplo.com.br"),
    (r"^\s+|\s+$", "  texto com espaços  ", "texto sem espaços nas pontas"),
]

for padrao, casa, nao_casa in padroes:
    achou_1 = bool(re.search(padrao, casa))
    achou_2 = bool(re.fullmatch(padrao, nao_casa))
    print("Padrão:", padrao)
    print("   casa com", repr(casa), "->", achou_1)
    print("   fullmatch em", repr(nao_casa), "->", achou_2)
