pessoa = {
    "nome": "Ana Souza",
    "idade": 28,
    "cidade": "Florianópolis",
    "profissao": "Analista de dados",
}

# update() adiciona (ou altera) campos
pessoa.update({"email": "ana@exemplo.com"})
print("Dicionário completo:", pessoa)

# .items() devolve pares (chave, valor)
for chave, valor in pessoa.items():
    print(chave + ": " + str(valor))
