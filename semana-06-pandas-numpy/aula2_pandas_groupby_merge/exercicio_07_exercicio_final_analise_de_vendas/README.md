# Exercício 07 — Exercício final: análise de vendas por cliente

**Tipo:** projeto integrador · 25 min · branch + Pull Request

## Objetivo
Aplicar **limpeza, merge, groupby e pivot** em uma mini-análise entregue via **branch e Pull Request**.

## O que fazer
1. Crie a branch `feature/analise-vendas-pandas`.
2. Escreva `analise.py`: leia `pedidos.csv` e `clientes.csv`, junte com `merge` **left**, preencha o nome ausente com `"Cliente não cadastrado"` e crie uma coluna de **faixa de valor** (valor acima de 500 = `Alto`, senão `Baixo`).
3. Calcule o **total por cidade** e o **total por produto e cidade** (`pivot_table`); salve os dois resumos em CSV.
4. Commit, push da branch e **Pull Request** para a `main`, descrevendo a análise e o que você descobriu.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_pandas_groupby_merge/exercicio_07_exercicio_final_analise_de_vendas/analise.py
```

No Windows, se `python` não funcionar, use `py aula2_pandas_groupby_merge/exercicio_07_exercicio_final_analise_de_vendas/analise.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `analise.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`clientes.csv`, `pedidos.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
   id_pedido                    nome   valor  faixa
0        101               Ana Souza   120.0  Baixo
1        102               Ana Souza    60.0  Baixo
2        103              Bruno Lima   900.0   Alto
3        104            Carla Mendes  3500.0   Alto
4        105  Cliente não cadastrado    60.0  Baixo

Total por cidade:
cidade
Blumenau         3500.0
Florianópolis     180.0
Joinville         900.0
Sem cidade         60.0
Name: valor, dtype: float64

Produto por cidade:
cidade    Blumenau  Florianópolis  Joinville  Sem cidade
produto
Monitor        0.0            0.0      900.0         0.0
Mouse          0.0           60.0        0.0        60.0
Notebook    3500.0            0.0        0.0         0.0
Teclado        0.0          120.0        0.0         0.0
```

## Dicas e erros comuns
- Para a faixa de valor: crie a coluna com `"Baixo"` para todos e troque por `"Alto"` onde o valor passa de 500 (`df.loc[condição, "faixa"] = "Alto"`).
- No `pivot_table`, `fill_value=0` troca as combinações sem vendas por zero.

## Git deste exercício
```bash
git switch -c feature/analise-vendas-pandas
git add analise.py clientes.csv pedidos.csv
git commit -m "Adiciona análise de vendas por cliente com pandas"
git push -u origin feature/analise-vendas-pandas
```
Depois, no GitHub: **Compare & pull request** → descreva o que o programa faz → **Create pull request**.
