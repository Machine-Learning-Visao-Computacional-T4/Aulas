# Exercício 09 — Quiz relâmpago: revisão da Aula 2

Cobre as 4 partes da aula: gráficos básicos, customização, subplots e gráficos honestos.

1. Que tipo de gráfico responde a cada pergunta: "como algo muda no tempo?", "qual grupo é maior?", "duas variáveis numéricas se relacionam?" e "como os valores se distribuem?"
2. Qual a diferença entre `Figure` e `Axes`?
3. Por que `plt.savefig` precisa vir antes de `plt.show()`?
4. O que é preciso para um gráfico se explicar sozinho?
5. Para que serve o `FuncFormatter`?
6. Qual a vantagem do seaborn com `data=`, `x=` e `y=`? O que faz o `hue`?
7. Como acessar o gráfico `"topo"` de um `plt.subplot_mosaic([["topo", "topo"], ["esq", "dir"]])`?
8. Qual a diferença entre uma função do seaborn de **nível de eixo** e uma de **nível de figura**?
9. Por que uma barra de gráfico de barras deve começar no zero?
10. O que uma matriz 8 x 8 de zeros e 255 tem a ver com visão computacional?
11. **Preveja:** quantas barras e qual a mais alta em `plt.bar(["A", "B", "C"], [3, 7, 5])`?

<details>
<summary>Ver respostas</summary>

1. Linha; barra (`plt.bar`/`plt.barh`); dispersão (`plt.scatter`); histograma (`plt.hist`).
2. A `Figure` é a tela inteira (tamanho, fundo, conjunto de gráficos); cada `Axes` é um gráfico dentro dela, com eixos, título, legenda e os dados desenhados.
3. Depois do `show` a figura é descartada: o arquivo sairia em branco.
4. Título que diz o que é, rótulos nos eixos com unidade, legenda quando há mais de uma série, período e fonte.
5. Para formatar os rótulos do eixo, por exemplo como moeda (`R$ 1.500`).
6. Usa nomes de colunas direto do DataFrame e já cuida de estilo e legenda. O `hue` acrescenta uma variável pela **cor** (uma linha ou ponto de cor diferente por categoria).
7. `ax["topo"]`: o `subplot_mosaic` devolve os eixos em um dicionário indexado pelos nomes.
8. Nível de eixo (`barplot`, `lineplot`, `scatterplot`, `histplot`) desenha em um `ax` e aceita `ax=`; nível de figura (`relplot`, `displot`, `catplot`) cria a figura inteira, divide por `col=`/`row=` e não aceita `ax=`.
9. Porque o **comprimento** da barra representa o valor: cortar o eixo exagera as diferenças (4,3 x 4,2 pareceria enorme).
10. Uma imagem em tons de cinza **é** uma matriz: 0 é preto e 255 é branco. O `imshow` desenha essa matriz, e é a base do trabalho em visão computacional.
11. 3 barras; a mais alta é a **B** (7) e a mais baixa vale 3.

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
