# Exercício 02 — Mãos à obra + commit: suas primeiras funções

**Tipo:** prática + commit · 15 min

## Objetivo
Transformar códigos **já feitos** em funções reutilizáveis. O objetivo é só **empacotar** o que você já resolveu.

## O que fazer
1. Crie `funcoes.py` com uma função `e_bissexto(ano)` e uma função `calcular_imc(peso, altura)`, **ambas com docstring**.
2. Chame cada uma **pelo menos duas vezes**, com valores diferentes, e imprima os resultados.
3. Teste `e_bissexto` com **2000, 1900, 2024 e 2023**.
4. Commit e push no GitHub.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_funcoes_modulos/exercicio_02_suas_primeiras_funcoes/funcoes.py
```

No Windows, se `python` não funcionar, use `py aula3_funcoes_modulos/exercicio_02_suas_primeiras_funcoes/funcoes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `funcoes.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
2000 é bissexto? True
1900 é bissexto? False
2024 é bissexto? True
2023 é bissexto? False
IMC de 70 kg e 1,75 m: 22.9
IMC de 90 kg e 1,80 m: 27.8
```

## Dicas e erros comuns
- A **docstring** é a string entre aspas triplas logo abaixo do `def`; ela aparece em `help(e_bissexto)`.
- Resultado esperado de `e_bissexto`: 2000 → `True`, 1900 → `False`, 2024 → `True`, 2023 → `False`.
- Funções devolvem valores com `return`. Quem imprime é quem chama.
