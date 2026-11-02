# Exercício 06 — Quantas linhas?

**Tipo:** dinâmica + script · 12 min

## Objetivo
Prever o tamanho do resultado de cada tipo de junção, incluindo o efeito de uma chave repetida.

## O que fazer
1. Veja as duas tabelas do script: `esq` com `id` 1, 2, 3 e 4; `dir` com `id` 2, 3, 3 e 5 (note o **3 repetido**).
2. Antes de rodar, escreva quantas linhas terão o `inner`, o `left`, o `right`, o `outer` e o `concat`.
3. Rode o script e compare com as previsões.
4. Discuta de onde vêm as linhas extras causadas pelo 3 repetido.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_06_quantas_linhas/quantas_linhas.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_06_quantas_linhas/quantas_linhas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `quantas_linhas.py` em uma célula e execute com `Shift + Enter`. Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
inner: 3 linhas
 left: 5 linhas
right: 4 linhas
outer: 6 linhas
concat: 8 linhas (empilha, não liga por chave)

   id valor_esq valor_dir      _merge
0   1         a       NaN   left_only
1   2         b         x        both
2   3         c         y        both
3   3         c         z        both
4   4         d       NaN   left_only
5   5       NaN         w  right_only

validate='1:1' interrompeu o merge: Merge keys are not unique in right dataset; not a one-to-one merge
```

## Para pensar
- O `id` 3 aparece uma vez em `esq` e duas em `dir`. Quantas linhas ele gera em cada tipo de junção?
- Em um relatório de vendas, o que aconteceria com os totais se uma chave repetida passasse despercebida?

## Dicas e erros comuns
- Compare sempre `len()` antes e depois de um `merge`.
- O `indicator=True` cria a coluna `_merge` (`both`, `left_only`, `right_only`) e mostra a origem de cada linha.
