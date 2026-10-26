# Exercício 04 — Qual ferramenta?

**Tipo:** dinâmica + script · 12 min

## Objetivo
Escolher a ferramenta condicional adequada para cada problema e justificar a escolha.

## O que fazer
1. Para cada um dos 6 problemas da tabela abaixo, escreva a ferramenta que você usaria (`np.where`, `np.select`, `.loc`, `pd.cut`, `isin` ou `map`).
2. Compare com a dupla: existe mais de uma resposta correta?
3. Rode o script, que resolve os seis problemas, e confira.

Os 6 problemas:

| # | Problema |
| --- | --- |
| 1 | Marcar nota 5 como "ótimo" e o resto como "ok" |
| 2 | Classificar a nota em satisfeito, neutro e insatisfeito |
| 3 | Dar 10% de desconto só nos pedidos do App |
| 4 | Separar o tempo de entrega em rápido, médio e lento |
| 5 | Marcar pedidos de sábado ou domingo |
| 6 | Trocar o código do produto pelo nome |

<details>
<summary>Ver as ferramentas sugeridas</summary>

| # | Ferramenta |
| --- | --- |
| 1 | `np.where` |
| 2 | `np.select` |
| 3 | `.loc[máscara, coluna]` |
| 4 | `pd.cut` |
| 5 | `isin` (gera a máscara) |
| 6 | `map` com dicionário |

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_04_qual_ferramenta/ferramentas.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_04_qual_ferramenta/ferramentas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `ferramentas.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_transformacoes.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
1) {'ok': 443, 'ótimo': 244}
2) {'satisfeito': 492, 'sem nota': 116, 'neutro': 76, 'insatisfeito': 3}
3) total sem desconto: 11085.50 | com desconto no App: 10712.40
4) {'rápida': 47, 'média': 62, 'lenta': 10}
5) {False: 397, True: 290}
6) [[3, 'Latte'], [11, 'Brownie'], [11, 'Brownie']]
```

## Dicas e erros comuns
- Mais de uma resposta pode funcionar: o `np.select` também resolveria o problema 4 e `.dt.dayofweek >= 5` resolveria o 5.
