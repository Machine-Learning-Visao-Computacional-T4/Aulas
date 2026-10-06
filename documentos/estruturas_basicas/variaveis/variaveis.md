# Variáveis, strings e números

## Sumário

- [Variáveis](#variáveis)
  - [Regras para nomes de variáveis](#regras-para-nomes-de-variáveis)
  - [Erros comuns](#erros-comuns)
- [Strings](#strings)
- [Números](#números)
- [Constantes e comentários](#constantes-e-comentários)
- [Ideia principal](#ideia-principal)
- [Exercícios com resolução](#exercícios-com-resolução)
  - [Exercício 1 — Mensagem simples](#exercício-1--mensagem-simples)
  - [Exercício 2 — Alterando o valor de uma variável](#exercício-2--alterando-o-valor-de-uma-variável)
  - [Exercício 3 — Identificando tipos de dados](#exercício-3--identificando-tipos-de-dados)
  - [Exercício 4 — Nome formatado](#exercício-4--nome-formatado)
  - [Exercício 5 — Criando uma mensagem com f-string](#exercício-5--criando-uma-mensagem-com-f-string)
  - [Exercício 6 — Calculando o total de uma compra](#exercício-6--calculando-o-total-de-uma-compra)
  - [Exercício 7 — Operações matemáticas](#exercício-7--operações-matemáticas)
  - [Exercício 8 — Limpando uma entrada de texto](#exercício-8--limpando-uma-entrada-de-texto)
  - [Exercício 9 — Corrigindo um erro](#exercício-9--corrigindo-um-erro)
  - [Exercício 10 — Mini cadastro de produto](#exercício-10--mini-cadastro-de-produto)
  - [Desafio — Desconto em camisetas](#desafio--desconto-em-camisetas)

## Variáveis

Arquivos Python usam a extensão `.py` e são executados pelo interpretador Python, que lê e executa cada instrução.

Uma **variável** é um nome que referencia um valor:

```python
mensagem = "Olá, mundo!"
print(mensagem)
```

O valor de uma variável pode mudar durante a execução:

```python
mensagem = "Olá!"
mensagem = "Bem-vindo!"
```

### Regras para nomes de variáveis

- Podem conter letras, números e `_`.
- Não podem começar com números.
- Não podem conter espaços.
- Não devem usar palavras reservadas, como `print`.
- Devem ser curtos, claros e descritivos.

Por convenção, variáveis comuns são escritas em letras minúsculas:

```python
nome_aluno = "Ana"
```

### Erros comuns

- **`NameError`**: acontece quando uma variável não foi definida ou seu nome foi digitado incorretamente.
- **`SyntaxError`**: acontece quando o código não segue a sintaxe do Python, como em uma string com aspas incompatíveis.

O *traceback* mostra a linha, o tipo e uma possível causa do erro.

## Strings

Uma **string** é uma sequência de caracteres escrita entre aspas:

```python
nome = "Ada Lovelace"
```

Métodos importantes:

```python
nome.title()   # Ada Lovelace
nome.upper()   # ADA LOVELACE
nome.lower()   # ada lovelace
```

As **f-strings** permitem inserir variáveis em textos:

```python
nome = "Ada"
print(f"Olá, {nome}!")
```

Também é possível:

- Usar `\n` para uma nova linha.
- Usar `\t` para tabulação.
- Remover espaços com `strip()`, `lstrip()` e `rstrip()`.
- Remover partes de uma string com `removeprefix()` e `removesuffix()`.

## Números

Python trabalha principalmente com:

- `int`: números inteiros, como `10`.
- `float`: números decimais, como `10.5`.

Operações apresentadas:

```python
2 + 3    # adição
3 - 2    # subtração
2 * 3    # multiplicação
3 / 2    # divisão
3 ** 2   # potência
```

Uma divisão com `/` sempre produz um `float`. Ao misturar `int` e `float`, o resultado também será `float`.

Números grandes podem usar `_` para facilitar a leitura:

```python
populacao = 14_000_000
```

Também é possível atribuir várias variáveis de uma vez:

```python
x, y, z = 0, 0, 0
```

## Constantes e comentários

Python não possui constantes formais, mas nomes em letras maiúsculas indicam valores que não devem mudar:

```python
MAX_CONEXOES = 5000
```

Comentários começam com `#` e são ignorados pelo interpretador:

```python
# Calcula o total da compra
total = preco * quantidade
```

Eles devem explicar a **intenção** ou o raciocínio do código, e não apenas repetir o que a instrução já mostra.

## Ideia principal

Incentiva-se código:

- simples;
- claro;
- legível;
- fácil de manter.

> A mensagem central é: primeiro escreva um código que funcione; depois você pode melhorá-lo.

## Exercícios com resolução

### Exercício 1 — Mensagem simples

Crie uma variável chamada `mensagem`, armazene nela uma frase e mostre o conteúdo na tela.

#### Resolução

```python
mensagem = "Estou aprendendo Python!"
print(mensagem)
```

Saída:

```text
Estou aprendendo Python!
```

### Exercício 2 — Alterando o valor de uma variável

Crie uma variável chamada `status` com o valor `"Pedido recebido"`. Mostre o valor, altere-o para `"Pedido enviado"` e mostre novamente.

#### Resolução

```python
status = "Pedido recebido"
print(status)

status = "Pedido enviado"
print(status)
```

Saída:

```text
Pedido recebido
Pedido enviado
```

### Exercício 3 — Identificando tipos de dados

Crie quatro variáveis para armazenar:

- o nome de um produto;
- a quantidade disponível;
- o preço;
- se o produto está disponível.

Depois, use `type()` para mostrar o tipo de cada variável.

#### Resolução

```python
produto = "Caderno"
quantidade = 20
preco = 14.90
disponivel = True

print(type(produto))
print(type(quantidade))
print(type(preco))
print(type(disponivel))
```

Saída:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### Exercício 4 — Nome formatado

Armazene um nome completo em letras minúsculas. Depois, mostre-o:

- com as iniciais maiúsculas;
- completamente em maiúsculas;
- completamente em minúsculas.

#### Resolução

```python
nome = "ada lovelace"

print(nome.title())
print(nome.upper())
print(nome.lower())
```

Saída:

```text
Ada Lovelace
ADA LOVELACE
ada lovelace
```

### Exercício 5 — Criando uma mensagem com f-string

Crie variáveis para armazenar o nome e a idade de uma pessoa. Mostre a seguinte mensagem:

```text
Olá, Mariana! Você tem 25 anos.
```

#### Resolução

```python
nome = "Mariana"
idade = 25

print(f"Olá, {nome}! Você tem {idade} anos.")
```

### Exercício 6 — Calculando o total de uma compra

Uma pessoa comprou três unidades de um produto que custa R$ 12,50. Crie variáveis para o preço e a quantidade, calcule o total e mostre o resultado.

#### Resolução

```python
preco = 12.50
quantidade = 3

total = preco * quantidade

print(f"Total da compra: R$ {total:.2f}")
```

Saída:

```text
Total da compra: R$ 37.50
```

O trecho `:.2f` determina que o número seja apresentado com duas casas decimais.

### Exercício 7 — Operações matemáticas

Crie duas variáveis com os valores 10 e 3. Mostre o resultado das seguintes operações:

- soma;
- subtração;
- multiplicação;
- divisão;
- divisão inteira;
- resto da divisão;
- potência.

#### Resolução

```python
numero_1 = 10
numero_2 = 3

print("Soma:", numero_1 + numero_2)
print("Subtração:", numero_1 - numero_2)
print("Multiplicação:", numero_1 * numero_2)
print("Divisão:", numero_1 / numero_2)
print("Divisão inteira:", numero_1 // numero_2)
print("Resto:", numero_1 % numero_2)
print("Potência:", numero_1 ** numero_2)
```

Saída:

```text
Soma: 13
Subtração: 7
Multiplicação: 30
Divisão: 3.3333333333333335
Divisão inteira: 3
Resto: 1
Potência: 1000
```

### Exercício 8 — Limpando uma entrada de texto

A variável a seguir contém espaços extras:

```python
linguagem = "   Python   "
```

Mostre:

- o valor original;
- o valor sem espaços à esquerda;
- o valor sem espaços à direita;
- o valor sem espaços nos dois lados.

#### Resolução

```python
linguagem = "   Python   "

print(f"Original: '{linguagem}'")
print(f"Sem espaços à esquerda: '{linguagem.lstrip()}'")
print(f"Sem espaços à direita: '{linguagem.rstrip()}'")
print(f"Sem espaços nos dois lados: '{linguagem.strip()}'")
```

### Exercício 9 — Corrigindo um erro

O código abaixo produz um erro. Identifique e corrija o problema.

```python
nome_aluno = "Carlos"
print(nome_Aluno)
```

#### Resolução

Python diferencia letras maiúsculas de minúsculas. Portanto, `nome_aluno` e `nome_Aluno` são nomes diferentes.

```python
nome_aluno = "Carlos"
print(nome_aluno)
```

O erro original seria um `NameError`, pois a variável `nome_Aluno` não foi definida.

### Exercício 10 — Mini cadastro de produto

Crie variáveis para armazenar:

- nome do produto;
- preço unitário;
- quantidade;
- disponibilidade.

Calcule o valor total do estoque e mostre uma ficha organizada.

#### Resolução

```python
produto = "Teclado"
preco = 120.00
quantidade = 8
disponivel = True

valor_estoque = preco * quantidade

print("DADOS DO PRODUTO")
print(f"\tProduto: {produto}")
print(f"\tPreço: R$ {preco:.2f}")
print(f"\tQuantidade: {quantidade}")
print(f"\tDisponível: {disponivel}")
print(f"\tValor do estoque: R$ {valor_estoque:.2f}")
```

Saída:

```text
DADOS DO PRODUTO
    Produto: Teclado
    Preço: R$ 120.00
    Quantidade: 8
    Disponível: True
    Valor do estoque: R$ 960.00
```

### Desafio — Desconto em camisetas

Uma loja oferece 10% de desconto na compra de cinco camisetas de R$ 40,00 cada. Calcule:

- valor sem desconto;
- valor do desconto;
- valor final.

#### Resolução

```python
produto = "Camiseta"
preco = 40.00
quantidade = 5
percentual_desconto = 10

subtotal = preco * quantidade
desconto = subtotal * percentual_desconto / 100
total = subtotal - desconto

print(f"Produto: {produto}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")
```

Saída:

```text
Produto: Camiseta
Subtotal: R$ 200.00
Desconto: R$ 20.00
Total: R$ 180.00
```
