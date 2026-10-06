def media(notas):
    """Média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)


def desconto(preco, percentual=10):
    """Preço com desconto. Se não informar o percentual, aplica 10%."""
    return preco - preco * percentual / 100


def estatisticas(notas):
    """Devolve três valores: mínimo, máximo e média."""
    return min(notas), max(notas), media(notas)


def situacao(media_final):
    """Devolve 'Aprovado' ou 'Reprovado' (usa return, não print)."""
    if media_final >= 7:
        return "Aprovado"
    return "Reprovado"


notas = [8.0, 6.5, 9.0, 5.0]

# Argumentos posicionais e nomeados
print("Média:", media(notas))
print("Desconto padrão (10%):", desconto(200))
print("Desconto de 25% (posicional):", desconto(200, 25))
print("Desconto de 25% (nomeado):", desconto(preco=200, percentual=25))

# Retorno múltiplo
minimo, maximo, media_geral = estatisticas(notas)
print("Mínimo:", minimo, "| Máximo:", maximo, "| Média:", media_geral)

# situacao() dentro de um for
for m in [8.5, 6.9, 7.0, 4.0]:
    print("Média", m, "->", situacao(m))
