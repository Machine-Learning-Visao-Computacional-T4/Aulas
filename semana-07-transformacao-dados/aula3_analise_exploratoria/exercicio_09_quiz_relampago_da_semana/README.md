# Exercício 09 — Quiz relâmpago: revisão da Semana 07

Cobre as 3 aulas da semana (transformação, visualização e análise exploratória).

1. Por que `map` com uma chave inexistente exige cuidado?
2. Quando usar `np.select` em vez de `np.where`? E por que o `default` importa?
3. Quantas linhas tem o resultado de um `merge` quando a chave se repete na tabela da direita e você **não** usou `validate`?
4. Que gráfico responde a "como o faturamento mudou mês a mês?" e por que as barras devem começar no zero?
5. Por que o painel da cafeteria usa `ax=` com o seaborn?
6. Quais são os passos iniciais do roteiro de EDA (o primeiro olhar)?
7. O que a regra de 1,5 x IQR calcula?
8. Por que a correlação entre `qtd` e `total` ser 0,95 não é uma descoberta?
9. O que mudou na correlação entre tempo de entrega e nota ao retirar os 480 minutos?
10. Um `id_cliente` ausente em pedidos de balcão deve ser removido, corrigido ou mantido? Justifique.
11. O que o quarteto de Anscombe ensina?
12. **Preveja:** `pd.to_datetime(pd.Series(["2025-03-14"])).dt.dayofweek`

<details>
<summary>Ver respostas</summary>

1. Porque ela vira `NaN` **sem aviso**. Confira com `isna()` depois do `map`.
2. Quando há **mais de duas** saídas ou várias regras em ordem. O `default` cobre quem não bateu em nenhuma regra (como os pedidos sem nota, já que comparações com `NaN` dão `False`).
3. Mais linhas que a tabela da esquerda: cada linha repetida na chave multiplica o resultado (por exemplo, 687 viram 838 ou mais), inflando totais sem avisar. O `validate="m:1"` interrompe o merge com erro.
4. **Linha**, porque o eixo x tem ordem (tempo). Nas barras, o **comprimento** representa o valor: cortar o eixo exagera as diferenças.
5. Para dizer **em qual gráfico** desenhar: as funções de nível de eixo (`barplot`, `lineplot`, `scatterplot`) aceitam `ax=` e assim se encaixam no layout do Matplotlib.
6. `shape`, `head`, `info`, `describe`, valores ausentes (`isna`), duplicados (`duplicated`) e categorias (`value_counts`).
7. O limite superior de valores normais: `Q3 + 1,5 × (Q3 − Q1)`. O que passa disso é marcado como atípico (outlier).
8. Porque `total = qtd × preço`: é uma relação **construída**, esperada. Correlação alta nem sempre é informação nova.
9. De **0,03 para -0,15**: o sinal passou a ser negativo (entregas mais demoradas, notas um pouco menores), mas ainda é uma correlação fraca.
10. **Manter**: são vendas de balcão não identificadas; a ausência tem sentido. Toda decisão deve ser registrada e, se possível, validada com o negócio.
11. Que média, variância e correlação iguais podem esconder conjuntos de dados completamente diferentes: **sempre olhe o gráfico**.
12. **4**: 14/03/2025 foi uma **sexta-feira** (segunda = 0).

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
