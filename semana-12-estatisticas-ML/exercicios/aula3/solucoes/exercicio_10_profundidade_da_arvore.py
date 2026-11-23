# Aula 3 - Exercício 10: subajuste e superajuste em uma árvore
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
colunas_de_entrada = ["temperatura_c", "ocupacao_pct", "dia_util", "evento"]
entradas_treino, entradas_teste, consumo_treino, consumo_teste = train_test_split(consumo_campus[colunas_de_entrada], consumo_campus["consumo_kwh"], test_size=0.25, random_state=42)
linhas = []
for profundidade in [1, 2, 3, 4, 6, 8, 12]:
    arvore = DecisionTreeRegressor(max_depth=profundidade, random_state=42).fit(entradas_treino, consumo_treino)
    linhas.append({"profundidade": profundidade,
                   "erro_treino": mean_absolute_error(consumo_treino, arvore.predict(entradas_treino)),
                   "erro_teste": mean_absolute_error(consumo_teste, arvore.predict(entradas_teste))})
tabela = pd.DataFrame(linhas)
print(tabela.round(1).to_string(index=False))
melhor = tabela.loc[tabela["erro_teste"].idxmin()]
print(f"menor erro de teste: profundidade {int(melhor['profundidade'])} com {melhor['erro_teste']:.1f} kWh")
