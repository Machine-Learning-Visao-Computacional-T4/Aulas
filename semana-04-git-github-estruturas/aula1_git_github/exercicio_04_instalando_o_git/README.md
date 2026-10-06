# Exercício 04 — Instalando o Git (Git Bash)

**Tipo:** instalação

## Objetivo
Instalar o **Git** no computador, habilitando comandos Git pelo terminal.

## Passo a passo (Windows)
1. Acesse [git-scm.com/downloads](https://git-scm.com/downloads) e baixe a versão para o seu sistema operacional.
2. Execute o instalador **aceitando as opções padrão** (não precisa mudar nada, a menos que seja instruído).
3. Ao final, procure e abra o programa **Git Bash**.
4. Digite e aperte Enter:
   ```bash
   git --version
   ```
   Se aparecer um número de versão (algo como `git version 2.x.x`), a instalação funcionou.

## macOS e Linux
- **macOS:** abra o Terminal e digite `git --version`. Se o Git não estiver instalado, o sistema oferece instalar as ferramentas de linha de comando.
- **Linux (Debian/Ubuntu):** `sudo apt install git`.

## Configure seu nome e e-mail (uma única vez)
O Git registra quem fez cada alteração. Use o mesmo e-mail da sua conta do GitHub:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

Para conferir: `git config --global --list`.

## Problemas comuns
- Este costuma ser o passo mais sensível a diferenças de sistema operacional. Se travar, peça ajuda com a mensagem de erro em mãos.
