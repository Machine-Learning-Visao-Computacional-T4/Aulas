# Exercício 03 — Mãos à obra: comparando valores

**Tipo:** prática · reforça `=` × `==`

## Objetivo
Praticar **operadores relacionais** e reforçar a diferença entre `=` e `==`.

## O que fazer
1. Crie duas variáveis com notas de prova: `nota_joao = 7.5` e `nota_maria = 8.2`.
2. Escreva e imprima **4 comparações diferentes** entre essas duas variáveis (maior, menor, igual, diferente).
3. Para cada resultado, escreva um **comentário** (`#`) explicando em português o que aquela comparação significa.
4. Tente (de propósito) escrever uma comparação com **um único `=`** e observe a mensagem de erro.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_operadores_logica/exercicio_03_comparando_valores/comparacoes.py
```

No Windows, se `python` não funcionar, use `py aula2_operadores_logica/exercicio_03_comparando_valores/comparacoes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `comparacoes.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
False
True
False
True
```

## Dicas e erros comuns
- Para o passo 4, `print(nota_joao = nota_maria)` gera: `TypeError: 'nota_joao' is an invalid keyword argument for print()`. O erro aparece porque `=` **atribui**, e a comparação correta é `==`.
- Memorize: `=` guarda um valor numa variável; `==` pergunta "são iguais?".
