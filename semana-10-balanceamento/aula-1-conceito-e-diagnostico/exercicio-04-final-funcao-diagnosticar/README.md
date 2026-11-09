# Exercício 04: Final da Aula 1: função diagnosticar

**Tipo:** Final, com Git e Pull Request

## Objetivo
Entregar uma função de diagnóstico reutilizável.

## O que fazer
1. Crie a branch `feature/diagnostico-balanceamento`.
2. Crie `diagnostico.py` com `diagnosticar(df, alvo)`, que devolve um dicionário com classe majoritária, classe minoritária, proporção da minoritária, razão e acurácia do baseline.
3. No final do arquivo, chame a função para a coluna `fraude` de `arquivos/transacoes.csv`.
4. Acrescente uma segunda chamada com um conjunto criado por você, com três classes.
5. Resultado esperado para as transações: razão 53,1 e proporção 0,0185.

## Como executar
Na raiz do repositório (`semana-10-balanceamento`), com `pip install -r requirements.txt` já feito:
```bash
python aula-1-conceito-e-diagnostico/exercicio-04-final-funcao-diagnosticar/diagnostico.py
```
A solução de referência está em `diagnostico.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
{'classe_majoritaria': 0, 'classe_minoritaria': 1, 'proporcao_minoritaria': 0.0185, 'razao': 53.1, 'acuracia_baseline': 0.9815}
{'classe_majoritaria': 0, 'classe_minoritaria': 2, 'proporcao_minoritaria': 0.05, 'razao': 16.0, 'acuracia_baseline': 0.8}
```
(Saída gerada com pandas 3, NumPy 2, scikit-learn 1.9 e imbalanced-learn 0.14; em versões diferentes podem aparecer variações pequenas.)

## Para pensar
- O que a função faria com colunas de texto como alvo?
- Por que a acurácia do baseline é a proporção da classe majoritária?

## Dicas
- Use `int()` e `float()` para tipos limpos na saída.
- Confira os números esperados antes de abrir o Pull Request.

## Git deste exercício
```bash
git checkout -b feature/diagnostico-balanceamento
git add diagnostico.py
git commit -m "feat: função diagnosticar"
git push -u origin feature/diagnostico-balanceamento
```
Abra o Pull Request para a `main` pelo GitHub e descreva em duas frases o que o programa faz e quais números você conferiu.
