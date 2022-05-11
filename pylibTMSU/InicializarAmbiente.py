"""
Objetivo: Criar um login para o usuário, extraindo
          motorista, reboque e tração
Dependências: Framework Selenium 4, pylibTMSU.LerProgramacaoViagem
Responsavel: Michel Viana

Histórico: 12/04/2022: Desenvolvido chamada do Browser e a realização de login
           13/04/2022: Desenvolvido função para chamada realização do logoff
           18/04/2022: Inserida classe LoginIn e reestruturada as funções
           20/04/2022: Adicionado mensagens de tratamento quando houver erros
                       Inserida classe FinalizandoAmbiente
"""

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from LerProgramacaoViagem import CarregarXML

"""
---- Chamada do Browser na variavel 'driver' ------
Está dentro deste script os dois browsers (Edge e IE).Por padrão 
estamos executando o EDGE, mas caso queira usar o IE descomentar
a linha.
# driver = webdriver.Ie(executable_path=r'bin\\IEDriverServer.exe')
Microsoft Edge
# driver = webdriver.Edge(executable_path=r'../bin/msedgedriver.exe')
"""
# variavel crida para chamar o arquvivo 'LerProgramacaoViagem'
# onde foi importado um modulo

xml = CarregarXML()


class LoginIn:
    """
    Criada class para realizar abertura de browser e login
    """

    def __init__(self):
        # variaveis referencidas do 'LerProgramacaoViagem '
        self.driver = driver
        self.url = xml.url_ambiente()
        self.usuario = xml.usuario_login()
        self.password = xml.password_login()
        self.filial = xml.filial_login()

    def abrir_browser(self):
        """
        Abre o browser e está determinando o tamanho deste
        pegando a url(self.url) que está no xml
        """
        try:
            driver.maximize_window()  # mudar o zoom o
            driver.get(self.url)
            time.sleep(0.5)
        except Exception as e:
            print(f'Não foi incializado o Navegador'
                  f'Ocorreu algo inesperdado -----> {str(e.__doc__)}')
            # sys.exit()

    def realizar_login(self):
        """
        Função criada para logar no TMSU
        usuario: nome do usuario é passado por parametro indicado quando a função é invocada
        senha: dados de senha é passado por parametro indicado quando a função é invocada
        filial: filial é passda por parametro indicado quando a função é invocada
        """
        try:

            wait.until(ec.element_to_be_clickable((By.ID, 'txtUsuario')))
            driver.find_element(By.ID, 'txtUsuario').send_keys(self.usuario)
            wait.until(ec.element_to_be_clickable((By.ID, 'txtSenha')))
            driver.find_element(By.ID, 'txtSenha').send_keys(self.password)
            driver.find_element(By.ID, 'selFiliais').send_keys(self.filial)
            driver.find_element(By.ID, 'selFiliais').send_keys(Keys.ENTER)
            driver.find_element(By.ID, 'btnLogin').click()
            window = driver.window_handles[0]
            print('first page Login ', driver.current_window_handle)
            # time.sleep(3)
        except Exception as e:
            print(f'Nome do Usuário ou Senha invalidos, revise-os'
                  f'\n\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.close()
            # sys.exit()


class FinalizandoAmbiente:
    """
    Criada class para finalizar o ambiente
    1º Realizando logoff
    2º fechando o browser
    """

    def realizar_logoff(self):
        """
        Quando está em outra aba no TMSU é trocada para
        a aba onde driver vai achar o botão sair
        """
        main_page = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != main_page:
                sair = handle
                driver.switch_to.window(sair)
        try:
            time.sleep(2)
            driver.find_element(By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem012').click()
            time.sleep(0.2)
            Alert(driver).accept()
            time.sleep(0.2)
            Alert(driver).accept()
            time.sleep(0.5)
        except Exception as e:
            print(f'Logoff não realizado'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # sys.exit()

    def fechar_browser(self):
        """
        fecha o browser
        """
        driver.quit()


ieOptions = webdriver.IeOptions()

ieOptions.add_additional_option("ie.edgechromium", True)
# ieOptions.ensure_clean_session = True
ieOptions.ignore_protected_mode_settings = True
ieOptions.add_additional_option("ie.edgepath", 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
driver = webdriver.Ie(executable_path=r'../bin/IEDriverServer.exe', options=ieOptions)

# driver = webdriver.Edge(executable_path="../bin/msedgedriver.exe")
wait = WebDriverWait(driver, 15, poll_frequency=0.5)
inicia = LoginIn()
logoff = FinalizandoAmbiente()
