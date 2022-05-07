"""
Objetivo: Inserir uma viagem para aprovação

Dependências: Framework Selenium 4 (requeriments.txt)
Responsavel: Michel Viana

Histórico:  25/04/2022: Criada a classe AcessarTelaViagens
            26/04/2022: Inserida função: carrega_tela_viagens()
            27/04/2022: Ajuste na carrega_tela_viagens
            28/04/2022: Reescrita a carrega_tela_viagens()
            29/04/2022: Inserido variavel para pegar ID da Viagem
            06/05/2022: Alterado

"""

import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from InicializarAmbiente import driver, wait

# Constante criadas
DRIVER = driver
WAIT = wait


class AcessarTelaViagens:
    # Realiza acessoa a tela de Viagem e realizar a inserção da Viagem

    def carrega_tela_viagens(self):
        # print('Criação da Viagem, vai ser buscada a Programação de Viagem e vai ser gerado um ID')
        # Após a criação da programação de viagem é acessado a tela de viagem para inserir a programação no sistema
        # trocando para a tela principal


        try:
            # acesso submenu 'Viagens'

            #DRIVER.switch_to.window(DRIVER.window_handles[1])
            time.sleep(0.3)
            menu = WAIT.until(ec.element_to_be_clickable(By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002'))
            menu.click()
            time.sleep(0.3)
            viagem = WAIT.until(ec.element_to_be_clickable(By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002-subMenu-menuItem029'))
            viagem.click()
            time.sleep(0.3)
            # DRIVER.get('http://nshm0001.expresso.corp/NewSitex/Paginas/Operacoes/Viagens/Viagens.aspx')
            # clique no Anexar
            anexa = WAIT.until(ec.element_to_be_clickable(By.ID, 'EJRodapeViagens_ibtnProgramacaoViagem'))
            anexa.click()
            time.sleep(2)

            # 1º Seleção: Programação de Viagem Aprovaaa

            main_page = driver.current_window_handle
            for handle in driver.window_handles:
                if handle != main_page:
                    aprova = handle
                    driver.switch_to.window(aprova)
            DRIVER.find_element(By.CSS_SELECTOR, '#dtgProgramacaoViagem > tbody > tr.linha_tabela ')
        except Exception as e:
            print(f'Erro ao acessar tela de Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            # 2º Seleção: Tração

            WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione'))).click()
            time.sleep(2)
            for handle in driver.window_handles:
                if handle != main_page:
                    reboque = handle
                    driver.switch_to.window(reboque)

            # 3º Seleção: Reboque 1

            WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione'))).click()
            time.sleep(2)
            list = driver.window_handles
            for handle in driver.window_handles:
                if handle != main_page:
                    viagem = handle
                    driver.switch_to.window(viagem)
            WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione'))).click()
            time.sleep(2)
            # Retorna a pagina principal
            DRIVER.switch_to.window(list[0])
            # Inclui a Viagem
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeViagens_ibtnIncluir'))).click()
            time.sleep(2)
            con = DRIVER.switch_to.alert
            con.accept()
            time.sleep(2)
        except Exception as e:
            print(f'Erro ao selecionar itens para consulta de Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')


        try:

            # Abre janela de inclusão de eixo de veiculo
            for handle in driver.window_handles:
                if handle != main_page:
                    eixo = handle
                    driver.switch_to.window(eixo)
            DRIVER.set_window_size(300, 300)
            time.sleep(2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).clear()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).send_keys('1')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnQtEixosVeiculos'))).click()
        except Exception as e:
            print('erro aqui')
            print(e.__doc__)
            print(f'Erro ao fechar a escolha'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            time.sleep(5)
            for handle in driver.window_handles:
                if handle == main_page:
                    clique = handle
                    driver.switch_to.window(clique)

            numId = WAIT.until(ec.element_to_be_clickable((By.ID, "lblNrViagem")))
            numId.click()
            time.sleep(5)
            texto = numId.text
            print(f'Viagem ID: {str(texto)}')

        except Exception as e:
            print('erro aqui')
            print(e.__doc__)
            print(f'Erro ao tentar pegar ID Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()



viagem = AcessarTelaViagens()

