# Exercício 01 — Ache os problemas nos dados

**Tipo:** dinâmica de abertura + script · 10 min

## Objetivo
Reativar o olhar crítico da Semana 02 **antes** de limpar dados com código.

## O que fazer
1. Abra `contatos_sujos.csv` (5 linhas) e **liste todos os problemas** que encontrar.
2. Agrupe os problemas por tipo: **ausentes**, **duplicatas**, **formato de texto** e **formato de data**.
3. Pergunta: qual dessas correções, na Semana 05, exigia um **laço**? Hoje nenhuma exigirá.
4. Rode o script de diagnóstico e compare com a sua lista.

## O arquivo
```text
nome,telefone,data_cadastro,nota
"  ana   souza ","(48) 99999-1234",05/03/2025,8.5
BRUNO lima,48 98888 5678,18/03/2025,
carla mendes,48-97777-0000,02/04/2025,9.0
carla mendes,48-97777-0000,02/04/2025,9.0
Diego Alves,(48) 96666-1111,10/04/2025,6.5
```

<details>
<summary>Ver respostas</summary>

- **Ausente:** a `nota` de Bruno está vazia.
- **Duplicata:** Carla aparece duas vezes, com os mesmos dados.
- **Texto:** nomes com espaços extras (`"  ana   souza "`) e caixa irregular (`BRUNO lima`); telefones em 4 formatos diferentes.
- **Data:** `data_cadastro` é só texto no formato dd/mm/aaaa.

</details>

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula2_pandas_groupby_merge/exercicio_01_ache_os_problemas_nos_dados/diagnostico.py
```

No Windows, se `python` não funcionar, use `py aula2_pandas_groupby_merge/exercicio_01_ache_os_problemas_nos_dados/diagnostico.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `diagnostico.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`contatos_sujos.csv`); veja o [guia](../../docs/guia_pandas.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
Linhas e colunas: (5, 4)

Valores ausentes por coluna:
nome             0
telefone         0
data_cadastro    0
nota             1
dtype: int64

Linhas duplicadas: 1

Nomes como estão (repare nos espaços e na caixa):
['  ana   souza ', 'BRUNO lima', 'carla mendes', 'carla mendes', 'Diego Alves']

Telefones como estão (sem padrão):
['(48) 99999-1234', '48 98888 5678', '48-97777-0000', '48-97777-0000', '(48) 96666-1111']

Datas ainda são texto, por exemplo: 05/03/2025
```

## Dicas e erros comuns
- Primeiro **descobrimos** onde estão os problemas; só depois decidimos o que fazer com cada um.
- Todos os dados do arquivo são **fictícios**.
