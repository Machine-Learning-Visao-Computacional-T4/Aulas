# Exercício 02 — Mão na massa + commit: transformando colunas

**Tipo:** prática + commit · 18 min

## Objetivo
Aplicar `.dt`, `.str`, `map` e `apply` para limpar e enriquecer a tabela de pedidos.

## O que fazer
1. Crie `transformacoes.py`, importe o pandas e leia `pedidos.csv`.
2. Converta `data` com `to_datetime` e crie as colunas `mes` e `dia_semana` com o acessor `.dt`.
3. Padronize `canal` com `.str.strip().str.title()` e confira com `value_counts`: devem sobrar **3 canais**.
4. Crie a coluna `dia` (seg a dom) com `map` e a coluna `faixa_entrega` com uma função sua e `apply`.
5. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula1_transformacoes_funcoes_juncoes/exercicio_02_transformando_colunas/transformacoes.py
```

No Windows, se `python` não funcionar, use `py aula1_transformacoes_funcoes_juncoes/exercicio_02_transformando_colunas/transformacoes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `transformacoes.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`); veja o [guia](../../docs/guia_transformacoes.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
Canais antes: 9 grafias
canal
Balcão      309
App         253
Delivery    125
Name: count, dtype: int64
Dias sem correspondência: 0
        data  mes  dia_semana  dia
0 2025-01-01    1           2  qua
1 2025-01-02    1           3  qui
2 2025-01-03    1           4  sex
faixa_entrega
sem entrega    568
demorada        72
rápida          47
Name: count, dtype: int64
```

## Dicas e erros comuns
- `map` com chave inexistente vira `NaN` sem aviso: confira com `isna()` depois.
- O dia da semana começa em **zero** (segunda-feira).
- Prefira criar uma coluna nova e conferir o resultado antes de sobrescrever a original.
- Para uma conta simples como `n * 20`, a operação direta na coluna (`avaliacao * 20`) é ainda melhor que `apply`.
