import pandas as pd

esq = pd.DataFrame({"id": [1, 2, 3, 4], "valor_esq": ["a", "b", "c", "d"]})
dir_ = pd.DataFrame({"id": [2, 3, 3, 5], "valor_dir": ["x", "y", "z", "w"]})

for como in ["inner", "left", "right", "outer"]:
    print(f"{como:>5}: {len(esq.merge(dir_, on='id', how=como))} linhas")
print(f"concat: {len(pd.concat([esq, dir_]))} linhas (empilha, não liga por chave)")

print()
print(esq.merge(dir_, on="id", how="outer", indicator=True))

# O validate protege você de chaves repetidas
try:
    esq.merge(dir_, on="id", validate="1:1")
except pd.errors.MergeError as erro:
    print("\nvalidate='1:1' interrompeu o merge:", str(erro).splitlines()[0])
