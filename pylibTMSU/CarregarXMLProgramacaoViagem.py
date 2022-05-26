"""
Função: Ler um arquivo XML(ProgramacaoViagem.xml) e coloca-los em variaveis
Objetivo: ter funções para serem usadas em varios trechos
         (dados de uma programação de viagem com rota,
         com data e hora, motorista, reboque e tração
Dependências: Framework BeautifulSoup 4.9.3 (requeriments.txt)
Responsavel: Michel Viana

Histórico: 11/04/2022: criação das funções para leitura do arquivo XML
           12/04/2022: alterado script para pegar dados do banco de dados
           18/04/2022: Inserida classe CarregarXML e reestruturada as funções
           22/04/2022: Alterado a variavel PATH com o caminho relativo
           23/05/2022: Desmembrada funções e variaveis para outros arquivos, mantendo
                       este aquivo com informações para Programação de Viagem
"""

from bs4 import BeautifulSoup




class CarregarXMLProgramacaoViagem:


    def __init__(self):
        # XML Programação de Viagem
        PATH = r'..//parametros'

        with open(f'{PATH}\\ProgramacaoViagem.xml', 'r') as f:
            data = f.read()
        bs_data = BeautifulSoup(data, "xml")
        self.tipo = bs_data.find('Tipo').text
        self.rota = bs_data.find('Rota').text
        self.tracao = bs_data.find('Tracao').text
        self.data_saida = bs_data.find('DataSaida').text
        self.hora_saida = bs_data.find('HoraSaida').text
        self.reboque_1 = bs_data.find('Reboque1').text
        self.reboque_2 = bs_data.find('Reboque2').text
        self.cpf_motorista = bs_data.find('CpfMotorista').text

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


programacao_viagem_xml = CarregarXMLProgramacaoViagem()


