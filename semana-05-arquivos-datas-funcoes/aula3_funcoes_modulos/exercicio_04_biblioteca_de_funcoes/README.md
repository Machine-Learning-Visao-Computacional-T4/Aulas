# Exercício 04 — Mãos à obra + commit: biblioteca de funções

**Tipo:** prática + commit · 18 min

## Objetivo
Praticar **parâmetros, valores padrão e retorno múltiplo**.

## O que fazer
1. Crie `utilidades.py` com: `media(notas)`, `desconto(preco, percentual=10)` e `estatisticas(notas)` retornando **mínimo, máximo e média**.
2. Chame cada função com **argumentos posicionais e nomeados**.
3. Escreva uma função `situacao(media)` que **retorna** `"Aprovado"` ou `"Reprovado"` (use `return`, **não** `print`).
4. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_funcoes_modulos/exercicio_04_biblioteca_de_funcoes/utilidades.py
```

No Windows, se `python` não funcionar, use `py aula3_funcoes_modulos/exercicio_04_biblioteca_de_funcoes/utilidades.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `utilidades.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Média: 7.125
Desconto padrão (10%): 180.0
Desconto de 25% (posicional): 150.0
Desconto de 25% (nomeado): 150.0
Mínimo: 5.0 | Máximo: 9.0 | Média: 7.125
Média 8.5 -> Aprovado
Média 6.9 -> Reprovado
Média 7.0 -> Aprovado
Média 4.0 -> Reprovado
```

## Dicas e erros comuns
- **Valor padrão:** em `desconto(200)` o `percentual` vale 10 sem você informar.
- **Retorno múltiplo:** `return a, b, c` devolve uma tupla; receba com `x, y, z = funcao(...)`.
- Se sobrar tempo, use `situacao()` dentro de um `for` sobre uma lista de médias (o exemplo já faz isso).
