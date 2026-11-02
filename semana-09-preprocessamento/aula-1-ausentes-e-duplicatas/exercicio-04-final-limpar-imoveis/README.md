# Exercício 04: Final da Aula 1: função limpar_imoveis

**Tipo:** Final, com Git e Pull Request

## Objetivo
Reunir toda a limpeza em uma função reutilizável e entregar por Pull Request.

## O que fazer
1. Crie a branch `feature/limpar-imoveis`.
2. Crie `limpeza.py` com a função `limpar_imoveis(caminho)`, com docstring de uma linha.
3. A função trata os ausentes disfarçados, padroniza `bairro`, remove duplicatas ignorando o id, cria `idade_ausente` e preenche as colunas com a mediana do grupo e a moda.
4. No final do arquivo, chame a função com `arquivos/imoveis_bruto.csv` e imprima o shape, os ausentes e as duplicatas.
5. Resultado esperado: 600 linhas e nenhum ausente.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-1-ausentes-e-duplicatas/exercicio-04-final-limpar-imoveis/limpeza.py
```
A solução de referência está em `limpeza.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
(600, 14)
0 ausentes
0 duplicadas
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Por que a função recebe o caminho e não o DataFrame?
- O que aconteceria se a ordem entre deduplicar e preencher fosse invertida?

## Dicas
- Use `if __name__ == '__main__':` para separar a função do teste.
- Confira os números esperados antes de abrir o Pull Request.

## Git deste exercício
```bash
git checkout -b feature/limpar-imoveis
git add limpeza.py arquivos/imoveis_limpo.csv
git commit -m "feat: função limpar_imoveis"
git push -u origin feature/limpar-imoveis
```
Abra o Pull Request para a `main` pelo GitHub e descreva em duas frases o que a função faz e quais números você conferiu.
