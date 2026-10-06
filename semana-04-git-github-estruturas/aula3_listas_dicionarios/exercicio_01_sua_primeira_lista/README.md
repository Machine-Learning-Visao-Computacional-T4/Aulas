# Exercício 01 — Mãos à obra + commit: sua primeira lista

**Tipo:** prática + commit · 15 min

## Objetivo
Praticar criação e manipulação de **listas** e já fazer o primeiro commit da aula.

## O que fazer
1. Crie um arquivo `listas.py` com uma lista de **pelo menos 5 itens favoritos**.
2. Use `append()` para adicionar um item, `remove()` ou `pop()` para remover outro, e `sort()` para ordenar.
3. Imprima a lista **em cada etapa**, para ver as mudanças acontecendo.
4. Commit (mensagem: `Adiciona exercício de listas`) e push para o GitHub.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_listas_dicionarios/exercicio_01_sua_primeira_lista/listas.py
```

No Windows, se `python` não funcionar, use `py aula3_listas_dicionarios/exercicio_01_sua_primeira_lista/listas.py`.

## Exemplo de execução

```text
Lista inicial: ['pizza', 'violão', 'praia', 'cinema', 'café']
Depois do append: ['pizza', 'violão', 'praia', 'cinema', 'café', 'livros']
Depois do remove: ['pizza', 'violão', 'praia', 'café', 'livros']
pop removeu: livros
Depois do pop: ['pizza', 'violão', 'praia', 'café']
Depois do sort: ['café', 'pizza', 'praia', 'violão']
Primeiro item (índice 0): café
```

## Dicas e erros comuns
- O índice começa em **0**: o primeiro item é `lista[0]`. Vale para praticamente todas as linguagens.
- `remove("x")` apaga pelo **valor**; `pop()` apaga por **posição** (o último, se não disser qual) e devolve o item.
- Commits **pequenos e frequentes** são o hábito profissional: um commit por exercício.
