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
"""

from bs4 import BeautifulSoup

PATH = r'..//parametros'

with open(f'{PATH}\\ProgramacaoViagem.xml', 'r') as f:
    data = f.read()
bs_data = BeautifulSoup(data, "xml")

with open(f'{PATH}\\Conexao.xml', 'r') as f:
    data = f.read()
bs_conec = BeautifulSoup(data, "xml")


class CarregarXML:

    def __init__(self):
        self.usuario = bs_conec.find('Login').text
        self.password = bs_conec.find('Senha').text
        self.url = bs_conec.find('URL_Aplicacao').text
        self.filial = bs_conec.find('Filial_login').text
        self.tipo = bs_data.find('Tipo').text
        self.rota = bs_data.find('Rota').text
        self.tracao = bs_data.find('Tracao').text
        self.data_saida = bs_data.find('DataSaida').text
        self.hora_saida = bs_data.find('HoraSaida').text
        self.reboque_1 = bs_data.find('Reboque1').text
        self.reboque_2 = bs_data.find('Reboque2').text
        self.cpf_motorista = bs_data.find('CpfMotorista').text

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
        return self.url

    def filial_login(self):
        # faz chamada da filial no arquivo conexao.XML
        return self.filial

    def programacao_viagem_tipo(self):
        # faz chamada do tipo no XML
        return self.tipo

    def programacao_viagem_rota(self):
        # faz chamada da rota no XML
        return self.rota

    def programacao_viagem_tracao(self):
        # faz chamada do recurso tracao no XML
        return self.tracao

    def programacao_viagem_data_saida(self):
        # faz a chamada da data de saída no XML
        return self.data_saida

    def programacao_viagem_hora_saida(self):
        # faz a chamada da data de saída no XML
        return self.hora_saida

    def programacao_viagem_reboque1(self):
        # faz chamada do recurso reboque 1 no XML
        return self.reboque_1

    def programacao_viagem_reboqque2(self):
        # faz chamada do recurso reboque 2 no XML
        return self.reboque_2

    def programacao_viagem_cpf_motorista(self):
        # faz chamada do cpf do motorista no XML
        return self.cpf_motorista

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


inicio = CarregarXML()
