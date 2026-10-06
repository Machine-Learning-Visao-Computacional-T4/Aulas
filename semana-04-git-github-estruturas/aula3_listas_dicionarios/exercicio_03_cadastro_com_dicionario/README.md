# Exercício 03 — Mãos à obra + commit: cadastro simples com dicionário

**Tipo:** prática + commit · 15 min

## Objetivo
Praticar criação e manipulação de **dicionários** em um cenário realista.

## O que fazer
1. Crie um arquivo `cadastro.py` com um dicionário representando uma pessoa (**nome, idade, cidade, profissão**).
2. Use `update()` para adicionar um novo campo (por exemplo, e-mail) e imprima o dicionário completo.
3. Use um `for` com `.items()` para imprimir cada chave e valor em uma linha separada, no formato **`chave: valor`**.
4. Commit (mensagem descritiva) e push para o GitHub.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_listas_dicionarios/exercicio_03_cadastro_com_dicionario/cadastro.py
```

No Windows, se `python` não funcionar, use `py aula3_listas_dicionarios/exercicio_03_cadastro_com_dicionario/cadastro.py`.

## Exemplo de execução

```text
Dicionário completo: {'nome': 'Ana Souza', 'idade': 28, 'cidade': 'Florianópolis', 'profissao': 'Analista de dados', 'email': 'ana@exemplo.com'}
nome: Ana Souza
idade: 28
cidade: Florianópolis
profissao: Analista de dados
email: ana@exemplo.com
```

## Dicas e erros comuns
- Dicionário guarda dados por **chave** (`pessoa["cidade"]`), não por posição.
- Use **dados fictícios** em exercícios que vão para o GitHub público.
