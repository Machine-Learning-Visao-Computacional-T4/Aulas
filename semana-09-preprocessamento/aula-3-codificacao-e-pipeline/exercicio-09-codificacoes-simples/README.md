# Exercício 09: Codificar binárias e ordinal

**Tipo:** Guiado

## Objetivo
Transformar colunas de texto com duas categorias e com ordem natural em números.

## O que fazer
1. Leia `arquivos/imoveis_tratado.csv` e liste as colunas de texto.
2. Converta `aceita_pet` e `mobiliado` para 0 e 1 com `map` e confira se algo ficou sem correspondência.
3. Crie `condicao_num` com a ordem Ruim, Regular, Bom e Ótimo.
4. Reproduza com `OrdinalEncoder(categories=...)` e compare.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-3-codificacao-e-pipeline/exercicio-09-codificacoes-simples/codificacoes_simples.py
```
A solução de referência está em `codificacoes_simples.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
['bairro', 'tipo', 'condicao', 'aceita_pet', 'mobiliado']
0 sem correspondência
map e OrdinalEncoder iguais: True
{0: 34, 1: 166, 2: 294, 3: 103}
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- O que acontece com o `map` se escrevermos 'Otimo' sem acento?
- Quando numerar uma ordinal pode ser uma má ideia?

## Dicas
- Confira os NaN logo depois do `map`.
- Sem `categories`, o scikit-learn usa a ordem alfabética.
