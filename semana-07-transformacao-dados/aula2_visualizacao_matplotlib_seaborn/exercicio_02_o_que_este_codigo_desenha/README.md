# Exercício 02 — O que este código desenha?

**Tipo:** dinâmica + script · 6 min

## Objetivo
Treinar a leitura de código de gráfico **antes** de escrever o seu.

## O que fazer
1. Leia no script: `plt.bar(["A", "B", "C"], [3, 7, 5])` seguido de `plt.show()`.
2. Descreva o que verá: quantas barras, qual a mais alta, qual o valor da mais baixa.
3. Rode o script e compare.
4. Variação: troque `bar` por `barh` e pergunte o que muda.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_02_o_que_este_codigo_desenha/codigo_misterioso.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_02_o_que_este_codigo_desenha/codigo_misterioso.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `codigo_misterioso.py` em uma célula e execute com `Shift + Enter`. Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
3 barras | a mais alta é a B (7) | a mais baixa vale 3
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Para pensar
- Em que `barh` é melhor que `bar`? (Pense em nomes de categoria longos.)

## Dicas e erros comuns
- `plt.barh` coloca o primeiro rótulo embaixo; por isso se ordena com `sort_values()` antes: o maior fica no topo.
