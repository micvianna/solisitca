
# Data:
# Conexão com Banco de dados NewSitex
# Autor: Michel Viana


from LerProgramacaoViagem import inicio as lpv

import pyodbc

dados_conexao = (
    'Driver={ODBC Driver 17 for SQL Server};'
    f'Server={lpv.conexao_database()};'
    'Database=NewSitex;'
    f'UID={lpv.conexao_user_db()};'
    f'PWD={lpv.conexao_passw_db()};'
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()
cursor.execute('SELECT TOP 1 * FROM [dbo].[TB_COLETAS];')

for i in cursor:
    print(i)



