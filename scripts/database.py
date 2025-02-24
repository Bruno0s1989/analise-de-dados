import sqlite3
import pandas as pd

# Conectar ao banco de dados (ou criar se não existir)
def conectar_banco():
    conn = sqlite3.connect('analise_de_dados.db')
    return conn

# Criar tabela dinamicamente com base nas colunas do CSV
def criar_tabela(conn, colunas):
    cursor = conn.cursor()
    
    # Define os tipos de dados com base no tipo de dado do pandas
    tipos = {
        'int64': 'INTEGER',
        'float64': 'REAL',
        'object': 'TEXT'
    }

    # Cria a query SQL para criar a tabela
    colunas_sql = []
    for coluna, tipo in colunas.items():
        tipo_sql = tipos.get(tipo, 'TEXT')  # Usa TEXT como padrão se o tipo não for reconhecido
        colunas_sql.append(f"{coluna} {tipo_sql}")
    
    query = f"CREATE TABLE IF NOT EXISTS dados ({', '.join(colunas_sql)})"
    cursor.execute(query)
    conn.commit()

# Inserir dados no banco de dados
def inserir_dados(conn, dados, colunas):
    cursor = conn.cursor()
    colunas_str = ', '.join(colunas)
    placeholders = ', '.join(['?'] * len(colunas))
    
    query = f"INSERT INTO dados ({colunas_str}) VALUES ({placeholders})"
    cursor.executemany(query, dados)
    conn.commit()

# Consultar dados do banco de dados
def consultar_dados(conn):
    return pd.read_sql('SELECT * FROM dados', conn)