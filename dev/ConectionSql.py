# Data:
# Conexão com Banco de dados NewSitex
# Autor: Michel Viana


from CarregarXMLConexao import conexao_xml as lpv

import pyodbc

dados_conexao = (
    'Driver={ODBC Driver 17 for SQL Server};'
    f'Server={lpv.conexao_database()};'
    'Database=NewSitex;'
    f'UID={lpv.conexao_user_db()};'
    f'PWD={lpv.conexao_passw_db()};'
)

conexao = pyodbc.connect(dados_conexao)
#print("Conexão Bem Sucedida")

cursor = conexao.cursor()
# cursor.execute('SELECT TOP 1 * FROM [dbo].[TB_COLETAS];')

#Sample select query
cursor.execute("SELECT COD_FILIAIS ,"
               "IDENT_FILIAIS, "
               "SIGLA_FILIAIS, "
               "NM_FILIAIS UF_FILIAIS, "
               "CNPJ_FILIAIS, "
               "UF_FILIAIS, "
               "COD_DOMINIO,"
               "COD_EMPRESAS FROM [dbo].[TB_FILIAIS] where "
               "IDENT_FILIAIS = '401';")

lista = []
row = cursor.fetchone()
while row:
    for i in row:
        lista.append(i)
    row = cursor.fetchone()



for i in lista:
    print(i)
"""
cursor.execute("SELECT COD_FILIAIS ,"
               "IDENT_FILIAIS, "
               "SIGLA_FILIAIS, "
               "NM_FILIAIS , "
               "CNPJ_FILIAIS, "
               "UF_FILIAIS, "
               "COD_DOMINIO,"
               "COD_EMPRESAS FROM [dbo].[TB_FILIAIS] where "
               "IDENT_FILIAIS = '401';")
"""




    # Criando uma lista dentro de um for.




