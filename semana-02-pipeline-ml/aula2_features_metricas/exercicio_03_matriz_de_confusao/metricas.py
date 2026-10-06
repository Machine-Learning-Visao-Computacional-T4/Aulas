"""Calcula acurácia, precisão, recall e F1 a partir de uma matriz de confusão."""

# Altere estes quatro números para testar outros cenários
VP = 40   # verdadeiros positivos
FP = 10   # falsos positivos
FN = 5    # falsos negativos
VN = 945  # verdadeiros negativos

total = VP + FP + FN + VN
acuracia = (VP + VN) / total
precisao = VP / (VP + FP) if (VP + FP) else 0.0
recall = VP / (VP + FN) if (VP + FN) else 0.0
f1 = 2 * precisao * recall / (precisao + recall) if (precisao + recall) else 0.0

print(f"Total de casos: {total}")
print(f"Acurácia: {acuracia:.1%}")
print(f"Precisão: {precisao:.1%}")
print(f"Recall:   {recall:.1%}")
print(f"F1-score: {f1:.1%}")
