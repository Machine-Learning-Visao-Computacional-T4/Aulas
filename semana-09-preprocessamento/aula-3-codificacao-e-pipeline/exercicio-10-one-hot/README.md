# Exercício 10: One-Hot com pandas e scikit-learn

**Tipo:** Guiado

## Objetivo
Codificar categorias sem ordem e comparar as duas ferramentas.

## O que fazer
1. Aplique `pd.get_dummies` a `tipo` e `bairro` com `drop_first=True` e `dtype=int`; mostre o shape antes e depois.
2. Mostre que a soma das dummies de `tipo` (sem `drop_first`) é sempre 1.
3. Ajuste um `OneHotEncoder(handle_unknown='ignore')` em `tipo` e transforme uma linha com tipo 'Galpão'.
4. Escreva em comentário qual ferramenta você usaria em produção e por quê.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-3-codificacao-e-pipeline/exercicio-10-one-hot/one_hot.py
```
A solução de referência está em `one_hot.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
(597, 15) -> (597, 23)
soma por linha: [1]
['tipo_Apartamento', 'tipo_Casa', 'tipo_Cobertura', 'tipo_Studio']
[[0. 1. 0. 0.]
 [0. 0. 0. 0.]]
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que remover uma categoria não perde informação?
- O que aconteceria com `get_dummies` se os dados novos não tivessem todos os tipos?

## Dicas
- `sparse_output=False` devolve um array comum.
- A linha de zeros significa 'categoria desconhecida'.
