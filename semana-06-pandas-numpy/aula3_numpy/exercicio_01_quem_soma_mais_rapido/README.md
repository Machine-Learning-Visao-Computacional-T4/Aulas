# Exercício 01 — Quem soma mais rápido?

**Tipo:** dinâmica de abertura + script · 8 min

## Objetivo
Fazer uma **previsão sobre desempenho** e conferi-la medindo.

## O que fazer
1. Tarefa: multiplicar por 2 cada um dos **1 milhão** de números de uma sequência, uma vez com um **laço sobre uma lista** e outra com um **array NumPy**.
2. **Aposte:** quantas vezes o NumPy será mais rápido? (1x, 3x, 10x ou 100x)
3. Rode o script e veja a resposta medida no **seu** computador.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_numpy/exercicio_01_quem_soma_mais_rapido/medir_tempo.py
```

No Windows, se `python` não funcionar, use `py aula3_numpy/exercicio_01_quem_soma_mais_rapido/medir_tempo.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `medir_tempo.py` em uma célula e execute com `Shift + Enter`.

## Exemplo de execução

```text
lista: 0.0383s | numpy: 0.0035s
O NumPy foi cerca de 11 vezes mais rápido nesta máquina.
```

Os números acima são de uma execução de exemplo: **os seus serão diferentes**.

## Dicas e erros comuns
- Os tempos mudam de computador para computador e a cada execução; o que importa é a **ordem de grandeza** da diferença.
- O ganho vem de a conta ser feita por código C otimizado **dentro** do NumPy, e não pelo laço do Python.
