# Exercício 08 — Exercício final: `preparar_pedidos`

**Tipo:** projeto integrador · branch + Pull Request · 25 min

## Objetivo
Integrar **funções, condicionais e junções** em um pipeline reutilizável entregue por branch e Pull Request.

## O que fazer
1. Crie a branch `feature/preparar-pedidos`.
2. Escreva `preparar.py` com a função `preparar_pedidos(pedidos, produtos, clientes)`, usando `assign` e `merge` com `validate`, e inclua as colunas `pedido_grande` e `perfil`.
3. Salve o resultado em `pedidos_prontos.csv` (`index=False`) e mostre `shape` e `head`.
4. Commit, push da branch e Pull Request para a `main`, explicando o que cada etapa do pipeline faz.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_08_exercicio_final_preparar_pedidos/preparar.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_08_exercicio_final_preparar_pedidos/preparar.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `preparar.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`, `clientes.csv`); veja o [guia](../../docs/guia_transformacoes.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
(687, 22)
   id_pedido   canal  produto     plano  total      perfil
0       5000  Balcão    Latte  Gratuito   31.5      neutro
1       5001     App  Brownie  Gratuito   18.0  satisfeito
2       5002  Balcão  Brownie       NaN    9.0  satisfeito
Faturamento bruto: 11085.5 | lucro bruto: 7311.5
Arquivo pedidos_prontos.csv gravado.
```

O `pedidos_prontos.csv` gerado aqui tem 22 colunas (as 20 do pipeline básico mais `pedido_grande` e `perfil`) e é a base da Aula 2.

## Dicas e erros comuns
- O `assign` cria colunas **sem alterar** a tabela original: a função devolve uma tabela nova.
- Cada `.merge` com `validate="m:1"` e `how="left"` mantém as 687 linhas: só as colunas aumentam.
- Antes do commit, rode o script do zero (em uma pasta limpa ou no Colab) para ter certeza de que ele não depende de células soltas.

## Git deste exercício
```bash
git switch -c feature/preparar-pedidos
git add preparar.py pedidos.csv produtos.csv clientes.csv pedidos_prontos.csv
git commit -m "Adiciona pipeline preparar_pedidos"
git push -u origin feature/preparar-pedidos
```
Depois, no GitHub: **Compare & pull request** → descreva o que o programa faz → **Create pull request**.
