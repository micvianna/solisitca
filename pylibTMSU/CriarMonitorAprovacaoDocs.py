import time

from selenium.webdriver.common.alert import Alert

from pylibTMSU.CarregarXMLConexao import CarregarXMLConexao, banco_dados
from pylibTMSU.InicializarAmbiente import driver, wait, inicia
from pylibTMSU.CarregaXMLMonitorAprovacao import monitor_xml
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Constantes criadas
DRIVER = driver
WAIT = wait


class MonitorAprovaDocumento:

    def __init__(self):

        # variaveis de chamada de classe
        conec = CarregarXMLConexao()

        self.link = banco_dados()
        self.url = conec.url_ambiente()
        self.filial_concexao = conec.filial
        self.filial_monitor = monitor_xml.filial
        self.data_saida = monitor_xml.dt_inicial
        self.data_final = monitor_xml.dt_final
        self.situacao = monitor_xml.situacao

    def carrega_tela_monitor_aprova_doc_sub(self):

        try:
            # Acessa a tela Monitor Aprovação Documentos Subcontratada
            # Acesso para tela de Monitor Aprovação Documentos Subcontratada atraves do link
            url = f'{self.url}/Femsa.Zeus/MonitorAprovacaoDocumentosSubcontratadas?cod=706{self.link}'
            DRIVER.get(url)
            time.sleep(0.5)
        except Exception as e:
            print(f'Erro ao tentar Acesso para tela de Monitor Aprovação Documentos subcontratada atraves do link'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            if self.filial_monitor == '':
                pass
            else:
                filial = self.filial_monitor
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Filial'))).click()
                time.sleep(0.5)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Filial'))).send_keys(filial)
                time.sleep(0.5)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Filial'))).send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Filial'))).send_keys(Keys.ENTER)
                time.sleep(0.4)
        except Exception as e:
            print(f'Erro ao inserir a filial'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            #  Informa Data de Inicio
            WAIT.until(ec.element_to_be_clickable((By.ID, 'DataInicio'))).click()
            time.sleep(0.4)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'DataInicio'))).clear()
            time.sleep(0.4)
            WAIT.until(ec.element_to_be_clickable(
                (By.ID, 'DataInicio'))).send_keys(self.data_saida)
            time.sleep(0.4)
        except Exception as e:
            print(f'Erro ao selecionar a Data Inicio'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            #  Informa Data de Final
            time.sleep(0.4)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'DataFinal'))).click()
            time.sleep(0.4)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'DataFinal'))).clear()
            time.sleep(0.4)
            WAIT.until(ec.element_to_be_clickable(
                (By.ID, 'DataFinal'))).send_keys(self.data_final)
            time.sleep(0.4)
        except Exception as e:
            print(f'Erro ao selecionar a Data Inicio'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            #  Informar Situação
            time.sleep(0.2)
            situacao = self.situacao
            try:
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Situacao'))).click()
                if len(str(situacao)) > 8:
                    WAIT.until(ec.element_to_be_clickable(
                        (By.ID, 'Situacao'))).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
                    time.sleep(0.2)
                elif str(situacao) == 'Aprovado':
                    for i in range(2):
                        WAIT.until(ec.element_to_be_clickable(
                            (By.ID, 'Situacao'))).send_keys(Keys.ARROW_DOWN)
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'Situacao'))).send_keys(Keys.ENTER)
                    time.sleep(0.2)
                elif str(situacao) == 'Recusado':
                    for i in range(3):
                        WAIT.until(ec.element_to_be_clickable(
                            (By.ID, 'Situacao'))).send_keys(Keys.ARROW_DOWN)
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'Situacao'))).send_keys(Keys.ENTER)
                    time.sleep(0.2)
                else:
                    pass
            except Exception as e:
                print(f'Erro ao tentar usar uma Situação'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        except Exception as e:
            print(f'Erro ao tentar usar uma Situação'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        # Botão pesquisar
        try:
            #  Informa Data de Inicio
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnPesquisar'))).click()
            time.sleep(0.2)
        except Exception as e:
            print(f'Erro ao Pesquisar'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            #  Grid do resultado
            result = WAIT.until(ec.element_to_be_clickable(
                (By.ID, 'ContainerGrid')))
            result2 = WAIT.until(ec.element_to_be_clickable(
                (By.ID, 'GridViagens')))
            detalhes = WAIT.until(ec.element_to_be_clickable(
                (By.ID, 'btnExibirDetalhes')))
            if result.is_displayed():
                print('sim')
                if result2.is_displayed():
                    time.sleep(0.2)
                    detalhes.click()
                else:
                    print('deu ruim')
                    pass
            else:
                print('naõ')
                time.sleep(0.2)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnPesquisar'))).click()
            time.sleep(0.2)
        except Exception as e:
            print(f'Erro ao Pesquisar'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')


monior = MonitorAprovaDocumento()

