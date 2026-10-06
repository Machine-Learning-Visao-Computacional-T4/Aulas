# Exercício 08 — Dê o próximo comando

**Tipo:** leitura de `git status` + decisão

## Objetivo
Ler a saída de um `git status` e decidir **qual comando (ou botão) vem a seguir** no fluxo. `git status` é sempre um bom primeiro passo quando há dúvida.

## O que fazer
Para cada uma das 4 situações, escreva qual comando resolveria aquele passo. Depois confira.

### Situação 1
```text
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	ola.py

nothing added to commit but untracked files present (use "git add" to track)
```

### Situação 2
```text
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   ola.py

```

### Situação 3
```text
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

### Situação 4
```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

<details>
<summary>Ver respostas</summary>

1. O arquivo é novo e ainda não está no próximo commit: `git add ola.py` (ou o **+** no VS Code).
2. O arquivo está preparado (*staged*): `git commit -m "Adiciona ola.py"`.
3. O commit existe só no seu computador: `git push` (ou **Sync Changes**).
4. Não há nada a fazer: tudo está commitado e enviado. Crie ou altere algo, ou rode `git pull` para trazer novidades do GitHub.

</details>

> Estas 4 saídas foram geradas com o Git 2.43 e escolhidas para este repositório; as situações usadas na aula (em um quadro colaborativo) podem ser outras.
