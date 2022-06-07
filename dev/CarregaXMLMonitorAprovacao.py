"""
Função: Ler um arquivo XML(MonitorAprovacao.xml) e coloca-los em variaveis
Objetivo:
Dependências: Framework BeautifulSoup 4.9.3 (requeriments.txt)
Responsavel: Michel Viana

Histórico:  02/06/2022: Criada estrutura para pegar os dados das tags do XML MonitorAprovacao:
                        self.filial = bs_monitor_aprov.find('Filial').text
                        self.dt_inicial = bs_monitor_aprov.find('DtInicial').getText()
                        self.dt_final = bs_monitor_aprov.find('DtFinal').getText()
                        self.situacao = bs_monitor_aprov.find('Situacao').text
                        self.justificativa = bs_monitor_aprov.find('Justificativa').text
"""

from bs4 import BeautifulSoup

PATH = r'..//parametros'

with open(f'{PATH}\\MonitorAprovacao.xml', 'r') as f:
    data = f.read()
bs_monitor_aprov = BeautifulSoup(data, "xml")


class CarregarXMLMonitorAprovacao:

    def __init__(self):
        # XML MonitorAprovacao
        self.filial = bs_monitor_aprov.find('Filial').text
        self.dt_inicial = bs_monitor_aprov.find('DtInicial').getText()
        self.dt_final = bs_monitor_aprov.find('DtFinal').getText()
        self.situacao = bs_monitor_aprov.find('Situacao').getText()
        self.justificativa = bs_monitor_aprov.find('Justificativa')


monitor_xml = CarregarXMLMonitorAprovacao()




"""
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
"""
