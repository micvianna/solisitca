from bs4 import BeautifulSoup
import pyodbc

PATH = r'..//parametros'

with open(f'{PATH}\\Conexao.xml', 'r') as f:
    data = f.read()
bs_conec = BeautifulSoup(data, "xml")


class CarregarXMLConexao:

    def __init__(self):
        # XML Programação de Viagem
        self.usuario = bs_conec.find('Login').text
        self.password = bs_conec.find('Senha').text
        self.url_amb = bs_conec.find('URL_Aplicacao').text
        self.filial = bs_conec.find('Filial_login').text

        # conexão do banco de dados
        self.navegador = bs_conec.find('Navegador').text
        self.database = bs_conec.find('FDQN_BD').text
        self.user_db = bs_conec.find('Login_BD').text
        self.password_db = bs_conec.find('Senha_BD').text

    def usuario_login(self):
        # faz chamada do nome do usuário no XML
        return self.usuario

    def password_login(self):
        # faz chamada do password no XML
        return self.password

    def url_ambiente(self):
        # faz chamada da url que está no XML de conexão
        return self.url_amb

    def filial_login(self):
        # faz chamada da filial no arquivo conexao.XML
        return self.filial

    # abaixo conexão com o XML do banco de dados

    def navegador(self):
        # faz chamada do Navegador que está no XML ()
        return self.navegador

    def conexao_database(self):
        # faz chamada do banco do SQL que está no XML ()
        return self.database

    def conexao_user_db(self):
        # faz chamada user do SQL que está no XML ()
        return self.user_db

    def conexao_passw_db(self):
        # faz chamada password do SQL que está no XML ()
        return self.password_db


conexao_xml = CarregarXMLConexao()
ident = conexao_xml.usuario.upper()
conec = conexao_xml


def banco_dados():
    dados_conexao = (
        'Driver={ODBC Driver 17 for SQL Server};'
        f'Server={conec.conexao_database()};'
        'Database=NewSitex;'
        f'UID={conec.conexao_user_db()};'
        f'PWD={conec.conexao_passw_db()};'
    )
    conect = pyodbc.connect(dados_conexao)
    cursor = conect.cursor()

    consulta_user = f"""
            SELECT COD_USUARIOS,
            LOGIN_USUARIOS, 
            COD_FILIAIS FROM dbo.TB_USUARIOS 
            WHERE LOGIN_USUARIOS = '{str(ident)}';

            """
    cursor.execute(consulta_user)
    lista = []
    row = cursor.fetchone()
    while row:
        for i in row:
            lista.append(i)
        row = cursor.fetchone()
    cod_usuario = lista[0]
    login_usuario = lista[1]
    cod_filial_bd = lista[2]

    consulta_banco = f"""
    SELECT IDENT_FILIAIS, 
    SIGLA_FILIAIS, 
    NM_FILIAIS, 
    CNPJ_FILIAIS,
    UF_FILIAIS, 
    COD_DOMINIO, 
    COD_EMPRESAS 
    from dbo.TB_FILIAIS where IDENT_FILIAIS = '{conec.filial}';"""

    conect = pyodbc.connect(dados_conexao)
    cursor = conect.cursor()

    cursor.execute(consulta_banco)
    lista = []
    row = cursor.fetchone()
    while row:
        for i in row:
            lista.append(i)
        row = cursor.fetchone()
    banco_ident_filial = lista[0]
    banco_sigla_filial = lista[1]
    banco_nome_filial = lista[2]
    banco_cnpj_filial = lista[3]
    banco_uf_filial = lista[4]
    banco_cod_dominio = lista[5]
    banco_cod_empresa = lista[6]

    link_n = f'&zeusCodigo={cod_usuario}' \
             f'&zeusNome={login_usuario}' \
             f'&zeusFusoHorario=0' \
             f'&zeusCodigoFilial={cod_filial_bd}' \
             f'&zeusIdentFilial={banco_ident_filial.replace(" ", "")}' \
             f'&zeusSiglaFilial={banco_sigla_filial.replace(" ", "")}' \
             f'&zeusNomeFilial={banco_nome_filial.replace(" ", "")}' \
             f'&zeusCnpjFilial={banco_cnpj_filial.replace(" ", "")}' \
             f'&zeusEstadoFilial={banco_uf_filial.replace(" ", "")}' \
             f'&zeusCodigoDominio={banco_cod_dominio}' \
             f'&zeusCodigoEmpresa={banco_cod_empresa}' \
             f'&zeusPermissoes=9' \
             f'&zeusProgramacaoViagem=10'

    return link_n


banco_dados()
