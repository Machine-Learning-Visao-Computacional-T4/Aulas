# Exercício 06 — FizzBuzz como arquivo `.py`

**Tipo:** prática + versionamento

## Objetivo
Reescrever o clássico FizzBuzz como **arquivo de script** e **versioná-lo no GitHub**. O foco é o **fluxo**, não a lógica (você já a dominou na Semana 03).

## O que fazer
1. Crie um arquivo `fizzbuzz.py` no seu ambiente (VS Code local ou Colab conectado ao GitHub).
2. Escreva o programa que imprime, de 1 a 30: `Fizz` para múltiplos de 3, `Buzz` para múltiplos de 5, `FizzBuzz` para múltiplos de ambos, e o número nos demais casos.
3. Rode o arquivo e confirme que a saída está correta.
4. Faça **commit** com a mensagem `Adiciona exercício FizzBuzz` e **push** para o GitHub.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_python_local_vscode/exercicio_06_fizzbuzz_como_arquivo_py/fizzbuzz.py
```

No Windows, se `python` não funcionar, use `py aula2_python_local_vscode/exercicio_06_fizzbuzz_como_arquivo_py/fizzbuzz.py`.

Os comandos de versionamento no terminal:

```bash
git add fizzbuzz.py
git commit -m "Adiciona exercício FizzBuzz"
git push
```

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
- Fluxo que você repetirá em **todos** os exercícios do curso: **código → teste → commit → push**.
