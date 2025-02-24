import pandas as pd

def analisar_dados(df):
    # Estatísticas básicas
    estatisticas = df.describe().round(1)  # Arredonda para 1 casa decimal

    # Média de salários por departamento
    media_salario_por_departamento = df.groupby('departamento')['salario'].mean().round(1)  # Arredonda para 1 casa decimal

    return estatisticas, media_salario_por_departamento