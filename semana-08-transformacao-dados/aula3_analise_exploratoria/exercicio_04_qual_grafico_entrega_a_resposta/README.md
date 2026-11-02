# Exercício 04 — Qual gráfico entrega a resposta?

**Tipo:** dinâmica + script · 8 min

## Objetivo
Escolher o gráfico de exploração adequado a cada pergunta.

## O que fazer
1. Para cada pergunta, escolha um gráfico: **"há valores extremos na quantidade?"**, **"os canais estão padronizados?"**, **"em que dia vendemos mais?"** e **"a nota muda com o tempo de entrega?"**.
2. Confira com a turma: `boxplot`, `countplot`, `countplot` por dia e dispersão.
3. Rode o script, que desenha os quatro gráficos em uma figura.
4. Abra para discordâncias: mais de uma resposta pode funcionar.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_04_qual_grafico_entrega_a_resposta/qual_grafico.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_04_qual_grafico_entrega_a_resposta/qual_grafico.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `qual_grafico.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_eda.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
Pedidos de domingo (sem duplicados): 149
Variações de canal no arquivo bruto: 9
```

Os gráficos são salvos ao lado do script; se quiser vê-los na tela, acrescente `plt.show()` ao final (no Colab/notebook eles aparecem logo abaixo da célula).

## Dicas e erros comuns
- Distribuição pede histograma ou boxplot; contagem pede barras; evolução pede linha; relação pede dispersão ou mapa de calor.
- Explorar é diferente de apresentar: na exploração cada gráfico responde a uma pergunta e **não precisa de capricho**.
