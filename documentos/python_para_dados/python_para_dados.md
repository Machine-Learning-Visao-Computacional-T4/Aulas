# Exercícios de Python para dados — Fundamentos com exemplos de ML

## Sumário

- [Orientações](#orientações)
- [Fundamentos básicos de Python](#fundamentos-básicos-de-python)
  - [Exibindo informações com `print`](#exibindo-informações-com-print)
  - [Operações matemáticas](#operações-matemáticas)
  - [Entrada de dados e conversão de tipos](#entrada-de-dados-e-conversão-de-tipos)
  - [Decisões com `if`, `elif` e `else`](#decisões-com-if-elif-e-else)
  - [Repetições com `while`](#repetições-com-while)
- [Aquecimento](#aquecimento)
  - [Exercício A1 — Soma](#exercício-a1--soma)
  - [Exercício A2 — Divisão](#exercício-a2--divisão)
  - [Exercício A3 — If e else](#exercício-a3--if-e-else)
  - [Exercício A4 — Positivo, negativo ou zero](#exercício-a4--positivo-negativo-ou-zero)
  - [Exercício A5 — Contagem com while](#exercício-a5--contagem-com-while)
  - [Exercício A6 — Soma com while](#exercício-a6--soma-com-while)
  - [Exercício A7 — Validação de entrada](#exercício-a7--validação-de-entrada)
- [Parte 1 — Sintaxe e estrutura básica](#parte-1--sintaxe-e-estrutura-básica)
  - [Exercício 1 — Variáveis e tipos](#exercício-1--variáveis-e-tipos)
  - [Exercício 2 — Correção de código](#exercício-2--correção-de-código)
  - [Exercício 3 — Conversão de tipos](#exercício-3--conversão-de-tipos)
  - [Exercício 4 — Função para calcular erro](#exercício-4--função-para-calcular-erro)
  - [Exercício 5 — Leitura e interpretação](#exercício-5--leitura-e-interpretação)
- [Parte 2 — Estruturas condicionais e de repetição](#parte-2--estruturas-condicionais-e-de-repetição)
  - [Exercício 6 — Classificação de desempenho](#exercício-6--classificação-de-desempenho)
  - [Exercício 7 — Dados ausentes](#exercício-7--dados-ausentes)
  - [Exercício 8 — Tipo de tarefa de ML](#exercício-8--tipo-de-tarefa-de-ml)
  - [Exercício 9 — Critério de aprovação](#exercício-9--critério-de-aprovação)
  - [Exercício 10 — Percorrendo modelos](#exercício-10--percorrendo-modelos)
  - [Exercício 11 — Média sem sum](#exercício-11--média-sem-sum)
  - [Exercício 12 — Filtro e contagem](#exercício-12--filtro-e-contagem)
- [Parte 3 — Listas, vetores, tuplas e dicionários](#parte-3--listas-vetores-tuplas-e-dicionários)
  - [Exercício 13 — Lista de features](#exercício-13--lista-de-features)
  - [Exercício 14 — Tupla de dimensões](#exercício-14--tupla-de-dimensões)
  - [Exercício 15 — Dicionário de métricas](#exercício-15--dicionário-de-métricas)
  - [Exercício 16 — Estrutura composta](#exercício-16--estrutura-composta)
  - [Exercício 17 — Melhor modelo](#exercício-17--melhor-modelo)
  - [Exercício 18 — Features e rótulos](#exercício-18--features-e-rótulos)
- [Gabarito](#gabarito)
  - [Respostas do aquecimento](#respostas-do-aquecimento)
  - [Respostas dos exercícios](#respostas-dos-exercícios)

**Sintaxe, estruturas de controle, coleções e complexidade de algoritmos**

> **Objetivo.** Praticar os fundamentos de Python por meio de situações comuns em projetos de dados e Machine Learning. Os exercícios avançam de variáveis e decisões simples até a organização de datasets e a análise intuitiva da eficiência dos algoritmos.

## Orientações

- Resolva primeiro sem consultar o gabarito.
- Execute e modifique os códigos em um Google Colab.

## Fundamentos básicos de Python

Esta seção apresenta os comandos necessários para começar a escrever e compreender pequenos programas em Python. Os exemplos utilizam situações simples e fazem a transição para dados e Machine Learning.

### Exibindo informações com `print`

A função `print` apresenta textos, números, resultados de operações e valores armazenados em variáveis.

```python
print("Olá, mundo!")
print("Introdução ao Machine Learning")
print(5 + 3)

modelo = "Random Forest"
acuracia = 0.87
print("Modelo:", modelo)
print(f"O modelo {modelo} obteve acurácia de {acuracia}.")
```

### Operações matemáticas

Python utiliza operadores para realizar cálculos. A divisão comum retorna um valor decimal; `//` retorna o quociente inteiro; e `%` retorna o resto.

```python
a = 10
b = 3
print(a + b)   # soma: 13
print(a - b)   # subtração: 7
print(a * b)   # multiplicação: 30
print(a / b)   # divisão: 3.333...
print(a // b)  # divisão inteira: 3
print(a % b)   # resto: 1
```

Em ML, a divisão pode ser usada para calcular uma métrica simples:

```python
previsoes_corretas = 85
total_previsoes = 100
acuracia = previsoes_corretas / total_previsoes
print("Acurácia:", acuracia)
```

### Entrada de dados e conversão de tipos

A função `input` recebe uma informação digitada pelo usuário e a devolve como **texto**. Use `int` para converter um inteiro e `float` para converter um número decimal.

```python
nome = input("Digite seu nome: ")
quantidade = int(input("Quantidade de amostras: "))
acuracia = float(input("Acurácia: "))
print(nome, quantidade, acuracia)
```

### Decisões com `if`, `elif` e `else`

O `if` executa um bloco quando uma condição é verdadeira. O `elif` testa condições adicionais e o `else` trata os demais casos. A **indentação** define quais comandos pertencem a cada bloco.

```python
acuracia = 0.84
if acuracia >= 0.90:
    print("Desempenho excelente")
elif acuracia >= 0.80:
    print("Desempenho bom")
else:
    print("Desempenho abaixo do esperado")
```

Use `==` para comparar valores e `=` para atribuir um valor. As condições também podem ser combinadas com `and`, `or` e `not`.

```python
acuracia = 0.85
diferenca_treino_teste = 0.05
if acuracia >= 0.80 and diferenca_treino_teste <= 0.10:
    print("Modelo aprovado")
else:
    print("Modelo não aprovado")
```

### Repetições com `while`

O `while` repete um bloco enquanto sua condição permanece verdadeira. A variável da condição deve ser atualizada para evitar um *loop* infinito.

```python
epoca = 1
while epoca <= 5:
    print("Treinando época", epoca)
    epoca += 1
print("Treinamento concluído")
```

O comando `break` pode encerrar o laço antes que a condição se torne falsa.

```python
tentativa = 1
while tentativa <= 10:
    if tentativa == 4:
        print("Resultado encontrado")
        break
    tentativa += 1
```

## Aquecimento

### Exercício A1 — Soma

Crie duas variáveis com 150 e 350. Some os valores e apresente `Total de amostras: 500`.

### Exercício A2 — Divisão

Um modelo realizou 90 previsões corretas entre 120 previsões. Calcule e apresente a acurácia.

### Exercício A3 — If e else

Se a acurácia for maior ou igual a 0.80, apresente `Modelo aprovado`. Caso contrário, apresente `Modelo não aprovado`. Teste com 0.75.

### Exercício A4 — Positivo, negativo ou zero

Verifique se o valor de uma feature é positivo, negativo ou igual a zero. Teste com -5.

### Exercício A5 — Contagem com while

Apresente os números de 1 a 10 utilizando `while`.

### Exercício A6 — Soma com while

Some os números de 1 a 5 utilizando `while` e apresente o resultado.

### Exercício A7 — Validação de entrada

Solicite uma acurácia. Enquanto o valor estiver fora do intervalo de 0 a 1, informe que ele é inválido e solicite-o novamente.

## Parte 1 — Sintaxe e estrutura básica

### Exercício 1 — Variáveis e tipos

Identifique o tipo de cada variável e escreva uma frase que apresente o modelo e sua acurácia.

```python
modelo = "Random Forest"
acuracia = 0.87
numero_amostras = 1500
modelo_treinado = True
```

### Exercício 2 — Correção de código

O código deveria calcular a acurácia. Identifique e corrija os erros.

```python
previsoes_corretas = 85
total_amostras = 100
acuracia = previsoes_corretas / total_amostras
Print("Acurácia:" acuracia)
```

### Exercício 3 — Conversão de tipos

A quantidade foi recebida como texto. Converta-a para inteiro e calcule o total após adicionar 50 amostras.

```python
quantidade = "250"
```

### Exercício 4 — Função para calcular erro

Crie a função `calcular_erro`, que recebe uma acurácia e retorna 1 menos a acurácia. Teste com 0.82.

### Exercício 5 — Leitura e interpretação

Informe a saída do código. Depois explique o que uma diferença elevada entre treino e teste pode sugerir.

```python
modelo = "Regressão Logística"
acuracia_treino = 0.92
acuracia_teste = 0.78
diferenca = acuracia_treino - acuracia_teste
print(modelo)
print(round(diferenca, 2))
```

## Parte 2 — Estruturas condicionais e de repetição

### Exercício 6 — Classificação de desempenho

Use `if`, `elif` e `else` para classificar a acurácia: `Excelente` para valor maior ou igual a 0.90; `Bom` para 0.80 ou mais; `Regular` para 0.70 ou mais; `Precisa melhorar` nos demais casos. Teste com 0.84.

### Exercício 7 — Dados ausentes

Apresente `Valor ausente` quando `idade` for `None` e `Valor disponível` nos demais casos.

```python
idade = None
```

### Exercício 8 — Tipo de tarefa de ML

Para `tipo_alvo` igual a `categoria`, apresente `Problema de classificação`. Para `numero`, apresente `Problema de regressão`. Para outro valor, apresente `Tipo de problema desconhecido`.

```python
tipo_alvo = "categoria"
```

### Exercício 9 — Critério de aprovação

Um modelo é aprovado quando a acurácia de teste é pelo menos 0.80 e a diferença entre treino e teste não ultrapassa 0.10. Implemente a regra.

```python
acuracia_treino = 0.87
acuracia_teste = 0.82
```

### Exercício 10 — Percorrendo modelos

Use `for` para apresentar o nome de cada modelo.

```python
modelos = [
    "Regressão Logística",
    "Árvore de Decisão",
    "Random Forest"
]
```

### Exercício 11 — Média sem sum

Calcule a média usando uma estrutura de repetição, sem utilizar `sum()`.

```python
acuracias = [0.78, 0.84, 0.91, 0.87]
```

### Exercício 12 — Filtro e contagem

Apresente somente as acurácias maiores ou iguais a 0.80 e conte quantos modelos atendem ao critério.

```python
acuracias = [0.65, 0.82, 0.91, 0.73, 0.88]
```

## Parte 3 — Listas, vetores, tuplas e dicionários

### Exercício 13 — Lista de features

Adicione `numero_compras`, remova `tempo_cliente`, apresente a primeira feature e a quantidade final de features.

```python
features = ["idade", "renda", "tempo_cliente"]
```

### Exercício 14 — Tupla de dimensões

Em `dimensoes = (224, 224, 3)`, explique os valores, acesse o número de canais e justifique o uso de uma tupla.

```python
dimensoes = (224, 224, 3)
```

### Exercício 15 — Dicionário de métricas

Crie um dicionário com acurácia 0.88, precisão 0.84 e recall 0.79. Mostre o recall, adicione F1 igual a 0.81 e percorra todos os itens.

### Exercício 16 — Estrutura composta

Apresente somente os modelos com acurácia maior ou igual a 0.80.

```python
resultados = [
    {"modelo": "Regressão Logística", "acuracia": 0.81},
    {"modelo": "Árvore de Decisão", "acuracia": 0.76},
    {"modelo": "Random Forest", "acuracia": 0.89}
]
```

### Exercício 17 — Melhor modelo

Utilizando a estrutura do exercício anterior, encontre o modelo com maior acurácia sem ordenar a lista.

```python
resultados = [
    {"modelo": "Regressão Logística", "acuracia": 0.81},
    {"modelo": "Árvore de Decisão", "acuracia": 0.76},
    {"modelo": "Random Forest", "acuracia": 0.89}
]
```

### Exercício 18 — Features e rótulos

Crie `X` com idade e renda e `y` com o rótulo comprou.

```python
dataset = [
    {"idade": 22, "renda": 2500, "comprou": 0},
    {"idade": 35, "renda": 5200, "comprou": 1},
    {"idade": 47, "renda": 6800, "comprou": 1},
    {"idade": 29, "renda": 3100, "comprou": 0}
]
```

## Gabarito

As soluções mostram uma forma possível de resolver cada exercício. Em programação, soluções diferentes podem estar corretas quando produzem o resultado esperado e respeitam os requisitos.

### Respostas do aquecimento

#### Resposta A1 — Soma

```python
amostras_1 = 150
amostras_2 = 350
total = amostras_1 + amostras_2
print("Total de amostras:", total)
```

#### Resposta A2 — Divisão

```python
acertos = 90
total = 120
acuracia = acertos / total
print("Acurácia:", acuracia)  # 0.75
```

#### Resposta A3 — If e else

```python
acuracia = 0.75
if acuracia >= 0.80:
    print("Modelo aprovado")
else:
    print("Modelo não aprovado")
```

#### Resposta A4 — Positivo, negativo ou zero

```python
valor = -5
if valor > 0:
    print("Valor positivo")
elif valor < 0:
    print("Valor negativo")
else:
    print("Valor igual a zero")
```

#### Resposta A5 — Contagem com while

```python
numero = 1
while numero <= 10:
    print(numero)
    numero += 1
```

#### Resposta A6 — Soma com while

```python
numero = 1
total = 0
while numero <= 5:
    total += numero
    numero += 1
print("Resultado:", total)  # 15
```

#### Resposta A7 — Validação de entrada

```python
acuracia = float(input("Digite uma acurácia entre 0 e 1: "))
while acuracia < 0 or acuracia > 1:
    print("Valor inválido")
    acuracia = float(input("Digite novamente: "))
print("Acurácia registrada:", acuracia)
```

### Respostas dos exercícios

#### Resposta 1 — Variáveis e tipos

`modelo` é `str`; `acuracia` é `float`; `numero_amostras` é `int`; `modelo_treinado` é `bool`.

```python
print(f"O modelo {modelo} obteve acurácia de {acuracia}.")
```

#### Resposta 2 — Correção de código

Os erros estavam na última linha: `Print` deve ser escrito em minúsculas (`print`) e falta uma vírgula entre `"Acurácia:"` e `acuracia`.

```python
previsoes_corretas = 85
total_amostras = 100
acuracia = previsoes_corretas / total_amostras
print("Acurácia:", acuracia)
```

#### Resposta 3 — Conversão de tipos

```python
quantidade = int("250")
total = quantidade + 50
print(total)  # 300
```

#### Resposta 4 — Função para calcular erro

```python
def calcular_erro(acuracia):
    return 1 - acuracia

print(round(calcular_erro(0.82), 2))  # 0.18
```

#### Resposta 5 — Leitura e interpretação

A saída é `Regressão Logística` e `0.14`. Uma diferença elevada pode sugerir *overfitting*, mas a conclusão depende dos dados, da métrica e do procedimento de avaliação.

#### Resposta 6 — Classificação de desempenho

```python
acuracia = 0.84
if acuracia >= 0.90:
    print("Excelente")
elif acuracia >= 0.80:
    print("Bom")
elif acuracia >= 0.70:
    print("Regular")
else:
    print("Precisa melhorar")
```

#### Resposta 7 — Dados ausentes

```python
if idade is None:
    print("Valor ausente")
else:
    print("Valor disponível")
```

#### Resposta 8 — Tipo de tarefa de ML

```python
if tipo_alvo == "categoria":
    print("Problema de classificação")
elif tipo_alvo == "numero":
    print("Problema de regressão")
else:
    print("Tipo de problema desconhecido")
```

#### Resposta 9 — Critério de aprovação

```python
diferenca = acuracia_treino - acuracia_teste
if acuracia_teste >= 0.80 and diferenca <= 0.10:
    print("Modelo aprovado")
else:
    print("Modelo não aprovado")
```

#### Resposta 10 — Percorrendo modelos

```python
for modelo in modelos:
    print(modelo)
```

#### Resposta 11 — Média sem sum

```python
total = 0
for acuracia in acuracias:
    total += acuracia
media = total / len(acuracias)
print(media)  # 0.85
```

#### Resposta 12 — Filtro e contagem

```python
contador = 0
for acuracia in acuracias:
    if acuracia >= 0.80:
        print(acuracia)
        contador += 1
print("Quantidade:", contador)  # 3
```

#### Resposta 13 — Lista de features

```python
features.append("numero_compras")
features.remove("tempo_cliente")
print(features[0])
print(len(features))
```

#### Resposta 14 — Tupla de dimensões

Os valores representam altura, largura e canais. `dimensoes[2]` retorna `3`. A tupla ajuda a representar uma configuração fixa, pois é imutável.

#### Resposta 15 — Dicionário de métricas

```python
metricas = {"acuracia": 0.88, "precisao": 0.84, "recall": 0.79}
print(metricas["recall"])
metricas["f1"] = 0.81
for nome, valor in metricas.items():
    print(nome, valor)
```

#### Resposta 16 — Estrutura composta

```python
for resultado in resultados:
    if resultado["acuracia"] >= 0.80:
        print(resultado["modelo"])
```

#### Resposta 17 — Melhor modelo

```python
melhor = resultados[0]
for resultado in resultados:
    if resultado["acuracia"] > melhor["acuracia"]:
        melhor = resultado
print("Melhor modelo:", melhor["modelo"])
print("Acurácia:", melhor["acuracia"])
```

#### Resposta 18 — Features e rótulos

```python
X = []
y = []
for registro in dataset:
    X.append([registro["idade"], registro["renda"]])
    y.append(registro["comprou"])
print(X)
print(y)
```
