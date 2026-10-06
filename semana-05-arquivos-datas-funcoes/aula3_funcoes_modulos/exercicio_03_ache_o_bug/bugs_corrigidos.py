# As três funções do exercício "Ache o bug", já corrigidas

# Bug 1: usava print em vez de return (o programa "rodava", mas devolvia None)
def dobro(n):
    return n * 2


# Bug 2: faltavam os dois-pontos depois do def
def somar(a, b):
    return a + b


# Bug 3: a função era chamada ANTES de ser definida
def saudacao(nome):
    return "Olá, " + nome + "!"


print(dobro(5))
print(somar(2, 3))
print(saudacao("Ana"))
