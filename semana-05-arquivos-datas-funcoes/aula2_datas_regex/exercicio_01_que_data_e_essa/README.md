# Exercício 01 — Que data é essa?

**Tipo:** dinâmica de abertura · 8 min

## Objetivo
Mostrar, **sem código**, por que datas são uma fonte clássica de erro em dados. (Depois, veja o problema acontecendo em código.)

## O que fazer
1. Leia esta data: **03/04/2025**. Que dia é esse? Responda: **3 de abril** ou **4 de março**?
2. Veja quantas pessoas da turma responderam cada opção.
3. No Brasil se escreve **dia/mês/ano**; nos Estados Unidos, **mês/dia/ano**. **Um arquivo não avisa qual padrão usa.**
4. Pense: o que pode dar errado ao **juntar planilhas de dois países**?
5. Rode o script para ver as duas leituras acontecendo.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_datas_regex/exercicio_01_que_data_e_essa/datas_ambiguas.py
```

No Windows, se `python` não funcionar, use `py aula2_datas_regex/exercicio_01_que_data_e_essa/datas_ambiguas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `datas_ambiguas.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Lendo como dia/mês/ano (Brasil): 03 de April de 2025
Lendo como mês/dia/ano (EUA):    04 de March de 2025

Em ordem de texto, o formato AAAA-MM-DD ordena corretamente:
2025-04-03 < 2025-12-01
```

## Dicas e erros comuns
- Por isso, em projetos de dados, padronize datas para **AAAA-MM-DD**: é o único formato que ordena corretamente mesmo como texto.
- Os nomes dos meses saem em inglês se o seu sistema estiver em inglês. Isso não afeta o aprendizado.
