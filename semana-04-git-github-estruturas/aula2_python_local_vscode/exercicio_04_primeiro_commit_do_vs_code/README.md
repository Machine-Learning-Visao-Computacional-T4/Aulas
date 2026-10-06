# Exercício 04 — Seu primeiro commit direto do VS Code

**Tipo:** prática

## Objetivo
Completar o ciclo **editar → commit → push** sem sair do VS Code.

## O que fazer
1. Com o repositório aberto no VS Code, crie um novo arquivo chamado `ola.py` com um `print("Olá, mundo!")`.
2. Abra o painel de **Controle de Código-Fonte** (ícone de ramificação na barra lateral): o arquivo novo aparece na lista de mudanças.
3. Clique no **+** ao lado do arquivo (isso é o *stage*), escreva uma **mensagem de commit** e clique no ✓ (**Commit**).
4. Clique em **Sync Changes** (ou no botão de nuvem) para enviar (*push*) ao GitHub.
5. Confirme **no navegador** que `ola.py` apareceu no repositório.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_python_local_vscode/exercicio_04_primeiro_commit_do_vs_code/ola.py
```

No Windows, se `python` não funcionar, use `py aula2_python_local_vscode/exercicio_04_primeiro_commit_do_vs_code/ola.py`.

Ou clique no botão ▶ no canto superior direito do VS Code.

## Exemplo de execução

```text
Olá, mundo!
Este arquivo foi enviado ao GitHub direto do VS Code.
```

## Dicas e erros comuns
- O terminal integrado do VS Code abre com `Ctrl + '` (ou menu **Terminal → New Terminal**).
- Depois do `Commit`, o botão vira **Sync Changes**. É ele que envia ao GitHub.
