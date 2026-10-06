# Exercício 07 — Exercício final do módulo: refatorando a faxina

**Tipo:** projeto integrador · 25 min · branch + Pull Request

## Objetivo
Reorganizar o `faxina.py` da Aula 2 em **funções e módulos**, entregando via **branch e Pull Request**. Arquivos, datas, regex, funções, módulos e Git no mesmo exercício.

## O que fazer
1. Crie a branch `feature/refatoracao-faxina`.
2. Mova a lógica de limpeza para `limpeza.py`, com **funções para nome, telefone e data** (com docstrings) e um bloco `if __name__ == "__main__":` de teste.
3. Reescreva `faxina.py` para **importar `limpeza`**, ler `sujo.csv` e gravar `limpo.csv`.
4. Escreva um **`README.md` curto** explicando como rodar; commit, push e abra um **Pull Request** para a `main`.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_funcoes_modulos/exercicio_07_refatorando_a_faxina/faxina.py
```

No Windows, se `python` não funcionar, use `py aula3_funcoes_modulos/exercicio_07_refatorando_a_faxina/faxina.py`.

## Exemplo de execução

```text
Ana Souza | 48999991234 | 2025-03-05 | válido
Bruno Lima | 48988885678 | 2025-03-18 | válido
Carla Dias | 48977770000 | 2025-04-02 | válido
Diego Alves | 4833334444 | 2025-04-30 | inválido
Elisa Rocha | 48996665555 | 2025-05-15 | válido
Fernando Costa | 5548991112222 | 2025-06-01 | inválido
Arquivo limpo.csv gravado.
```

## Dicas e erros comuns
- O resultado deve ser **idêntico** ao do Exercício 05 da Aula 2: refatorar muda a organização, não o comportamento.
- Se aparecer `ModuleNotFoundError: No module named 'limpeza'`, confira se `limpeza.py` e `faxina.py` estão na mesma pasta.
- Rode `limpeza.py` sozinho para testar as funções antes de usá-las no `faxina.py`.

## Testando o módulo de limpeza
```bash
python aula3_funcoes_modulos/exercicio_07_refatorando_a_faxina/limpeza.py
```
Deve imprimir: `Todos os testes de limpeza.py passaram.`

## Exemplo de README para o seu projeto
```markdown
# Faxina de dados

Lê `sujo.csv` e grava `limpo.csv` com nome, telefone e data padronizados.

## Como rodar
    python faxina.py

## Arquivos
- `faxina.py`: lê o CSV, usa as funções e grava o resultado
- `limpeza.py`: funções de limpeza (nome, telefone, data)
- `sujo.csv`: dados fictícios de entrada
```

## Estrutura de um projeto organizado
```text
meu-projeto/
|-- main.py
|-- limpeza.py
|-- dados/
|   `-- sujo.csv
|-- requirements.txt
|-- .gitignore
`-- README.md
```
Código em módulos, dados em uma pasta própria, dependências listadas, README explicando o projeto e `.gitignore` protegendo o que não deve subir: esse é o formato ideal de um repositório no GitHub.

## Git deste exercício
```bash
git switch -c feature/refatoracao-faxina
git add limpeza.py faxina.py README.md
git commit -m "Refatora a faxina em funções e módulo"
git push -u origin feature/refatoracao-faxina
```
Depois, no GitHub, **Compare & pull request** → descreva a mudança → **Create pull request**.
