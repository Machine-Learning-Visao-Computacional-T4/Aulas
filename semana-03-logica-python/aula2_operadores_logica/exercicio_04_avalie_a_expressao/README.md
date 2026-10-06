# Exercício 04 — Avalie a expressão

**Tipo:** dinâmica de previsão

## Objetivo
Praticar a **previsão do resultado** de expressões que combinam operadores aritméticos, relacionais e lógicos.

## O que fazer
1. Abra [`previsoes.md`](previsoes.md) e escreva, ao lado de cada expressão, o resultado que você acha que ela produz (`True` ou `False`), **sem rodar o código ainda**.
2. Depois de responder todas, rode o script para conferir.
3. Para cada resposta errada, descubra **por quê**: foi precedência? curto-circuito?

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_operadores_logica/exercicio_04_avalie_a_expressao/expressoes.py
```

No Windows, se `python` não funcionar, use `py aula2_operadores_logica/exercicio_04_avalie_a_expressao/expressoes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `expressoes.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
1 | 10 > 5 and 3 < 1 -> False
2 | not (4 == 4) -> False
3 | 7 % 2 == 1 -> True
4 | 2 + 3 * 4 == 20 -> False
5 | (2 + 3) * 4 == 20 -> True
6 | True or 1 / 0 == 1 -> True
7 | False and 1 / 0 == 1 -> False
8 | 5 > 3 or 2 > 8 and 1 > 2 -> True
9 | not True or True -> True
10 | 17 // 5 == 3 and 17 % 5 == 2 -> True
```

## Dicas e erros comuns
- Precedência: aritmética primeiro, depois comparações, depois `not`, depois `and`, depois `or`. Parênteses mandam em tudo.
- **Curto-circuito:** em `True or ...` o Python nem olha o lado direito (por isso `1 / 0` não dá erro nas expressões 6 e 7).
- Estas 10 expressões foram preparadas para este repositório; as da aula podem ser outras.
