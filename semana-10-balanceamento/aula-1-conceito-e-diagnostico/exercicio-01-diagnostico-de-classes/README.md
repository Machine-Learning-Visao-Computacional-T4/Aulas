# Exercício 01: Diagnóstico de classes

**Tipo:** Guiado

## Objetivo
Medir o desbalanceamento de um arquivo antes de qualquer modelo.

## O que fazer
1. Leia `arquivos/transacoes.csv` e mostre o shape.
2. Mostre as contagens e as proporções da coluna `fraude` com `value_counts`.
3. Calcule a razão de desbalanceamento (classe maior dividida pela menor) e imprima a frase completa.
4. Desenhe o `countplot` com os rótulos Legítima e Fraude e salve em `arquivos/classes.png`.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-1-conceito-e-diagnostico/exercicio-01-diagnostico-de-classes/diagnostico_classes.py
```
A solução de referência está em `diagnostico_classes.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
(10000, 10)
fraude
0    9815
1     185
Name: count, dtype: int64
fraude
0    0.9815
1    0.0185
Name: proportion, dtype: float64
Para cada fraude existem 53 transações legítimas.
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- Por que o gráfico de barras sozinho não basta para descrever o desbalanceamento?
- Em que situação a classe rara não é a classe 'ruim'?

## Dicas
- `value_counts(normalize=True)` devolve proporções.
- Use `plt.savefig` para gravar o gráfico quando rodar fora do Jupyter.
