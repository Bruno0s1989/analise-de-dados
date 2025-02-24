import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
from database import conectar_banco, criar_tabela, inserir_dados, consultar_dados
from analysis import analisar_dados
from visualization import plotar_graficos

# Variável global para armazenar os dados carregados
dados_carregados = None
colunas_csv = None

# Função para carregar dados de um arquivo CSV
def carregar_dados():
    global dados_carregados, colunas_csv
    arquivo = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if arquivo:
        try:
            dados_carregados = pd.read_csv(arquivo)
            colunas_csv = {col: str(dados_carregados[col].dtype) for col in dados_carregados.columns}
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

# Função para salvar dados no banco de dados
def salvar_dados():
    global dados_carregados, colunas_csv
    if dados_carregados is not None:
        try:
            conn = conectar_banco()
            criar_tabela(conn, colunas_csv)  # Cria a tabela com base nas colunas do CSV

            # Converte os dados para o formato esperado
            dados = [tuple(row) for row in dados_carregados.to_numpy()]
            
            # Insere os dados no banco de dados
            inserir_dados(conn, dados, dados_carregados.columns.tolist())
            messagebox.showinfo("Sucesso", "Dados salvos no banco de dados!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")
    else:
        messagebox.showwarning("Aviso", "Nenhum dado carregado. Use 'Carregar Dados' primeiro.")

# Função para exibir análise de dados
def exibir_analise():
    try:
        conn = conectar_banco()
        df = consultar_dados(conn)
        if df.empty:
            messagebox.showwarning("Aviso", "Nenhum dado encontrado no banco de dados.")
            return

        # Realiza a análise
        estatisticas, media_salario_por_departamento = analisar_dados(df)

        # Exibe os resultados na área de texto
        resultado_texto.delete(1.0, tk.END)  # Limpa o conteúdo anterior
        resultado_texto.insert(tk.END, "Estatísticas Gerais:\n")
        resultado_texto.insert(tk.END, estatisticas.to_string() + "\n\n")
        resultado_texto.insert(tk.END, "Média de Salários por Departamento:\n")
        resultado_texto.insert(tk.END, media_salario_por_departamento.to_string())
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao analisar os dados: {e}")

# Função para exibir gráficos
def exibir_graficos():
    try:
        conn = conectar_banco()
        df = consultar_dados(conn)
        if df.empty:
            messagebox.showwarning("Aviso", "Nenhum dado encontrado no banco de dados.")
            return

        # Gera os gráficos
        plotar_graficos(df)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exibir gráficos: {e}")

# Interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Análise de Dados")
    root.geometry("600x400")

    # Usa ttk para estilização
    style = ttk.Style()
    style.configure("TButton", padding=6, font=("Arial", 10))

    # Frame para os botões
    frame_botoes = ttk.Frame(root)
    frame_botoes.pack(pady=10)

    # Botão para carregar dados
    btn_carregar = ttk.Button(frame_botoes, text="Carregar Dados", command=carregar_dados)
    btn_carregar.grid(row=0, column=0, padx=5)

    # Botão para salvar dados no banco
    btn_salvar = ttk.Button(frame_botoes, text="Salvar no Banco", command=salvar_dados)
    btn_salvar.grid(row=0, column=1, padx=5)

    # Botão para analisar dados
    btn_analisar = ttk.Button(frame_botoes, text="Analisar Dados", command=exibir_analise)
    btn_analisar.grid(row=0, column=2, padx=5)

    # Botão para exibir gráficos
    btn_graficos = ttk.Button(frame_botoes, text="Exibir Gráficos", command=exibir_graficos)
    btn_graficos.grid(row=0, column=3, padx=5)

    # Área de texto para exibir resultados
    resultado_texto = scrolledtext.ScrolledText(root, width=70, height=15, font=("Arial", 10))
    resultado_texto.pack(pady=10)

    # Rodar a interface
    root.mainloop()