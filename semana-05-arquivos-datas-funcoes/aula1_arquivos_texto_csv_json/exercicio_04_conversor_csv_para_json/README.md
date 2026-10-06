# Exercício 04 — Exercício final: conversor CSV para JSON

**Tipo:** projeto integrador · 20 min · branch + Pull Request

## Objetivo
Consolidar a aula criando um **conversor de formatos** e entregando via **branch e Pull Request**.

## O que fazer
1. Crie a branch `feature/conversor-csv-json` no seu repositório.
2. Escreva `conversor.py`: lê `notas.csv` (ou outro CSV fictício), **converte as notas para número** e grava `dados.json`.
3. **Opcional:** aceite o nome do arquivo via `input()`.
4. Commit, push da branch e abra um **Pull Request** para a `main`, descrevendo o que o programa faz.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_arquivos_texto_csv_json/exercicio_04_conversor_csv_para_json/conversor.py
```

No Windows, se `python` não funcionar, use `py aula1_arquivos_texto_csv_json/exercicio_04_conversor_csv_para_json/conversor.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `conversor.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Arquivo CSV (Enter para notas.csv): 
5 registros convertidos para dados.json
```

(Os valores digitados no exemplo acima foram: ``.)

## Dicas e erros comuns
- Sem `float()`, as notas ficam como texto no JSON (`"8.5"` entre aspas). Confira o `dados.json`.
- Para ler outro CSV, coloque-o na mesma pasta e digite o nome quando o programa perguntar.

## Git deste exercício
```bash
git switch -c feature/conversor-csv-json
git add conversor.py notas.csv
git commit -m "Adiciona conversor de CSV para JSON"
git push -u origin feature/conversor-csv-json
```
Depois, no GitHub: **Compare & pull request** → descreva o que o programa faz → **Create pull request**.
