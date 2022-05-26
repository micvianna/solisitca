"""
Função: ()
Objetivo:
Dependências:
Responsavel: Michel Viana

Historico:
"""


# import random
# import sys
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.select import Select

from CarregarXMLManifesto import CarregarXMLManifesto
from InicializarAmbiente import driver, wait

# Constantes criadas
DRIVER = driver
WAIT = wait
global atual

class GerarManifesto:

    def __init__(self):
        xml = CarregarXMLManifesto()
        self.rota = xml.rota_manifesto
        self.tipo = xml.tipo_manifesto
        self.tracao = xml.tracao_maifesto
        self.reboque = xml.reboque_manifesto
        self.motorista = xml.cpf_motorista_manifesto
        self.num_viagem = xml.num_viagem
        self.sub_entrega = xml.sub_entrega
        self.filial_mercadoria = xml.filial_mercadoria
        self.filial_destino = xml.filial_manifesto
        self.sub_transferencia = xml.sub_transferencia

    def carrega_tela_manifesto(self):

        global atual

        try:
            # Acessa a tela Manifesto
            time.sleep(0.5)
            acao = ActionChains(DRIVER)
            DRIVER.find_element(By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002').click()
            time.sleep(1)
            submenu = WAIT.until(
                ec.element_to_be_clickable((By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002-subMenu-menuItem014')))
            acao.click(submenu).perform()
            DRIVER.switch_to.frame('Teste')
            time.sleep(1)
        except Exception as e:
            print(f'Erro ao tentar acessar a tela de Manifesto'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        # Verifica se existe numero da viagem o tipo é igual ENTREGA / COLETA




sub = GerarManifesto()
