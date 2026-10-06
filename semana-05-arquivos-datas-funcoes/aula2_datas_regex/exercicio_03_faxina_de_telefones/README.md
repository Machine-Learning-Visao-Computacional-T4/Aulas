# Exercício 03 — Mãos à obra + commit: faxina de telefones

**Tipo:** prática + commit · 15 min

## Objetivo
Usar `re.sub` e `re.fullmatch` para **padronizar e validar telefones** de um arquivo.

## O que fazer
1. Crie `contatos.csv` **fictício** com 5 linhas e telefones em formatos variados: `(48) 99999-1234`, `48 98888 5678`, `48-97777-0000`... (há um exemplo pronto nesta pasta).
2. Para cada linha, **remova tudo que não for dígito** com `re.sub`.
3. Valide com `re.fullmatch` se o resultado tem **11 dígitos**; imprima `válido` ou `inválido` ao lado.
4. Commit e push (**só dados fictícios!**).

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_datas_regex/exercicio_03_faxina_de_telefones/faxina_telefones.py
```

No Windows, se `python` não funcionar, use `py aula2_datas_regex/exercicio_03_faxina_de_telefones/faxina_telefones.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `faxina_telefones.py` em uma célula e execute com `Shift + Enter`. Quando o programa usar `input()`, uma caixa de texto aparece logo abaixo da célula para você digitar.

## Exemplo de execução

```text
Ana Souza | (48) 99999-1234 -> 48999991234 | válido
Bruno Lima | 48 98888 5678 -> 48988885678 | válido
Carla Dias | 48-97777-0000 -> 48977770000 | válido
Diego Alves | (48) 3333-4444 -> 4833334444 | inválido
Elisa Rocha | 48996665555 -> 48996665555 | válido
```

## Dicas e erros comuns
- `\D` (D maiúsculo) casa **qualquer coisa que não seja dígito**; `\d` (minúsculo) casa um dígito.
- O arquivo de exemplo traz de propósito um telefone com **10 dígitos** (fixo) para você ver o `inválido` acontecer.
- Use sempre **string crua** para regex: `r"\D"`, com o `r` antes das aspas.
