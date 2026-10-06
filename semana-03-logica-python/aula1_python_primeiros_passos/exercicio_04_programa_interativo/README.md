# Exercício 04 — Mãos à obra: seu primeiro programa interativo

**Tipo:** prática · primeiro programa "completo"

## Objetivo
Escrever um pequeno programa que **lê dados do usuário, converte tipos corretamente e produz uma saída personalizada**.

## O que fazer
1. Peça (com `input()`) o **nome** e o **ano de nascimento** da pessoa.
2. Converta o ano de nascimento para número com `int()`.
3. Calcule a **idade aproximada** (ano atual − ano de nascimento) e guarde em uma variável.
4. Exiba uma frase final juntando o nome e a idade calculada, usando `print()`.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_python_primeiros_passos/exercicio_04_programa_interativo/idade.py
```

No Windows, se `python` não funcionar, use `py aula1_python_primeiros_passos/exercicio_04_programa_interativo/idade.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `idade.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Qual é o seu nome? Ana
Em que ano você nasceu? 2000
Olá, Ana! Você tem aproximadamente 26 anos.
```

(Os valores digitados no exemplo acima foram: `Ana`, `2000`.)

## Dicas e erros comuns
- `input()` **sempre devolve texto**, mesmo se você digitar só números. Por isso é preciso `int()` antes de fazer conta.
- O exemplo calcula a idade com o ano atual do seu computador, então o número muda com o tempo.
