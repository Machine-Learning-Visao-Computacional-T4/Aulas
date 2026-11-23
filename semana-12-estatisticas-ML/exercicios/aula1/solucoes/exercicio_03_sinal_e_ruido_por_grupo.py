# Aula 1 - Exercício 3: quanto da variação do consumo vem do tipo de dia
import pandas as pd

consumo_campus = pd.read_csv("arquivos/consumo_campus.csv")
consumo = consumo_campus["consumo_kwh"]
print(consumo_campus.groupby("dia_semana")["consumo_kwh"].agg(["mean", "std", "count"]).round(1))

variancia_total = consumo.var(ddof=0)
media_do_grupo = consumo_campus.groupby("dia_util")["consumo_kwh"].transform("mean")
variancia_dentro_dos_grupos = ((consumo - media_do_grupo) ** 2).mean()
fracao_explicada = 1 - variancia_dentro_dos_grupos / variancia_total
print(f"variância total = {variancia_total:.0f}")
print(f"variância dentro dos grupos (dia útil x fim de semana) = {variancia_dentro_dos_grupos:.0f}")
print(f"fração da variação explicada pelo tipo de dia = {fracao_explicada:.1%}")
