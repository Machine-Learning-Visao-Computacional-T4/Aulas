# Exercício 02 — Mãos à obra + commit: boletim a partir de um CSV

**Tipo:** prática + commit · 18 min

## Objetivo
Ler um CSV, **converter tipos**, aplicar condicionais e **gravar um novo CSV** com o resultado.

## O que fazer
1. Crie `notas.csv` com **5 alunos fictícios** (`nome,nota1,nota2`). Há um exemplo pronto nesta pasta.
2. Com `DictReader`, calcule a **média** de cada aluno e classifique como **Aprovado** (>= 7) ou **Reprovado**.
3. Grave `resultado.csv` com as colunas `nome`, `media` e `situacao` usando `DictWriter`.
4. Commit e push. Use **SOMENTE dados fictícios** no repositório.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_arquivos_texto_csv_json/exercicio_02_boletim_a_partir_de_um_csv/boletim.py
```

No Windows, se `python` não funcionar, use `py aula1_arquivos_texto_csv_json/exercicio_02_boletim_a_partir_de_um_csv/boletim.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `boletim.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Ana | 8.75 | Aprovado
Elisa | 8.75 | Aprovado
Carla | 7.25 | Aprovado
Bruno | 5.75 | Reprovado
Diego | 5.25 | Reprovado
Arquivo resultado.csv gravado.
```

## Dicas e erros comuns
- Tudo que vem de um CSV é **texto**: converta com `float()` antes de calcular.
- `newline=""` ao abrir evita linhas em branco extras no Windows.
- O arquivo `notas.csv` deve estar na mesma pasta do script (o script já procura nela).
- Extra: o exemplo ordena o resultado pela média. Remova a linha do `sort` se quiser manter a ordem original.
