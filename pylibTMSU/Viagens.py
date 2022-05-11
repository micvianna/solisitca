"""
Objetivo: Inserir uma viagem para aprovação

Dependências: Framework Selenium 4 (requeriments.txt)
Responsavel: Michel Viana

Histórico:  25/04/2022: Criada a classe AcessarTelaViagens
            26/04/2022: Inserida função: carrega_tela_viagens()
            27/04/2022: Ajuste na carrega_tela_viagens
            28/04/2022: Reescrita a carrega_tela_viagens()
            29/04/2022: Inserido variavel para pegar ID da Viagem
            06/05/2022: Alterado os timers

"""

import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from InicializarAmbiente import driver, wait

# Constante criadas
DRIVER = driver
WAIT = wait

class AcessarTelaViagens:
    # Realiza acessoa a tela de Viagem e realizar a inserção da Viagem

    def carrega_tela_viagens(self):
        global main_page
        time.sleep(5)
        # print('Criação da Viagem, vai ser buscada a Programação de Viagem e vai ser gerado um ID')
        # Após a criação da programação de viagem é acessado a tela de viagem para inserir a programação no sistema
        # trocando para a tela principal
        #browser = DRIVER.window_handles
        #DRIVER.switch_to.window(browser[0])
        acao = ActionChains(DRIVER)
        DRIVER.execute_script("document.body.style.zoom='80%'")
        submenu = WAIT.until(ec.element_to_be_clickable((By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002')))
        acao.click_and_hold(submenu).perform()
        acao.click()
        time.sleep(0.3)

        # acesso submenu 'Viagens'
        viagem = WAIT.until(ec.element_to_be_clickable(
            (By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002-subMenu-menuItem029')))
        acao.move_to_element(viagem).click().perform()
        viagem.click()
        time.sleep(0.3)
        DRIVER.switch_to.frame('Teste')
        anex = WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeViagens_ibtnProgramacaoViagem')))
        if anex.is_displayed():
            anexa = WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeViagens_ibtnProgramacaoViagem')))
            anexa.click()
            print(DRIVER.window_handles)
       

        # 1º Seleção: Programação de Viagem Aprovaaa.
        DRIVER.switch_to.window(DRIVER.window_handles[0])
        print('2', DRIVER.window_handles)
        print(DRIVER.current_window_handle)
        DRIVER.switch_to.window(DRIVER.window_handles[1])
        # DRIVER.execute_script("__doPostBack('dtgProgramacaoViagem$ctl02$ctl00','');")
        selecione = WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione')))
        if selecione.is_displayed():
            DRIVER.execute_script("__doPostBack('dtgProgramacaoViagem$ctl02$ctl00','');")
            time.sleep(1)

            #print(DRIVER.window_handles)

        # 2º Seleção: Tração
        main_page = DRIVER.current_window_handle
        for handle in DRIVER.window_handles:
            if handle != main_page:
                prog = handle
                DRIVER.switch_to.window(prog)
        time.sleep(5)
        # DRIVER.execute_script("__doPostBack('dtgQuery$ctl02$ctl00','');")
        tracao = WAIT.until(ec.invisibility_of_element((By.LINK_TEXT, 'Selecione')))
        if tracao.is_displayed():
            DRIVER.execute_script("__doPostBack('dtgQuery$ctl02$ctl00','');")
            time.sleep(1)


        try:
            # 3º Seleção: Reboque

            print('reboque', DRIVER.window_handles)
            DRIVER.switch_to.window(DRIVER.window_handles[0])
            time.sleep(0.5)
            DRIVER.switch_to.window(DRIVER.window_handles[1])
            time.sleep(1)
            #DRIVER.execute_script("__doPostBack('dtgQuery$ctl02$ctl00','');")
            reboque = WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione')))
            reboque.click()

        except Exception as e:
            driver.quit()
            print('Não Selecionou a Reboque  ')
            print(e.__doc__)
        try:
            # Retorna a pagina principal
            time.sleep(1)
            DRIVER.switch_to.window(DRIVER.window_handles[0])
            DRIVER.switch_to.frame('Teste')
            # Inclui a Viagem
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeViagens_ibtnIncluir'))).click()
            time.sleep(1)
            con = DRIVER.switch_to.alert
            con.accept()
            time.sleep(1)
        except Exception as e:
            driver.quit()
            print(f'Erro ao selecionar itens para consulta de Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')


"""
        try:

            # Abre janela de inclusão de eixo de veiculo
            DRIVER.switch_to.window(DRIVER.window_handles[0])
            time.sleep(0.5)
            DRIVER.switch_to.window(DRIVER.window_handles[1])
            DRIVER.set_window_size(300, 300)
            time.sleep(1)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).click()
            # time.sleep(0.2)
            # WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).clear()
            time.sleep(0.2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).send_keys('3')
            time.sleep(0.2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnQtEixosVeiculos'))).click()
        except Exception as e:
            print('erro aqui')
            print(e.__doc__)
            print(f'Erro ao fechar a escolha'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            time.sleep(5)
            for handle in DRIVER.window_handles:
                if handle == main_page:
                    clique = handle
                    DRIVER.switch_to.window(clique)

            numId = WAIT.until(ec.element_to_be_clickable((By.ID, "lblNrViagem")))
            numId.click()
            time.sleep(5)
            texto = numId.text
            print(f'Viagem ID: {str(texto)}')
     

        except Exception as e:
            print('erro aqui')
            print(e.__doc__)
            print(f'Erro ao tentar pegar ID Viagens'
                  f'\\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # DRIVER.quit()
            # sys.exit()

"""

viagem = AcessarTelaViagens()

