# Exercício 04 — O que está faltando?

**Tipo:** dinâmica + script · 6 min

## Objetivo
Praticar o olhar crítico sobre gráficos antes de customizar os próprios.

## O que fazer
1. Rode o script e olhe o gráfico da **esquerda**: o gráfico padrão, sem título e sem rótulos.
2. Liste tudo o que falta para um leitor entender o gráfico sozinho.
3. Agrupe as respostas: título, rótulos dos eixos, unidades, legenda, fonte.
4. Compare com o gráfico da **direita** e aplique dois ajustes no seu gráfico de linha.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_04_o_que_esta_faltando/faltando.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_04_o_que_esta_faltando/faltando.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `faltando.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos_prontos.csv`); veja o [guia](../../docs/guia_visualizacao.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
Faltava: título, rótulos nos eixos com unidade, legenda e uma grade discreta.
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Dicas e erros comuns
- Mínimo necessário: **título** que diz o que é, **rótulos nos eixos com unidade**, **legenda** quando há mais de uma série.
- Menos é mais: cada elemento a mais (grade, cor, anotação) precisa ajudar a entender; se não ajuda, tire.
