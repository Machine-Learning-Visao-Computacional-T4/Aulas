# Guia rápido: NumPy

## Instalar e importar
```bash
pip install numpy
```
```python
import numpy as np   # "np" é a convenção mundial
```

## Lista x array
| Característica | Lista Python | Array NumPy |
| --- | --- | --- |
| Tipos dos elementos | podem ser misturados | todos do mesmo tipo (`dtype`) |
| Contas | exigem laço ou compreensão | atuam em **todos os elementos de uma vez** |
| Dimensões | listas dentro de listas | 1D, 2D, 3D... nativas |
| Velocidade com números | mais lenta | muito mais rápida |

`[1, 2] * 2` repete a lista (`[1, 2, 1, 2]`); `np.array([1, 2]) * 2` multiplica cada elemento (`[2 4]`).

## Criar arrays
```python
np.array([[1, 2, 3], [4, 5, 6]])
np.zeros(3)                 # [0. 0. 0.]
np.ones((2, 3), dtype=int)  # matriz 2x3 de uns
np.arange(0, 10, 2)         # [0 2 4 6 8]  (o fim é exclusivo)
np.linspace(0, 1, 5)        # 5 pontos igualmente espaçados (inclui as pontas)
```

## Conhecer o array
| Atributo | Significa |
| --- | --- |
| `a.shape` | formato, por exemplo `(4, 3)` = 4 linhas e 3 colunas |
| `a.ndim` | número de dimensões |
| `a.size` | número total de elementos |
| `a.dtype` | tipo dos elementos |

## Indexar e fatiar
```python
a[0, 1]        # linha 0, coluna 1
a[2]           # linha inteira
a[:, 0]        # coluna inteira
a[1:3, 1:]     # linhas 1 e 2, da coluna 1 em diante (o fim é exclusivo)
a[a >= 7]      # máscara booleana: só os valores que passam
a.reshape(3, 4)   # muda o formato (o total de elementos não muda); reshape(-1) "achata"
```

## Vetorização: troque o laço por uma operação em bloco
```python
precos * quantidades        # elemento a elemento
precos * 1.1                # escalar sobre o array inteiro
np.sqrt(qtd)                # funções universais
np.where(medias >= 7, "Aprovado", "Reprovado")   # if/else vetorizado
```
| Função | O que faz |
| --- | --- |
| `sum`, `mean`, `std`, `min`, `max` | resumos do array |
| `argmin`, `argmax` | **posição** do menor e do maior valor |
| `round`, `clip` | arredonda; limita valores a um intervalo |

### O parâmetro `axis`
Em um array `(4, 3)` (4 alunos, 3 provas):
- `axis=0` percorre as **linhas** e dá **um valor por coluna** → shape `(3,)` (média de cada prova);
- `axis=1` percorre as **colunas** e dá **um valor por linha** → shape `(4,)` (média de cada aluno).

Confira sempre o **shape do resultado**.

## Broadcasting
Regras para operar arrays de **formatos diferentes**:
1. Alinhe os shapes pela **direita**.
2. Cada par de dimensões precisa ser **igual** ou ter um **1** (ou estar ausente).
3. A dimensão de tamanho 1 é "esticada".
4. Se alguma dimensão não for igual nem 1: `ValueError`.

| Operação | Resultado |
| --- | --- |
| `(4, 3) + (3,)` | funciona → `(4, 3)` |
| `(4, 3) + (4, 1)` | funciona → `(4, 3)` |
| `(3, 1) + (1, 4)` | funciona → `(3, 4)` |
| `(4, 3) + (4,)` | **erro** (3 e 4) |

Para somar um valor **por linha**, transforme `(4,)` em `(4, 1)` com `v[:, np.newaxis]`.

Aplicações clássicas (por coluna, com `axis=0`):
```python
minmax = (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))   # valores entre 0 e 1
z = (x - x.mean(axis=0)) / x.std(axis=0)                          # média 0, desvio 1
```

## NumPy, pandas e imagens
- `df.to_numpy()` extrai o array de um DataFrame; funções do NumPy aceitam colunas do pandas.
- Uma imagem em tons de cinza é um array 2D `(altura, largura)` de 0 a 255; uma colorida é 3D `(altura, largura, 3)`. O OpenCV usa a ordem de canais **BGR**.
- Imagens usam o tipo `uint8` (0 a 255): `np.array([250], dtype=np.uint8) + 10` **não** dá 260, e sim `4` (o valor "dá a volta", sem aviso). Para clarear com segurança:
```python
claro = np.clip(img.astype(int) + 10, 0, 255).astype(np.uint8)
```

## No Google Colab
O NumPy já vem instalado. Para usar um arquivo de dados de um exercício, envie-o com `files.upload()` (veja o [guia do pandas](guia_pandas.md#no-google-colab)).
