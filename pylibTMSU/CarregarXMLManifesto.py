"""
Função: Ler um arquivo XML(Manifeto.xml) e coloca-los em variaveis
Objetivo: ter funções para serem usadas em varios trechos
         (dados de uma programação de viagem com rota,
         com data e hora, motorista, reboque e tração
Dependências: Framework BeautifulSoup 4.9.3 (requeriments.txt)
Responsavel: Michel Viana

Histórico:  18/05/2022: Criada estrutura para pegar os dados das tags do XML Manifesto:
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

with open(f'{PATH}\\Manifesto.xml', 'r') as f:
    data = f.read()
bs_mani = BeautifulSoup(data, "xml")


class CarregarXMLManifesto:

    def __init__(self):
        # XML Manifesto
        self.tipo_manifesto = bs_mani.find('Tipo').text
        self.rota_manifesto = bs_mani.find('Rota').text
        self.tracao_manifesto = bs_mani.find('Tracao').text
        self.reboque_manifesto = bs_mani.find('Reboque').text
        self.cpf_motorista_manifesto = bs_mani.find('CpfMotorista').text
        self.num_viagem = bs_mani.find('NumViagem').text
        self.filial_manifesto_destino = bs_mani.find('FilalDestino').text
        self.filial_retira_mercadoria = bs_mani.find('FilialRetiraMercadoria').text
        self.sub_transferencia = bs_mani.find('SubTransferencia').text
        self.sub_entrega = bs_mani.find('SubEntrega').text

    def tipo_manifesto(self):
        # Faz a chamada da tag "CpfMotorista" no XML Manifesto
        return self.tipo_manifesto

    def rota_manifesto(self):
        # Faz a chamada da tag "Rota" no XML Manifesto
        return self.rota_manifesto

    def tracao_manifesto(self):
        # Faz a chamada da tag "Tracao" no XML Manifesto
        return self.tracao_manifesto

    def reboque_manifesto(self):
        # Faz a chamada da tag "CpfMotorista" no XML Manifesto
        return self.reboque_manifesto

    def cpf_motorista_manifesto(self):
        # Faz a chamada da tag "CpfMotorista" no XML Manifesto
        return self.cpf_motorista_manifesto

    def num_viagem(self):
        # Faz a chamada da tag "IdViagem"
        return self.num_viagem

    def filial_manifesto_destino(self):
        # Faz a chamada da tag "FilalDestino" no XML Manifesto
        return self.filial_manifesto_destino

    def filial_retira_mercadoria(self):
        # Faz a chamada da etiqueta "FilialRetiraMercadoria"
        return self.filial_retira_mercadoria

    def sub_transferencia(self):
        # Faz a chamada da tag "SubTransferencia"
        return self.sub_transferencia

    def sub_entrega(self):
        # Faz a chamada da tag "SubEntrega"
        return self.sub_entrega

    def filial_manifesto(self):
        # Faz a chamada da tag "filial_manifesto" do XML  Manifesto
        return self.filial_manifesto


manifesto_xml = CarregarXMLManifesto()
