# Exercício 01 — Qual gráfico responde?

**Tipo:** dinâmica de abertura + script · 8 min

## Objetivo
Ativar o que você já intui sobre tipos de gráfico **antes** de aprender o código.

## O que fazer
1. Leia as três perguntas: **"como o faturamento mudou mês a mês?"**, **"qual categoria vende mais?"** e **"quem demora mais para entregar também recebe nota pior?"**.
2. Escreva um tipo de gráfico para cada pergunta (linha, barra, dispersão, pizza...).
3. Compare com a turma e discuta onde houve divergência.
4. Rode o script: ele desenha uma sugestão para cada pergunta. No fim do Bloco 1 da aula, confira se as suas escolhas se confirmaram.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_01_qual_grafico_responde/perguntas_graficos.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_01_qual_grafico_responde/perguntas_graficos.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `perguntas_graficos.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos_prontos.csv`); veja o [guia](../../docs/guia_visualizacao.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
Pergunta 1 -> linha (tempo tem ordem). Mês de maior faturamento: 3
Pergunta 2 -> barra (comparar grupos). Categoria líder: Café
Pergunta 3 -> dispersão (duas variáveis numéricas). 98 entregas com nota
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Dicas e erros comuns
- Tempo pede **linha**, comparação entre grupos pede **barra**, relação entre variáveis pede **dispersão** e distribuição pede **histograma**.
- Pizza e gráficos 3D quase nunca são a melhor escolha.
