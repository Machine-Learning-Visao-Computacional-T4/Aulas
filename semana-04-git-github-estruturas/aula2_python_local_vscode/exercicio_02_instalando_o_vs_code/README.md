# Exercício 02 — Instalando o VS Code e a extensão Python

**Tipo:** instalação

## Objetivo
Instalar o VS Code e habilitar suporte completo a Python pela extensão oficial.

## Passo a passo
1. Acesse [code.visualstudio.com](https://code.visualstudio.com) e baixe o instalador.
2. Execute o instalador aceitando as opções padrão.
3. Abra o VS Code, clique no ícone **Extensions** da barra lateral (ou `Ctrl + Shift + X`), procure por **Python** e instale a extensão **oficial da Microsoft**.
4. **Reinicie** o VS Code.

## Como saber que deu certo
Ao abrir um arquivo `.py`, aparece o botão ▶ (executar) no canto superior direito e o código ganha cores.

## Por que a extensão importa
Ela habilita o botão de execução, o realce de sintaxe e o autocompletar. Sem ela, o VS Code é só um editor de texto genérico.

## Notebook (Colab) × script (`.py`)
| | Notebook (Colab) | Script (`.py`) |
| --- | --- | --- |
| Execução | Célula por célula, na ordem que você mandar | O arquivo inteiro roda de uma vez, de cima a baixo |
| Resultado | Logo abaixo de cada célula | No terminal integrado, ao final |
| Melhor para | Explorar dados e testar ideias | Programas completos e reutilizáveis |

Um arquivo `.py` roda **inteiro** a cada execução: não dá para rodar "por partes" como num notebook.
