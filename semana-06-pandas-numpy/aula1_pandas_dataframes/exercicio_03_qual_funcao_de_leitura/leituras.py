from pathlib import Path

import sqlite3

import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

# Cada formato tem a sua função de leitura, mas todas devolvem um DataFrame
csv_simples = pd.read_csv(BASE / "vendas.csv")
csv_brasileiro = pd.read_csv(BASE / "vendas_br.csv", sep=";", decimal=",")  # CSV do Excel em português
excel = pd.read_excel(BASE / "vendas.xlsx", sheet_name="Janeiro")           # escolhe a aba
json_ = pd.read_json(BASE / "vendas.json")

conexao = sqlite3.connect(BASE / "loja.db")
sql = pd.read_sql("SELECT * FROM vendas", conexao)                           # consulta SQL -> DataFrame
conexao.close()

fontes = {
    "CSV": csv_simples,
    "CSV (;)": csv_brasileiro,
    "Excel": excel,
    "JSON": json_,
    "SQL": sql,
}

for nome, tabela in fontes.items():
    soma = tabela["preco"].sum()
    print(f"{nome:<8} -> {tabela.shape[0]} linhas, {tabela.shape[1]} colunas, soma dos preços = {soma:.1f}")

print("\nDepois de lido, o formato de origem deixa de importar: é tudo DataFrame.")
