# Exercício 08 — Exercício final: painel da cafeteria

**Tipo:** projeto integrador · branch + Pull Request · 25 min

## Objetivo
Integrar **gráficos básicos, customização e subplots** em um painel entregue por Pull Request.

## O que fazer
1. Crie a branch `feature/painel-cafeteria`.
2. Escreva `painel_cafeteria.py` com uma função `criar_painel(base)` que desenha **pelo menos quatro gráficos** em subplots.
3. Inclua título geral, títulos nos eixos, unidades e uma paleta consistente.
4. Salve `painel.png` (`dpi=150`), faça commit e push da branch.
5. Abra um Pull Request para a `main` descrevendo **qual pergunta cada gráfico responde**.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_visualizacao_matplotlib_seaborn/exercicio_08_exercicio_final_painel_da_cafeteria/painel_cafeteria.py
```

No Windows, se `python` não funcionar, use `py aula2_visualizacao_matplotlib_seaborn/exercicio_08_exercicio_final_painel_da_cafeteria/painel_cafeteria.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `painel_cafeteria.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos_prontos.csv`); veja o [guia](../../docs/guia_visualizacao.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
Painel com 4 gráficos gravado em painel.png
```

Uma janela com o gráfico abre ao final (`plt.show()`); feche-a para o script terminar. A imagem também é salva ao lado do script. No Colab/notebook o gráfico aparece logo abaixo da célula.

## Dicas e erros comuns
- Checklist de gráfico honesto: barras começam no zero, a escolha vem da pergunta, tudo está rotulado e as exceções ficam **à vista** (sinalize o ponto isolado em vez de apagá-lo).
- Funções do seaborn de **nível de eixo** (`barplot`, `lineplot`, `scatterplot`) aceitam `ax=`; as de **nível de figura** (`relplot`, `catplot`) criam a própria figura e não aceitam.
- O pico de março e o ponto de 480 minutos são pistas: a Aula 3 investiga os dois.

## Git deste exercício
```bash
git switch -c feature/painel-cafeteria
git add painel_cafeteria.py pedidos_prontos.csv painel.png
git commit -m "Adiciona painel da cafeteria com subplots"
git push -u origin feature/painel-cafeteria
```
Depois, no GitHub: **Compare & pull request** → descreva o que o programa faz → **Create pull request**.
