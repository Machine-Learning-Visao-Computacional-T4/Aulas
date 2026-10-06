"""Funções de limpeza de dados (nome, telefone e data)."""
import re
from datetime import datetime


def limpar_nome(nome):
    """Tira espaços extras e padroniza a caixa (Title Case)."""
    return " ".join(nome.split()).title()


def limpar_telefone(telefone):
    """Devolve só os dígitos do telefone."""
    return re.sub(r"\D", "", telefone)


def telefone_valido(telefone):
    """True se o telefone (só dígitos) tem exatamente 11 dígitos."""
    return re.fullmatch(r"\d{11}", telefone) is not None


def limpar_data(data):
    """Converte dd/mm/aaaa para AAAA-MM-DD."""
    return datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")


if __name__ == "__main__":
    # Testes simples: rode "python limpeza.py" para conferir
    assert limpar_nome("  ana   SOUZA ") == "Ana Souza"
    assert limpar_telefone("(48) 99999-1234") == "48999991234"
    assert telefone_valido("48999991234") is True
    assert telefone_valido("4833334444") is False
    assert limpar_data("05/03/2025") == "2025-03-05"
    print("Todos os testes de limpeza.py passaram.")
