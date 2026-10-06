# Exercício 07 — Criando sua primeira branch

**Tipo:** prática

## Objetivo
Criar uma **branch**, fazer uma mudança nela e **observar como ela fica isolada** da `main`.

## Passo a passo (GitHub Desktop)
1. Clique em **Current branch → New branch** e nomeie como `teste-de-branch`.
2. Com a nova branch ativa, edite o `README.md` adicionando uma linha nova e salve.
3. Faça o commit (**Commit to teste-de-branch**).
4. Volte para a `main` (**Current branch → main**) e **observe**: a mudança que você fez **não aparece** mais no arquivo.

O passo 4 é o mais importante: o "sumiço" mostra que cada branch é uma linha de trabalho separada.

## O mesmo pelo terminal
```bash
git switch -c teste-de-branch    # cria a branch e já vai para ela
# (edite o README.md e salve)
git add README.md
git commit -m "Adiciona linha de teste na branch"

git switch main                  # volta para a main: a linha some do arquivo
git switch teste-de-branch       # volta para a branch: a linha reaparece
```

(Em versões antigas do Git, use `git checkout -b teste-de-branch` e `git checkout main`.)

## Extra (opcional): trazendo a mudança para a main
```bash
git switch main
git merge teste-de-branch        # "dar merge" = juntar a branch na main
```

## Para pensar
- Por que criar uma branch separada **antes** de testar uma ideia arriscada?
- O que significa "dar merge"? E se dois colegas mudarem a mesma linha (conflito)? Conflito é normal, não é motivo de pânico.
