# Exercício 01 — Mãos à obra + commit: seu diário em texto

**Tipo:** prática + commit · 15 min

## Objetivo
Praticar **escrita, acréscimo e leitura** de arquivo de texto e versionar o resultado.

## O que fazer
1. Crie `diario.py` que **grava 3 frases** em `diario.txt` (modo `"w"`).
2. Rode o programa de novo trocando para o modo `"a"` e **acrescente mais 2 frases**.
3. Leia o arquivo e **imprima cada linha numerada** (dica: `enumerate` ou um contador).
4. Commit (mensagem descritiva) e push; confira no GitHub que `diario.py` e `diario.txt` apareceram.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_arquivos_texto_csv_json/exercicio_01_seu_diario_em_texto/diario.py
```

No Windows, se `python` não funcionar, use `py aula1_arquivos_texto_csv_json/exercicio_01_seu_diario_em_texto/diario.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `diario.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
1 Hoje comecei a trabalhar com arquivos.
2 Aprendi que o modo w apaga o conteúdo anterior.
3 Estou gostando de ver meus dados virarem arquivos.
4 Agora estou acrescentando com o modo a.
5 O diário já tem cinco linhas.
```

## Dicas e erros comuns
- **Experimento:** rode duas vezes o trecho do modo `"w"`. O conteúdo anterior some: é a melhor demonstração da diferença entre `"w"` (apaga) e `"a"` (acrescenta).
- Sempre informe `encoding="utf-8"` para os acentos funcionarem sem dor de cabeça.
- O `with` fecha o arquivo sozinho ao terminar o bloco.
- No exemplo, as duas etapas de escrita estão no mesmo arquivo para você ver o resultado de uma vez. No exercício da aula, você pode separar em duas execuções.
