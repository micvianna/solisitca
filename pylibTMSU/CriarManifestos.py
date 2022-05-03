


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from LerProgramacaoViagem import CarregarXML

from InicializarAmbiente import driver, wait

# Constantes criadas
DRIVER = driver
WAIT = wait


class GerarManifesto:

        def __init__(self):
            xml = CarregarXML()
            self.rota = xml.programacao_viagem_rota()
            self.tracao = xml.programacao_viagem_tracao()
            self.reboque = xml.programacao_viagem_reboque1()
            self.motorista = xml.cpf_motorista


        def carrega_tela_manifesto(self):
            try:
                time.sleep(2)
                # DRIVER.execute_script("window.open('/NewSitex/Paginas/Operacoes/Baixas/BaixaManifestos.aspx?")
                DRIVER.execute_script("window.location.href =('/NewSitex/Paginas/Operacoes/Manifestos.aspx?');")
                time.sleep(1)
                DRIVER.find_element(By.ID, 'imgViagem').click()
                time.sleep(1)
                main_page = DRIVER.current_window_handle
                for handle in DRIVER.window_handles:
                    if handle != main_page:
                        viagem = handle
                        driver.switch_to.window(viagem)
                        driver.set_window_size(950,330)

            except Exception as e:
                print(e)
                print('--------')
                print(f'Erro ao tentar acessar a tela de Manifesto'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

            try:
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'EJProcuraDadosRota_txtValueColumn').click()
                DRIVER.find_element(By.ID, 'EJProcuraDadosRota_txtValueColumn').send_keys('01')
                DRIVER.find_element(By.ID, 'EJProcuraDadosRota_btnProcurar').click()
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'EJProcuraDadosTracao_txtValueColumn').click()
                DRIVER.find_element(By.ID, 'EJProcuraDadosTracao_txtValueColumn').send_keys(self.tracao)
                DRIVER.find_element(By.ID, 'EJProcuraDadosTracao_btnProcurar').click()
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'EJProcuraDadosReboque_txtValueColumn').click()
                DRIVER.find_element(By.ID, 'EJProcuraDadosReboque_txtValueColumn').send_keys(self.reboque)
                DRIVER.find_element(By.ID, 'EJProcuraDadosReboque_btnProcurar').click()
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'EJProcuraDadosMotorista_txtValueColumn').click()
                DRIVER.find_element(By.ID, 'EJProcuraDadosMotorista_txtValueColumn').send_keys(self.motorista)
                DRIVER.find_element(By.ID, 'EJProcuraDadosMotorista_btnProcurar').click()
            except Exception as e:
                print(e)
                print('--------')
                print(f'Erro ao tentar acessar a tela de Manifesto'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')



sub = GerarManifesto()

