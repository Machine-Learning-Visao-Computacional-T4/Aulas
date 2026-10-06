# Exercício 02 — Mãos à obra: calculadora de troco

**Tipo:** prática · 15 min

## Objetivo
Praticar **operadores aritméticos**, incluindo `//` e `%`, em um problema prático.

## O que fazer
1. Peça (com `input()`) o **valor de uma compra** e o **valor pago em dinheiro**, convertendo para `float`.
2. Calcule o troco (valor pago − valor da compra).
3. Usando `//` e `%`, calcule **quantas notas de R$ 10** e **quantas moedas de R$ 1** formariam esse troco (dica: `troco // 10` e `troco % 10`).
4. Exiba o resultado com `print()`, de forma legível.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_operadores_logica/exercicio_02_calculadora_de_troco/troco.py
```

No Windows, se `python` não funcionar, use `py aula2_operadores_logica/exercicio_02_calculadora_de_troco/troco.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `troco.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Valor da compra (R$): 36.50
Valor pago em dinheiro (R$): 50
Troco total: R$ 13.5
Notas de R$ 10: 1
Moedas de R$ 1: 3
Sobra em centavos: R$ 0.5
```

(Os valores digitados no exemplo acima foram: `36.50`, `50`.)

## Dicas e erros comuns
- `//` é a divisão inteira (quantas vezes cabe) e `%` é o resto. `17 // 5` dá `3` e `17 % 5` dá `2`.
- Assuma que o valor pago é **maior ou igual** ao da compra. Depois da Aula 3, volte aqui e use `if` para avisar quando o pagamento for insuficiente.
- Valores com centavos têm pequenas imprecisões em `float`; por isso o exemplo usa `round(..., 2)`.
