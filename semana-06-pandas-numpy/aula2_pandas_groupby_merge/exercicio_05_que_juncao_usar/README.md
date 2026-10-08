# Exercício 05 — Que junção usar?

**Tipo:** dinâmica + script · 12 min

## Objetivo
Escolher o **tipo de junção** (`inner`, `left`, `right`, `outer`) para cada pergunta.

## O que fazer
1. Olhe as duas tabelas (`clientes.csv` e `pedidos.csv`). Detalhes propositais: o pedido **105** é do cliente **5**, que não existe no cadastro; e o cliente **4 (Diego)** nunca fez um pedido.
2. Para cada pergunta abaixo, escreva o **tipo de junção** e uma justificativa em uma frase.
3. Rode o script para conferir quantas linhas cada junção devolve.
4. Discuta os casos com mais de uma resposta possível (trocar a ordem das tabelas troca `left` por `right`).

## As 4 perguntas
1. Listar os **pedidos com o nome do cliente**.
2. Achar os **clientes que nunca compraram**.
3. Achar os **pedidos de clientes não cadastrados**.
4. Ter a **lista completa dos dois lados**.

<details>
<summary>Ver respostas</summary>

1. `inner` (só o que casa nos dois lados).
2. `right` (todos os clientes) e filtrar quem ficou sem pedido; ou `left` com as tabelas invertidas.
3. `left` (todos os pedidos) e filtrar quem ficou sem nome.
4. `outer`.

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_pandas_groupby_merge/exercicio_05_que_juncao_usar/juncoes.py
```

No Windows, se `python` não funcionar, use `py aula2_pandas_groupby_merge/exercicio_05_que_juncao_usar/juncoes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `juncoes.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`clientes.csv`, `pedidos.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
4 clientes e 5 pedidos

inner  -> 4 linhas
left   -> 5 linhas
right  -> 5 linhas
outer  -> 6 linhas

Pedidos sem cliente cadastrado (left + nome ausente):
   id_pedido  id_cliente  valor
4        105           5   60.0

Clientes que nunca compraram (right + pedido ausente):
   id_cliente         nome
4           4  Diego Alves
```

## Dicas e erros comuns
- Sempre confira `len()` antes e depois de um `merge`: chaves **repetidas** em uma das tabelas **multiplicam** linhas.
- `indicator=True` cria a coluna `_merge`, que diz de onde veio cada linha (`both`, `left_only`, `right_only`).
