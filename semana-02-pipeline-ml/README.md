# Semana 02 — O pipeline de um projeto de Machine Learning

Material de prática da **Semana 02** do curso *Machine Learning e Visão Computacional* (Turma T4, SC TEC / SENAI). A semana percorre o caminho que todo projeto de ML faz: **do problema ao dataset, das features às métricas, e do treino à produção**.

> Esta semana é mais de **raciocínio** do que de código. Por isso, cada exercício tem um guia em `README.md` e, quando faz sentido, um script Python para você **ver os números acontecendo**.

## Aulas e exercícios

| Aula | Tema | Exercícios |
| --- | --- | --- |
| [Aula 1](aula1_problema_dataset/) | Do problema ao dataset: definição, coleta e exploração de dados | [01 Problema mal definido](aula1_problema_dataset/exercicio_01_problema_mal_definido/) · [02 Traduza o problema](aula1_problema_dataset/exercicio_02_traduza_o_problema/) · [03 Leia o gráfico](aula1_problema_dataset/exercicio_03_leia_o_grafico/) · [04 Checklist no seu problema](aula1_problema_dataset/exercicio_04_checklist_problema_pessoal/) |
| [Aula 2](aula2_features_metricas/) | Features, datasets e métricas de avaliação | [01 Acurácia engana](aula2_features_metricas/exercicio_01_acuracia_engana/) · [02 Crie uma feature](aula2_features_metricas/exercicio_02_crie_uma_feature/) · [03 Matriz de confusão](aula2_features_metricas/exercicio_03_matriz_de_confusao/) · [04 Qual métrica usar?](aula2_features_metricas/exercicio_04_qual_metrica_usar/) · [05 Métricas no seu problema](aula2_features_metricas/exercicio_05_metricas_no_seu_problema/) |
| [Aula 3](aula3_overfitting_producao/) | Overfitting, regularização e produção | [01 O aluno que decorou](aula3_overfitting_producao/exercicio_01_aluno_que_decorou/) · [02 Ajuste o hiperparâmetro](aula3_overfitting_producao/exercicio_02_ajuste_o_hiperparametro/) · [03 Ciclo de vida (streaming)](aula3_overfitting_producao/exercicio_03_ciclo_de_vida_streaming/) · [04 Do treino à produção](aula3_overfitting_producao/exercicio_04_do_treino_a_producao/) |

## O fio condutor da semana: o seu problema

Na Aula 1 você escolhe **um problema pessoal, acadêmico ou profissional** que poderia virar um projeto de ML. Esse mesmo problema volta na Aula 2 (métricas) e na Aula 3 (treino à produção). Escolha com carinho e guarde suas respostas na pasta de cada exercício.

## Como executar os scripts

Os scripts usam Python 3 e as bibliotecas de `requirements.txt`.

```bash
# 1. clone (ou faça o fork do repositório e clone a sua cópia)
git clone https://github.com/Machine-Learning-Visao-Computacional-T4/semana-02-pipeline-ml.git
cd semana-02-pipeline-ml

# 2. instale as bibliotecas (uma vez)
pip install -r requirements.txt

# 3. rode um exercício
python aula2_features_metricas/exercicio_03_matriz_de_confusao/metricas.py
```

No Windows, se `python` não funcionar, use `py`. No **Google Colab**, rode `!pip install -r requirements.txt` numa célula e depois cole o conteúdo do script em outra célula (veja o guia da Semana 03 para o passo a passo no Colab).

## Como usar este repositório

1. Leia o `README.md` do exercício (objetivo, passo a passo, o que esperar).
2. **Tente sozinho primeiro.** Os arquivos `solucao`/exemplo estão aqui para você conferir depois.
3. Registre suas respostas em um arquivo seu (por exemplo `minhas_respostas.md`) dentro da pasta do exercício e faça commit e push na sua cópia.

> **Nota:** a Semana 01 (aula inaugural e fundamentos) é conceitual e não tem exercícios de código; por isso não há repositório dela.
