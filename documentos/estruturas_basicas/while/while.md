# Entrada de dados e laço `while`

## Sumário

- [1. Recebendo informações com input()](#1-recebendo-informações-com-input)
- [2. Convertendo entradas numéricas](#2-convertendo-entradas-numéricas)
- [3. Criando perguntas claras](#3-criando-perguntas-claras)
- [4. Operador módulo %](#4-operador-módulo-)
- [5. Laço while](#5-laço-while)
- [6. Encerrando o programa com uma palavra](#6-encerrando-o-programa-com-uma-palavra)
- [7. Controlando o while com uma flag](#7-controlando-o-while-com-uma-flag)
- [8. Utilizando break](#8-utilizando-break)
- [9. Utilizando continue](#9-utilizando-continue)
- [10. Evitando laços infinitos](#10-evitando-laços-infinitos)
- [11. Movendo elementos entre listas](#11-movendo-elementos-entre-listas)
- [12. Removendo todas as ocorrências](#12-removendo-todas-as-ocorrências)
- [13. Preenchendo um dicionário](#13-preenchendo-um-dicionário)
- [Exercícios com resolução](#exercícios-com-resolução)
  - [Exercício 1 — Saudação personalizada](#exercício-1--saudação-personalizada)
  - [Exercício 2 — Soma de dois números](#exercício-2--soma-de-dois-números)
  - [Exercício 3 — Reserva de restaurante](#exercício-3--reserva-de-restaurante)
  - [Exercício 4 — Múltiplo de 10](#exercício-4--múltiplo-de-10)
  - [Exercício 5 — Contagem regressiva](#exercício-5--contagem-regressiva)
  - [Exercício 6 — Ingredientes de uma pizza](#exercício-6--ingredientes-de-uma-pizza)
  - [Exercício 7 — Preço do ingresso](#exercício-7--preço-do-ingresso)
  - [Exercício 8 — Mostrando somente números ímpares](#exercício-8--mostrando-somente-números-ímpares)
  - [Exercício 9 — Transferência de pedidos](#exercício-9--transferência-de-pedidos)
  - [Exercício 10 — Removendo produtos indisponíveis](#exercício-10--removendo-produtos-indisponíveis)
  - [Exercício 11 — Pesquisa de linguagens](#exercício-11--pesquisa-de-linguagens)
  - [Exercício 12 — Tentativas de senha](#exercício-12--tentativas-de-senha)
  - [Desafio — Sistema de pedidos](#desafio--sistema-de-pedidos)

## 1. Recebendo informações com `input()`

A função `input()` pausa o programa e espera uma informação do usuário:

```python
nome = input("Digite seu nome: ")

print(f"Olá, {nome}!")
```

Tudo o que é recebido por `input()` é inicialmente uma **string**:

```python
idade = input("Digite sua idade: ")

print(type(idade))
```

Mesmo que o usuário digite `25`, o tipo será `str`.

## 2. Convertendo entradas numéricas

Para realizar cálculos ou comparações, precisamos converter a entrada:

```python
idade = input("Digite sua idade: ")
idade = int(idade)
```

Também podemos fazer a conversão diretamente:

```python
idade = int(input("Digite sua idade: "))
```

Conversões comuns:

| Função | Conversão |
| --- | --- |
| `int()` | Número inteiro |
| `float()` | Número decimal |
| `str()` | String |

Exemplo com um valor decimal:

```python
preco = float(input("Digite o preço: "))

print(f"Preço: R$ {preco:.2f}")
```

Se o usuário informar um texto que não pode ser convertido, como `"vinte"` em `int()`, o programa produzirá um `ValueError`.

## 3. Criando perguntas claras

A mensagem exibida pelo `input()` é chamada de **prompt**:

```python
nome = input("Digite seu primeiro nome: ")
```

Podemos criar um prompt com mais de uma linha:

```python
prompt = "Precisamos da sua idade para verificar o acesso."
prompt += "\nDigite sua idade: "

idade = int(input(prompt))
```

O operador `+=` adiciona um novo conteúdo ao valor atual da variável.

## 4. Operador módulo `%`

O operador `%` retorna o **resto** de uma divisão:

```python
print(10 % 3)
```

Resultado:

```text
1
```

Podemos utilizá-lo para descobrir se um número é par ou ímpar:

```python
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

Se o resto da divisão por 2 for 0, o número é par.

Também podemos verificar múltiplos:

```python
if numero % 10 == 0:
    print("É múltiplo de 10.")
```

## 5. Laço `while`

O `while` repete um bloco **enquanto** uma condição for verdadeira:

```python
numero = 1

while numero <= 5:
    print(numero)
    numero += 1
```

Resultado:

```text
1
2
3
4
5
```

A instrução:

```python
numero += 1
```

equivale a:

```python
numero = numero + 1
```

É fundamental que alguma instrução altere a condição do `while`. Caso contrário, podemos criar um **laço infinito**.

## 6. Encerrando o programa com uma palavra

Podemos manter um programa ativo até que o usuário informe uma palavra de encerramento:

```python
mensagem = ""

while mensagem != "sair":
    mensagem = input(
        "Digite uma mensagem ou 'sair': "
    )

    if mensagem != "sair":
        print(mensagem)
```

O valor inicial `""` permite que Python avalie a condição pela primeira vez.

## 7. Controlando o `while` com uma flag

Uma **flag** é uma variável booleana que controla se o programa deve continuar:

```python
programa_ativo = True

while programa_ativo:
    mensagem = input(
        "Digite uma mensagem ou 'sair': "
    )

    if mensagem == "sair":
        programa_ativo = False
    else:
        print(mensagem)
```

Flags são úteis quando existem várias situações capazes de encerrar o programa.

## 8. Utilizando `break`

O comando `break` encerra imediatamente um laço:

```python
while True:
    cidade = input(
        "Digite uma cidade ou 'sair': "
    )

    if cidade == "sair":
        break

    print(f"Você informou: {cidade}")
```

`while True` cria um laço que somente termina quando um `break` é executado.

## 9. Utilizando `continue`

O comando `continue` ignora o restante da repetição atual e retorna ao início do laço:

```python
numero = 0

while numero < 10:
    numero += 1

    if numero % 2 == 0:
        continue

    print(numero)
```

Resultado:

```text
1
3
5
7
9
```

Quando o número é par, o `continue` impede a execução do `print()`.

## 10. Evitando laços infinitos

Este laço nunca termina:

```python
numero = 1

while numero <= 5:
    print(numero)
```

A variável `numero` nunca muda, então a condição sempre permanece verdadeira.

A correção é:

```python
numero = 1

while numero <= 5:
    print(numero)
    numero += 1
```

Para interromper um laço infinito no terminal, normalmente utilizamos `Ctrl+C`.

## 11. Movendo elementos entre listas

O `while` é útil quando precisamos modificar uma lista enquanto a percorremos:

```python
usuarios_pendentes = [
    "Ana",
    "Bruno",
    "Carla"
]

usuarios_confirmados = []

while usuarios_pendentes:
    usuario = usuarios_pendentes.pop()

    print(f"Confirmando {usuario}.")
    usuarios_confirmados.append(usuario)
```

O laço continua enquanto a lista `usuarios_pendentes` possuir elementos.

## 12. Removendo todas as ocorrências

O método `remove()` elimina apenas a primeira ocorrência. Para remover todas, podemos usar `while`:

```python
animais = [
    "gato",
    "cachorro",
    "gato",
    "coelho",
    "gato"
]

while "gato" in animais:
    animais.remove("gato")

print(animais)
```

Resultado:

```text
['cachorro', 'coelho']
```

## 13. Preenchendo um dicionário

Podemos utilizar `while` e `input()` para coletar respostas:

```python
respostas = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input("Digite seu nome: ")
    linguagem = input(
        "Qual é sua linguagem favorita? "
    )

    respostas[nome] = linguagem

    repetir = input(
        "Outra pessoa responderá? (sim/não): "
    )

    if repetir.lower() == "não":
        pesquisa_ativa = False

for nome, linguagem in respostas.items():
    print(f"{nome}: {linguagem}")
```

## Exercícios com resolução

### Exercício 1 — Saudação personalizada

Peça o nome do usuário e mostre uma saudação.

#### Resolução

```python
nome = input("Digite seu nome: ")

print(f"Olá, {nome}! Seja bem-vindo.")
```

### Exercício 2 — Soma de dois números

Peça dois números inteiros e mostre a soma.

#### Resolução

```python
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

soma = numero_1 + numero_2

print(f"Resultado: {soma}")
```

Sem `int()`, Python concatenaria os textos. Por exemplo, `"10" + "5"` produziria `"105"`.

### Exercício 3 — Reserva de restaurante

Pergunte quantas pessoas fazem parte de um grupo. Se houver mais de oito pessoas, informe que será necessário aguardar. Caso contrário, informe que a mesa está pronta.

#### Resolução

```python
quantidade = int(
    input("Quantas pessoas estão no grupo? ")
)

if quantidade > 8:
    print("Será necessário aguardar uma mesa.")
else:
    print("A mesa está pronta.")
```

### Exercício 4 — Múltiplo de 10

Peça um número e informe se ele é múltiplo de 10.

#### Resolução

```python
numero = int(input("Digite um número: "))

if numero % 10 == 0:
    print(f"{numero} é múltiplo de 10.")
else:
    print(f"{numero} não é múltiplo de 10.")
```

### Exercício 5 — Contagem regressiva

Utilize `while` para mostrar os números de 10 até 1. Depois, mostre `"Fim!"`.

#### Resolução

```python
numero = 10

while numero >= 1:
    print(numero)
    numero -= 1

print("Fim!")
```

### Exercício 6 — Ingredientes de uma pizza

Peça ingredientes até que o usuário digite `"sair"`. Para cada ingrediente, mostre uma confirmação.

#### Resolução

```python
while True:
    ingrediente = input(
        "Digite um ingrediente ou 'sair': "
    )

    if ingrediente.lower() == "sair":
        break

    print(
        f"{ingrediente.title()} será adicionado à pizza."
    )

print("Pedido finalizado.")
```

### Exercício 7 — Preço do ingresso

Peça repetidamente a idade dos clientes:

- menos de 3 anos: gratuito;
- de 3 até 12 anos: R$ 10;
- acima de 12 anos: R$ 15.

O usuário pode digitar `"sair"` para encerrar.

#### Resolução

```python
while True:
    entrada = input(
        "Digite a idade ou 'sair': "
    )

    if entrada.lower() == "sair":
        break

    idade = int(entrada)

    if idade < 3:
        preco = 0
    elif idade <= 12:
        preco = 10
    else:
        preco = 15

    print(f"Preço do ingresso: R$ {preco:.2f}")
```

Primeiro verificamos `"sair"` e somente depois convertemos o valor para inteiro.

### Exercício 8 — Mostrando somente números ímpares

Utilize `while` e `continue` para mostrar os números ímpares de 1 até 20.

#### Resolução

```python
numero = 0

while numero < 20:
    numero += 1

    if numero % 2 == 0:
        continue

    print(numero)
```

### Exercício 9 — Transferência de pedidos

Considere uma lista de pedidos pendentes. Mova cada pedido para uma lista de pedidos concluídos.

#### Resolução

```python
pedidos_pendentes = [
    "pedido_101",
    "pedido_102",
    "pedido_103"
]

pedidos_concluidos = []

while pedidos_pendentes:
    pedido = pedidos_pendentes.pop(0)

    print(f"Processando {pedido}.")
    pedidos_concluidos.append(pedido)

print("\nPedidos concluídos:")

for pedido in pedidos_concluidos:
    print(pedido)
```

Usamos `pop(0)` para retirar os pedidos na mesma ordem em que aparecem na lista.

### Exercício 10 — Removendo produtos indisponíveis

Remova todas as ocorrências de `"indisponível"`:

```python
produtos = [
    "notebook",
    "indisponível",
    "mouse",
    "indisponível",
    "teclado"
]
```

#### Resolução

```python
produtos = [
    "notebook",
    "indisponível",
    "mouse",
    "indisponível",
    "teclado"
]

while "indisponível" in produtos:
    produtos.remove("indisponível")

print(produtos)
```

Resultado:

```text
['notebook', 'mouse', 'teclado']
```

### Exercício 11 — Pesquisa de linguagens

Faça uma pesquisa perguntando o nome e a linguagem de programação favorita de cada pessoa. Armazene as respostas em um dicionário.

#### Resolução

```python
respostas = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input("\nDigite seu nome: ")
    linguagem = input(
        "Qual é sua linguagem favorita? "
    )

    respostas[nome] = linguagem

    continuar = input(
        "Outra pessoa responderá? (sim/não): "
    )

    if continuar.lower() == "não":
        pesquisa_ativa = False

print("\nResultados da pesquisa:")

for nome, linguagem in respostas.items():
    print(
        f"{nome} escolheu {linguagem}."
    )
```

### Exercício 12 — Tentativas de senha

Defina uma senha correta e permita no máximo três tentativas. Encerre o laço quando a senha estiver correta ou quando as tentativas terminarem.

#### Resolução

```python
senha_correta = "python123"
tentativas = 0
limite = 3

while tentativas < limite:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Acesso permitido.")
        break

    tentativas_restantes = limite - tentativas

    if tentativas_restantes > 0:
        print(
            f"Senha incorreta. "
            f"Restam {tentativas_restantes} tentativa(s)."
        )
    else:
        print("Acesso bloqueado.")
```

### Desafio — Sistema de pedidos

Crie um programa que:

1. solicite produtos até o usuário digitar `"finalizar"`;
2. peça a quantidade de cada produto;
3. armazene os produtos e quantidades em um dicionário;
4. ao final, mostre o resumo do pedido.

#### Resolução

```python
pedido = {}

while True:
    produto = input(
        "Digite o produto ou 'finalizar': "
    )

    if produto.lower() == "finalizar":
        break

    quantidade = int(
        input("Digite a quantidade: ")
    )

    if produto in pedido:
        pedido[produto] += quantidade
    else:
        pedido[produto] = quantidade

print("\nResumo do pedido:")

if pedido:
    for produto, quantidade in pedido.items():
        print(
            f"{produto.title()}: {quantidade} unidade(s)"
        )
else:
    print("Nenhum produto foi adicionado.")
```
