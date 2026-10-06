# Estruturas condicionais em Python

## Sumário

- [1. O que é uma condição?](#1-o-que-é-uma-condição)
- [2. Atribuição e comparação](#2-atribuição-e-comparação)
- [3. Comparações de strings](#3-comparações-de-strings)
- [4. Operadores and e or](#4-operadores-and-e-or)
  - [Operador and](#operador-and)
  - [Operador or](#operador-or)
- [5. Verificando valores em listas](#5-verificando-valores-em-listas)
- [6. Estrutura if](#6-estrutura-if)
- [7. Estrutura if-else](#7-estrutura-if-else)
- [8. Estrutura if-elif-else](#8-estrutura-if-elif-else)
- [9. Vários if independentes](#9-vários-if-independentes)
  - [Diferença principal](#diferença-principal)
- [10. Condições dentro de um for](#10-condições-dentro-de-um-for)
- [11. Verificando se uma lista está vazia](#11-verificando-se-uma-lista-está-vazia)
- [12. Comparando duas listas](#12-comparando-duas-listas)
- [Exercícios com resolução](#exercícios-com-resolução)
  - [Exercício 1 — Maioridade](#exercício-1--maioridade)
  - [Exercício 2 — Número positivo, negativo ou zero](#exercício-2--número-positivo-negativo-ou-zero)
  - [Exercício 3 — Aprovado ou reprovado](#exercício-3--aprovado-ou-reprovado)
  - [Exercício 4 — Classificação da nota](#exercício-4--classificação-da-nota)
  - [Exercício 5 — Login simples](#exercício-5--login-simples)
  - [Exercício 6 — Entrada em um evento](#exercício-6--entrada-em-um-evento)
  - [Exercício 7 — Verificando uma fruta](#exercício-7--verificando-uma-fruta)
  - [Exercício 8 — Usuário administrador](#exercício-8--usuário-administrador)
  - [Exercício 9 — Lista vazia](#exercício-9--lista-vazia)
  - [Exercício 10 — Produtos disponíveis](#exercício-10--produtos-disponíveis)
  - [Exercício 11 — Nomes de usuário duplicados](#exercício-11--nomes-de-usuário-duplicados)
  - [Exercício 12 — Números ordinais](#exercício-12--números-ordinais)
  - [Desafio — Sistema de descontos](#desafio--sistema-de-descontos)

## 1. O que é uma condição?

Uma condição é uma expressão que pode resultar em:

- `True`: verdadeiro;
- `False`: falso.

Python utiliza esses resultados para decidir quais instruções devem ser executadas.

```python
idade = 20

print(idade >= 18)
```

Resultado:

```text
True
```

## 2. Atribuição e comparação

O sinal `=` **atribui** um valor a uma variável:

```python
curso = "Python"
```

O operador `==` **compara** dois valores:

```python
curso == "Python"
```

| Operador | Significado |
| --- | --- |
| `=` | Atribuição |
| `==` | Igual a |
| `!=` | Diferente de |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual a |
| `<=` | Menor ou igual a |

Exemplos:

```python
idade = 18

print(idade == 18)  # True
print(idade != 18)  # False
print(idade > 18)   # False
print(idade >= 18)  # True
```

## 3. Comparações de strings

As comparações diferenciam letras maiúsculas e minúsculas:

```python
linguagem = "Python"

print(linguagem == "python")
```

Resultado:

```text
False
```

Para ignorar essa diferença, podemos usar `lower()`:

```python
print(linguagem.lower() == "python")
```

Resultado:

```text
True
```

O método `lower()` não modifica permanentemente a string original nesse caso. Ele cria uma versão temporária em letras minúsculas para a comparação.

## 4. Operadores `and` e `or`

### Operador `and`

O resultado somente será `True` quando **todas** as condições forem verdadeiras:

```python
idade = 25
possui_documento = True

print(idade >= 18 and possui_documento)
```

### Operador `or`

O resultado será `True` quando **pelo menos uma** condição for verdadeira:

```python
tem_ingresso = False
esta_na_lista = True

print(tem_ingresso or esta_na_lista)
```

| Condição A | Condição B | `A and B` | `A or B` |
| --- | --- | --- | --- |
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

## 5. Verificando valores em listas

O operador `in` verifica se um valor está presente em uma lista:

```python
frutas = ["maçã", "banana", "uva"]

print("banana" in frutas)
```

O operador `not in` verifica se o valor **não** está presente:

```python
print("laranja" not in frutas)
```

Essas verificações também podem ser utilizadas em estruturas condicionais:

```python
if "banana" in frutas:
    print("Banana está disponível.")
```

## 6. Estrutura `if`

O `if` executa um bloco somente quando a condição for verdadeira:

```python
idade = 19

if idade >= 18:
    print("Você é maior de idade.")
```

Todas as instruções pertencentes ao `if` precisam estar indentadas:

```python
if idade >= 18:
    print("Você é maior de idade.")
    print("Seu cadastro pode continuar.")
```

Se a condição for falsa, nenhuma dessas instruções será executada.

## 7. Estrutura `if-else`

O `else` define o que deve acontecer quando a condição do `if` for falsa:

```python
idade = 16

if idade >= 18:
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")
```

Uma das duas alternativas sempre será executada.

## 8. Estrutura `if-elif-else`

Quando existem mais de duas possibilidades, usamos `elif`:

```python
nota = 7.5

if nota >= 9:
    conceito = "Excelente"
elif nota >= 7:
    conceito = "Aprovado"
elif nota >= 5:
    conceito = "Recuperação"
else:
    conceito = "Reprovado"

print(conceito)
```

Python testa as condições **de cima para baixo**. Quando encontra a primeira condição verdadeira, executa aquele bloco e ignora os demais.

Por isso, a **ordem das condições é importante**.

## 9. Vários `if` independentes

Uma estrutura `if-elif-else` executa apenas um bloco. Quando mais de uma condição pode ser verdadeira, utilizamos vários `if` independentes:

```python
habilidades = ["Python", "SQL"]

if "Python" in habilidades:
    print("Possui conhecimento em Python.")

if "SQL" in habilidades:
    print("Possui conhecimento em SQL.")
```

As duas mensagens serão exibidas.

### Diferença principal

```python
if condicao_1:
    ...
elif condicao_2:
    ...
```

Executa somente o primeiro bloco verdadeiro.

```python
if condicao_1:
    ...

if condicao_2:
    ...
```

Testa todas as condições de maneira independente.

## 10. Condições dentro de um `for`

Podemos verificar cada elemento de uma lista:

```python
produtos = ["arroz", "leite", "café"]

for produto in produtos:
    if produto == "leite":
        print("O leite está em promoção.")
    else:
        print(f"Produto: {produto}")
```

Isso permite tratar um elemento de maneira diferente dos demais.

## 11. Verificando se uma lista está vazia

Uma lista com elementos é considerada verdadeira. Uma lista vazia é considerada falsa:

```python
pedidos = []

if pedidos:
    print("Existem pedidos para processar.")
else:
    print("Não existem pedidos.")
```

Essa verificação evita executar um `for` sobre dados inexistentes.

## 12. Comparando duas listas

Podemos verificar se os itens solicitados estão disponíveis:

```python
produtos_disponiveis = ["arroz", "feijão", "café"]
produtos_solicitados = ["arroz", "leite", "café"]

for produto in produtos_solicitados:
    if produto in produtos_disponiveis:
        print(f"{produto.title()} adicionado.")
    else:
        print(f"{produto.title()} não está disponível.")
```

## Exercícios com resolução

### Exercício 1 — Maioridade

Crie uma variável chamada `idade`. Informe se a pessoa é maior ou menor de idade.

#### Resolução

```python
idade = 17

if idade >= 18:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é menor de idade.")
```

### Exercício 2 — Número positivo, negativo ou zero

Crie uma variável numérica e informe se o valor é positivo, negativo ou igual a zero.

#### Resolução

```python
numero = -8

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
```

### Exercício 3 — Aprovado ou reprovado

Considere que um estudante será aprovado se tiver nota maior ou igual a 7.

#### Resolução

```python
nota = 8.5

if nota >= 7:
    print("Estudante aprovado.")
else:
    print("Estudante reprovado.")
```

### Exercício 4 — Classificação da nota

Classifique a nota utilizando as seguintes regras:

- de 9 até 10: excelente;
- de 7 até menos de 9: aprovado;
- de 5 até menos de 7: recuperação;
- abaixo de 5: reprovado.

#### Resolução

```python
nota = 6.5

if nota >= 9:
    resultado = "Excelente"
elif nota >= 7:
    resultado = "Aprovado"
elif nota >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Resultado: {resultado}")
```

Não precisamos escrever `nota >= 5 and nota < 7`, pois, quando o programa chega ao terceiro teste, já sabemos que a nota é menor que 7.

### Exercício 5 — Login simples

Crie duas variáveis: `usuario` e `senha`. O acesso será permitido somente quando o usuário for `"admin"` e a senha for `"1234"`.

#### Resolução

```python
usuario = "admin"
senha = "1234"

if usuario == "admin" and senha == "1234":
    print("Acesso permitido.")
else:
    print("Usuário ou senha incorretos.")
```

### Exercício 6 — Entrada em um evento

Uma pessoa pode entrar se possuir ingresso ou estiver na lista de convidados.

#### Resolução

```python
possui_ingresso = False
esta_na_lista = True

if possui_ingresso or esta_na_lista:
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")
```

Como pelo menos uma condição é verdadeira, a entrada será permitida.

### Exercício 7 — Verificando uma fruta

Crie uma lista com três frutas favoritas. Verifique se `"banana"` está na lista.

#### Resolução

```python
frutas_favoritas = ["maçã", "banana", "uva"]

if "banana" in frutas_favoritas:
    print("Você gosta de banana!")
else:
    print("Banana não está entre suas frutas favoritas.")
```

### Exercício 8 — Usuário administrador

Crie uma lista com usuários, incluindo `"admin"`. Mostre uma mensagem especial para o administrador e uma mensagem comum para os demais usuários.

#### Resolução

```python
usuarios = ["ana", "bruno", "admin", "carla"]

for usuario in usuarios:
    if usuario == "admin":
        print(
            "Olá, admin! Deseja visualizar o relatório do sistema?"
        )
    else:
        print(f"Olá, {usuario.title()}! Bem-vindo novamente.")
```

### Exercício 9 — Lista vazia

Modifique o exercício anterior para verificar se existem usuários antes de percorrer a lista.

#### Resolução

```python
usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == "admin":
            print("Olá, admin! Deseja visualizar o relatório?")
        else:
            print(f"Olá, {usuario.title()}!")
else:
    print("Precisamos cadastrar usuários.")
```

### Exercício 10 — Produtos disponíveis

Considere as listas:

```python
produtos_disponiveis = [
    "notebook",
    "mouse",
    "teclado",
    "monitor"
]

produtos_solicitados = [
    "mouse",
    "impressora",
    "monitor"
]
```

Informe quais produtos podem ser adicionados ao pedido.

#### Resolução

```python
produtos_disponiveis = [
    "notebook",
    "mouse",
    "teclado",
    "monitor"
]

produtos_solicitados = [
    "mouse",
    "impressora",
    "monitor"
]

for produto in produtos_solicitados:
    if produto in produtos_disponiveis:
        print(f"{produto.title()} adicionado ao pedido.")
    else:
        print(f"{produto.title()} não está disponível.")

print("Verificação concluída.")
```

Resultado:

```text
Mouse adicionado ao pedido.
Impressora não está disponível.
Monitor adicionado ao pedido.
Verificação concluída.
```

### Exercício 11 — Nomes de usuário duplicados

Crie uma lista de usuários existentes e outra com novos usuários. Verifique se cada novo nome já está em uso, ignorando diferenças entre letras maiúsculas e minúsculas.

#### Resolução

```python
usuarios_atuais = [
    "Ana",
    "Bruno",
    "Carlos",
    "Mariana"
]

novos_usuarios = [
    "PEDRO",
    "ana",
    "Laura",
    "CARLOS"
]

usuarios_minusculos = []

for usuario in usuarios_atuais:
    usuarios_minusculos.append(usuario.lower())

for novo_usuario in novos_usuarios:
    if novo_usuario.lower() in usuarios_minusculos:
        print(
            f"O nome {novo_usuario} já está em uso. "
            "Escolha outro nome."
        )
    else:
        print(f"O nome {novo_usuario} está disponível.")
```

Também poderíamos criar a lista em uma linha:

```python
usuarios_minusculos = [
    usuario.lower() for usuario in usuarios_atuais
]
```

### Exercício 12 — Números ordinais

Percorra os números de 1 a 9 e mostre:

```text
1º
2º
3º
...
9º
```

#### Resolução

Em português:

```python
numeros = list(range(1, 10))

for numero in numeros:
    print(f"{numero}º")
```

Em português, o símbolo ordinal pode ser usado igualmente para os números apresentados.

Versão do exercício original em inglês:

```python
numeros = list(range(1, 10))

for numero in numeros:
    if numero == 1:
        print("1st")
    elif numero == 2:
        print("2nd")
    elif numero == 3:
        print("3rd")
    else:
        print(f"{numero}th")
```

### Desafio — Sistema de descontos

Uma loja utiliza as seguintes regras:

- compras abaixo de R$ 100 não recebem desconto;
- compras de R$ 100 até menos de R$ 300 recebem 10%;
- compras de R$ 300 até menos de R$ 500 recebem 15%;
- compras a partir de R$ 500 recebem 20%;
- clientes VIP recebem mais 5% de desconto.

Calcule o valor do desconto e o total final.

#### Resolução

```python
valor_compra = 450.00
cliente_vip = True

if valor_compra < 100:
    percentual_desconto = 0
elif valor_compra < 300:
    percentual_desconto = 10
elif valor_compra < 500:
    percentual_desconto = 15
else:
    percentual_desconto = 20

if cliente_vip:
    percentual_desconto += 5

valor_desconto = (
    valor_compra * percentual_desconto / 100
)

valor_final = valor_compra - valor_desconto

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor descontado: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
```

Resultado:

```text
Valor da compra: R$ 450.00
Desconto: 20%
Valor descontado: R$ 90.00
Valor final: R$ 360.00
```

O programa utiliza:

- `if-elif-else` para selecionar somente uma faixa de desconto;
- um segundo `if` independente para acrescentar o benefício VIP.
