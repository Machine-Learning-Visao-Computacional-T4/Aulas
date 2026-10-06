# Exercício 04 — Mãos à obra: validador de senha

**Tipo:** prática com `while` · 15 min

## Objetivo
Praticar `while` em um cenário onde **não sabemos de antemão quantas repetições** serão necessárias.

## O que fazer
1. Defina uma variável `senha_correta = "python123"` no seu código.
2. Use um `while` para pedir repetidamente (`input()`) que o usuário digite a senha, **até acertar**.
3. A cada tentativa errada, exiba: **"Senha incorreta, tente novamente"**.
4. Quando acertar, exiba **"Acesso liberado!"** e encerre o loop.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_condicionais_loops/exercicio_04_validador_de_senha/validador_senha.py
```

No Windows, se `python` não funcionar, use `py aula3_condicionais_loops/exercicio_04_validador_de_senha/validador_senha.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `validador_senha.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Digite a senha: abc
Senha incorreta, tente novamente
Digite a senha: 123
Senha incorreta, tente novamente
Digite a senha: python123
Acesso liberado!
```

(Os valores digitados no exemplo acima foram: `abc`, `123`, `python123`.)

## Dicas e erros comuns
- Aqui o `while` é melhor que o `for`: ninguém sabe quantas tentativas a pessoa precisará.
- Se o programa nunca terminar, aperte `Ctrl + C` no terminal. (Provavelmente a condição do `while` nunca fica falsa.)
- Desafio: limite a 3 tentativas usando `break` ou um contador.
