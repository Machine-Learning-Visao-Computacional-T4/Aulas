# Exercício 07 — Exercício final do módulo: seu próprio programa completo

**Tipo:** criação livre · 18 min

## Objetivo
Consolidar todo o módulo de Python construindo um **programa original** que combine condicionais e loops.

## O que fazer
1. Escolha um mini-programa de sua preferência (jogo de adivinhação de número, lista de tarefas simples, conversor de notas em lote...).
2. Use **pelo menos**: 1 estrutura condicional (`if/elif/else`), 1 estrutura de repetição (`for` ou `while`) e **ao menos 2 operadores diferentes**.
3. Teste o programa **mais de uma vez**, cobrindo cenários diferentes.
4. Se der tempo, apresente para 1 colega e explique sua lógica em voz alta.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_condicionais_loops/exercicio_07_exercicio_final_programa_completo/adivinha_numero.py
```

No Windows, se `python` não funcionar, use `py aula3_condicionais_loops/exercicio_07_exercicio_final_programa_completo/adivinha_numero.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `adivinha_numero.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Adivinhe o número secreto entre 1 e 20!
Seu palpite: 10
Muito baixo!
Seu palpite: 15
Muito alto!
Seu palpite: 12
Muito alto!
Seu palpite: 11
Parabéns! Você acertou em 4 tentativas.
```

(Os valores digitados no exemplo acima foram: `10`, `15`, `12`, `11`.)

## Dicas e erros comuns
- `adivinha_numero.py` é um **exemplo** de projeto. O número sorteado muda a cada execução, então o exemplo acima é só uma partida possível.
- Comece pequeno: faça funcionar para um caso, depois acrescente as regras.
