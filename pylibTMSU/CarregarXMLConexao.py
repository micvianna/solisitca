"""
Função: Ler um arquivo XML(ProgramacaoViagem.xml) e coloca-los em variaveis
Objetivo: ter funções para serem usadas em varios trechos
         (dados de uma programação de viagem com rota,
         com data e hora, motorista, reboque e tração
Dependências: Framework BeautifulSoup 4.9.3 (requeriments.txt)
Responsavel: Michel Viana

Histórico: 11/04/2022: criação das funções para leitura do arquivo XML
           12/04/2022: alterado script para pegar dados do banco de dados
           18/04/2022 - Inserida classe CarregarXML e reestruturada as funções
           22/04/2022: Alterado a variavel PATH com o caminho relativo
           13/05/2022: Adicioando variaveis:
                        self.filial_mercadoria = bs_data.find('FilialRetiraMercadoria').text
                        self.sub_transferencia = bs_data.find('SubTransferencia').text
                        self.sub_entrega = bs_data.find('SubEntrega').text
                        self.viagem = bs_data.find('Viagem')
           16/05/2022: Adiconado Funções
           17/05/2022: Criada estrutura para pegar os dados das tags do XML Manifesto:
                        self.tipo_manifesto = bs_mani.find('Tipo').text
                        self.rota_manifesto = bs_mani.find('Rota').text
                        self.tracao_maifesto = bs_mani.find('Tracao').text
                        self.reboque_manifesto = bs_mani.find('Reboque').text
                        self.cpf_motorista_manifesto = bs_mani.find('CpfMotorista').text
                        self.filial_mercadoria = bs_mani.find('FilialRetiraMercadoria').text
                        self.sub_transferencia = bs_mani.find('SubTransferencia').text
                        self.sub_entrega = bs_mani.find('SubEntrega').text
                        self.viagem = bs_mani.find('Viagem').text
                        self.viagem_id = bs_mani.find('IdViagem').text
"""

from bs4 import BeautifulSoup

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


