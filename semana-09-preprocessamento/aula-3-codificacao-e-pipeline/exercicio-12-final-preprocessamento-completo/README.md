# Exercício 12: Final da semana: do bruto ao pronto

**Tipo:** Final, com Git e Pull Request

## Objetivo
Entregar um programa que percorre todo o roteiro, do arquivo bruto aos dados prontos para um modelo.

## O que fazer
1. Crie a branch `feature/preprocessamento-completo`.
2. Crie `preprocessamento.py` com `limpar_imoveis`, `tratar_erros` e `montar_pipeline`, cada uma com docstring de uma linha.
3. No final do arquivo, leia `arquivos/imoveis_bruto.csv`, aplique as etapas, divida em treino e teste e imprima os shapes de entrada e saída.
4. Crie `PREPROCESSAMENTO.md` com uma tabela de decisões (problema, quantos, decisão, justificativa) e uma frase sobre o que ainda poderia melhorar.
5. Resultados esperados: 600, 597, (477, 12), (120, 12) e 22 colunas na saída.

## Como executar
Na raiz do repositório (`semana-09-preprocessamento`):
```bash
python aula-3-codificacao-e-pipeline/exercicio-12-final-preprocessamento-completo/preprocessamento.py
```
A solução de referência está em `preprocessamento.py` nesta pasta. Tente antes de olhar.

## Exemplo de execução
```text
depois da limpeza: 600
depois dos erros: 597
treino/teste: (477, 12) (120, 12)
saída: (477, 22) (120, 22)
```
(Saída gerada com pandas 3, NumPy 2 e scikit-learn 1.9; no Colab podem aparecer diferenças pequenas, como `str` no lugar de `object`.)

## Para pensar
- Em que ponto do roteiro cada decisão poderia causar vazamento?
- O que você faria diferente com mais tempo?

## Dicas
- Rode `python preprocessamento.py` antes de abrir o Pull Request.
- Na descrição do PR, explique a ordem das etapas.

## Git deste exercício
```bash
git checkout -b feature/preprocessamento-completo
git add preprocessamento.py PREPROCESSAMENTO.md
git commit -m "feat: preprocessamento completo"
git push -u origin feature/preprocessamento-completo
```
Abra o Pull Request para a `main` pelo GitHub e descreva em duas frases o que a função faz e quais números você conferiu.
