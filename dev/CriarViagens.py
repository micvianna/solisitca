"""
Objetivo: Inserir uma viagem para aprovação

Dependências: Framework Selenium 4 (requeriments.txt)
Responsavel: Michel Viana

Histórico:  25/04/2022: Criada a classe AcessarTelaViagens
            26/04/2022: Inserida função: carrega_tela_viagens()
            27/04/2022: Ajuste na carrega_tela_viagens
            28/04/2022: Reescrita a carrega_tela_viagens()
            29/04/2022: Inserido variavel para pegar ID da Viagem
            16/05/2022: Inserida rotina para gravar Id da Viagem no XML Manifesto
"""
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pylibTMSU.InicializarAmbiente import driver, wait
from pylibTMSU.CarregarXMLConexao import CarregarXMLConexao, banco_dados
import xml.etree.ElementTree as et

# Constante criadas
DRIVER = driver
WAIT = wait


class AcessarTelaViagens:
    # Realiza acessoa a tela de Viagem e realizar a inserção da Viagem
    time.sleep(1)

    def __init__(self):
        conec = CarregarXMLConexao()
        self.url = conec.url_ambiente()
        self.link = banco_dados()

    def carrega_tela_viagens(self):
        # print('Criação da Viagem, vai ser buscada a Programação de Viagem e vai ser gerado um ID')
        # Após a criação da programação, é acessado a tela de viagem para inserir a programação no sistema
        # Janela atual
        main_page = DRIVER.current_window_handle
        for handle in DRIVER.window_handles:
            if handle != main_page:
                prog = handle
                if main_page != prog:
                    # Fecha a janela que está sendo utilizada
                    DRIVER.close()
                # trocando para a tela principal
                DRIVER.switch_to.window(prog)
        time.sleep(2)
        try:
            time.sleep(0.5)
            # acao = ActionChains(DRIVER)
            time.sleep(0.3)
            # Acessa o menu
            # Acessa a tela de viagem com parte do varivel "self.url" mais complemento
            DRIVER.get(f'{self.url}/NewSitex/Paginas/Operacoes/Viagens/Viagens.aspx?{self.link}')
            # clique no Anexar
            time.sleep(3)
            # clica no rodapé e clica no clipe
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeViagens_ibtnProgramacaoViagem'))).click()
            time.sleep(2)

            # 1.º Seleção: Programação de Viagem Aprova
            main_page = driver.current_window_handle
            for handle in driver.window_handles:
                if handle != main_page:
                    aprova = handle
                    # Alterna para a janela
                    driver.switch_to.window(aprova)
            # clica no 1.º elemento
            DRIVER.find_element(By.CSS_SELECTOR, '#dtgProgramacaoViagem > tbody > tr.linha_tabela ')
        except Exception as e:
            print(f'Erro ao acessar tela de Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            # 2º Seleção: Tração
            WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione'))).click()
            time.sleep(1)
            for handle in driver.window_handles:
                if handle != main_page:
                    tracao = handle
                    # Alterna para a janela
                    driver.switch_to.window(tracao)
            # 3.º Seleção: Reboque 1
            WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione'))).click()
            time.sleep(1)
            list = driver.window_handles
            for handle in driver.window_handles:
                if handle != main_page:
                    reboque = handle
                    # Alterna para a janela
                    driver.switch_to.window(reboque)
            WAIT.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Selecione'))).click()
            time.sleep(1)
            # Retorna a pagina principal
            DRIVER.switch_to.window(list[0])
            # Inclui a Viagem
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeViagens_ibtnIncluir'))).click()
            time.sleep(1)
            con = DRIVER.switch_to.alert
            con.accept()
            time.sleep(1)
        except Exception as e:
            print(f'Erro ao selecionar itens para consulta de Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            # Abre janela de inclusão de eixo de veículo
            for handle in driver.window_handles:
                if handle != main_page:
                    eixo = handle
                    # Alterna para a janela
                    driver.switch_to.window(eixo)
            # muda o tamanho da janela
            DRIVER.set_window_size(300, 300)
            time.sleep(1)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).clear()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtQtEixosVeiculos'))).send_keys('1')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnQtEixosVeiculos'))).click()
            time.sleep(1)

        except Exception as e:
            print(f'Erro ao fechar a escolha''erro tela de 300 x 300'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            for handle in driver.window_handles:
                if handle == main_page:
                    clique = handle
                    # Alterna para a janela
                    driver.switch_to.window(clique)
                    time.sleep(1)
            numero_viagem = WAIT.until(ec.element_to_be_clickable((By.ID, "lblNrViagem")))
            numero_viagem.click()
            time.sleep(3)
            # Grava Id da Viagem na variavel
            num_da_viagem = numero_viagem.text
            print(f'Numero da Viagem: {num_da_viagem}')
            # Abre o arquivo de parametros/Manifesto.xml
            tree = et.parse('../parametros/Manifesto.xml')
            # Acessa _todo o xml
            root = tree.getroot()
            for num_viagem in root.iter('NumViagem'):
                # Grava Id da Viagem em um arquivo de texto
                new_id_viagem = num_da_viagem
                num_viagem.text = str(new_id_viagem)
                print(num_viagem.text)
            # Grava o XML com a nova informação
            tree.write('../parametros/Manifesto.xml')
            # Printa o Id da Viagem
            print(f"Número da Viagem no XML:  {root.find('NumViagem').text}")

            """
            root = tree.getroot()
            for num_viagem in root.iter('NumViagem'):
                # Grava Id da Viagem num arquivo de texto
                new_num_viagem = num_da_viagem
                num_viagem = str(new_num_viagem)
                print(f'numero da Viagem {num_viagem}')
                # Grava o XML com a nova informação
                tree.write('../parametros/Manifesto.xml')
            """


        except Exception as e:
            print('erro aqui')
            print(e.__doc__)
            print(f'Erro ao tentar pegar ID Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()


viagem = AcessarTelaViagens()
