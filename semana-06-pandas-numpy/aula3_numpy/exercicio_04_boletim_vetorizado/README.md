# Exercício 04 — Mãos à obra + commit: boletim vetorizado

**Tipo:** prática + commit · 18 min

## Objetivo
Calcular um **boletim inteiro sem nenhum laço `for`** para fazer contas.

## O que fazer
1. Crie `boletim_numpy.py` com a matriz de notas 4x3 usada em aula.
2. Calcule a **média de cada aluno** (`axis=1`) e a **média de cada prova** (`axis=0`), arredondadas com duas casas.
3. Use `np.where` para classificar cada aluno como **Aprovado** (média >= 7) ou **Reprovado**; mostre **quem tem a maior média** (`argmax`).
4. Commit e push.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_numpy/exercicio_04_boletim_vetorizado/boletim_numpy.py
```

No Windows, se `python` não funcionar, use `py aula3_numpy/exercicio_04_boletim_vetorizado/boletim_numpy.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `boletim_numpy.py` em uma célula e execute com `Shift + Enter`.

## Exemplo de execução

```text
Ana | 8.33 | Aprovado
Bruno | 6.17 | Reprovado
Carla | 8.83 | Aprovado
Diego | 5.17 | Reprovado
Média de cada prova: [7.25 7.62 6.5 ]
Maior média: Carla com 8.83
```

## Dicas e erros comuns
- Compare com o `boletim.py` da Semana 05: o mesmo resultado, sem nenhum laço para calcular.
- O `for` do script serve apenas para **imprimir** as linhas; as contas são todas em bloco.
