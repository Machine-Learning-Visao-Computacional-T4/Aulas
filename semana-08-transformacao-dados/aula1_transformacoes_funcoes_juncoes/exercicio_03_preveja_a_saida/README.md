# Exercício 03 — Preveja a saída

**Tipo:** dinâmica + script · 10 min

## Objetivo
Treinar a leitura de código de transformação **antes** de executá-lo.

## O que fazer
1. Sem rodar nada, escreva o valor esperado de cada um dos 4 trechos do script.
2. Rode o script e compare com as suas respostas.
3. Discuta os erros mais comuns: o valor sem chave no `map` e o dia da semana começar em zero.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_03_preveja_a_saida/trechos.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_03_preveja_a_saida/trechos.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `trechos.py` em uma célula e execute com `Shift + Enter`. Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
1) Texto
0      Sul
1    Norte
dtype: str

2) map com dicionário
0      a
1      b
2    NaN
dtype: str

3) apply com lambda
0     3
1    16
dtype: int64

4) Dia da semana de 14/03/2025
0    4
dtype: int32
```

## Para pensar
- Por que o `7` virou `NaN` no trecho 2?
- Que dia da semana é o número que apareceu no trecho 4?

## Dicas e erros comuns
- Escreva a previsão **antes** de rodar: errar faz parte e é como se aprende.
