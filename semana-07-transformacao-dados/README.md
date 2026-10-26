# Semana 07 — Transformação de dados: funções, gráficos e análise exploratória

Material de prática da **Semana 07** do curso *Machine Learning e Visão Computacional* (Turma T4, SC TEC / SENAI). Com o pandas e o NumPy da Semana 06 nas mãos, você agora **transforma** dados brutos em dados prontos, **desenha** gráficos que respondem perguntas e **explora** um conjunto de dados para descobrir (e registrar) os seus problemas antes de qualquer modelo.

Nos slides, esta semana aparece como **Semana 07 — Transformação de dados**.

## Aulas e exercícios

| Aula | Tema | Pasta |
| --- | --- | --- |
| 1 | Transformações: funções em colunas, condições e junções | [aula1_transformacoes_funcoes_juncoes](aula1_transformacoes_funcoes_juncoes/) |
| 2 | Visualização com Matplotlib e seaborn | [aula2_visualizacao_matplotlib_seaborn](aula2_visualizacao_matplotlib_seaborn/) |
| 3 | Análise exploratória de dados (EDA) com pandas | [aula3_analise_exploratoria](aula3_analise_exploratoria/) |

Resumos teóricos em [`docs/guia_transformacoes.md`](docs/guia_transformacoes.md), [`docs/guia_visualizacao.md`](docs/guia_visualizacao.md) e [`docs/guia_eda.md`](docs/guia_eda.md).

## Um caso para as três aulas: a cafeteria Grão Certo
Todos os exercícios usam os dados de uma **cafeteria fictícia** (nenhum dado real, sem preocupação com LGPD):

| Arquivo | Linhas x colunas | O que guarda |
| --- | --- | --- |
| `pedidos.csv` | 687 x 8 | Um pedido por linha, de janeiro a junho de 2025: data, cliente, produto, quantidade, canal, avaliação e tempo de entrega |
| `produtos.csv` | 12 x 5 | Nome, categoria, custo e preço de cada produto do cardápio |
| `clientes.csv` | 60 x 5 | Nome, bairro, ano de cadastro e plano (Gratuito, Fidelidade ou Premium) |

Há **problemas escondidos de propósito** nos pedidos (canais com várias grafias, linhas duplicadas, quantidades impossíveis, tempos de entrega suspeitos...). Eles aparecem aos poucos, e a Aula 3 é a caça a todos eles.

## O fio condutor: do dado bruto ao relatório
Os exercícios finais de cada aula formam uma sequência:
1. **Aula 1:** juntar e transformar as três tabelas em uma só, pronta para análise ([`preparar_pedidos`](aula1_transformacoes_funcoes_juncoes/exercicio_08_exercicio_final_preparar_pedidos/)).
2. **Aula 2:** transformar a tabela pronta em um painel de gráficos ([painel da cafeteria](aula2_visualizacao_matplotlib_seaborn/exercicio_08_exercicio_final_painel_da_cafeteria/)). O gráfico mostra duas pistas: o **pico de março** e uma **entrega de 480 minutos**.
3. **Aula 3:** investigar essas pistas com um roteiro de EDA e entregar um relatório ([relatório de EDA](aula3_analise_exploratoria/exercicio_08_exercicio_final_relatorio_de_eda/)).

Dado ruim vira resultado ruim: tudo o que você investigou aqui é o que decide se o modelo de Machine Learning das próximas semanas vai aprender a coisa certa.

## Como executar
Esta semana usa bibliotecas externas: **pandas**, **NumPy**, **Matplotlib** e **seaborn**. Instale com:

```bash
git clone https://github.com/Machine-Learning-Visao-Computacional-T4/semana-07-transformacao-dados.git
cd semana-07-transformacao-dados
pip install -r requirements.txt
python aula1_transformacoes_funcoes_juncoes/exercicio_08_exercicio_final_preparar_pedidos/preparar.py
```

No Windows, se `python` ou `pip` não funcionarem, use `py` e `py -m pip`.

Os scripts procuram os arquivos de dados **na mesma pasta do próprio script**, então você pode rodá-los de qualquer lugar. Cada exercício que grava arquivos (`pedidos_prontos.csv`, `painel.png`, `registro_problemas.csv`...) cria o resultado ao lado do script.

Nos exercícios de gráficos, o script **salva a imagem** (`.png`) ao lado dele e, nos da Aula 2, abre uma janela com `plt.show()`: feche a janela para o script terminar.

No **Google Colab** o pandas, o NumPy, o Matplotlib e o seaborn já vêm instalados: envie os arquivos de dados da pasta do exercício (veja o [guia](docs/guia_transformacoes.md#no-google-colab)) e cole o script em uma célula.

## Como estudar
1. Leia o `README.md` do exercício.
2. **Tente sozinho**, com os seus próprios dados fictícios.
3. Compare com a solução de exemplo.
4. Faça commit e push no **seu** repositório. Use **somente dados fictícios**.

## Observação
Os exemplos foram testados com **pandas 3**, **NumPy 2**, **Matplotlib 3.11** e **seaborn 0.13**. Em versões anteriores (como as do Google Colab), a saída pode ter pequenas diferenças, por exemplo o tipo de colunas de texto aparecer como `object` em vez de `str`.

Os dados da cafeteria são fictícios e foram preparados para reproduzir de perto os números mostrados nos slides (687 pedidos, 9 grafias de canal, 12 duplicatas, 3 entregas de 480 minutos...). Alguns valores contínuos, como o faturamento total e o lucro por categoria, podem diferir dos slides em alguns reais. Os tempos do exercício "A aposta do dia" mudam de computador para computador. As perguntas dos quizzes foram preparadas para este repositório e podem diferir das usadas na aula ao vivo.
