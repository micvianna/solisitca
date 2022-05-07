import random
from datetime import timedelta, date
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        self.hora_de_saida = xml.hora_saida
        self.user = xml.usuario
        self.senha = xml.password

    def carrega_tela_manifesto(self):
        try:
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002'))).click()
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((
                By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002-subMenu-menuItem014'))).click()
            time.sleep(5)
            print('teste 1', DRIVER.window_handles)
            teste = DRIVER.current_window_handle
            print(teste)
            # DRIVER.switch_to.window(teste)
            # print(DRIVER.page_source)
            # clic = WAIT.until(ec.invisibility_of_element((By.ID, 'pnlViagem')))
            # print(str(clic))
            # DRIVER.execute_script("document.querySelector('img#imgViagem.imagem').click();")
            DRIVER.execute_script("window.open('/NewSitex/Paginas/Operacoes/Viagens/ViagensPerformance.aspx',"
                                "'Viagens','height=250,width=950');")

            print('teste 2', DRIVER.window_handles)
            print('atual janela', teste)
            """
            time.sleep(1)
            # Troca de Janela
            main_page = DRIVER.current_window_handle
            for handle in DRIVER.window_handles:
                if handle != main_page:
                    main = handle
                    DRIVER.switch_to.window(main)
                    DRIVER.set_window_size(950, 330)
                """
        except Exception as e:
            print(e)
            print('--------')
            print(f'Erro ao tentar acessar a tela de Manifesto'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            # Preenche os campos
            # DRIVER.execute_script(
            #    "window.open('/NewSitex/Paginas/Operacoes/Viagens/ViagensPerformance.aspx','Viagens','height=250,width=950');")
            atual = DRIVER.window_handles
            DRIVER.switch_to.window(atual[1])
            time.sleep(0.7)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_txtValueColumn'))).click()

            rand = random.randint(1, 14)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_txtValueColumn'))).send_keys(str(rand))
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_btnProcurar'))).click()
            time.sleep(0.7)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).send_keys(
                self.tracao)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_btnProcurar'))).click()
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosReboque_txtValueColumn'))).click()
            # WAIT.until(ec.element_to_be_clickable((By.ID,
            # 'EJProcuraDadosReboque_txtValueColumn'))).send_keys(self.reboque)
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosReboque_btnProcurar'))).click()
            time.sleep(0.7)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosMotorista_txtValueColumn'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID,
                                                   'EJProcuraDadosMotorista_txtValueColumn'))).send_keys(self.motorista)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosMotorista_btnProcurar'))).click()
            time.sleep(0.7)
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada').click()
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada').clear()
            hoje = (date.today() + timedelta(days=1))
            amanha = str(hoje.strftime('%d/%m/%Y'))

            um = random.randint(1, 2)

            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).clear()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(1)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(':')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(1)
            time.sleep(0.7)
            doi = random.randint(1, 2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).clear()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(':')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(2)
            time.sleep(0.7)
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'txtKmInicialReboque'))).send_keys('1')
            time.sleep(1)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnVerificacao'))).click()
            time.sleep(1)
            # acpt = DRIVER.switch_to.alert
            # acpt.accept()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnIncluir'))).click()
            DRIVER.switch_to.window(DRIVER.window_handles[1])
            time.sleep(3)
            acpt = DRIVER.switch_to.alert
            acpt.accept()
            # DRIVER.execute_script('window.close();')
            # print('Janelas Atuis: ', DRIVER.current_window_handle)


        except Exception as e:
            print(e.__doc__)
            print('--------')
            print(f'Erro ao tentar acessar a tela de Manifesto'
                  f'--------'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

sub = GerarManifesto()


class Manifesto:

    def __init__(self):
        xml = CarregarXML()
        self.rota = xml.programacao_viagem_rota()
        self.tracao = xml.programacao_viagem_tracao()
        self.reboque = xml.programacao_viagem_reboque1()
        self.motorista = xml.cpf_motorista
        self.hora_de_saida = xml.hora_saida
        self.user = xml.usuario
        self.senha = xml.password

    def carrega_outro(self):
        try:
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002'))).click()
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((
                By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002-subMenu-menuItem014'))).click()
            time.sleep(1)
            print('teste 1', DRIVER.window_handles)
            teste = DRIVER.current_window_handle
            print(teste)
            # DRIVER.switch_to.window(teste)
            # print(DRIVER.page_source)

            DRIVER.execute_script('window.open("/NewSitex/Paginas/Operacoes/Viagens/ViagensPerformance.aspx");')


            #WAIT.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'img#imgViagem'))).click()
            print('teste 2', DRIVER.window_handles)
            print('atual janela', teste)

        except Exception as e:
            print(e)
            print('--------')
            print(f'Erro ao tentar acessar a tela de Manifesto'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            # Preenche os campos
            # DRIVER.execute_script(
            #    "window.open('/NewSitex/Paginas/Operacoes/Viagens/ViagensPerformance.aspx','Viagens','height=250,width=950');")
            atual = DRIVER.window_handles
            DRIVER.switch_to.window(atual[1])
            time.sleep(0.7)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_txtValueColumn'))).click()

            rand = random.randint(1, 14)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_txtValueColumn'))).send_keys(str(rand))
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_btnProcurar'))).click()
            time.sleep(0.7)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).send_keys(self.tracao)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_btnProcurar'))).click()
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosReboque_txtValueColumn'))).click()
            # WAIT.until(ec.element_to_be_clickable((By.ID,
            # 'EJProcuraDadosReboque_txtValueColumn'))).send_keys(self.reboque)
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosReboque_btnProcurar'))).click()
            time.sleep(0.7)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosMotorista_txtValueColumn'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID,
                                                   'EJProcuraDadosMotorista_txtValueColumn'))).send_keys(self.motorista)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosMotorista_btnProcurar'))).click()
            time.sleep(0.7)
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada').click()
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada').clear()
            hoje = (date.today() + timedelta(days=1))
            amanha = str(hoje.strftime('%d/%m/%Y'))

            um = random.randint(1, 2)

            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).clear()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(1)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(':')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(1)
            time.sleep(0.7)
            doi = random.randint(1, 2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).clear()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(':')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(str(rand))
            time.sleep(0.7)
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'txtKmInicialReboque'))).send_keys('1')
            time.sleep(1)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnVerificacao'))).click()
            time.sleep(1)
            # acpt = DRIVER.switch_to.alert
            # acpt.accept()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnIncluir'))).click()
            DRIVER.switch_to.window(DRIVER.window_handles[1])
            time.sleep(3)
            acpt = DRIVER.switch_to.alert
            acpt.accept()
            print('Janelas Atuis: ', DRIVER.current_window_handle)
            time.sleep(2)
            # DRIVER.switch_to.window(DRIVER.window_handles[0])
            # DRIVER.quit()
            # DRIVER.execute_script('window.close();')


        except Exception as e:
            print(e.__doc__)
            print('--------')
            print(f'Erro ao tentar acessar a tela de Manifesto'
                  f'--------'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

# sub = Manifesto()