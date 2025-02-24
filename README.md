# Sistema de Análise de Dados com SQL e Python
 
Este projeto é um sistema de análise de dados desenvolvido em Python e SQL. Ele permite carregar dados de arquivos CSV, armazená-los em um banco de dados SQLite, realizar análises básicas e gerar visualizações gráficas. O sistema é versátil e pode ser adaptado para uso em empresas ou projetos pessoais.

**Funcionalidades**

Carregamento de Dados: Importação de dados de arquivos CSV.

Armazenamento em Banco de Dados: Os dados são armazenados em um banco de dados SQLite.

Análise de Dados: Geração de estatísticas descritivas e médias de salários por departamento.

Visualização de Dados: Criação de gráficos de barras e histogramas.

Interface Gráfica: Interface simples e intuitiva para interação com o usuário.


**Tecnologias Utilizadas**

Python (bibliotecas: pandas, sqlite3, matplotlib, seaborn, tkinter)

SQLite (banco de dados)


**Como Usar**

Pré-requisitos

Python 3.x: Instale o Python em python.org.
Bibliotecas Python: Instale as bibliotecas necessárias executando:
pip install pandas matplotlib seaborn

Executando o Projeto

python scripts/main.py
Interface Gráfica:

Carregar Dados: Clique em "Carregar Dados" e selecione um arquivo CSV.
Salvar no Banco: Clique em "Salvar no Banco" para armazenar os dados no banco de dados SQLite.
Analisar Dados: Clique em "Analisar Dados" para ver estatísticas descritivas.
Exibir Gráficos: Clique em "Exibir Gráficos" para visualizar gráficos de barras e histogramas.

**Personalização**

Você pode personalizar o projeto para atender às suas necessidades:

Adicionar Novas Colunas:

Atualize a função criar_tabela no arquivo database.py para incluir novas colunas.

Novas Análises:

Modifique a função analisar_dados no arquivo analysis.py para incluir novas métricas.

Novos Gráficos:

Adicione novos gráficos no arquivo visualization.py.

