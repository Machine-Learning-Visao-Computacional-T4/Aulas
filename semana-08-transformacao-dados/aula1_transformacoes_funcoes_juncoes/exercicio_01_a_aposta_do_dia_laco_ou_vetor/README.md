# Exercício 01 — A aposta do dia: laço ou vetor?

**Tipo:** dinâmica de abertura + script · 8 min

## Objetivo
Formar uma expectativa sobre desempenho **antes** de aprender as ferramentas e conferir o resultado depois.

## O que fazer
1. Leia o script: ele dobra a coluna `qtd` de uma tabela de cerca de 100 mil linhas de duas formas, `apply` linha a linha (`axis=1`) e operação direta na coluna.
2. **Aposte antes de rodar:** A) a diferença é de uns 2 vezes; B) uns 10 vezes; C) 100 vezes ou mais.
3. Rode o script e confira a aposta.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_01_a_aposta_do_dia_laco_ou_vetor/medir_tempo.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_01_a_aposta_do_dia_laco_ou_vetor/medir_tempo.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `medir_tempo.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`); veja o [guia](../../docs/guia_transformacoes.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
103050 linhas
apply(axis=1): 0.47s | vetorizado: 0.0008s
O vetorizado foi cerca de 583 vezes mais rápido
Mesmo resultado? True
```

Os tempos mudam de computador para computador, mas a ordem de grandeza se mantém: o vetorizado ganha por muito.

## Para pensar
- Por que o `apply(axis=1)` é tão mais lento? (Pense em quantas vezes o Python precisa chamar a função.)
- Em que situação você ainda usaria `apply`?

## Dicas e erros comuns
- Regra prática: primeiro operação vetorizada, depois `.str` e `.dt`, depois `map` e só por último `apply`.
