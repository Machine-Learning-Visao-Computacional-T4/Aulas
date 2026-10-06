# Exercício 05 — Exercício final: seu próprio mini-programa

**Tipo:** criação livre

## Objetivo
Consolidar todos os conceitos da aula construindo um **pequeno programa original**.

## O que fazer
1. Escolha um cálculo simples do seu interesse (conversor de moeda, calculadora de gorjeta, conversor de temperatura...).
2. Use `input()` para coletar os dados necessários, **convertendo os tipos corretamente**.
3. Faça o cálculo e exiba o resultado com `print()`, usando **uma frase completa** (não só o número).
4. Adicione **pelo menos 1 comentário** (`#`) explicando alguma parte do seu código.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_python_primeiros_passos/exercicio_05_exercicio_final_mini_programa/gorjeta.py
```

No Windows, se `python` não funcionar, use `py aula1_python_primeiros_passos/exercicio_05_exercicio_final_mini_programa/gorjeta.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `gorjeta.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Valor da conta (R$): 120
Percentual de gorjeta (%): 10
Gorjeta de 10.0 % sobre R$ 120.0 = R$ 12.0
Total a pagar: R$ 132.0
```

(Os valores digitados no exemplo acima foram: `120`, `10`.)

## Dicas e erros comuns
- O arquivo `gorjeta.py` é **um exemplo** de mini-programa. O seu deve ser diferente!
- Use `float()` para valores com vírgula (preço, temperatura) e `int()` para valores inteiros (idade, quantidade).
