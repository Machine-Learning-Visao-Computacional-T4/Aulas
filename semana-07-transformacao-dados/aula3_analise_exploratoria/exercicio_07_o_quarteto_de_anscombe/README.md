# Exercício 07 — O quarteto de Anscombe

**Tipo:** demonstração + script · 10 min

## Objetivo
Entender por que **só os números não bastam**: sempre olhe o gráfico.

## O que fazer
1. Leia no script os quatro conjuntos de 11 pontos: os três primeiros compartilham o mesmo `x`; o quarto tem `x` quase constante.
2. Antes de rodar, aposte: as estatísticas (média, variância, correlação) dos quatro conjuntos são parecidas ou muito diferentes?
3. Rode o script, compare as estatísticas e olhe os quatro gráficos.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_07_o_quarteto_de_anscombe/anscombe.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_07_o_quarteto_de_anscombe/anscombe.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `anscombe.py` em uma célula e execute com `Shift + Enter`. Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
conjunto | média de y | variância de y | correlação
       1 |       7.50 |           4.13 | 0.816
       2 |       7.50 |           4.13 | 0.816
       3 |       7.50 |           4.12 | 0.816
       4 |       7.50 |           4.12 | 0.817
```

Estatísticas praticamente idênticas, gráficos completamente diferentes: reta, curva, reta com um ponto fora e uma coluna vertical com um ponto fora. O gráfico `anscombe.png` é salvo ao lado do script (acrescente `plt.show()` para vê-lo na tela).

## Dicas e erros comuns
- Média, variância e correlação iguais **não** significam dados parecidos.
- Em 2013, um erro de planilha derrubou as conclusões de um estudo muito citado sobre dívida pública (Herndon, Ash e Pollin): dados conferidos e reproduzíveis importam.
