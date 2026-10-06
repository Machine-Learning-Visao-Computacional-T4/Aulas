# Exercício 03 — Mãos à obra + commit: cadastro em JSON

**Tipo:** prática + commit · 15 min

## Objetivo
Gravar e ler uma **lista de dicionários em JSON**, aplicando filtros com `for` e `if`.

## O que fazer
1. Crie uma lista com **4 contatos fictícios** (`nome`, `telefone`, `cidade`) como dicionários.
2. Grave a lista em `contatos.json` com `json.dump` (`indent=2`, `ensure_ascii=False`).
3. Leia o arquivo de volta e imprima **apenas os contatos de uma cidade** escolhida.
4. Commit e push; abra `contatos.json` no GitHub e veja como ele é exibido.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_arquivos_texto_csv_json/exercicio_03_cadastro_em_json/cadastro_json.py
```

No Windows, se `python` não funcionar, use `py aula1_arquivos_texto_csv_json/exercicio_03_cadastro_em_json/cadastro_json.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `cadastro_json.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Mostrar contatos de qual cidade? Florianópolis
Ana Souza | 48999991111
Diego Alves | 48966664444
```

(Os valores digitados no exemplo acima foram: `Florianópolis`.)

## Dicas e erros comuns
- Retoma o projeto de agenda de contatos da Semana 04, agora com **persistência em arquivo**.
- `json.dump` grava em arquivo; `json.dumps` devolve um texto. `json.load` lê de arquivo; `json.loads` lê de texto.
- Sem `ensure_ascii=False`, os acentos viram `\u00e3` etc. dentro do arquivo.
