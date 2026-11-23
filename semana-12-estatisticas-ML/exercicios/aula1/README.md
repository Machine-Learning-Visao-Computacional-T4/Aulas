# Semana 12, Aula 1: exercícios

**Tema:** A estatística como lente para dados e modelos

Todos os exercícios usam os arquivos da pasta `arquivos/` do kit. Execute os scripts a partir da **raiz do kit**, por exemplo `python exercicios/aula1/solucoes/exercicio_01_amostras_de_umidade.py`. Use nomes de variáveis explicativos (nada de `K`, `N`, `X`, `y`) e fixe sempre `random_state` ou `seed`.

Os exercícios 1 a 3 desta aula são individuais e rápidos. O último é um mini-projeto entregue por **Pull Request**, na branch `feature/estatistica-amostras`.

## Exercício 1: Amostras de umidade

**Enunciado.** Com a coluna `umidade_pct` de `consumo_campus.csv`, sorteie 1000 amostras de 30 dias (`random_state` igual ao número da repetição) e depois 1000 amostras de 120 dias. Para cada tamanho, compare o desvio padrão das médias amostrais com o erro padrão teórico (desvio dos dados dividido pela raiz do tamanho da amostra).

**O que você deve observar.** O desvio das médias fica muito próximo do erro padrão teórico. Quando o tamanho da amostra quadruplica (30 para 120), o desvio cai pela metade.

**Dica.** Use `Series.sample(n=..., random_state=...)` dentro de uma compreensão de listas e `np.sqrt`.

**Solução de referência:** `solucoes/exercicio_01_amostras_de_umidade.py` · **Saída esperada:** `solucoes/saidas/exercicio_01_amostras_de_umidade.txt`

---

## Exercício 2: Bootstrap da mediana

**Enunciado.** Escreva uma função que receba uma amostra e devolva o intervalo bootstrap de 95% da **mediana**. Aplique a uma amostra de 40 dias de `ocupacao_pct`. Depois repita para 20 amostras diferentes e conte em quantas o intervalo contém a mediana real da coluna.

**O que você deve observar.** O intervalo contém a mediana real na grande maioria das amostras (esperado: cerca de 19 em 20).

**Dica.** Troque `.mean()` por `np.median(...)` no laço do bootstrap e use `gerador.choice(..., replace=True)`.

**Solução de referência:** `solucoes/exercicio_02_bootstrap_da_mediana.py` · **Saída esperada:** `solucoes/saidas/exercicio_02_bootstrap_da_mediana.txt`

---

## Exercício 3: Sinal e ruído por grupo

**Enunciado.** Calcule média, desvio e contagem do consumo por `dia_semana`. Depois calcule a variância total e a variância **dentro** dos grupos dia útil/fim de semana (use `groupby(...).transform('mean')`). A fração da variação explicada é 1 menos a razão entre as duas.

**O que você deve observar.** Os dias úteis têm consumo parecido entre si (cerca de 541 a 549 kWh), e sábado e domingo ficam perto de 368 kWh. O tipo de dia explica cerca de 69% da variação do consumo.

**Dica.** Use `var(ddof=0)` para a variância total, de modo que seja comparável à média dos quadrados dos desvios dentro dos grupos.

**Solução de referência:** `solucoes/exercicio_03_sinal_e_ruido_por_grupo.py` · **Saída esperada:** `solucoes/saidas/exercicio_03_sinal_e_ruido_por_grupo.txt`

---

## Exercício 4: Estatística de amostras (Git e Pull Request)

**Enunciado.** Crie a branch `feature/estatistica-amostras` e o arquivo `estatistica_amostras.py`. Nele: (1) compare o desvio das médias de 1000 amostras de 30 dias de `umidade_pct` com o erro padrão teórico; (2) calcule o intervalo bootstrap de 95% da mediana de `ocupacao_pct` em uma amostra de 40 dias; (3) compare `DummyRegressor` e `LinearRegression` para prever `consumo_kwh` usando só `temperatura_c`. Escreva em `ANALISE.md` três frases interpretando os números e abra um Pull Request.

**O que você deve observar.** A regressão só com temperatura melhora muito pouco o baseline (cerca de 2%). Quem carrega o sinal é o tipo de dia, que você usará no próximo exercício da semana.

**Dica.** Faça commits pequenos, com mensagens claras, e descreva no Pull Request o que cada parte do arquivo calcula.

**Solução de referência:** `solucoes/exercicio_04_estatistica_amostras.py` · **Saída esperada:** `solucoes/saidas/exercicio_04_estatistica_amostras.txt`

---

## Critérios de avaliação do Pull Request

- Branch `feature/estatistica-amostras` criada a partir da `main`, com commits pequenos e mensagens claras.
- Nomes de variáveis explicativos e `random_state`/`seed` fixados.
- Resultados corretos e comparados com o baseline (quando for o caso).
- Arquivo `.md` com três frases (ou um parágrafo) interpretando os números.
- Descrição do Pull Request explicando o que foi feito.
