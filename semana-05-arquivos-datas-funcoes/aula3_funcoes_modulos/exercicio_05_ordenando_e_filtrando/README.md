# Exercício 05 — Mãos à obra + commit: ordenando e filtrando

**Tipo:** prática + commit · 15 min

## Objetivo
Usar `lambda` com `sorted` e `filter` sobre uma **lista de dicionários**.

## O que fazer
1. Crie `lambdas.py` com uma lista de **5 alunos fictícios**, cada um um dicionário com `nome` e `nota`.
2. Ordene do **maior para o menor** pela nota usando `sorted` com `key=lambda` e `reverse=True`.
3. Use `filter` com `lambda` para listar **só os alunos com nota >= 7** e imprima os nomes.
4. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_funcoes_modulos/exercicio_05_ordenando_e_filtrando/lambdas.py
```

No Windows, se `python` não funcionar, use `py aula3_funcoes_modulos/exercicio_05_ordenando_e_filtrando/lambdas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `lambdas.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Do maior para o menor:
- Ana 9.0
- Elisa 8.2
- Carla 7.0
- Bruno 6.5
- Diego 5.5
Aprovados: ['Ana', 'Carla', 'Elisa']
```

## Dicas e erros comuns
- `lambda aluno: aluno["nota"]` é uma função pequena e sem nome: recebe um aluno e devolve a nota.
- `filter` devolve um objeto "preguiçoso": envolva com `list(...)` para ver o resultado.
- Combina listas de dicionários (Semana 04) com `lambda`.
