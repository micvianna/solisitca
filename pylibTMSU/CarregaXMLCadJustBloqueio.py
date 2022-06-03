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

with open(f'{PATH}\\CadastrarJustificativaBloqueio.xml', 'r') as f:
    data = f.read()
bs_cad_just_bloq = BeautifulSoup(data, "xml")


class CarregarXMLCadJustBloqueio:

    def __init__(self):
        # XML MonitorAprovacao
        self.excluido = bs_cad_just_bloq.find('Excluido').getText()
        self.complemento = bs_cad_just_bloq.find('ComplementoObrigatorio').getText()
        self.descricao = bs_cad_just_bloq.find('Descricao').getText()



just_bloqueio = CarregarXMLCadJustBloqueio()