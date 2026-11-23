# Kit da Semana 12: Estatística no Contexto de ML

Curso **Machine Learning e Visão Computacional** (Turma T4), SENAI/SC TEC. Todos os dados são **fictícios**, criados para as aulas, sem dados pessoais (LGPD).

## Conteúdo

| Pasta | O que tem |
|---|---|
| `arquivos/` | `consumo_campus.csv` (730 dias) e `consumo_campus_serra.csv` (180 dias de um campus em clima mais frio) |
| `aulas/` | `aulaN.py` (código das aulas) e `aulaN_saida_esperada.txt` (saída real da execução) |
| `exercicios/` | Para cada aula, `README.md` com os 4 exercícios e `solucoes/` com a solução de referência e a saída esperada |
| `figuras/` | Gráficos gerados pelos scripts das aulas |

## Como executar

Rode sempre a partir da raiz do kit (a pasta que contém `arquivos/`):

```bash
pip install pandas numpy scipy scikit-learn matplotlib
python aulas/aula1.py
python exercicios/aula1/solucoes/exercicio_01_amostras_de_umidade.py
```

Versões usadas para gerar as saídas: pandas 3.0, NumPy 2, SciPy 1.18, scikit-learn 1.9. Em outras versões podem aparecer diferenças pequenas nos números.

## Dicionário de dados (`consumo_campus.csv`)

| Coluna | Descrição |
|---|---|
| `data` | Dia da medição |
| `dia_semana` | 0 (segunda-feira) a 6 (domingo) |
| `temperatura_c` | Temperatura média do dia, em °C |
| `umidade_pct` | Umidade relativa média, em % |
| `ocupacao_pct` | Percentual de salas ocupadas |
| `evento` | 1 se houve evento no campus |
| `dia_util` | 1 de segunda a sexta |
| `consumo_kwh` | Energia consumida no dia (alvo), em kWh |

## Entrega com Git e Pull Request

Cada aula termina com um exercício entregue por Pull Request. Fluxo sugerido:

```bash
git checkout main && git pull
git checkout -b feature/estatistica-amostras      # o nome da branch está no README da aula
git add estatistica_amostras.py ANALISE.md
git commit -m "Adiciona estatística de amostras do consumo do campus"
git push -u origin feature/estatistica-amostras
```

Depois, abra o Pull Request no GitHub descrevendo o que foi feito.
