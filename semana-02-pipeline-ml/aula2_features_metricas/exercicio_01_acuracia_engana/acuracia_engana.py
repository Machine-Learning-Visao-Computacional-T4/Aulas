"""Mostra que um modelo 'preguiçoso' pode ter acurácia altíssima em um problema raro."""
import random

random.seed(42)

TOTAL = 100_000
TAXA_DOENCA = 1 / 1000

# 1 = doente, 0 = saudável
reais = [1 if random.random() < TAXA_DOENCA else 0 for _ in range(TOTAL)]

# Modelo preguiçoso: sempre diz "saudável"
previsoes = [0] * TOTAL

acertos = sum(1 for real, prev in zip(reais, previsoes) if real == prev)
doentes = sum(reais)
doentes_encontrados = sum(1 for real, prev in zip(reais, previsoes) if real == 1 and prev == 1)

print(f"Pessoas avaliadas:          {TOTAL}")
print(f"Pessoas realmente doentes:  {doentes}")
print(f"Acurácia do modelo:         {acertos / TOTAL:.2%}")
print(f"Doentes encontrados:        {doentes_encontrados} de {doentes}")
print()
print("Conclusão: o modelo acerta quase sempre e não encontra NENHUM doente.")
