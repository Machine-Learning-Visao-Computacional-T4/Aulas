# Dicionários em Python

## Sumário

- [1. O que é um dicionário?](#1-o-que-é-um-dicionário)
- [2. Acessando valores](#2-acessando-valores)
- [3. Adicionando informações](#3-adicionando-informações)
- [4. Modificando valores](#4-modificando-valores)
- [5. Removendo informações](#5-removendo-informações)
- [6. Acessando valores com get()](#6-acessando-valores-com-get)
- [7. Percorrendo chaves e valores](#7-percorrendo-chaves-e-valores)
- [8. Percorrendo somente as chaves](#8-percorrendo-somente-as-chaves)
- [9. Percorrendo somente os valores](#9-percorrendo-somente-os-valores)
- [10. Lista de dicionários](#10-lista-de-dicionários)
- [11. Lista dentro de um dicionário](#11-lista-dentro-de-um-dicionário)
- [12. Dicionário dentro de outro dicionário](#12-dicionário-dentro-de-outro-dicionário)
- [Resumo dos principais comandos](#resumo-dos-principais-comandos)
- [Exercícios com resolução](#exercícios-com-resolução)
  - [Exercício 1 — Cadastro de uma pessoa](#exercício-1--cadastro-de-uma-pessoa)
  - [Exercício 2 — Construindo um dicionário vazio](#exercício-2--construindo-um-dicionário-vazio)
  - [Exercício 3 — Atualizando o estoque](#exercício-3--atualizando-o-estoque)
  - [Exercício 4 — Removendo uma informação](#exercício-4--removendo-uma-informação)
  - [Exercício 5 — Evitando um KeyError](#exercício-5--evitando-um-keyerror)
  - [Exercício 6 — Glossário de programação](#exercício-6--glossário-de-programação)
  - [Exercício 7 — Números favoritos](#exercício-7--números-favoritos)
  - [Exercício 8 — Linguagens sem repetição](#exercício-8--linguagens-sem-repetição)
  - [Exercício 9 — Lista de produtos](#exercício-9--lista-de-produtos)
  - [Exercício 10 — Aluno com várias notas](#exercício-10--aluno-com-várias-notas)
  - [Exercício 11 — Pessoas e lugares favoritos](#exercício-11--pessoas-e-lugares-favoritos)
  - [Exercício 12 — Cadastro de cidades](#exercício-12--cadastro-de-cidades)
  - [Desafio — Sistema de pedidos](#desafio--sistema-de-pedidos)

## 1. O que é um dicionário?

Um dicionário armazena informações em pares de **chave** e **valor**.

```python
produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 8
}
```

Nesse exemplo:

- `"nome"`, `"preco"` e `"estoque"` são as chaves;
- `"Notebook"`, `3500.00` e `8` são os valores.

Dicionários utilizam chaves `{}`, enquanto listas utilizam colchetes `[]`.

## 2. Acessando valores

Para acessar um valor, informamos a chave entre colchetes:

```python
produto = {
    "nome": "Notebook",
    "preco": 3500.00
}

print(produto["nome"])
print(produto["preco"])
```

Resultado:

```text
Notebook
3500.0
```

Também podemos usar o valor em uma mensagem:

```python
print(f"O produto custa R$ {produto['preco']:.2f}.")
```

## 3. Adicionando informações

Um dicionário pode receber novas chaves após sua criação:

```python
produto = {
    "nome": "Notebook"
}

produto["preco"] = 3500.00
produto["estoque"] = 8

print(produto)
```

Resultado:

```text
{'nome': 'Notebook', 'preco': 3500.0, 'estoque': 8}
```

Também podemos começar com um dicionário vazio:

```python
aluno = {}

aluno["nome"] = "Ana"
aluno["nota"] = 8.5
aluno["aprovado"] = True
```

## 4. Modificando valores

Para modificar um valor, utilizamos uma chave existente:

```python
produto = {
    "nome": "Notebook",
    "estoque": 8
}

produto["estoque"] = 7

print(produto)
```

Também podemos utilizar o valor anterior em um cálculo:

```python
produto["estoque"] = produto["estoque"] - 1
```

Forma abreviada:

```python
produto["estoque"] -= 1
```

## 5. Removendo informações

O comando `del` remove permanentemente uma chave e seu valor:

```python
produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 8
}

del produto["estoque"]

print(produto)
```

Resultado:

```text
{'nome': 'Notebook', 'preco': 3500.0}
```

## 6. Acessando valores com `get()`

Se tentarmos acessar uma chave inexistente com colchetes, Python produzirá um `KeyError`:

```python
produto = {"nome": "Notebook"}

print(produto["desconto"])
```

Para evitar o erro, podemos utilizar `get()`:

```python
desconto = produto.get("desconto", 0)

print(desconto)
```

Se a chave existir, `get()` retorna seu valor. Caso contrário, retorna o valor padrão informado.

```python
cidade = pessoa.get("cidade", "Cidade não informada")
```

Sem um valor padrão, `get()` retorna `None`:

```python
cidade = pessoa.get("cidade")
```

## 7. Percorrendo chaves e valores

O método `items()` permite percorrer as chaves e os valores:

```python
aluno = {
    "nome": "Ana",
    "curso": "Python",
    "nota": 8.5
}

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
```

Resultado:

```text
nome: Ana
curso: Python
nota: 8.5
```

## 8. Percorrendo somente as chaves

O método `keys()` retorna as chaves:

```python
for chave in aluno.keys():
    print(chave)
```

Também podemos omitir `keys()`:

```python
for chave in aluno:
    print(chave)
```

Para percorrer as chaves em ordem:

```python
for chave in sorted(aluno.keys()):
    print(chave)
```

## 9. Percorrendo somente os valores

O método `values()` retorna os valores:

```python
for valor in aluno.values():
    print(valor)
```

Se houver valores repetidos, podemos usar `set()` para obter somente os valores únicos:

```python
linguagens = {
    "Ana": "Python",
    "Bruno": "Java",
    "Carla": "Python"
}

for linguagem in set(linguagens.values()):
    print(linguagem)
```

Resultado:

```text
Python
Java
```

A ordem pode variar porque conjuntos não mantêm uma ordem específica.

## 10. Lista de dicionários

Podemos armazenar vários dicionários dentro de uma lista:

```python
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.0}
]

for aluno in alunos:
    print(f"{aluno['nome']}: {aluno['nota']}")
```

Cada dicionário representa um aluno.

## 11. Lista dentro de um dicionário

Um valor do dicionário pode ser uma lista:

```python
aluno = {
    "nome": "Ana",
    "disciplinas": [
        "Python",
        "Banco de Dados",
        "Estatística"
    ]
}

for disciplina in aluno["disciplinas"]:
    print(disciplina)
```

## 12. Dicionário dentro de outro dicionário

Também podemos colocar um dicionário dentro de outro:

```python
usuarios = {
    "ana123": {
        "nome": "Ana",
        "cidade": "Curitiba"
    },
    "bruno456": {
        "nome": "Bruno",
        "cidade": "São Paulo"
    }
}
```

Para percorrer:

```python
for usuario, informacoes in usuarios.items():
    print(f"Usuário: {usuario}")
    print(f"Nome: {informacoes['nome']}")
    print(f"Cidade: {informacoes['cidade']}")
```

É recomendado que os dicionários internos possuam a mesma estrutura.

## Resumo dos principais comandos

| Operação | Exemplo |
| --- | --- |
| Criar dicionário | `aluno = {"nome": "Ana"}` |
| Acessar valor | `aluno["nome"]` |
| Acesso seguro | `aluno.get("idade", 0)` |
| Adicionar chave | `aluno["idade"] = 20` |
| Modificar valor | `aluno["idade"] = 21` |
| Remover chave | `del aluno["idade"]` |
| Percorrer pares | `aluno.items()` |
| Percorrer chaves | `aluno.keys()` |
| Percorrer valores | `aluno.values()` |

## Exercícios com resolução

### Exercício 1 — Cadastro de uma pessoa

Crie um dicionário para representar uma pessoa. Armazene nome, idade, cidade e profissão. Mostre cada informação individualmente.

#### Resolução

```python
pessoa = {
    "nome": "Mariana",
    "idade": 28,
    "cidade": "Curitiba",
    "profissao": "Engenheira"
}

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")
print(f"Profissão: {pessoa['profissao']}")
```

### Exercício 2 — Construindo um dicionário vazio

Comece com um dicionário vazio chamado `produto`. Adicione nome, preço e quantidade.

#### Resolução

```python
produto = {}

produto["nome"] = "Teclado"
produto["preco"] = 150.00
produto["quantidade"] = 10

print(produto)
```

Resultado:

```text
{'nome': 'Teclado', 'preco': 150.0, 'quantidade': 10}
```

### Exercício 3 — Atualizando o estoque

O dicionário abaixo representa um produto:

```python
produto = {
    "nome": "Mouse",
    "estoque": 15
}
```

Considere que três unidades foram vendidas. Atualize o estoque.

#### Resolução

```python
produto = {
    "nome": "Mouse",
    "estoque": 15
}

produto["estoque"] -= 3

print(f"Estoque atual: {produto['estoque']}")
```

Resultado:

```text
Estoque atual: 12
```

### Exercício 4 — Removendo uma informação

Remova a chave `"senha"` do dicionário antes de exibi-lo.

#### Resolução

```python
usuario = {
    "nome": "Ana",
    "email": "ana@email.com",
    "senha": "123456"
}

del usuario["senha"]

print(usuario)
```

Resultado:

```text
{'nome': 'Ana', 'email': 'ana@email.com'}
```

### Exercício 5 — Evitando um KeyError

O dicionário não possui a chave `"telefone"`. Mostre uma mensagem adequada sem produzir erro.

#### Resolução

```python
cliente = {
    "nome": "Carlos",
    "email": "carlos@email.com"
}

telefone = cliente.get(
    "telefone",
    "Telefone não informado"
)

print(telefone)
```

### Exercício 6 — Glossário de programação

Crie um dicionário com cinco termos de programação e seus significados. Utilize um `for` para mostrar todos os termos.

#### Resolução

```python
glossario = {
    "variável": "Nome que referencia um valor.",
    "lista": "Coleção ordenada de elementos.",
    "dicionário": "Coleção de pares de chave e valor.",
    "condição": "Expressão avaliada como verdadeira ou falsa.",
    "laço": "Estrutura que repete instruções."
}

for termo, significado in glossario.items():
    print(f"{termo.title()}:")
    print(f"  {significado}\n")
```

### Exercício 7 — Números favoritos

Crie um dicionário que relacione cinco pessoas aos seus números favoritos. Mostre uma mensagem para cada pessoa.

#### Resolução

```python
numeros_favoritos = {
    "Ana": 7,
    "Bruno": 10,
    "Carla": 3,
    "Daniel": 21,
    "Eduarda": 8
}

for pessoa, numero in numeros_favoritos.items():
    print(
        f"O número favorito de {pessoa} é {numero}."
    )
```

### Exercício 8 — Linguagens sem repetição

Considere a pesquisa:

```python
linguagens = {
    "Ana": "Python",
    "Bruno": "Java",
    "Carla": "Python",
    "Daniel": "C",
    "Eduarda": "Java"
}
```

Mostre todas as linguagens mencionadas sem repetições.

#### Resolução

```python
linguagens = {
    "Ana": "Python",
    "Bruno": "Java",
    "Carla": "Python",
    "Daniel": "C",
    "Eduarda": "Java"
}

print("Linguagens mencionadas:")

for linguagem in set(linguagens.values()):
    print(linguagem)
```

### Exercício 9 — Lista de produtos

Crie três dicionários representando produtos. Armazene-os em uma lista e mostre as informações utilizando `for`.

#### Resolução

```python
produtos = [
    {
        "nome": "Notebook",
        "preco": 3500.00,
        "estoque": 5
    },
    {
        "nome": "Mouse",
        "preco": 80.00,
        "estoque": 20
    },
    {
        "nome": "Teclado",
        "preco": 150.00,
        "estoque": 12
    }
]

for produto in produtos:
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Estoque: {produto['estoque']}\n")
```

### Exercício 10 — Aluno com várias notas

Crie um dicionário que contenha o nome de um aluno e uma lista de notas. Calcule a média.

#### Resolução

```python
aluno = {
    "nome": "Mariana",
    "notas": [8.0, 7.5, 9.0, 8.5]
}

media = sum(aluno["notas"]) / len(aluno["notas"])

print(f"Aluno: {aluno['nome']}")
print(f"Notas: {aluno['notas']}")
print(f"Média: {media:.2f}")
```

Resultado:

```text
Aluno: Mariana
Notas: [8.0, 7.5, 9.0, 8.5]
Média: 8.25
```

### Exercício 11 — Pessoas e lugares favoritos

Crie um dicionário em que cada pessoa possua uma lista de lugares favoritos.

#### Resolução

```python
lugares_favoritos = {
    "Ana": ["Curitiba", "Florianópolis"],
    "Bruno": ["São Paulo"],
    "Carla": ["Recife", "Salvador", "Fortaleza"]
}

for pessoa, lugares in lugares_favoritos.items():
    print(f"\nLugares favoritos de {pessoa}:")

    for lugar in lugares:
        print(f"- {lugar}")
```

Aqui temos um `for` externo para percorrer o dicionário e um `for` interno para percorrer cada lista.

### Exercício 12 — Cadastro de cidades

Crie um dicionário no qual cada cidade esteja relacionada a outro dicionário com país, população e uma curiosidade.

#### Resolução

```python
cidades = {
    "Curitiba": {
        "pais": "Brasil",
        "populacao": 1_770_000,
        "curiosidade": "É a capital do Paraná."
    },
    "Paris": {
        "pais": "França",
        "populacao": 2_100_000,
        "curiosidade": "É conhecida pela Torre Eiffel."
    },
    "Tóquio": {
        "pais": "Japão",
        "populacao": 14_000_000,
        "curiosidade": "É uma das maiores cidades do mundo."
    }
}

for cidade, informacoes in cidades.items():
    print(f"\nCidade: {cidade}")
    print(f"País: {informacoes['pais']}")
    print(f"População: {informacoes['populacao']}")
    print(f"Curiosidade: {informacoes['curiosidade']}")
```

### Desafio — Sistema de pedidos

Crie um pedido contendo:

- número do pedido;
- nome do cliente;
- lista de produtos;
- situação do pedido.

Depois:

1. mostre os dados do pedido;
2. percorra e mostre os produtos;
3. altere a situação para `"enviado"`;
4. tente acessar uma chave opcional chamada `"cupom"` usando `get()`.

#### Resolução

```python
pedido = {
    "numero": 1001,
    "cliente": "Ana",
    "produtos": [
        {
            "nome": "Notebook",
            "preco": 3500.00,
            "quantidade": 1
        },
        {
            "nome": "Mouse",
            "preco": 80.00,
            "quantidade": 2
        }
    ],
    "situacao": "em preparação"
}

print(f"Pedido: {pedido['numero']}")
print(f"Cliente: {pedido['cliente']}")
print(f"Situação: {pedido['situacao']}")

total = 0

print("\nProdutos:")

for produto in pedido["produtos"]:
    subtotal = produto["preco"] * produto["quantidade"]
    total += subtotal

    print(f"- {produto['nome']}")
    print(f"  Quantidade: {produto['quantidade']}")
    print(f"  Subtotal: R$ {subtotal:.2f}")

pedido["situacao"] = "enviado"

cupom = pedido.get("cupom", "Nenhum cupom utilizado")

print(f"\nTotal: R$ {total:.2f}")
print(f"Nova situação: {pedido['situacao']}")
print(f"Cupom: {cupom}")
```
