# Exercício 11: ColumnTransformer e Pipeline

**Tipo:** Guiado

## Objetivo
Montar o fluxo completo e avaliar sem vazamento.

## O que fazer
1. Leia `arquivos/imoveis_tratado.csv` e separe `X` (sem `preco`, `id_anuncio` e `preco_atipico`) e `y` (`log1p` do preço).
2. Divida em treino e teste (80/20, `random_state=42`).
3. Monte um `ColumnTransformer` com `StandardScaler`, `OrdinalEncoder` (condição), `OneHotEncoder` (tipo e bairro) e as binárias.
4. Ajuste no treino, transforme o teste e mostre os shapes. Depois encadeie com `LinearRegression` em um `Pipeline` e mostre o R² do teste.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-3-codificacao-e-pipeline/exercicio-11-pipeline/pipeline.py
```
A solução de referência está em `pipeline.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
(477, 12) (120, 12)
(477, 22) | (120, 22)
R2 no teste: 0.911
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que `preco_atipico` fica fora de `X`?
- O que muda se usarmos `fit_transform` também no teste?

## Dicas
- Cada tupla do `ColumnTransformer` é (nome, transformador, colunas).
- `get_feature_names_out()` mostra o nome de cada coluna de saída.
