# Exercício 04 — Mãos à obra + commit: mini banco de dados de alunos

**Tipo:** prática + commit · 18 min · o mais completo do bloco

## Objetivo
Construir e percorrer uma **estrutura composta** (lista de dicionários), aplicando tudo o que foi visto na aula.

## O que fazer
1. Crie um arquivo `banco_alunos.py` com uma **lista de pelo menos 4 dicionários**, cada um representando um aluno (**nome e nota**).
2. Use um `for` com `if` para imprimir **apenas os alunos aprovados** (nota >= 7).
3. Adicione um **contador** para exibir, ao final, quantos alunos foram aprovados no total.
4. Commit (mensagem descritiva) e push para o GitHub.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_listas_dicionarios/exercicio_04_mini_banco_de_dados_de_alunos/banco_alunos.py
```

No Windows, se `python` não funcionar, use `py aula3_listas_dicionarios/exercicio_04_mini_banco_de_dados_de_alunos/banco_alunos.py`.

## Exemplo de execução

```text
Alunos aprovados (nota >= 7):
- Ana | nota: 9.0
- Carla | nota: 7.0
- Elisa | nota: 8.2
Total de aprovados: 3
```

## Dicas e erros comuns
- Uma **lista de dicionários** é a forma como a maioria dos dados da internet (JSON) chega ao Python.
- Esqueceu de zerar o contador (`aprovados = 0`) **antes** do `for`? Dará erro.

## Você sabia?
O formato **JSON**, usado por sites, aplicativos e APIs para trocar dados, é estruturalmente quase idêntico às listas e dicionários do Python. Quando o Python lê um JSON, ele o transforma exatamente nessas estruturas. (Você vai fazer isso na Semana 05.)
