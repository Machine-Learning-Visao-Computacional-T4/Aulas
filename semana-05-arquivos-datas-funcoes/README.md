# Semana 05 — Arquivos, datas, regex, funções e módulos

Material de prática da **Semana 05** do curso *Machine Learning e Visão Computacional* (Turma T4, SC TEC / SENAI). Seus programas passam a trabalhar com **dados de verdade**: ler arquivos, limpar datas e textos sujos, e organizar o código em funções e módulos.

Nos slides, esta semana aparece como **Módulo 05 — Manipulação de dados e funções**.

## Aulas e exercícios

| Aula | Tema | Pasta |
| --- | --- | --- |
| 1 | Manipulação de arquivos: texto, CSV, JSON e Excel | [aula1_arquivos_texto_csv_json](aula1_arquivos_texto_csv_json/) |
| 2 | Datas e expressões regulares: limpando dados sujos | [aula2_datas_regex](aula2_datas_regex/) |
| 3 | Funções e modularização: escreva uma vez, use sempre | [aula3_funcoes_modulos](aula3_funcoes_modulos/) |

Resumo teórico em [`docs/guia_arquivos.md`](docs/guia_arquivos.md).

## O fio condutor: a faxina de dados
Os três exercícios finais formam uma sequência:
1. **Aula 1:** ler CSV e gravar JSON ([conversor](aula1_arquivos_texto_csv_json/exercicio_04_conversor_csv_para_json/)).
2. **Aula 2:** limpar um CSV sujo com datas e regex ([faxina](aula2_datas_regex/exercicio_05_faxina_dataset_sujo/)).
3. **Aula 3:** reorganizar a faxina em funções e módulos ([refatoração](aula3_funcoes_modulos/exercicio_07_refatorando_a_faxina/)).

## Como executar
Só a biblioteca padrão do Python é usada: **não há nada para instalar**.

```bash
git clone https://github.com/Machine-Learning-Visao-Computacional-T4/semana-05-arquivos-datas-funcoes.git
cd semana-05-arquivos-datas-funcoes
python aula2_datas_regex/exercicio_05_faxina_dataset_sujo/faxina.py
```

No Windows, se `python` não funcionar, use `py`.

Os scripts procuram os arquivos de dados **na mesma pasta do próprio script**, então você pode rodá-los de qualquer lugar. Cada exercício que grava arquivos (`resultado.csv`, `dados.json`, `limpo.csv`...) cria o resultado ao lado do script.

No **Google Colab**, envie os arquivos de dados da pasta do exercício (veja o [guia](docs/guia_arquivos.md#no-google-colab)) e cole o script em uma célula.

## Como estudar
1. Leia o `README.md` do exercício.
2. **Tente sozinho**, criando seus próprios dados fictícios.
3. Compare com a solução de exemplo.
4. Faça commit e push no **seu** repositório. Use **somente dados fictícios**.

## Observação
As perguntas dos quizzes e os trechos do "Ache o bug" foram preparados para este repositório e podem diferir dos usados na aula ao vivo. O trecho de aula sobre Excel não gerou exercício prático e, por isso, não tem pasta aqui.
