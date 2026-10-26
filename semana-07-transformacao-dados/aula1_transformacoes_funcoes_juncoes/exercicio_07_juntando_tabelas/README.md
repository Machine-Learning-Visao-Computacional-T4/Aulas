# Exercício 07 — Mão na massa + commit: juntando tabelas

**Tipo:** prática + commit · 18 min

## Objetivo
Cruzar pedidos, produtos e clientes com segurança, conferindo o número de linhas em cada etapa.

## O que fazer
1. Crie `juncoes.py` e leia `pedidos.csv`, `produtos.csv` e `clientes.csv`.
2. Una pedidos e produtos com `validate="m:1"` e confira que o número de linhas continua **687**.
3. Una o resultado com clientes usando `how="left"` e `indicator=True`; conte quantos pedidos **não têm cliente**.
4. Crie as colunas `total` e `lucro` e mostre o lucro por categoria.
5. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_07_juntando_tabelas/juncoes.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_07_juntando_tabelas/juncoes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `juncoes.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`, `clientes.csv`); veja o [guia](../../docs/guia_transformacoes.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
(687, 8) (12, 5) (60, 5)
(687, 8) -> (687, 12)
_merge
both          559
left_only     128
right_only      0
Name: count, dtype: int64
128 pedidos sem cliente (balcão não identificado)
left: 687 | inner: 559
   produto  qtd  preco  total  lucro
0    Latte    3   10.5   31.5   20.7
1  Brownie    2    9.0   18.0   11.8
2  Brownie    1    9.0    9.0    5.9
categoria
Bebida Gelada    1594.0
Café             2581.0
Doce             1422.0
Salgado          1714.0
Name: lucro, dtype: float64

Sem validate: 687 -> 841 linhas
```

## Dicas e erros comuns
- `validate="m:1"` afirma que a chave é única na tabela da direita; se não for, o pandas interrompe com `MergeError`.
- `inner` descarta em silêncio os pedidos sem cliente. A pergunta de negócio decide o `how`.
- Chaves com nomes diferentes: `left_on="id_produto", right_on="cod"`; depois descarte a coluna repetida com `drop`.
- O lucro desta etapa ainda inclui dados com problemas (duplicatas, quantidades inválidas): a Aula 3 investiga isso.
