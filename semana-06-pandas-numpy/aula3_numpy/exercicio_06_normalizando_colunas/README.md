# Exercício 06 — Mãos à obra + commit: normalizando colunas

**Tipo:** prática + commit · 18 min

## Objetivo
Aplicar **broadcasting** em duas transformações de dados clássicas.

## O que fazer
1. Crie `normalizacao.py` com a matriz de notas 4x3 usada em aula.
2. Aplique a **normalização min-max por coluna**: `(x - min) / (max - min)`, com `axis=0`, e confira que cada coluna fica entre 0 e 1.
3. Aplique o **Z-score por coluna** e verifique a **média** (próxima de 0) e o **desvio-padrão** (próximo de 1) de cada coluna.
4. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_numpy/exercicio_06_normalizando_colunas/normalizacao.py
```

No Windows, se `python` não funcionar, use `py aula3_numpy/exercicio_06_normalizando_colunas/normalizacao.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `normalizacao.py` em uma célula e execute com `Shift + Enter`.

## Exemplo de execução

```text
Min-max por coluna:
[[0.78 1.   0.67]
 [0.22 0.5  0.11]
 [1.   0.67 1.  ]
 [0.   0.   0.  ]]
Mínimo de cada coluna: [0. 0. 0.] | máximo: [1. 1. 1.]

Z-score por coluna:
[[ 0.69  1.27  0.54]
 [-0.69 -0.12 -0.82]
 [ 1.24  0.35  1.36]
 [-1.24 -1.5  -1.09]]
Média de cada coluna (perto de 0): [0. 0. 0.]
Desvio-padrão de cada coluna (perto de 1): [1. 1. 1.]
```

## Dicas e erros comuns
- `notas.min(axis=0)` tem shape `(3,)`, e o broadcasting cuida do resto.
- Lembre-se da Semana 02: ao treinar um modelo, calcule média e desvio **só com os dados de treino** (para não vazar dados do teste).
