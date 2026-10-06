# Exercício 03 — Mãos à obra: suas primeiras variáveis

**Tipo:** prática · continua o notebook anterior

## Objetivo
Praticar a criação de **variáveis com nomes significativos** e o uso de `print()` para exibi-las.

## O que fazer
1. No mesmo notebook, crie 3 variáveis sobre você: `seu_nome`, `sua_cidade` e `seu_ano_nascimento`.
2. Em uma nova célula, use `print()` para exibir uma frase juntando as 3 variáveis (por exemplo: `print("Eu sou", seu_nome, "de", sua_cidade)`).
3. Tente criar uma variável com um **nome inválido** (por exemplo, começando com número: `2nome = "teste"`) só para ver a mensagem de erro do Python.
4. Leia a mensagem de erro com calma. Vamos aprender a "ler erros" ao longo de todo o curso.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_python_primeiros_passos/exercicio_03_primeiras_variaveis/variaveis.py
```

No Windows, se `python` não funcionar, use `py aula1_python_primeiros_passos/exercicio_03_primeiras_variaveis/variaveis.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `variaveis.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Eu sou Ana de Florianópolis e nasci em 2000
<class 'str'>
<class 'int'>
```

## Dicas e erros comuns
- Para o passo 3, a mensagem que o Python 3.12 mostra é: `SyntaxError: invalid decimal literal`. A versão do seu Python pode escrever isso de outro jeito, mas a ideia é a mesma.
- Nomes de variáveis: sem espaços, sem começar com número, e use nomes que expliquem o conteúdo (`sua_cidade`, não `x`).
