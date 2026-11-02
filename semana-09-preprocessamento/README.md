# Semana 09: Pré-processamento de dados

Curso de Machine Learning e Visão Computacional, Turma T4. Dados 100% fictícios (anúncios de imóveis), sem dados pessoais.

## Como usar
```bash
pip install -r requirements.txt
python aula-1-ausentes-e-duplicatas/exercicio-01-diagnostico-de-ausentes/diagnostico_ausentes.py
```
Sempre execute os scripts **na raiz** desta pasta, para que o caminho `arquivos/...` funcione.

## Fio condutor
`imoveis_bruto.csv` (623 linhas) → Aula 1 → `imoveis_limpo.csv` (600) → Aula 2 → `imoveis_tratado.csv` (597) → Aula 3 → dados prontos para modelo (22 colunas).

## Exercícios

### Aula 1: Ausentes e duplicatas
- [Diagnóstico de ausentes](aula-1-ausentes-e-duplicatas/exercicio-01-diagnostico-de-ausentes/README.md) (Guiado)
- [Padronizar texto e remover duplicatas](aula-1-ausentes-e-duplicatas/exercicio-02-texto-e-duplicatas/README.md) (Guiado)
- [Preencher ausentes com critério](aula-1-ausentes-e-duplicatas/exercicio-03-preencher-ausentes/README.md) (Guiado)
- [Final da Aula 1: função limpar_imoveis](aula-1-ausentes-e-duplicatas/exercicio-04-final-limpar-imoveis/README.md) (Final, com Git e Pull Request)

### Aula 2: Outliers e escalas
- [Detectar atípicos com IQR e regras do negócio](aula-2-outliers-e-escalas/exercicio-05-outliers-com-iqr/README.md) (Guiado)
- [MinMax, padronização e RobustScaler](aula-2-outliers-e-escalas/exercicio-06-escalas/README.md) (Guiado)
- [Dividir antes de escalar](aula-2-outliers-e-escalas/exercicio-07-escala-sem-vazamento/README.md) (Guiado)
- [Final da Aula 2: função preparar_numericos](aula-2-outliers-e-escalas/exercicio-08-final-preparar-numericos/README.md) (Final, com Git e Pull Request)

### Aula 3: Codificação e Pipeline
- [Codificar binárias e ordinal](aula-3-codificacao-e-pipeline/exercicio-09-codificacoes-simples/README.md) (Guiado)
- [One-Hot com pandas e scikit-learn](aula-3-codificacao-e-pipeline/exercicio-10-one-hot/README.md) (Guiado)
- [ColumnTransformer e Pipeline](aula-3-codificacao-e-pipeline/exercicio-11-pipeline/README.md) (Guiado)
- [Final da semana: do bruto ao pronto](aula-3-codificacao-e-pipeline/exercicio-12-final-preprocessamento-completo/README.md) (Final, com Git e Pull Request)

## Roteiro de pré-processamento
1. Ausentes disfarçados → NaN
2. Padronizar texto e deduplicar (sem o id)
3. Tratar ausentes (mediana por grupo, moda, indicador)
4. Atípicos: investigar, remover erros, manter extremos reais
5. Dividir treino e teste antes de qualquer cálculo
6. Codificar categorias (binária, ordinal, One-Hot)
7. Escalar e encadear em um Pipeline, com fit só no treino
