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
           17/05/2022: Atualizada a função: realizar_logoff

"""

import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from CarregarXMLConexao import CarregarXMLConexao

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


class LoginIn:
    """
    Criada class para realizar abertura de browser e login
    """

    def __init__(self):
        # variaveis referencidas do
        xml = CarregarXMLConexao()
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
            # url = f'http://nsac0001.expresso.corp/NewSitex/Login.aspx'
            # Maximila o driver
            driver.maximize_window()
            # acessa a url
            driver.get(f'{self.url}NewSitex/Login.aspx')
            # aguarda em milesimos
            time.sleep(1.5)
        except Exception as e:
            print(f'Não foi incializado o Navegador'
                  f' Ocorreu algo inesperdado -----> {str(e.__doc__)}')
            # sys.exit()

    def realizar_login(self, filial=''):
        """
        Função criada para logar no TMSU
        usuario: nome do usuario é passado por parametro indicado quando a função é invocada
        senha: dados de senha é passado por parametro indicado quando a função é invocada
        filial: filial é passda por parametro indicado quando a função é invocada
        """
        try:
            if filial == '':
                filial = self.filial
            else:
                pass
            wait.until(ec.element_to_be_clickable((By.ID, 'txtUsuario')))
            # insere o usuário que está no arquivo Conexão XML
            user = driver.find_element(By.ID, 'txtUsuario')
            user.send_keys(self.usuario)
            wait.until(ec.element_to_be_clickable((By.ID, 'txtSenha')))
            # insere o password que está no arquivo Conexão XML
            driver.find_element(By.ID, 'txtSenha').send_keys(self.password)
            # insere a filial que está no arquivo Conexão XML
            driver.find_element(By.ID, 'selFiliais').send_keys(filial)
            driver.find_element(By.ID, 'selFiliais').send_keys(Keys.ENTER)
            # clica no botão login
            driver.find_element(By.ID, 'btnLogin').click()
            # print('Nome da page: ', atual)
            # time.sleep(3)
        except Exception as e:
            print(f'Nome do Usuário ou Senha invalidos, revise-os'
                  f'\n\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.close()
            # sys.exit()

    def realizar_logoff(self):
        """
        Quando está em outra aba no TMSU é trocada para
        a aba onde driver vai achar o botão sair
        """
        try:
            # Alterna para a janela principal
            driver.switch_to.window(driver.window_handles[0])
            # Alterna para o frame
            driver.switch_to.parent_frame()
            # verifica se o menu está visivel
            menu = wait.until(ec.all_of(By.CSS_SELECTOR, '#EJCabecalho1_EJMenu1__skmMenu'))
            if menu.is_displayed():
                if driver.find_element(By.CSS_SELECTOR, '#EJCabecalho1_EJMenu1__skmMenu').is_displayed():
                    print('Fazendo Logoff')
                    time.sleep(1)
                    acao = ActionChains(driver)
                    driver.find_element(By.CSS_SELECTOR, '#EJCabecalho1_EJMenu1__skmMenu')
                    time.sleep(1)
                    submenu = wait.until(
                        ec.element_to_be_clickable(
                            (By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem009')))
                    acao.click(submenu).perform()
                    time.sleep(2)
                    # driver.switch_to.frame('Teste')
                    Alert(driver).accept()
                    time.sleep(0.2)
                    Alert(driver).accept()
                    time.sleep(0.5)
                    time.sleep(1)
                else:
                    print('Não fez logoff corretamente')
                    driver.quit()
            else:
                pass
        except Exception as e:
            print(f'Logoff não realizado'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # sys.exit()

    def fechar_browser(self):
        """
        fecha o browser
        """
        driver.quit()


"""
#########
Configurações para colocar o Edge em modo IE
#########
ieOptions = webdriver.IeOptions()
ieOptions.add_additional_option("ie.edgechromium", True)
ieOptions.ensure_clean_session = True
ieOptions.ignore_protected_mode_settings = True
ieOptions.add_additional_option("ie.edgepath", 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
#########
"""

# Descomentando a linha de baixo faz a chamada a do Internet Explorer (Modo Ie)
# driver = webdriver.Ie(executable_path=r'../bin/IEDriverServer.exe', options=ieOptions)
driver = webdriver.Edge(executable_path="../bin/msedgedriver.exe")
wait = WebDriverWait(driver, 15, poll_frequency=0.5)
inicia = LoginIn()

