# Exercício 07 — Exercício final: análise de provas

**Tipo:** projeto integrador · 25 min · branch + Pull Request

## Objetivo
Integrar **pandas e NumPy** em uma análise entregue via **branch e Pull Request**.

## O que fazer
1. Crie a branch `feature/analise-provas-numpy`.
2. Escreva `analise_provas.py`: leia `provas.csv` com pandas, extraia as notas com `to_numpy` e calcule a **média ponderada** com pesos `(0.3, 0.3, 0.4)` por **broadcasting**.
3. Classifique com `np.where`, **normalize as notas por coluna** com Z-score e salve o resultado completo em `resultado_provas.csv` (`index=False`).
4. Commit, push da branch e **Pull Request** para a `main`, explicando o que cada etapa faz.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_numpy/exercicio_07_exercicio_final_analise_de_provas/analise_provas.py
```

No Windows, se `python` não funcionar, use `py aula3_numpy/exercicio_07_exercicio_final_analise_de_provas/analise_provas.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `analise_provas.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`provas.csv`); veja o [guia](../../docs/guia_numpy.md#no-google-colab). Instale o que faltar com `!pip install pandas openpyxl`.

## Exemplo de execução

```text
    nome   p1   p2   p3  final   situacao  z_p1  z_p2  z_p3
0    Ana  8.5  9.0  7.5   8.25   Aprovado  0.69  1.27  0.54
1  Bruno  6.0  7.5  5.0   6.05  Reprovado -0.69 -0.12 -0.82
2  Carla  9.5  8.0  9.0   8.85   Aprovado  1.24  0.35  1.36
3  Diego  5.0  6.0  4.5   5.10  Reprovado -1.24 -1.50 -1.09
Arquivo resultado_provas.csv gravado.
```

## Dicas e erros comuns
- `df[["p1", "p2", "p3"]].to_numpy()` entrega as três colunas como uma matriz NumPy 4x3.
- `(notas * pesos).sum(axis=1)` multiplica cada prova pelo seu peso e soma por aluno.

## Git deste exercício
```bash
git switch -c feature/analise-provas-numpy
git add analise_provas.py provas.csv
git commit -m "Adiciona análise de provas com pandas e NumPy"
git push -u origin feature/analise-provas-numpy
```
Depois, no GitHub: **Compare & pull request** → descreva o que o programa faz → **Create pull request**.
