# Arquivos, exceções e JSON em Python

## Sumário

- [1. Trabalhando com arquivos](#1-trabalhando-com-arquivos)
- [2. Lendo um arquivo](#2-lendo-um-arquivo)
- [3. Caminhos relativos e absolutos](#3-caminhos-relativos-e-absolutos)
- [4. Percorrendo as linhas](#4-percorrendo-as-linhas)
- [5. Todo conteúdo lido é texto](#5-todo-conteúdo-lido-é-texto)
- [6. Escrevendo em arquivos](#6-escrevendo-em-arquivos)
- [7. O que são exceções?](#7-o-que-são-exceções)
- [8. Estrutura try-except](#8-estrutura-try-except)
- [9. Utilizando else](#9-utilizando-else)
- [10. Tratando arquivos inexistentes](#10-tratando-arquivos-inexistentes)
- [11. Ignorando uma exceção com pass](#11-ignorando-uma-exceção-com-pass)
- [12. Verificando se um arquivo existe](#12-verificando-se-um-arquivo-existe)
- [13. Salvando dados em JSON](#13-salvando-dados-em-json)
- [14. Lendo dados JSON](#14-lendo-dados-json)
- [15. Refatoração](#15-refatoração)
- [Exercícios com resolução](#exercícios-com-resolução)
  - [Exercício 1 — Leitura completa](#exercício-1--leitura-completa)
  - [Exercício 2 — Leitura linha por linha](#exercício-2--leitura-linha-por-linha)
  - [Exercício 3 — Substituindo palavras](#exercício-3--substituindo-palavras)
  - [Exercício 4 — Salvando o nome de um usuário](#exercício-4--salvando-o-nome-de-um-usuário)
  - [Exercício 5 — Livro de convidados](#exercício-5--livro-de-convidados)
  - [Exercício 6 — Divisão segura](#exercício-6--divisão-segura)
  - [Exercício 7 — Tratando entrada inválida](#exercício-7--tratando-entrada-inválida)

## 1. Trabalhando com arquivos

Arquivos permitem que o programa:

- leia grandes quantidades de dados;
- salve resultados;
- preserve informações após o encerramento;
- compartilhe dados com outros programas.

A biblioteca `pathlib` fornece a classe `Path`, utilizada para representar caminhos de arquivos:

```python
from pathlib import Path

caminho = Path("dados.txt")
```

Ele **não** cria nem abre o arquivo. Como o caminho é relativo, `dados.txt` se refere à pasta de onde o programa está sendo executado.

## 2. Lendo um arquivo

O método `read_text()` lê todo o conteúdo do arquivo e retorna uma string:

```python
from pathlib import Path

caminho = Path("dados.txt")
conteudo = caminho.read_text()

print(conteudo)
```

É possível informar o *encoding*:

```python
conteudo = caminho.read_text(encoding="utf-8")
```

O `encoding="utf-8"` ajuda Python a interpretar corretamente caracteres como `ç`, `ã` e `é`.

Podemos remover espaços e quebras de linha no final:

```python
conteudo = caminho.read_text(
    encoding="utf-8"
).rstrip()
```

Se o arquivo `dados.txt` não existir, o Python mostrará um erro ao tentar lê-lo.

> **Criando o arquivo manualmente no Colab**
>
> 1. Abra o painel **Arquivos** 📁 à esquerda e entre na pasta `content`.
> 2. Clique com o botão direito dentro da pasta e escolha **Novo arquivo**.
> 3. Dê ao arquivo o nome `dados.txt`.
> 4. Abra o arquivo, escreva qualquer texto e salve com `Ctrl+S` (ou `⌘+S` no Mac).
> 5. Depois, execute novamente.

## 3. Caminhos relativos e absolutos

Um caminho **relativo** parte da pasta na qual o programa está sendo executado:

```python
caminho = Path("dados/clientes.txt")
```

Um caminho **absoluto** informa a localização completa:

```python
caminho = Path(
    "/usuarios/ana/projeto/dados/clientes.txt"
)
```

Caminhos relativos normalmente facilitam o compartilhamento de um projeto.

## 4. Percorrendo as linhas

O método `splitlines()` transforma o conteúdo em uma lista de linhas:

```python
from pathlib import Path

caminho = Path("alunos.txt")
conteudo = caminho.read_text(
    encoding="utf-8"
)

linhas = conteudo.splitlines()

for linha in linhas:
    print(linha)
```

Também podemos percorrer diretamente:

```python
for linha in conteudo.splitlines():
    print(linha)
```

> Para testar, crie o arquivo `alunos.txt` da mesma forma que `dados.txt` (veja o passo 2), escreva qualquer texto, salve e execute novamente.

## 5. Todo conteúdo lido é texto

Mesmo que um arquivo contenha números, `read_text()` retorna uma string:

```python
conteudo = caminho.read_text().strip()
numero = int(conteudo)
```

Para números decimais:

```python
valor = float(conteudo)
```

## 6. Escrevendo em arquivos

O método `write_text()` grava uma string em um arquivo:

```python
from pathlib import Path

caminho = Path("mensagem.txt")
caminho.write_text(
    "Estou aprendendo Python.",
    encoding="utf-8"
)
```

Se o arquivo não existir, ele será criado. Se já existir, seu conteúdo será **substituído**.

Para escrever várias linhas, podemos criar uma única string:

```python
conteudo = "Primeira linha.\n"
conteudo += "Segunda linha.\n"
conteudo += "Terceira linha.\n"

caminho.write_text(
    conteudo,
    encoding="utf-8"
)
```

O método `write_text()` recebe texto. Para escrever números, devemos convertê-los:

```python
idade = 25
caminho.write_text(str(idade))
```

## 7. O que são exceções?

Exceções são objetos criados por Python quando ocorre um erro durante a execução.

Exemplos:

| Exceção | Situação |
| --- | --- |
| `ZeroDivisionError` | Divisão por zero |
| `FileNotFoundError` | Arquivo inexistente |
| `ValueError` | Conversão inválida |
| `KeyError` | Chave inexistente em dicionário |
| `TypeError` | Operação com tipos incompatíveis |

Sem tratamento, a exceção encerra o programa e apresenta um *traceback*.

## 8. Estrutura `try-except`

O bloco `try` contém a operação que pode produzir um erro. O `except` define como o programa deve reagir:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Em vez de encerrar o programa, Python apresenta uma mensagem amigável.

## 9. Utilizando `else`

O bloco `else` é executado quando o `try` termina **sem erros**:

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Digite somente números inteiros.")
else:
    print(f"O número informado foi {numero}.")
```

A organização recomendada é:

```python
try:
    # Código que pode gerar uma exceção
except TipoDeErro:
    # Tratamento do erro
else:
    # Código executado quando não há erro
```

O `try` deve conter somente as instruções que realmente podem gerar a exceção esperada.

## 10. Tratando arquivos inexistentes

```python
from pathlib import Path

caminho = Path("clientes.txt")

try:
    conteudo = caminho.read_text(
        encoding="utf-8"
    )
except FileNotFoundError:
    print(
        f"O arquivo {caminho} não foi encontrado."
    )
else:
    print(conteudo)
```

Esse tratamento permite que o programa continue funcionando mesmo quando um arquivo estiver ausente.

## 11. Ignorando uma exceção com `pass`

O comando `pass` permite tratar uma exceção sem executar nenhuma ação:

```python
try:
    conteudo = caminho.read_text(
        encoding="utf-8"
    )
except FileNotFoundError:
    pass
```

Isso é chamado de **falha silenciosa**. Deve ser utilizado conscientemente, pois esconder erros importantes pode dificultar a identificação de problemas.

## 12. Verificando se um arquivo existe

O método `exists()` verifica a existência de um arquivo:

```python
from pathlib import Path

caminho = Path("usuario.json")

if caminho.exists():
    print("O arquivo existe.")
else:
    print("O arquivo não existe.")
```

Ele retorna `True` ou `False`.

## 13. Salvando dados em JSON

**JSON** é um formato utilizado para armazenar e compartilhar dados entre diferentes programas e linguagens.

```python
import json
```

A função `json.dumps()` converte um objeto Python em uma string JSON:

```python
import json
from pathlib import Path

numeros = [2, 3, 5, 7, 11]

# json.dumps() transforma um objeto Python em texto no formato JSON.
conteudo = json.dumps(numeros)

caminho = Path("numeros.json")
caminho.write_text(conteudo)
```

## 14. Lendo dados JSON

A função `json.loads()` transforma uma string JSON em um objeto Python:

```python
import json
from pathlib import Path

caminho = Path("numeros.json")
conteudo = caminho.read_text()

numeros = json.loads(conteudo)

print(numeros)
```

| Função | Operação |
| --- | --- |
| `json.dumps()` | Python → string JSON |
| `json.loads()` | string JSON → Python |

## 15. Refatoração

**Refatorar** significa reorganizar um código que já funciona para deixá-lo:

- mais claro;
- mais fácil de testar;
- mais fácil de manter;
- mais fácil de reutilizar.

Uma boa função deve ter uma responsabilidade clara:

```python
def carregar_usuario(caminho):
    if caminho.exists():
        conteudo = caminho.read_text()
        return json.loads(conteudo)

    return None
```

## Exercícios com resolução

### Exercício 1 — Leitura completa

Crie um arquivo chamado `aprendizado.txt` com três frases sobre Python. Depois, crie um programa que leia e mostre todo o conteúdo.

Conteúdo de `aprendizado.txt`:

```text
Python permite criar variáveis.
Python permite trabalhar com listas.
Python permite automatizar tarefas.
```

#### Resolução

```python
from pathlib import Path

caminho = Path("aprendizado.txt")

conteudo = caminho.read_text(
    encoding="utf-8"
).rstrip()

print(conteudo)
```

### Exercício 2 — Leitura linha por linha

Leia o mesmo arquivo e mostre as linhas utilizando `for`.

#### Resolução

```python
from pathlib import Path

caminho = Path("aprendizado.txt")

conteudo = caminho.read_text(
    encoding="utf-8"
)

for linha in conteudo.splitlines():
    print(linha)
```

### Exercício 3 — Substituindo palavras

Leia `aprendizado.txt` e substitua `"Python"` por `"Java"` somente na saída. O arquivo original não deve ser modificado.

#### Resolução

```python
from pathlib import Path

caminho = Path("aprendizado.txt")

conteudo = caminho.read_text(
    encoding="utf-8"
)

conteudo_modificado = conteudo.replace(
    "Python",
    "Java"
)

print(conteudo_modificado)
```

O método `replace()` retorna uma nova string e não altera automaticamente o arquivo.

### Exercício 4 — Salvando o nome de um usuário

Peça o nome do usuário e salve-o em `convidado.txt`.

#### Resolução

```python
from pathlib import Path

nome = input("Digite seu nome: ")

caminho = Path("convidado.txt")
caminho.write_text(
    nome,
    encoding="utf-8"
)

print("Nome salvo com sucesso.")
```

### Exercício 5 — Livro de convidados

Solicite nomes até o usuário digitar `"sair"`. Depois, grave todos os nomes em `convidados.txt`, um por linha.

#### Resolução

```python
from pathlib import Path

nomes = []

while True:
    nome = input(
        "Digite um nome ou 'sair': "
    )

    if nome.lower() == "sair":
        break

    nomes.append(nome)

conteudo = ""

for nome in nomes:
    conteudo += f"{nome}\n"

caminho = Path("convidados.txt")
caminho.write_text(
    conteudo,
    encoding="utf-8"
)

print("Lista de convidados salva.")
```

### Exercício 6 — Divisão segura

Peça dois números e realize uma divisão. Trate a tentativa de divisão por zero.

#### Resolução

```python
numero_1 = float(
    input("Digite o primeiro número: ")
)

numero_2 = float(
    input("Digite o segundo número: ")
)

try:
    resultado = numero_1 / numero_2
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print(f"Resultado: {resultado}")
```

### Exercício 7 — Tratando entrada inválida

Peça dois números inteiros, some-os e trate o `ValueError` caso o usuário informe texto.

#### Resolução

```python
try:
    numero_1 = int(
        input("Digite o primeiro número: ")
    )

    numero_2 = int(
        input("Digite o segundo número: ")
    )
except ValueError:
    print("Informe somente números inteiros.")
else:
    soma = numero_1 + numero_2
    print(f"Resultado: {soma}")
```
