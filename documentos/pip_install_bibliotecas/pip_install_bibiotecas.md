# Como instalar pacotes no Python

Um **pacote** reúne ferramentas prontas para usarmos no Python. Por exemplo, o `pandas` ajuda a trabalhar com tabelas.

O **pip** é o instalador de pacotes do Python. Já o **PyPI** é um catálogo onde encontramos esses pacotes.

## 1. Abra o terminal no VS Code

No menu superior, clique em **Terminal → Novo Terminal**.

Clique dentro do terminal antes de digitar. Digite um comando por vez e pressione Enter.

## 2. Confira se você tem Python

**Windows:**

```bash
py --version
```

**Mac:**

```bash
python3 --version
```

Se aparecer uma versão, o Python está disponível.

No Windows, se `py` não funcionar, tente:

```bash
python --version
```

Se esse funcionar, use `python` no lugar de `py` nos próximos comandos.

Se nenhum funcionar, [instale o Python](https://www.python.org/downloads/). Depois da instalação, feche o terminal e abra um novo.

## 3. Confira se você tem pip

**Windows:**

```bash
py -m pip --version
```

**Mac:**

```bash
python3 -m pip --version
```

Se aparecer uma versão do pip, você já pode instalar pacotes.

> **Atenção:** se o comando `pip` sozinho não for reconhecido, isso não significa necessariamente que ele está ausente. Tente os comandos acima.

## 4. Como copiar o comando de instalação no PyPI

Vamos usar o `pandas` como exemplo.

1. Acesse: <https://pypi.org/project/pandas/>
2. Procure o comando de instalação:

   ```bash
   pip install pandas
   ```

3. Clique no botão de copiar ao lado do comando, quando disponível, ou selecione o texto e copie.
4. Volte ao terminal do VS Code.

Para indicar qual Python fará a instalação, use o comando correspondente ao seu sistema:

**Windows:**

```bash
py -m pip install pandas
```

**Mac:**

```bash
python3 -m pip install pandas
```

Leia assim: *"Use este Python para executar o pip e instalar pandas."*

Aguarde a instalação terminar. Se aparecer `Requirement already satisfied`, o pacote já está instalado nesse ambiente.

## 5. Como usar o pandas depois de instalar

No seu arquivo Python ou em uma célula do notebook, escreva:

```python
import pandas as pd

print(pd.__version__)
```

Se aparecer a versão do pandas, ele está funcionando.

Instalar e importar são ações diferentes:

- **Instalar:** disponibiliza o pacote no ambiente Python.
- **Importar:** permite usar o pacote no seu código.

## 6. Se estiver usando um notebook

Em uma célula de código do notebook, execute:

```python
%pip install pandas
```

Esse comando instala no ambiente do kernel atual.

Depois, em outra célula, execute:

```python
import pandas as pd

print(pd.__version__)
```

Se surgir uma mensagem pedindo para reiniciar o kernel, clique em **Restart / Reiniciar** na barra do notebook. Depois, execute novamente as células de cima para baixo.

## 7. Se você não tiver pip

Se aparecer `No module named pip`, tente instalar o pip com `ensurepip`.

**Windows:**

```bash
py -m ensurepip --upgrade
```

Depois confira:

```bash
py -m pip --version
```

**Mac:**

```bash
python3 -m ensurepip --upgrade
```

Depois confira:

```bash
python3 -m pip --version
```

Quando funcionar, volte ao comando de instalação do pandas. O `ensurepip` é um dos [métodos oficiais](https://pip.pypa.io) para instalar o pip.

## 8. Se o ensurepip também não funcionar

Outra opção oficial é o arquivo `get-pip.py` ([documentação](https://pip.pypa.io)).

1. Acesse: <https://bootstrap.pypa.io/get-pip.py>
2. Salve o arquivo como `get-pip.py`, sem acrescentar `.txt`.
3. No terminal, entre na pasta onde salvou o arquivo usando `cd`.
4. Execute:

   **Windows:**

   ```bash
   py get-pip.py
   ```

   **Mac:**

   ```bash
   python3 get-pip.py
   ```

Depois confira novamente a versão do pip.

## Onde digitar cada coisa?

| O que você quer fazer            | Onde digitar         | Exemplo                          |
| -------------------------------- | -------------------- | -------------------------------- |
| Instalar pelo terminal no Windows | Terminal do VS Code  | `py -m pip install pandas`       |
| Instalar pelo terminal no Mac     | Terminal do VS Code  | `python3 -m pip install pandas`  |
| Instalar pelo notebook            | Célula de código     | `%pip install pandas`            |
| Usar o pandas                     | Código Python        | `import pandas as pd`            |

> Se o notebook continuar mostrando `No module named pandas`, confira o kernel selecionado e execute `%pip install pandas` nele. Cada ambiente Python pode ter seus próprios pacotes.
