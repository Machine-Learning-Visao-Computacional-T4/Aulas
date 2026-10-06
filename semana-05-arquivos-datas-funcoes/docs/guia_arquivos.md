# Guia rápido: arquivos, CSV e JSON em Python

## Caminhos
| Tipo | Exemplo | Quando usar |
| --- | --- | --- |
| Relativo | `dados/vendas.csv` | Parte da pasta onde o programa roda; mais portátil entre computadores |
| Absoluto | `C:/Users/ana/projeto/dados/vendas.csv` | Aponta o lugar exato no disco; quebra ao mudar de máquina |

A causa nº 1 de `FileNotFoundError` é o programa rodar em uma pasta diferente da imaginada. Em repositórios no GitHub, prefira **caminhos relativos**.

```python
from pathlib import Path

arquivo = Path("dados") / "vendas.csv"   # o / junta partes de um caminho
print(arquivo.exists())                  # primeiro teste quando "não encontra o arquivo"
```

Nos exercícios deste repositório, os scripts procuram os arquivos **na mesma pasta do script**, então funcionam independentemente de onde você abre o terminal.

## Modos de abertura
| Modo | Significado | Cuidado |
| --- | --- | --- |
| `"r"` | Leitura (padrão) | Dá erro se o arquivo não existir |
| `"w"` | Escrita | **Apaga** todo o conteúdo anterior |
| `"a"` | Acrescenta ao final | Cria o arquivo se não existir |

Sempre use `with` (fecha o arquivo sozinho) e `encoding="utf-8"` (acentos corretos):

```python
with open("diario.txt", "w", encoding="utf-8") as f:
    f.write("Olá!\n")
```

## CSV
```python
import csv

with open("notas.csv", newline="", encoding="utf-8") as f:
    for aluno in csv.DictReader(f):     # cada linha vira um dicionário
        print(aluno["nome"], float(aluno["nota1"]))   # tudo vem como texto: converta

with open("saida.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome", "media"])
    escritor.writeheader()
    escritor.writerow({"nome": "Ana", "media": 8.5})
```
`newline=""` evita linhas em branco extras no Windows.

## JSON
```python
import json

with open("contatos.json", "w", encoding="utf-8") as f:
    json.dump(lista, f, indent=2, ensure_ascii=False)   # lista/dicionário -> arquivo

with open("contatos.json", encoding="utf-8") as f:
    lista = json.load(f)                                # arquivo -> lista/dicionário
```

## No Google Colab
```python
# Opção 1: enviar do seu computador
from google.colab import files
enviado = files.upload()

# Opção 2: acessar o Google Drive
from google.colab import drive
drive.mount("/content/drive")
```
Os arquivos enviados ao Colab ficam em uma pasta **temporária**, apagada ao fim da sessão. Grave resultados importantes no Drive.

## Dados fictícios
Em exercícios e portfólio, **use dados inventados** com a mesma estrutura dos reais. Nunca suba dados pessoais de verdade para um repositório público.
