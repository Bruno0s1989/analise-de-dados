import matplotlib.pyplot as plt
import seaborn as sns

def plotar_graficos(df):
    # Gráfico de barras (salários)
    plt.figure(figsize=(10, 5))
    sns.barplot(x='nome', y='salario', data=df)
    plt.title('Salários por Funcionário')
    plt.xlabel('Nome')
    plt.ylabel('Salário')
    plt.show()

    # Histograma (idades)
    plt.figure(figsize=(10, 5))
    sns.histplot(df['idade'], kde=True)
    plt.title('Distribuição de Idades')
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.show()