# Exercício 01: Diagnóstico de ausentes

**Tipo:** Guiado

## Objetivo
Descobrir onde estão os ausentes, inclusive os disfarçados, antes de decidir o que fazer com eles.

## O que fazer
1. Leia `arquivos/imoveis_bruto.csv` sem nenhum tratamento e mostre o shape.
2. Liste as colunas numéricas que vieram como texto (dtype object) e investigue com `value_counts`.
3. Releia o arquivo com `na_values=['N/D', '?', 's/i']` e troque o -1 de `idade_anos` por NaN.
4. Mostre a contagem de ausentes por coluna e a porcentagem de `idade_anos` ausente por tipo de imóvel.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-1-ausentes-e-duplicatas/exercicio-01-diagnostico-de-ausentes/diagnostico_ausentes.py
```
A solução de referência está em `diagnostico_ausentes.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
shape: (623, 13)
colunas de texto: ['bairro', 'tipo', 'area_m2', 'condicao', 'aceita_pet', 'mobiliado']
str
area_m2               33
idade_anos            69
condicao              56
distancia_praia_km    20
dtype: int64
tipo
Apartamento     8.1
Casa           20.2
Cobertura       2.8
Studio          4.8
Name: idade_anos, dtype: float64
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que `isna().sum()` não encontrava os ausentes antes de usar `na_values`?
- Os ausentes de `idade_anos` parecem aleatórios ou dependem do tipo do imóvel? O que isso muda na escolha do preenchimento?

## Dicas
- `bruto['area_m2'].value_counts().head()` mostra o texto estranho que impede a coluna de ser número.
- O -1 é um ausente disfarçado: números negativos não fazem sentido para idade.
