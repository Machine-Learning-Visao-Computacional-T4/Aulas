# Exercício 08: Final da Aula 2: função preparar_numericos

**Tipo:** Final, com Git e Pull Request

## Objetivo
Entregar uma função que trata os erros e marca atípicos reais, salvando o arquivo tratado.

## O que fazer
1. Crie a branch `feature/preparar-numericos`.
2. Crie `numericos.py` com `limites_iqr` e `preparar_numericos(caminho)`.
3. A função remove os erros (`area_m2 > 2000`, `preco < 10000`, `quartos > 10`), cria `preco_atipico` pelo IQR e salva `arquivos/imoveis_tratado.csv`.
4. No final do arquivo, imprima quantas linhas entraram, quantas saíram e quantos preços atípicos restaram.
5. Resultado esperado: 600 para 597 linhas.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-2-outliers-e-escalas/exercicio-08-final-preparar-numericos/numericos.py
```
A solução de referência está em `numericos.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
600 -> 597
24 preços atípicos mantidos
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que o preço atípico foi marcado e não removido?
- Qual é o risco de usar a coluna `preco_atipico` como entrada de um modelo que prevê o preço?

## Dicas
- O filtro de erros usa `~erros` para ficar com as linhas boas.
- Use `.copy()` depois de filtrar para evitar avisos.

## Git deste exercício
```bash
git checkout -b feature/preparar-numericos
git add numericos.py arquivos/imoveis_tratado.csv
git commit -m "feat: função preparar_numericos"
git push -u origin feature/preparar-numericos
```
Abra o Pull Request para a `main` pelo GitHub e descreva em duas frases o que a função faz e quais números você conferiu.
