# Exercício 07 — Verificador de ano bissexto

**Tipo:** prática + versionamento

## Objetivo
Praticar condicionais em um problema novo e **repetir o fluxo completo de versionamento**.

## O que fazer
1. Crie um arquivo `bissexto.py`.
2. Peça (`input()`) um ano e determine se é bissexto. Regra: **divisível por 4 E (não divisível por 100 OU divisível por 400)**.
3. Exiba o resultado com uma mensagem clara.
4. Faça **commit** (mensagem descritiva) e **push**. Confira no navegador se o arquivo apareceu no repositório.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_python_local_vscode/exercicio_07_verificador_de_ano_bissexto/bissexto.py
```

No Windows, se `python` não funcionar, use `py aula2_python_local_vscode/exercicio_07_verificador_de_ano_bissexto/bissexto.py`.

## Exemplo de execução

```text
Digite um ano: 2024
2024 é um ano bissexto.
```

(Os valores digitados no exemplo acima foram: `2024`.)

## Dicas e erros comuns
- Teste com `2000` (bissexto), `1900` (não), `2024` (sim) e `2023` (não). Se os quatro baterem, a regra está certa.
- A condição composta com `and`/`or` é a parte mais difícil: use parênteses.
