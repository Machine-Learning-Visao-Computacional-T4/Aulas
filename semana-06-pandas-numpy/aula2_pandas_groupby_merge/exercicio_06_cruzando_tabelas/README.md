# Exercício 06 — Mãos à obra + commit: cruzando tabelas

**Tipo:** prática + commit · 15 min

## Objetivo
Juntar **clientes e pedidos** e resumir **por cidade**.

## O que fazer
1. Crie `cruzamento.py`, que lê `clientes.csv` e `pedidos.csv`.
2. Faça um `merge` **left** e liste os pedidos **sem cliente cadastrado** (nome ausente).
3. Faça um `merge` **inner** e calcule o **valor total** e a **quantidade de pedidos** por cidade do cliente.
4. Salve o resumo em `resumo_cidades.csv`; commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_pandas_groupby_merge/exercicio_06_cruzando_tabelas/cruzamento.py
```

No Windows, se `python` não funcionar, use `py aula2_pandas_groupby_merge/exercicio_06_cruzando_tabelas/cruzamento.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `cruzamento.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`clientes.csv`, `pedidos.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
Pedidos sem cliente cadastrado:
   id_pedido  valor
4        105   60.0

Resumo por cidade:
               count     sum
cidade
Blumenau           1  3500.0
Florianópolis      2   180.0
Joinville          1   900.0
Arquivo resumo_cidades.csv gravado.
```

## Dicas e erros comuns
- `esquerda["nome"].isna()` devolve a máscara dos pedidos órfãos.
- `.agg(["count", "sum"])` calcula as duas medidas de uma vez.
