# Exercício 05 — Hands-on: gráficos de exploração

**Tipo:** prática + commit · 15 min

## Objetivo
Produzir gráficos de exploração e escrever o achado de cada um.

## O que fazer
1. Crie `exploracao.py` partindo do código do primeiro olhar.
2. Faça um **histograma** do tempo de entrega (com e sem os extremos), um **boxplot** de `qtd` e um **countplot** por dia da semana.
3. Para cada gráfico, escreva em comentário: **o que vi** e **o que faria**.
4. Salve as imagens em `graficos/` e faça commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_05_graficos_de_exploracao/exploracao.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_05_graficos_de_exploracao/exploracao.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `exploracao.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_eda.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
Gráficos gravados em: C:\Users\andre.friedrich\Desktop\Machine Learn Senai\T4_repositorios_prontos\semana-07-transformacao-dados\aula3_analise_exploratoria\exercicio_05_graficos_de_exploracao\graficos
 - boxplot_qtd.png
 - pedidos_por_dia.png
 - tempo_com_extremos.png
 - tempo_sem_extremos.png
```

Os gráficos são salvos ao lado do script; se quiser vê-los na tela, acrescente `plt.show()` ao final (no Colab/notebook eles aparecem logo abaixo da célula).

## Dicas e erros comuns
- Cada gráfico deve terminar em uma frase: **o que vi e o que farei**.
- Com `plt.close()` depois de cada `savefig` você evita acumular figuras abertas.
