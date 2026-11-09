import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

transacoes = pd.read_csv("arquivos/transacoes.csv")
print(transacoes.shape)
print(transacoes["fraude"].value_counts())
print(transacoes["fraude"].value_counts(normalize=True).round(4))

contagem = transacoes["fraude"].value_counts()
razao = contagem.max() / contagem.min()
print(f"Para cada fraude existem {razao:.0f} transações legítimas.")

sns.countplot(data=transacoes, x="fraude")
plt.xticks([0, 1], ["Legítima", "Fraude"])
plt.savefig("arquivos/classes.png", dpi=100, bbox_inches="tight")
