# Exercício 05: Detectar atípicos com IQR e regras do negócio

**Tipo:** Guiado

## Objetivo
Usar o IQR para suspeitar e uma regra de negócio para decidir.

## O que fazer
1. Leia `arquivos/imoveis_limpo.csv`.
2. Escreva `limites_iqr(serie, k=1.5)` e aplique a `area_m2`, `quartos`, `idade_anos` e `preco`.
3. Calcule `preco_m2` e liste os anúncios com `area_m2 > 600`, `preco < 50000` ou `quartos > 10`.
4. Defina como erro: `area_m2 > 2000`, `preco < 10000` ou `quartos > 10` e conte quantos são.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-2-outliers-e-escalas/exercicio-05-outliers-com-iqr/outliers_iqr.py
```
A solução de referência está em `outliers_iqr.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
area_m2       8 fora de [-56; 265]
quartos       1 fora de [-2; 6]
idade_anos   26 fora de [-10; 42]
preco        24 fora de [-376,250; 1,637,750]
     id_anuncio         tipo  area_m2  quartos      preco  preco_m2
46         3094    Cobertura    610.0        5  7800000.0   12787.0
110        3003         Casa  16100.0        3  1374000.0      85.0
537        3020         Casa    126.0       28   697000.0    5532.0
562        3002  Apartamento     37.0        1      244.0       7.0
3 anúncios com erro de digitação
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Todo valor fora do IQR é erro? Dê um exemplo dos dados.
- Por que o `preco_m2` ajuda a decidir?

## Dicas
- Compare o `preco_m2` do suspeito com a mediana da base.
- Um preço muito alto com área grande e bairro nobre pode ser real.
