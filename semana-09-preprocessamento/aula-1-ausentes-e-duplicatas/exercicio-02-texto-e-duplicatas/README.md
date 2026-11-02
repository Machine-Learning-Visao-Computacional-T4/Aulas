# Exercício 02: Padronizar texto e remover duplicatas

**Tipo:** Guiado

## Objetivo
Perceber que duplicatas só aparecem depois de padronizar o texto e que o identificador não entra na comparação.

## O que fazer
1. Conte as duplicatas completas em `arquivos/imoveis_bruto.csv` (com todas as colunas).
2. Padronize `bairro` com `str.strip().str.title()` e mostre os valores distintos antes e depois.
3. Conte as duplicatas ignorando `id_anuncio` e remova-as com `drop_duplicates(subset=...)`.
4. Mostre quantas linhas sobraram.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-1-ausentes-e-duplicatas/exercicio-02-texto-e-duplicatas/texto_e_duplicatas.py
```
A solução de referência está em `texto_e_duplicatas.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
duplicadas (todas as colunas): 15
bairros antes: 25
bairros depois: 8
duplicadas (sem o id): 23
623 -> 600
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que o `duplicated()` completo não achou nada, ou achou menos do que o esperado?
- Que risco existe em remover duplicatas depois de calcular a média de uma coluna?

## Dicas
- O id é diferente em cada anúncio: por isso ele fica fora do `subset`.
- Use `keep='first'` (padrão) para manter a primeira ocorrência.
