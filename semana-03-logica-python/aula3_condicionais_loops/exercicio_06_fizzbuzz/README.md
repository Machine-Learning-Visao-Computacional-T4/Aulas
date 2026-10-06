# Exercício 06 — Resolva o FizzBuzz você mesmo

**Tipo:** o grande marco do módulo · 18 min

## Objetivo
Implementar, **sem olhar o exemplo**, o clássico **FizzBuzz**.

## O que fazer
1. **Sem consultar a solução**, escreva um programa que percorre os números de **1 a 30**.
2. Para múltiplos de 3, imprima **"Fizz"**; para múltiplos de 5, **"Buzz"**; para múltiplos de **ambos**, **"FizzBuzz"**; senão, imprima o próprio número.
3. Teste seu código e compare o resultado com um colega.
4. **Desafio extra (opcional):** adapte para que múltiplos de 7 também imprimam **"Bang"** (veja `fizzbuzz_bang.py` só depois de tentar).

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_condicionais_loops/exercicio_06_fizzbuzz/fizzbuzz.py
```

No Windows, se `python` não funcionar, use `py aula3_condicionais_loops/exercicio_06_fizzbuzz/fizzbuzz.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `fizzbuzz.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
```

## Dicas e erros comuns
- Teste o caso do 15 **antes** dos outros (ou combine as condições): senão ele cai no "Fizz" e nunca vira "FizzBuzz".
- Use `%` (resto da divisão): `numero % 3 == 0` significa "múltiplo de 3".
- No desafio, `fizzbuzz_bang.py` combina os textos (21 vira `FizzBang`). Essa é uma das interpretações possíveis do enunciado.

## Origem do exercício
O FizzBuzz nasceu como um jogo infantil britânico de contar em voz alta. Em 2007, o programador Imran Ghory sugeriu usá-lo como teste rápido de entrevista de emprego, para verificar se um candidato sabe estruturar lógica básica. Resolver o FizzBuzz virou um marco simbólico de quem está aprendendo a programar.
