# Semana 12, Aula 2: exercícios

**Tema:** O impacto dos dados no comportamento do modelo

Todos os exercícios usam os arquivos da pasta `arquivos/` do kit. Execute os scripts a partir da **raiz do kit**, por exemplo `python exercicios/aula2/solucoes/exercicio_05_curva_de_aprendizado_comparada.py`. Use nomes de variáveis explicativos (nada de `K`, `N`, `X`, `y`) e fixe sempre `random_state` ou `seed`.

Os exercícios 1 a 3 desta aula são individuais e rápidos. O último é um mini-projeto entregue por **Pull Request**, na branch `feature/dados-e-modelo`.

## Exercício 5: Curva de aprendizado comparada

**Enunciado.** Use `learning_curve` com `train_sizes=[0.05, 0.2, 0.5, 1.0]` para a `LinearRegression` e para a `DecisionTreeRegressor(max_depth=6)`. Monte uma tabela com erro de treino, erro de validação e a lacuna entre eles. Qual modelo se beneficia mais de novos dados?

**O que você deve observar.** A regressão linear estabiliza cedo, com lacuna pequena. A árvore tem lacuna enorme com poucas linhas e continua melhorando com mais dados.

**Dica.** Lembre que o `scoring` devolve valores negativos para erros.

**Solução de referência:** `solucoes/exercicio_05_curva_de_aprendizado_comparada.py` · **Saída esperada:** `solucoes/saidas/exercicio_05_curva_de_aprendizado_comparada.txt`

---

## Exercício 6: Ruído na ocupação

**Enunciado.** Some ruído normal (desvios de 0, 10, 20 e 40 pontos) à coluna `ocupacao_pct`, no treino e no teste, e treine a regressão linear. Mostre o coeficiente da ocupação e o erro no teste em cada caso.

**O que você deve observar.** O coeficiente da ocupação cai de 1,65 para valores próximos de zero. O erro sobe pouco porque o tipo de dia continua informando o consumo.

**Dica.** Use `gerador.normal(0, desvio, tamanho)` e atenção: a coluna da ocupação é a segunda das entradas (`coef_[1]`).

**Solução de referência:** `solucoes/exercicio_06_ruido_na_ocupacao.py` · **Saída esperada:** `solucoes/saidas/exercicio_06_ruido_na_ocupacao.txt`

---

## Exercício 7: Contaminação: linear contra Huber

**Enunciado.** Multiplique por 5 o consumo de 0%, 1%, 3% e 10% das linhas de treino e compare o erro no teste da regressão linear com o do `HuberRegressor` (dentro de um `make_pipeline` com `StandardScaler`).

**O que você deve observar.** A regressão linear piora rapidamente (de 35,0 para mais de 180 kWh com 10%), enquanto o Huber fica estável perto de 35 kWh.

**Dica.** Treine sempre com as entradas de treino limpas e o alvo contaminado; o teste fica intacto.

**Solução de referência:** `solucoes/exercicio_07_contaminacao_linear_contra_huber.py` · **Saída esperada:** `solucoes/saidas/exercicio_07_contaminacao_linear_contra_huber.txt`

---

## Exercício 8: Dados e comportamento do modelo (Git e Pull Request)

**Enunciado.** Crie a branch `feature/dados-e-modelo` e o arquivo `dados_e_modelo.py`. Nele: (1) compare a curva de aprendizado de `LinearRegression` e `DecisionTreeRegressor(max_depth=6)`; (2) compare `ocupacao_pct` dos dois campi com `ks_2samp`; (3) calcule o viés e o erro absoluto do modelo linear (treinado no campus principal) aplicado ao campus da serra. Escreva em `DADOS.md` três frases sobre o que mais afetou o modelo e abra um Pull Request.

**O que você deve observar.** A ocupação também mudou entre os campi (KS de 0,38). O viés no campus da serra é de +36,1 kWh: o modelo subestima o consumo, pois nunca viu o efeito do aquecimento no frio.

**Dica.** Calcule o viés como real menos previsto; o sinal positivo significa que o modelo previu menos do que o real.

**Solução de referência:** `solucoes/exercicio_08_dados_e_modelo.py` · **Saída esperada:** `solucoes/saidas/exercicio_08_dados_e_modelo.txt`

---

## Critérios de avaliação do Pull Request

- Branch `feature/dados-e-modelo` criada a partir da `main`, com commits pequenos e mensagens claras.
- Nomes de variáveis explicativos e `random_state`/`seed` fixados.
- Resultados corretos e comparados com o baseline (quando for o caso).
- Arquivo `.md` com três frases (ou um parágrafo) interpretando os números.
- Descrição do Pull Request explicando o que foi feito.
