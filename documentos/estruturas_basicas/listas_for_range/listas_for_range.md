# Trabalhando com listas em Python

## Sumário

- [1. Percorrendo listas com for](#1-percorrendo-listas-com-for)
- [2. Executando várias ações](#2-executando-várias-ações)
- [3. Indentação](#3-indentação)
- [4. Criando sequências com range()](#4-criando-sequências-com-range)
- [5. Criando listas numéricas](#5-criando-listas-numéricas)
- [6. Estatísticas simples](#6-estatísticas-simples)
- [7. Compreensão de listas](#7-compreensão-de-listas)
- [8. Recortes de listas](#8-recortes-de-listas)
- [9. Copiando uma lista](#9-copiando-uma-lista)
- [10. Tuplas](#10-tuplas)
- [11. Organização do código](#11-organização-do-código)
- [Exercícios com resolução](#exercícios-com-resolução)
  - [Exercício 1 — Percorrendo uma lista](#exercício-1--percorrendo-uma-lista)
  - [Exercício 2 — Mensagens personalizadas](#exercício-2--mensagens-personalizadas)
  - [Exercício 3 — Corrigindo a indentação](#exercício-3--corrigindo-a-indentação)
  - [Exercício 4 — Contagem com range()](#exercício-4--contagem-com-range)
  - [Exercício 5 — Números pares](#exercício-5--números-pares)
  - [Exercício 6 — Múltiplos de três](#exercício-6--múltiplos-de-três)
  - [Exercício 7 — Quadrados dos números](#exercício-7--quadrados-dos-números)
  - [Exercício 8 — Análise de notas](#exercício-8--análise-de-notas)
  - [Exercício 9 — Trabalhando com recortes](#exercício-9--trabalhando-com-recortes)
  - [Exercício 10 — Cópia independente](#exercício-10--cópia-independente)
  - [Exercício 11 — Cardápio fixo com tupla](#exercício-11--cardápio-fixo-com-tupla)
  - [Exercício 12 — Identificando um erro lógico](#exercício-12--identificando-um-erro-lógico)
  - [Desafio — Análise de vendas](#desafio--análise-de-vendas)

## 1. Percorrendo listas com `for`

O laço `for` permite executar uma ação para cada elemento de uma lista.

```python
alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(aluno)
```

A variável `aluno` recebe temporariamente cada elemento da lista:

- `aluno` recebe `"Ana"`;
- depois recebe `"Bruno"`;
- por fim, recebe `"Carla"`.

É recomendado usar o nome da lista no plural e a variável temporária no singular:

```python
for produto in produtos:
    print(produto)
```

## 2. Executando várias ações

Todas as linhas indentadas pertencem ao `for` e são repetidas:

```python
alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Olá, {aluno}!")
    print("Bem-vindo à aula de Python.\n")
```

Uma linha sem indentação fica **fora** do laço e é executada apenas uma vez:

```python
for aluno in alunos:
    print(f"Olá, {aluno}!")

print("Todos os alunos foram chamados.")
```

## 3. Indentação

Python utiliza indentação para identificar blocos de código. Por convenção, utilizamos **quatro espaços**.

Correto:

```python
for aluno in alunos:
    print(aluno)
```

Incorreto:

```python
for aluno in alunos:
print(aluno)
```

Erros comuns:

- esquecer a indentação;
- indentar uma linha que deveria estar fora do `for`;
- deixar fora do `for` uma linha que deveria ser repetida;
- esquecer os dois-pontos (`:`) após o `for`.

## 4. Criando sequências com `range()`

A função `range()` gera uma sequência de números.

```python
for numero in range(1, 6):
    print(numero)
```

Resultado:

```text
1
2
3
4
5
```

O último valor **não é incluído**. Portanto, `range(1, 6)` produz os números de 1 até 5.

Formas de utilização:

```python
range(6)         # 0, 1, 2, 3, 4, 5
range(1, 6)      # 1, 2, 3, 4, 5
range(2, 11, 2)  # 2, 4, 6, 8, 10
```

O terceiro argumento indica o **passo**.

## 5. Criando listas numéricas

Podemos converter um `range()` em lista:

```python
numeros = list(range(1, 6))

print(numeros)
```

Resultado:

```text
[1, 2, 3, 4, 5]
```

Também podemos construir uma lista usando `for` e `append()`:

```python
quadrados = []

for numero in range(1, 6):
    quadrados.append(numero ** 2)

print(quadrados)
```

Resultado:

```text
[1, 4, 9, 16, 25]
```

## 6. Estatísticas simples

Python oferece funções para trabalhar com listas numéricas:

```python
notas = [7.5, 8.0, 6.5, 9.0]

print(min(notas))
print(max(notas))
print(sum(notas))
```

| Função | Resultado |
| --- | --- |
| `min()` | Menor valor |
| `max()` | Maior valor |
| `sum()` | Soma dos valores |
| `len()` | Quantidade de elementos |

A média pode ser calculada assim:

```python
media = sum(notas) / len(notas)
```

## 7. Compreensão de listas

Uma *list comprehension* permite criar uma lista em uma única linha:

```python
quadrados = [numero ** 2 for numero in range(1, 6)]

print(quadrados)
```

Esse código equivale a:

```python
quadrados = []

for numero in range(1, 6):
    quadrados.append(numero ** 2)
```

Para alunos iniciantes, é importante compreender primeiro a versão completa com `for`.

## 8. Recortes de listas

Um recorte, ou *slice*, permite selecionar parte de uma lista:

```python
alunos = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"]

print(alunos[0:3])
```

Resultado:

```text
['Ana', 'Bruno', 'Carla']
```

Assim como no `range()`, o índice final não é incluído.

| Código | Resultado |
| --- | --- |
| `alunos[:3]` | Primeiros três elementos |
| `alunos[1:4]` | Elementos dos índices 1, 2 e 3 |
| `alunos[2:]` | Do índice 2 até o final |
| `alunos[-3:]` | Últimos três elementos |
| `alunos[:]` | Todos os elementos |

Um recorte também pode ser usado em um `for`:

```python
for aluno in alunos[:3]:
    print(aluno)
```

## 9. Copiando uma lista

Para criar uma lista independente, podemos usar `[:]`:

```python
produtos = ["arroz", "feijão", "leite"]
copia_produtos = produtos[:]
```

Agora as listas são independentes:

```python
produtos.append("café")
copia_produtos.append("açúcar")

print(produtos)
print(copia_produtos)
```

Não devemos fazer isso se quisermos uma cópia independente:

```python
copia_produtos = produtos
```

Nesse caso, as duas variáveis fazem referência à **mesma lista**. Alterar uma também afeta a outra.

## 10. Tuplas

Uma **tupla** é semelhante a uma lista, mas seus elementos não podem ser alterados. Ela é criada com parênteses:

```python
dimensoes = (1920, 1080)
```

Podemos acessar e percorrer seus elementos:

```python
print(dimensoes[0])

for dimensao in dimensoes:
    print(dimensao)
```

Não podemos modificar um elemento:

```python
dimensoes[0] = 1280
```

Esse código produz um `TypeError`.

Podemos, entretanto, substituir a tupla inteira:

```python
dimensoes = (1920, 1080)
dimensoes = (1280, 720)
```

Use **listas** para coleções que podem mudar e **tuplas** para valores que devem permanecer fixos.

## 11. Organização do código

A **PEP 8** apresenta recomendações para escrever código Python legível:

- utilizar quatro espaços para cada nível de indentação;
- usar nomes claros para as variáveis;
- evitar linhas muito longas;
- utilizar linhas em branco para separar partes do programa;
- evitar linhas em branco em excesso;
- priorizar legibilidade.

## Exercícios com resolução

### Exercício 1 — Percorrendo uma lista

Crie uma lista com quatro disciplinas e utilize `for` para mostrar cada uma.

#### Resolução

```python
disciplinas = [
    "Programação",
    "Banco de Dados",
    "Estatística",
    "Machine Learning"
]

for disciplina in disciplinas:
    print(disciplina)
```

### Exercício 2 — Mensagens personalizadas

Crie uma lista com três alunos. Para cada aluno, mostre uma mensagem informando que sua atividade foi recebida. Depois do `for`, mostre uma mensagem final.

#### Resolução

```python
alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"{aluno}, sua atividade foi recebida.")

print("Todas as atividades foram registradas.")
```

A última mensagem aparece apenas uma vez porque está fora do `for`.

### Exercício 3 — Corrigindo a indentação

Corrija o programa:

```python
produtos = ["arroz", "feijão", "leite"]

for produto in produtos:
print(f"Produto: {produto}")

    print("Produto registrado.")

print("Cadastro concluído.")
```

#### Resolução

```python
produtos = ["arroz", "feijão", "leite"]

for produto in produtos:
    print(f"Produto: {produto}")
    print("Produto registrado.")

print("Cadastro concluído.")
```

As duas mensagens indentadas são executadas para cada produto. A mensagem final aparece somente uma vez.

### Exercício 4 — Contagem com range()

Use `range()` para mostrar os números de 1 até 10.

#### Resolução

```python
for numero in range(1, 11):
    print(numero)
```

Usamos 11 porque o valor final não é incluído.

### Exercício 5 — Números pares

Crie uma lista com os números pares de 2 até 20 e mostre cada número.

#### Resolução

```python
numeros_pares = list(range(2, 21, 2))

for numero in numeros_pares:
    print(numero)
```

Resultado da lista:

```text
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

### Exercício 6 — Múltiplos de três

Crie uma lista com os múltiplos de 3, começando em 3 e terminando em 30.

#### Resolução

```python
multiplos_de_tres = list(range(3, 31, 3))

print(multiplos_de_tres)
```

Resultado:

```text
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

### Exercício 7 — Quadrados dos números

Crie uma lista contendo o quadrado dos números de 1 até 10.

#### Resolução

Com `for`:

```python
quadrados = []

for numero in range(1, 11):
    quadrado = numero ** 2
    quadrados.append(quadrado)

print(quadrados)
```

Com compreensão de lista:

```python
quadrados = [numero ** 2 for numero in range(1, 11)]

print(quadrados)
```

Resultado:

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Exercício 8 — Análise de notas

Considere as notas:

```python
notas = [7.5, 8.0, 6.5, 9.5, 8.5]
```

Mostre:

- menor nota;
- maior nota;
- soma das notas;
- média;
- quantidade de notas.

#### Resolução

```python
notas = [7.5, 8.0, 6.5, 9.5, 8.5]

menor_nota = min(notas)
maior_nota = max(notas)
soma_notas = sum(notas)
quantidade = len(notas)
media = soma_notas / quantidade

print(f"Menor nota: {menor_nota}")
print(f"Maior nota: {maior_nota}")
print(f"Soma das notas: {soma_notas}")
print(f"Média: {media:.2f}")
print(f"Quantidade de notas: {quantidade}")
```

Resultado:

```text
Menor nota: 6.5
Maior nota: 9.5
Soma das notas: 40.0
Média: 8.00
Quantidade de notas: 5
```

### Exercício 9 — Trabalhando com recortes

Considere a lista:

```python
linguagens = [
    "Python",
    "Java",
    "JavaScript",
    "C",
    "C++",
    "Ruby"
]
```

Mostre:

- as três primeiras linguagens;
- três linguagens do meio;
- as três últimas linguagens.

#### Resolução

```python
linguagens = [
    "Python",
    "Java",
    "JavaScript",
    "C",
    "C++",
    "Ruby"
]

print("Primeiras três:")
print(linguagens[:3])

print("Três do meio:")
print(linguagens[1:4])

print("Últimas três:")
print(linguagens[-3:])
```

### Exercício 10 — Cópia independente

Crie uma lista de comidas favoritas e faça uma cópia para um amigo. Adicione um alimento diferente em cada lista e mostre os resultados.

#### Resolução

```python
minhas_comidas = ["pizza", "lasanha", "sushi"]

comidas_amigo = minhas_comidas[:]

minhas_comidas.append("hambúrguer")
comidas_amigo.append("sorvete")

print("Minhas comidas:")
for comida in minhas_comidas:
    print(comida)

print("\nComidas do meu amigo:")
for comida in comidas_amigo:
    print(comida)
```

As listas são independentes porque a cópia foi criada com `[:]`.

### Exercício 11 — Cardápio fixo com tupla

Um restaurante oferece cinco pratos fixos. Armazene-os em uma tupla e mostre cada prato.

Depois, crie uma nova versão do cardápio, substituindo dois pratos.

#### Resolução

```python
cardapio = (
    "arroz",
    "feijão",
    "macarrão",
    "salada",
    "frango"
)

print("Cardápio original:")

for prato in cardapio:
    print(prato)

cardapio = (
    "arroz",
    "feijão",
    "purê de batata",
    "legumes",
    "frango"
)

print("\nNovo cardápio:")

for prato in cardapio:
    print(prato)
```

Não modificamos elementos individuais. Substituímos a tupla inteira.

### Exercício 12 — Identificando um erro lógico

Observe:

```python
alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Bem-vindo, {aluno}!")
    print("Todos os alunos foram recebidos.")
```

Por que a segunda mensagem aparece três vezes? Como corrigir?

#### Resolução

Ela está indentada e, por isso, pertence ao `for`. Para executá-la somente uma vez, devemos retirar a indentação:

```python
alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Bem-vindo, {aluno}!")

print("Todos os alunos foram recebidos.")
```

### Desafio — Análise de vendas

Uma loja registrou as vendas dos últimos sete dias:

```python
vendas = [1200, 950, 1430, 870, 1600, 1100, 1350]
```

Crie um programa que:

1. mostre cada venda;
2. apresente a maior e a menor venda;
3. calcule o total;
4. calcule a média;
5. mostre as vendas dos três primeiros dias;
6. crie uma cópia da lista;
7. adicione uma nova venda somente à cópia.

#### Resolução

```python
vendas = [1200, 950, 1430, 870, 1600, 1100, 1350]

print("Vendas registradas:")

for venda in vendas:
    print(f"R$ {venda:.2f}")

maior_venda = max(vendas)
menor_venda = min(vendas)
total_vendas = sum(vendas)
media_vendas = total_vendas / len(vendas)

print(f"\nMaior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")
print(f"Total vendido: R$ {total_vendas:.2f}")
print(f"Média de vendas: R$ {media_vendas:.2f}")

print("\nVendas dos três primeiros dias:")
print(vendas[:3])

copia_vendas = vendas[:]
copia_vendas.append(1700)

print("\nLista original:")
print(vendas)

print("Cópia atualizada:")
print(copia_vendas)
```
