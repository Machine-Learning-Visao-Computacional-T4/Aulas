# Exercício 02 — Mãos à obra: classificador de notas

**Tipo:** prática com `if/elif/else` · 15 min

## Objetivo
Praticar `if/elif/else` em um programa completo.

## O que fazer
1. Peça (com `input()`) a nota de um aluno, convertendo para `float`.
2. Use `if/elif/else` para classificar: **"Excelente"** (≥ 9), **"Bom"** (≥ 7), **"Regular"** (≥ 5) ou **"Insuficiente"** (< 5).
3. Exiba o resultado com `print()`, **incluindo a nota digitada** na mensagem.
4. Teste seu programa com **pelo menos 3 notas diferentes**, cobrindo faixas diferentes.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_condicionais_loops/exercicio_02_classificador_de_notas/classificador_notas.py
```

No Windows, se `python` não funcionar, use `py aula3_condicionais_loops/exercicio_02_classificador_de_notas/classificador_notas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `classificador_notas.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Digite a nota do aluno: 7.5
Nota 7.5 -> Bom
```

(Os valores digitados no exemplo acima foram: `7.5`.)

## Dicas e erros comuns
- A **ordem** das condições importa: o Python para na primeira que for verdadeira. Por isso a maior nota é testada primeiro.
- Teste os limites: 9, 7, 5 e 4.9.
