# Exercício 05 — Exercício final: faxina em um dataset sujo

**Tipo:** mini-projeto de limpeza · 20 min · entrega via Git

## Objetivo
Aplicar **arquivos, datas e regex** em um mini-projeto de limpeza, entregue via Git.

## O que fazer
1. Crie `sujo.csv` **fictício** com 6 linhas e colunas `nome`, `telefone` e `data` (datas em `dd/mm/aaaa`, nomes com espaços extras e caixa irregular, telefones em formatos variados). Há um exemplo pronto nesta pasta.
2. Escreva `faxina.py` que lê o CSV, **padroniza** nome (Title Case), telefone (só dígitos) e data (`AAAA-MM-DD`) e grava `limpo.csv` com `DictWriter`.
3. Marque como **"inválido"** qualquer linha cujo telefone **não tenha 11 dígitos**.
4. Commit, push e (opcional) Pull Request em uma **branch própria**.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_datas_regex/exercicio_05_faxina_dataset_sujo/faxina.py
```

No Windows, se `python` não funcionar, use `py aula2_datas_regex/exercicio_05_faxina_dataset_sujo/faxina.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `faxina.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

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
- `" ".join(nome.split())` colapsa espaços repetidos e tira os das pontas; depois `.title()` padroniza a caixa.
- O exemplo traz de propósito um telefone fixo (10 dígitos) e um com `+55` (13 dígitos): ambos viram `inválido`.
- Guarde o `faxina.py`: na **Aula 3** você vai transformá-lo em funções e em um módulo.
- Use só dados fictícios no repositório.
