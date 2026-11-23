# Semana 12, Aula 3: exercícios

**Tema:** Noções intuitivas de erro e desempenho

Todos os exercícios usam os arquivos da pasta `arquivos/` do kit. Execute os scripts a partir da **raiz do kit**, por exemplo `python exercicios/aula3/solucoes/exercicio_09_metricas_a_mao.py`. Use nomes de variáveis explicativos (nada de `K`, `N`, `X`, `y`) e fixe sempre `random_state` ou `seed`.

Os exercícios 1 a 3 desta aula são individuais e rápidos. O último é um mini-projeto entregue por **Pull Request**, na branch `feature/relatorio-desempenho`.

## Exercício 9: Métricas à mão

**Enunciado.** Sem usar as funções de `sklearn.metrics`, calcule MAE, MSE, RMSE e R² a partir dos resíduos do modelo linear no teste. Depois confira os valores com o scikit-learn usando `np.isclose`.

**O que você deve observar.** Os valores manuais coincidem com os do scikit-learn: MAE 34,97; RMSE 43,04; R² 0,812.

**Dica.** R² = 1 menos a soma dos quadrados dos resíduos dividida pela soma dos quadrados totais (em relação à média do real).

**Solução de referência:** `solucoes/exercicio_09_metricas_a_mao.py` · **Saída esperada:** `solucoes/saidas/exercicio_09_metricas_a_mao.txt`

---

## Exercício 10: Profundidade da árvore

**Enunciado.** Treine árvores com `max_depth` em 1, 2, 3, 4, 6, 8 e 12. Monte a tabela de erro de treino e de teste e indique a profundidade com menor erro de teste. Explique em uma frase onde estão o subajuste e o superajuste.

**O que você deve observar.** O erro de teste é mínimo na profundidade 4 (31,4 kWh). O erro de treino continua caindo até 7,9 kWh na profundidade 12, enquanto o de teste sobe a 41,1: superajuste.

**Dica.** Use `DataFrame.loc[tabela['erro_teste'].idxmin()]` para achar a linha do melhor teste.

**Solução de referência:** `solucoes/exercicio_10_profundidade_da_arvore.py` · **Saída esperada:** `solucoes/saidas/exercicio_10_profundidade_da_arvore.txt`

---

## Exercício 11: Validação cruzada com várias métricas

**Enunciado.** Use `cross_validate` com `KFold(n_splits=5, shuffle=True, random_state=42)` para obter, ao mesmo tempo, MAE, RMSE e R² de baseline, regressão e árvore (profundidade 4). Diga se a diferença entre regressão e árvore é relevante.

**O que você deve observar.** O baseline tem R² próximo de zero (levemente negativo), e os dois modelos ficam em torno de 0,81. A diferença entre regressão e árvore é menor que o desvio entre as partes.

**Dica.** O parâmetro `scoring` aceita um dicionário de métricas, e os resultados vêm em chaves `test_<nome>`.

**Solução de referência:** `solucoes/exercicio_11_validacao_cruzada_com_rmse_e_r2.py` · **Saída esperada:** `solucoes/saidas/exercicio_11_validacao_cruzada_com_rmse_e_r2.txt`

---

## Exercício 12: Relatório de desempenho (Git e Pull Request)

**Enunciado.** Crie a branch `feature/relatorio-desempenho` e o arquivo `relatorio_desempenho.py`. Nele: (1) calcule MAE, RMSE, MAPE e R² da regressão linear no teste e compare com o baseline; (2) use `KFold` para comparar baseline, regressão e árvore; (3) calcule viés e erro absoluto por `dia_util`; (4) simule margens de segurança de 0 a 80 kWh com custo 5 para faltar e 1 para sobrar. Escreva em `DESEMPENHO.md` um parágrafo dizendo se o modelo serve para negociar a demanda contratada, e abra um Pull Request.

**O que você deve observar.** Com custo 5 para faltar e 1 para sobrar, a melhor margem fica entre 40 e 60 kWh (custo médio perto de 65), bem abaixo dos 118,8 de margem zero.

**Dica.** Justifique a conclusão com números, e não só com adjetivos.

**Solução de referência:** `solucoes/exercicio_12_relatorio_desempenho.py` · **Saída esperada:** `solucoes/saidas/exercicio_12_relatorio_desempenho.txt`

---

## Critérios de avaliação do Pull Request

- Branch `feature/relatorio-desempenho` criada a partir da `main`, com commits pequenos e mensagens claras.
- Nomes de variáveis explicativos e `random_state`/`seed` fixados.
- Resultados corretos e comparados com o baseline (quando for o caso).
- Arquivo `.md` com três frases (ou um parágrafo) interpretando os números.
- Descrição do Pull Request explicando o que foi feito.
