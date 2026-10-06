# Exercício 01 — Instalando o Python

**Tipo:** instalação

## Objetivo
Instalar o Python no computador com a configuração correta de **PATH**.

## Passo a passo (Windows)
1. Acesse [python.org/downloads](https://www.python.org/downloads/) e baixe a versão mais recente para o seu sistema.
2. Ao abrir o instalador, **marque a caixa "Add Python to PATH" ANTES de clicar em instalar**. Esse passo é essencial.
3. Finalize a instalação com as opções padrão.
4. Abra um terminal (ou o **Git Bash** instalado na aula passada) e digite:
   ```bash
   python --version
   pip --version
   ```
   Os dois comandos devem mostrar um número de versão.

## Se `python` não for reconhecido
- No Windows, tente `py --version`.
- Se também não funcionar, provavelmente a caixa **Add Python to PATH** ficou desmarcada: execute o instalador de novo, escolha **Modify** e marque a opção (ou reinstale).

## macOS e Linux
- Use `python3 --version` e `pip3 --version`. No Linux, se faltar: `sudo apt install python3 python3-pip`.

## Para que serve o pip?
O `pip` instala bibliotecas Python (por exemplo, `pip install pandas`). O nome é um acrônimo recursivo: *Pip Installs Packages*.
