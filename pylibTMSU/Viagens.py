"""
Objetivo: Inserir uma viagem para aprovação

Dependências: Framework Selenium 4 (requeriments.txt)
Responsavel: Michel Viana

Histórico:  25/04/2022: Criada a classe AcessarTelaViagens
            26/04/2022: Inserida função: carrega_tela_viagens()
            27/04/2022: Ajuste na carrega_tela_viagens
            28/04/2022: Reescrita a carrega_tela_viagens()
            29/04/2022: Inserido variavel para pegar ID da Viagem

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
    time.sleep(6)

    def carrega_tela_viagens(self):
        # print('Criação da Viagem, vai ser buscada a Programação de Viagem e vai ser gerado um ID')
        # Após a criação da programação de viagem é acessado a tela de viagem para inserir a programação no sistema
        # trocando para a tela principal

        main_page = DRIVER.current_window_handle
        for handle in DRIVER.window_handles:
            if handle != main_page:
                prog = handle
                DRIVER.switch_to.window(prog)
                DRIVER.maximize_window()

        time.sleep(2)
        try:
            # acesso submenu 'Viagens'
            DRIVER.get('http://nshm0001.expresso.corp/NewSitex/Paginas/Operacoes/Viagens/Viagens.aspx')
            # clique no Anexar

            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeViagens_ibtnProgramacaoViagem'))).click()
            time.sleep(2)

            # 1º Seleção: Programação de Viagem Aprovaaa

            main_page = driver.current_window_handle
            for handle in driver.window_handles:
                if handle != main_page:
                    aprova = handle
                    driver.switch_to.window(aprova)
            DRIVER.find_element(By.CSS_SELECTOR, '#dtgProgramacaoViagem > tbody > tr.linha_tabela ')

            # 2º Seleção: Tração

            WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione'))).click()
            time.sleep(2)
            for handle in driver.window_handles:
                if handle != main_page:
                    reboque = handle
                    driver.switch_to.window(reboque)

            # 3º Seleção: Reboque 1

            DRIVER.find_element(By.LINK_TEXT, 'Selecione').click()
            time.sleep(2)
            list = driver.window_handles
            for handle in driver.window_handles:
                if handle != main_page:
                    viagem = handle
                    driver.switch_to.window(viagem)
            DRIVER.find_element(By.LINK_TEXT, 'Selecione').click()
            time.sleep(2)
            # Retorna a pagina principal
            DRIVER.switch_to.window(list[0])
            # Inclui a Viagem
            DRIVER.find_element(By.ID, 'EJRodapeViagens_ibtnIncluir').click()
            time.sleep(2)
            con = DRIVER.switch_to.alert
            con.accept()
            time.sleep(2)

            # Abre janela de inclusão de eixo de veiculo
            for handle in driver.window_handles:
                if handle != main_page:
                    eixo = handle
                    driver.switch_to.window(eixo)
            DRIVER.set_window_size(300, 300)
            time.sleep(2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).click()
            DRIVER.find_element(By.ID, 'txtQtEixosVeiculos').clear()
            DRIVER.find_element(By.ID, 'txtQtEixosVeiculos').send_keys('1')
            DRIVER.find_element(By.ID, 'btnQtEixosVeiculos').click()

            for handle in driver.window_handles:
                if handle != main_page:
                    eixo = handle
                    driver.switch_to.window(eixo)
            con = DRIVER.switch_to.alert
            con.accept()

        except Exception as e:
            print(f'Erro ao tentar acessar o menu Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()


        try:
            page = driver.window_handles
            time.sleep(5)
            # Pega o numero da viagem
            DRIVER.switch_to.window(page[0])
            if DRIVER.find_element(By.ID, 'genericTB').is_displayed():
                DRIVER.switch_to.window(page[1])
            else:
                time.sleep(2)
                numId = WAIT.until(ec.element_to_be_clickable((By.ID, "lblNrViagem")))
                numId.click()
                time.sleep(5)
                texto = numId.text
                print(f'Viagem ID: {str(texto)}')
        except Exception as e:
            print('Não foi possível capturar o id da Viagem!'
                  f'\\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

viagem = AcessarTelaViagens()

