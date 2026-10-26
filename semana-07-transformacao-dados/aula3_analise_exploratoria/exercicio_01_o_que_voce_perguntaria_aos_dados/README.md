# Exercício 01 — O que você perguntaria aos dados?

**Tipo:** dinâmica de abertura + script · 8 min

## Objetivo
Formular perguntas de exploração **antes** de olhar a tabela.

## O que fazer
1. Você tem 687 pedidos de uma cafeteria e **há problemas escondidos de propósito**.
2. Escreva três perguntas que faria antes de confiar nos dados.
3. Agrupe as perguntas: tamanho, tipos, ausentes, duplicados, valores estranhos.
4. Rode o script e marque quais das suas perguntas ele já responde.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_01_o_que_voce_perguntaria_aos_dados/perguntas.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_01_o_que_voce_perguntaria_aos_dados/perguntas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `perguntas.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_eda.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
1) Quantas linhas e colunas? 687 x 12

2) Que tipo tem cada coluna?
id_pedido              int64
data                     str
id_cliente           float64
id_produto             int64
qtd                    int64
canal                    str
avaliacao            float64
tempo_entrega_min    float64
produto                  str
categoria                str
custo                float64
preco                float64

3) O que está faltando?
id_cliente           128
avaliacao            116
tempo_entrega_min    568

4) Há linhas repetidas? 12

5) Há valores estranhos? (mínimo e máximo)
     qtd  tempo_entrega_min
min   -1               13.0
max   40              480.0
```

## Dicas e erros comuns
- Boas perguntas de partida: tamanho, tipos, ausentes, duplicados e valores estranhos. Modelos de machine learning aprendem o que está nos dados, **inclusive os erros**.
- Guarde as suas perguntas: ao final do Bloco 1 da aula você marca quais já respondeu.
