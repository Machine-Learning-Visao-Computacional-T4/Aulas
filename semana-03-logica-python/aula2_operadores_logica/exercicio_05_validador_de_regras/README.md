# Exercício 05 — Exercício final: seu validador de regras

**Tipo:** criação com cenário livre · 15 min

## Objetivo
Consolidar operadores aritméticos, relacionais e lógicos em um **pequeno validador de regras combinadas**.

## O que fazer
1. Escolha um cenário com **pelo menos 2 condições combinadas** (por exemplo: "pode entrar na festa se tiver mais de 18 anos **E** estiver na lista", ou "aprovado se nota >= 7 **E** frequência >= 75%").
2. Use `input()` para coletar os dados, convertendo os tipos corretamente.
3. Escreva a **expressão lógica** combinando os operadores adequados (`and`, `or`, `not`).
4. Exiba o resultado com `print()`, de forma clara.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_operadores_logica/exercicio_05_validador_de_regras/validador.py
```

No Windows, se `python` não funcionar, use `py aula2_operadores_logica/exercicio_05_validador_de_regras/validador.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `validador.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Nota final: 7.5
Frequência (%): 80
Nota: 7.5 | Frequência: 80.0 %
Aprovado? True
```

(Os valores digitados no exemplo acima foram: `7.5`, `80`.)

## Dicas e erros comuns
- `validador.py` é só um exemplo (aprovação por nota e frequência). Crie o seu com outro cenário.
- Esta mesma expressão lógica será usada dentro de um `if` na próxima aula.
