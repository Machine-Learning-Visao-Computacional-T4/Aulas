# Exercício 05 — Mão na massa + commit: classificando pedidos

**Tipo:** prática + commit · 18 min

## Objetivo
Criar colunas de classificação com as quatro ferramentas condicionais.

## O que fazer
1. Crie `condicionais.py` partindo das colunas criadas no exercício 02 (data, canal limpo, dia da semana).
2. Crie `pedido_grande` com `np.where` (`qtd >= 3`) e `perfil` com `np.select` (3 regras e `default` `"sem nota"`).
3. Crie `taxa_entrega` com `.loc` (4,50 só para o Delivery) e `faixa_tempo` com `pd.cut`, usando os limites 0, 20, 30, 45 e infinito.
4. Crie `periodo` combinando `isin` e `np.where` (sex-dom x seg-qui).
5. Mostre o `value_counts` de cada coluna criada. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_05_classificando_pedidos/condicionais.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_05_classificando_pedidos/condicionais.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `condicionais.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`); veja o [guia](../../docs/guia_transformacoes.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
pedido_grande
não    578
sim    109
Name: count, dtype: int64

perfil
satisfeito      492
sem nota        116
neutro           76
insatisfeito      3
Name: count, dtype: int64

periodo
sex-dom    409
seg-qui    278
Name: count, dtype: int64

          min  max
canal
App       0.0  0.0
Balcão    0.0  0.0
Delivery  4.5  4.5

faixa_tempo
até 20        10
21-30         37
31-45         62
mais de 45    10
Name: count, dtype: int64

Sem avaliação: 116 | 'sem nota': 116
99 pedidos com 2+ itens pelo App
```

## Dicas e erros comuns
- Em Series use `&` (e), `|` (ou) e `~` (não), sempre com **cada condição entre parênteses**. `and`, `or` e `not` dão `ValueError: The truth value of a Series is ambiguous`.
- Qualquer comparação com `NaN` dá `False`: decida o que fazer com os pedidos sem nota em vez de deixá-los virar "insatisfeito" por acidente.
- `pd.cut` usa intervalos abertos à esquerda e fechados à direita: `(20, 30]`.
