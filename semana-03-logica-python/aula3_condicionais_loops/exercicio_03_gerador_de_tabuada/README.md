# Exercício 03 — Mãos à obra: gerador de tabuada

**Tipo:** prática com `for` e `range()` · 12 min

## Objetivo
Praticar `for` com `range()` em um problema clássico.

## O que fazer
1. Peça (com `input()`) um número, convertendo para `int`.
2. Use um `for` com `range(1, 11)` para gerar a tabuada desse número, de 1 a 10.
3. Para cada iteração, exiba uma linha no formato **"N x i = resultado"**.
4. Teste com **pelo menos 2 números diferentes**.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_condicionais_loops/exercicio_03_gerador_de_tabuada/tabuada.py
```

No Windows, se `python` não funcionar, use `py aula3_condicionais_loops/exercicio_03_gerador_de_tabuada/tabuada.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `tabuada.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Qual tabuada você quer? 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

(Os valores digitados no exemplo acima foram: `7`.)

## Dicas e erros comuns
- `range(1, 11)` vai de 1 até **10**: o número final **não** entra.
- Lembre-se da indentação: tudo que está dentro do `for` fica recuado.
