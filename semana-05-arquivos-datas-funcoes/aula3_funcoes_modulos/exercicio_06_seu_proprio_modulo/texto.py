"""Módulo com funções de limpeza de texto."""
import re
from datetime import datetime


def so_digitos(texto):
    """Remove tudo que não for dígito."""
    return re.sub(r"\D", "", texto)


def normalizar_nome(nome):
    """Tira espaços extras e padroniza a caixa (Title Case)."""
    return " ".join(nome.split()).title()


def formatar_data(texto):
    """Converte dd/mm/aaaa para AAAA-MM-DD."""
    return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")


# Este bloco só roda quando o arquivo é executado direto (python texto.py),
# e NÃO quando ele é importado por outro arquivo.
if __name__ == "__main__":
    print(so_digitos("(48) 99999-1234"))        # 48999991234
    print(normalizar_nome("  ana   SOUZA "))    # Ana Souza
    print(formatar_data("05/03/2025"))          # 2025-03-05
