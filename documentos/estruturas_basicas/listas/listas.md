# Listas em Python

## Sumário

- [1. O que é uma lista?](#1-o-que-é-uma-lista)
- [2. Acessando elementos](#2-acessando-elementos)
- [3. Alterando um elemento](#3-alterando-um-elemento)
- [4. Adicionando elementos](#4-adicionando-elementos)
  - [append()](#append)
  - [insert()](#insert)
- [5. Removendo elementos](#5-removendo-elementos)
  - [del](#del)
  - [pop()](#pop)
  - [remove()](#remove)
  - [Quando utilizar cada comando?](#quando-utilizar-cada-comando)
- [6. Organizando uma lista](#6-organizando-uma-lista)
  - [sort()](#sort)
  - [sorted()](#sorted)
  - [reverse()](#reverse)
- [7. Quantidade de elementos](#7-quantidade-de-elementos)
- [8. Erro de índice](#8-erro-de-índice)
- [Exercícios com resolução](#exercícios-com-resolução)
  - [Exercício 1 — Acessando elementos](#exercício-1--acessando-elementos)
  - [Exercício 2 — Mensagens personalizadas](#exercício-2--mensagens-personalizadas)
  - [Exercício 3 — Alterando um produto](#exercício-3--alterando-um-produto)
  - [Exercício 4 — Construindo uma lista](#exercício-4--construindo-uma-lista)
  - [Exercício 5 — Inserindo elementos](#exercício-5--inserindo-elementos)
  - [Exercício 6 — Removendo de maneiras diferentes](#exercício-6--removendo-de-maneiras-diferentes)
  - [Exercício 7 — Organizando cidades](#exercício-7--organizando-cidades)
  - [Exercício 8 — Contando convidados](#exercício-8--contando-convidados)
  - [Exercício 9 — Corrigindo o erro](#exercício-9--corrigindo-o-erro)
  - [Exercício 10 — Lista de compras](#exercício-10--lista-de-compras)
  - [Desafio — Lista de espera](#desafio--lista-de-espera)

## 1. O que é uma lista?

Uma lista é uma estrutura usada para guardar vários valores em uma única variável. Os elementos ficam entre colchetes e são separados por vírgulas.

```python
frutas = ["maçã", "banana", "uva"]
```

Como uma lista normalmente contém vários elementos, é recomendado usar nomes no plural, como `frutas`, `nomes` ou `produtos`.

Uma lista pode armazenar diferentes tipos de dados:

```python
dados = ["Ana", 25, 1.65, True]
```

Entretanto, normalmente utilizamos elementos relacionados e do mesmo tipo.

## 2. Acessando elementos

Cada elemento possui uma posição chamada **índice**. Em Python, a contagem começa em **0**.

```python
frutas = ["maçã", "banana", "uva"]

print(frutas[0])  # maçã
print(frutas[1])  # banana
print(frutas[2])  # uva
```

| Elemento | Índice |
| --- | --- |
| `"maçã"` | 0 |
| `"banana"` | 1 |
| `"uva"` | 2 |

Índices negativos contam a partir do final:

```python
print(frutas[-1])  # uva
print(frutas[-2])  # banana
```

Também podemos utilizar um elemento da lista em uma mensagem:

```python
print(f"Minha fruta favorita é {frutas[0]}.")
```

## 3. Alterando um elemento

Para modificar um elemento, informamos seu índice e o novo valor:

```python
frutas = ["maçã", "banana", "uva"]

frutas[1] = "laranja"

print(frutas)
```

Resultado:

```text
['maçã', 'laranja', 'uva']
```

## 4. Adicionando elementos

### `append()`

Acrescenta um elemento ao final da lista:

```python
frutas = ["maçã", "banana"]
frutas.append("uva")

print(frutas)
```

Resultado:

```text
['maçã', 'banana', 'uva']
```

Também podemos começar com uma lista vazia:

```python
alunos = []

alunos.append("Ana")
alunos.append("Carlos")
alunos.append("Mariana")
```

### `insert()`

Acrescenta um elemento em uma posição específica:

```python
frutas = ["banana", "uva"]
frutas.insert(0, "maçã")

print(frutas)
```

Resultado:

```text
['maçã', 'banana', 'uva']
```

Os outros elementos são deslocados para abrir espaço.

## 5. Removendo elementos

### `del`

Remove um elemento pelo índice quando não precisamos mais do valor:

```python
frutas = ["maçã", "banana", "uva"]

del frutas[1]

print(frutas)
```

### `pop()`

Remove um elemento, mas permite guardar o valor removido:

```python
frutas = ["maçã", "banana", "uva"]

fruta_removida = frutas.pop()

print(frutas)
print(fruta_removida)
```

Sem informar um índice, `pop()` remove o último elemento. Também podemos indicar uma posição:

```python
fruta_removida = frutas.pop(0)
```

### `remove()`

Remove um elemento pelo seu valor:

```python
frutas = ["maçã", "banana", "uva"]

frutas.remove("banana")

print(frutas)
```

O método `remove()` elimina somente a primeira ocorrência encontrada.

### Quando utilizar cada comando?

| Comando | Utilização |
| --- | --- |
| `del lista[indice]` | Remover pelo índice sem reutilizar o valor |
| `lista.pop()` | Remover o último elemento e reutilizar o valor |
| `lista.pop(indice)` | Remover por índice e reutilizar o valor |
| `lista.remove(valor)` | Remover procurando pelo valor |

## 6. Organizando uma lista

### `sort()`

Organiza a própria lista de maneira **permanente**:

```python
nomes = ["Carlos", "Ana", "Bruno"]

nomes.sort()

print(nomes)
```

Ordem inversa:

```python
nomes.sort(reverse=True)
```

### `sorted()`

Produz uma lista ordenada **sem alterar** a lista original:

```python
nomes = ["Carlos", "Ana", "Bruno"]

print(sorted(nomes))
print(nomes)
```

### `reverse()`

Inverte a ordem atual da lista. Não coloca necessariamente em ordem alfabética:

```python
nomes = ["Ana", "Bruno", "Carlos"]

nomes.reverse()

print(nomes)
```

## 7. Quantidade de elementos

A função `len()` informa quantos elementos existem:

```python
frutas = ["maçã", "banana", "uva"]

print(len(frutas))
```

Resultado:

```text
3
```

## 8. Erro de índice

O `IndexError` acontece quando tentamos acessar uma posição inexistente:

```python
frutas = ["maçã", "banana", "uva"]

print(frutas[3])
```

Essa lista possui três elementos, mas os índices disponíveis são 0, 1 e 2.

Para acessar o último elemento, podemos usar:

```python
print(frutas[-1])
```

Se houver dúvida, podemos verificar a lista e seu tamanho:

```python
print(frutas)
print(len(frutas))
```

## Exercícios com resolução

### Exercício 1 — Acessando elementos

Crie uma lista com quatro linguagens de programação. Mostre a primeira, a terceira e a última linguagem.

#### Resolução

```python
linguagens = ["Python", "Java", "JavaScript", "C"]

print(linguagens[0])
print(linguagens[2])
print(linguagens[-1])
```

Resultado:

```text
Python
JavaScript
C
```

### Exercício 2 — Mensagens personalizadas

Crie uma lista com três nomes. Mostre uma mensagem de boas-vindas para cada pessoa acessando os elementos individualmente.

#### Resolução

```python
nomes = ["Ana", "Bruno", "Carla"]

print(f"Olá, {nomes[0]}! Seja bem-vinda.")
print(f"Olá, {nomes[1]}! Seja bem-vindo.")
print(f"Olá, {nomes[2]}! Seja bem-vinda.")
```

### Exercício 3 — Alterando um produto

A lista a seguir contém um produto incorreto:

```python
produtos = ["notebook", "televisão", "mouse"]
```

Substitua `"televisão"` por `"teclado"`.

#### Resolução

```python
produtos = ["notebook", "televisão", "mouse"]

produtos[1] = "teclado"

print(produtos)
```

Resultado:

```text
['notebook', 'teclado', 'mouse']
```

### Exercício 4 — Construindo uma lista

Comece com uma lista vazia chamada `tarefas`. Adicione três tarefas utilizando `append()`.

#### Resolução

```python
tarefas = []

tarefas.append("Estudar Python")
tarefas.append("Fazer os exercícios")
tarefas.append("Revisar a matéria")

print(tarefas)
```

### Exercício 5 — Inserindo elementos

Considere a lista:

```python
cores = ["azul", "verde"]
```

Adicione `"vermelho"` no início e `"amarelo"` no final.

#### Resolução

```python
cores = ["azul", "verde"]

cores.insert(0, "vermelho")
cores.append("amarelo")

print(cores)
```

Resultado:

```text
['vermelho', 'azul', 'verde', 'amarelo']
```

### Exercício 6 — Removendo de maneiras diferentes

Considere a lista:

```python
animais = ["gato", "cachorro", "coelho", "papagaio"]
```

Faça as seguintes operações:

1. Remova `"cachorro"` pelo valor.
2. Remova o primeiro elemento com `pop()` e guarde-o em uma variável.
3. Remova o último elemento usando `del`.

#### Resolução

```python
animais = ["gato", "cachorro", "coelho", "papagaio"]

animais.remove("cachorro")

animal_removido = animais.pop(0)

del animais[-1]

print(f"Animal retirado com pop: {animal_removido}")
print(f"Lista final: {animais}")
```

Resultado:

```text
Animal retirado com pop: gato
Lista final: ['coelho']
```

### Exercício 7 — Organizando cidades

Crie uma lista com cinco cidades fora da ordem alfabética. Mostre:

- a lista original;
- a lista temporariamente ordenada;
- a lista original novamente;
- a lista permanentemente ordenada.

#### Resolução

```python
cidades = [
    "Curitiba",
    "Salvador",
    "Manaus",
    "Brasília",
    "Recife"
]

print("Original:")
print(cidades)

print("Temporariamente ordenada:")
print(sorted(cidades))

print("Original novamente:")
print(cidades)

cidades.sort()

print("Permanentemente ordenada:")
print(cidades)
```

O `sorted()` não altera a lista original, mas o `sort()` altera.

### Exercício 8 — Contando convidados

Crie uma lista com quatro convidados e mostre quantas pessoas serão convidadas.

#### Resolução

```python
convidados = ["Ana", "Bruno", "Carla", "Daniel"]

quantidade = len(convidados)

print(f"Foram convidadas {quantidade} pessoas.")
```

### Exercício 9 — Corrigindo o erro

Explique e corrija o seguinte programa:

```python
notas = [8.5, 7.0, 9.2]
print(notas[3])
```

#### Resolução

A lista possui três elementos, com índices 0, 1 e 2. O índice 3 não existe.

```python
notas = [8.5, 7.0, 9.2]

print(notas[2])
```

Também poderíamos acessar a última nota com:

```python
print(notas[-1])
```

### Exercício 10 — Lista de compras

Crie uma lista com três produtos. Depois:

1. adicione um produto no final;
2. insira um produto no início;
3. substitua o terceiro produto;
4. remova um produto pelo valor;
5. mostre a lista em ordem alfabética;
6. mostre a quantidade final de produtos.

#### Resolução

```python
compras = ["arroz", "feijão", "leite"]

compras.append("café")
compras.insert(0, "pão")
compras[2] = "macarrão"
compras.remove("leite")

compras.sort()

print("Lista de compras:")
print(compras)

print(f"Quantidade de produtos: {len(compras)}")
```

Resultado:

```text
Lista de compras:
['arroz', 'café', 'macarrão', 'pão']
Quantidade de produtos: 4
```

### Desafio — Lista de espera

Uma turma começa com os seguintes estudantes:

```python
estudantes = ["Ana", "Bruno", "Carla"]
```

Faça o programa:

1. adicionar `"Daniel"` ao final;
2. inserir `"Eduarda"` no início;
3. substituir `"Bruno"` por `"Bianca"`;
4. remover o último estudante e guardar seu nome;
5. mostrar quem foi removido;
6. ordenar a lista;
7. mostrar a lista final e a quantidade de estudantes.

#### Resolução

```python
estudantes = ["Ana", "Bruno", "Carla"]

estudantes.append("Daniel")
estudantes.insert(0, "Eduarda")
estudantes[2] = "Bianca"

estudante_removido = estudantes.pop()

estudantes.sort()

print(f"Estudante removido: {estudante_removido}")
print(f"Lista final: {estudantes}")
print(f"Quantidade de estudantes: {len(estudantes)}")
```

Resultado:

```text
Estudante removido: Daniel
Lista final: ['Ana', 'Bianca', 'Carla', 'Eduarda']
Quantidade de estudantes: 4
```
