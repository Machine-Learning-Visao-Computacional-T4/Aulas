# Habilitar o Jupyter Notebook no VS Code

Passo a passo para criar e executar notebooks (`.ipynb`) dentro do VS Code.

## 1. Instale a extensão Jupyter

No VS Code:

1. Clique em **Extensões**, na barra esquerda (ícone de quadradinhos).
2. Pesquise **Jupyter**.
3. Escolha a extensão publicada pela **Microsoft**.
4. Clique em **Instalar**.

> Confira também se a extensão **Python**, da Microsoft, está instalada.

## 2. Abra ou crie um notebook

Abra seu arquivo `.ipynb`. Se ainda não tiver um, crie um arquivo chamado:

```text
aula01.ipynb
```

## 3. Selecione o kernel

No canto superior direito do notebook:

1. Clique em **Select Kernel** (Selecionar Kernel).
2. Escolha **Python Environments** (Ambientes Python).
3. Selecione o Python que você já usa, ou `.venv`, se houver um ambiente do projeto.

> O **kernel** é quem executa o código das células.

## 4. Execute uma célula

Digite na célula:

```python
print("Jupyter funcionando!")
```

Clique no botão ▶ ao lado da célula.

Se aparecer uma solicitação para instalar o `ipykernel`, clique em **Instalar** e aguarde. Depois, execute novamente.

Quando aparecer `Jupyter funcionando!` abaixo da célula, está pronto! 😊
