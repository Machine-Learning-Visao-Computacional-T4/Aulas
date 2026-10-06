# Exercício 01 — A receita reutilizável

**Tipo:** dinâmica sem código · 10 min

## Objetivo
Entender a ideia de **função** a partir de uma receita: entradas, passos e resultado.

## O que fazer
1. Escreva uma **receita curta** de algo do cotidiano (por exemplo, fazer café) com: **o que precisa receber** (ingredientes), **os passos** e **o que entrega** no fim.
2. Pergunte-se: se precisássemos fazer café **50 vezes no dia**, reescreveríamos os passos todas as vezes ou "chamaríamos" a receita?
3. Note como a receita **muda com a quantidade de xícaras**, mas os passos são os mesmos.

## Tradução para Python
| Na receita | Na função |
| --- | --- |
| Ingredientes | **Parâmetros** |
| Passos | **Corpo** da função |
| Prato pronto | **`return`** |

```python
def fazer_cafe(xicaras):
    po = xicaras * 2          # colheres de pó
    agua = xicaras * 100      # ml de água
    return "Café para " + str(xicaras) + " xícaras: " + str(po) + " colheres de pó e " + str(agua) + " ml de água"

print(fazer_cafe(2))
print(fazer_cafe(50))
```
Escreva **uma vez**, use sempre.
