# Exercício 01 — Quantos passos para uma média?

**Tipo:** dinâmica de abertura · 10 min

## Objetivo
Sentir o problema que o pandas resolve **antes de conhecê-lo**.

## O que fazer
1. Abra `vendas.csv` nesta pasta: são **8 vendas** de uma loja de informática (produto, categoria, cidade, quantidade, preço).
2. Pergunta: usando **só o que já vimos** (`open`, `csv`, `for`, dicionários), quais passos seriam necessários para descobrir o **total vendido por cidade**?
3. Liste os passos (ler, converter tipos, agrupar em um dicionário, somar...) e **conte quantos são**.
4. Rode o script e compare: o jeito difícil x o pandas.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_pandas_dataframes/exercicio_01_quantos_passos_para_uma_media/quantos_passos.py
```

No Windows, se `python` não funcionar, use `py aula1_pandas_dataframes/exercicio_01_quantos_passos_para_uma_media/quantos_passos.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `quantos_passos.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`vendas.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
Jeito difícil (csv + dicionário + laço):
  Blumenau: 3980.0
  Florianópolis: 2280.0
  Joinville: 8200.0

Com pandas (groupby, que você vai aprender na Aula 2):
cidade
Blumenau         3980.0
Florianópolis    2280.0
Joinville        8200.0
Name: total, dtype: float64
```

## Para pensar
- Quantas linhas de código o jeito difícil tem a mais? O que acontece se o arquivo tiver 1 milhão de linhas?

## Dicas e erros comuns
- Passos típicos do jeito difícil: abrir o arquivo, ler cada linha, converter `quantidade` e `preco`, multiplicar, criar um dicionário, somar por cidade.
- O `groupby` do pandas será explicado em detalhes na **Aula 2**; hoje o objetivo é só ver o contraste.
