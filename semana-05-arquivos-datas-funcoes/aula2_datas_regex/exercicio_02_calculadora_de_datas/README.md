# Exercício 02 — Mãos à obra + commit: calculadora de datas

**Tipo:** prática + commit · 18 min

## Objetivo
Praticar **criação, conversão e cálculo de datas** e versionar o resultado.

## O que fazer
1. Crie `datas.py` que pede (`input`) uma **data de nascimento** no formato `dd/mm/aaaa` e converte com `strptime`.
2. Calcule e exiba a **idade em anos** (aproximada, dividindo os dias por 365) e o **dia da semana** em que a pessoa nasceu.
3. Calcule **quantos dias faltam para o próximo Natal**.
4. Commit com mensagem descritiva e push para o GitHub.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_datas_regex/exercicio_02_calculadora_de_datas/datas.py
```

No Windows, se `python` não funcionar, use `py aula2_datas_regex/exercicio_02_calculadora_de_datas/datas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `datas.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Data de nascimento (dd/mm/aaaa): 15/03/1990
Você tem aproximadamente 36 anos.
Você nasceu em uma quinta-feira.
Faltam 80 dias para o próximo Natal.
```

(Os valores digitados no exemplo acima foram: `15/03/1990`.)

## Dicas e erros comuns
- O formato de `strptime` é `"%d/%m/%Y"` (dia, mês, **ano com 4 dígitos** = `%Y` maiúsculo).
- `weekday()` devolve um número de 0 (segunda) a 6 (domingo): use um **dicionário** de 7 nomes para traduzir (reaproveita a Semana 04).
- Subtrair duas datas devolve um objeto com `.days`.
- Idade, dias para o Natal e a data de hoje mudam com o tempo: o exemplo acima foi gerado em uma data específica.
