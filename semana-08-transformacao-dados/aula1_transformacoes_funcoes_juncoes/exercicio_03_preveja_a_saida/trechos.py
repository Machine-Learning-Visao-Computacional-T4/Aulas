import pandas as pd

print("1) Texto")
print(pd.Series(["  Sul ", "norte"]).str.strip().str.title())

print("\n2) map com dicionário")
print(pd.Series([1, 2, 7]).map({1: "a", 2: "b"}))

print("\n3) apply com lambda")
print(pd.Series([3, 8]).apply(lambda x: x * 2 if x > 5 else x))

print("\n4) Dia da semana de 14/03/2025")
print(pd.to_datetime(pd.Series(["2025-03-14"])).dt.dayofweek)
