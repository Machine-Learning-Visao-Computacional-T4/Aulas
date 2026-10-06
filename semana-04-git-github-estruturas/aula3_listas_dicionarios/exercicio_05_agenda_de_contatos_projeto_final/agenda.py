contatos = [
    {"nome": "Ana Souza", "telefone": "(48) 99999-1111", "cidade": "Florianópolis"},
    {"nome": "Bruno Lima", "telefone": "(48) 98888-2222", "cidade": "São José"},
    {"nome": "Carla Dias", "telefone": "(47) 97777-3333", "cidade": "Joinville"},
    {"nome": "Diego Alves", "telefone": "(48) 96666-4444", "cidade": "Palhoça"},
    {"nome": "Elisa Rocha", "telefone": "(49) 95555-5555", "cidade": "Chapecó"},
]


def buscar_contato(nome):
    """Devolve o contato cujo nome contém o texto buscado, ou None se não achar."""
    for contato in contatos:
        if nome.lower() in contato["nome"].lower():
            return contato
    return None


busca = input("Nome para buscar: ")
resultado = buscar_contato(busca)

if resultado is None:
    print("Contato não encontrado.")
else:
    print("Encontrado:", resultado["nome"], "|", resultado["telefone"], "|", resultado["cidade"])
