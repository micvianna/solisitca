"""
Objetivo: Criar uma programação de viagem com rota, com data e hora,
          motorista, reboque e tração
Dependências: Framework Selenium 4 (requeriments.txt)
Responsavel: Michel Viana

Histórico: 11/04/2022: Desenvolvido script para criação de programação de viagem com funções
           18/04/2022: Inserida classe LoginIn e reestruturada as funções
           20/04/2022: Adicionado mensagens de tratamento quando houver erros
           22/04/2022: Alterado a função
           25/04/2022: Inserido verificação caso exista uma programação já cadastrada

"""

import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from InicializarAmbiente import driver, wait
from LerProgramacaoViagem import CarregarXML

# inserido para futura utilização no campo
# from datetime import datetime
# data_e_hora_atuais = datetime.now() -> pega a data e hora
# data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y') -> quebra para pegar somente a data

# Constante criadas
DRIVER = driver
WAIT = wait


class CarregarProgramacao:
    """
    Criada class para:
    Acessar o menu Programação de viagem (Novo)
    inserindo tipo de operação, Rota, Justificativa, Observação, Tração, Reboque
    e motorisa, opós isso é clicado para incluir
    """

    def __init__(self):

        lpv = CarregarXML()
        self.tipo = lpv.programacao_viagem_tipo()
        self.rota = lpv.programacao_viagem_rota()
        self.tracao = lpv.programacao_viagem_tracao()
        self.reboque = lpv.programacao_viagem_reboque1()
        self.motorista = lpv.programacao_viagem_cpf_motorista()
        self.data_saida = lpv.programacao_viagem_data_saida()
        self.hora_saida = lpv.programacao_viagem_hora_saida()

    def carrega_tela(self):
        # Executado via JavaScript um get no endereço "ProgramacaoViagem"
        try:
            DRIVER.execute_script("window.open('http://nshm0001.expresso.corp/Femsa.Zeus/ProgramacaoViagem')")
        except Exception as e:
            print(e)

            print(f'Erro ao tentar acessar a tela de Programacao Viagem (Novo)'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        # Reliza a troca da pagina inicial para a pagina de Programação de Viagem
        main_page = DRIVER.current_window_handle
        for handle in DRIVER.window_handles:
            if handle != main_page:
                prog = handle
                DRIVER.switch_to.window(prog)
                DRIVER.maximize_window()
        time.sleep(1)

    def criar_programacao(self):
        # Função para inserir os dados na tela, clicando nos campos e inserindo dados de variaveis
        try:
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoTipoOperacao'))).click()
            select = Select(DRIVER.find_element(By.ID, 'CodigoTipoOperacao'))
            select.select_by_visible_text(self.tipo)
        except Exception as e:
            print(f'Erro ao selecionar o Tipo de Operação'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
        try:
            #  Informa código do Tipo de Operação
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Rota'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Rota'))).send_keys(self.rota)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Rota'))).send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Rota'))).send_keys(Keys.ENTER)
        except Exception as e:
            print(f'Erro ao selecionar a Rota'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
        try:
            #  Informa Data de Saída
            WAIT.until(ec.element_to_be_clickable((By.ID, 'DataSaida'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'DataSaida'))).send_keys(self.data_saida)
        except Exception as e:
            print(f'Erro ao selecionar a Data Saida'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
        try:
            #  Informa Hora de Saída
            WAIT.until(ec.element_to_be_clickable((By.ID, 'HoraSaida'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'HoraSaida'))).send_keys(self.hora_saida)
        except Exception as e:
            print(f'Erro ao selecionar a Hora Saida'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
        try:
            # Insere uma observação fixa no codigo
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Observacao'))).click()
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Observacao'))).send_keys('Observação teste automatizado')
        except Exception as e:
            print(f'Erro ao inserir Observações'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
        try:
            # Insere Justificativa fixa no codigo
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'JustificativaViagem'))).click()
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'JustificativaViagem'))).send_keys('Justificativa teste automatizado')
        except Exception as e:
            print(f'Erro ao inserir Justificativa'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        # Insere 1º Recurso do tipo TRACAO
        try:
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoTipoRecurso'))).click()
            Select(DRIVER.find_element(By.ID, 'CodigoTipoRecurso')).select_by_value('1')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(self.tracao)
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(Keys.ENTER)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnAdicionarRecurso'))).click()
        except Exception as e:
            print(f'Erro ao selecionar a Tração'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        # Insere 2º Recurso do tipo REBOQUE
        try:
            # Insere o codigo do REBOQUE
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoTipoRecurso'))).click()
            Select(DRIVER.find_element(By.ID, 'CodigoTipoRecurso')).select_by_visible_text('Reboque')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(self.reboque)
            #DRIVER.find_element(By.ID, 'CodigoRecurso')
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(Keys.ENTER)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnAdicionarRecurso'))).click()
        except Exception as e:
            print(f'Erro ao selecionar o código do reboque'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        # Insere 3º Recurso do tipo MOTORISTA
        try:
            # Insere o CPF do Motorista
            if self.motorista == '':
                pass
            else:
                WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoTipoRecurso'))).click()
                Select(DRIVER.find_element(By.ID, 'CodigoTipoRecurso')).select_by_visible_text('Motorista')
                WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).click()
                WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(self.motorista)
                time.sleep(0.5)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).send_keys(Keys.ENTER)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnAdicionarRecurso'))).click()
        except Exception as e:
            print(f'Erro na inclusão do motorista'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        # finaliza a criação da Programação de Viagem
        try:

            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnIncluir'))).click()
            time.sleep(5)
            WAIT.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="btnConfirmarAcao"]'))).click()
            time.sleep(0.5)
            WAIT.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="btnConfirmarAcao"]'))).click()
            time.sleep(0.5)
        except Exception as e:
            print(f'Não foi possivel realizar a confirmação da escolha!'
                  f'\\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        # driver.quit()
        # sys.exit()

        try:
            btn = WAIT.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div[1]/button')))
            if btn.is_displayed():
                btn.click()
            else:
                pass

        except Exception as e:
            print('')
                  # f'\\nOcorreu algo inesperdado -----> {str(e)}')
        # driver.quit()
        # sys.exit()

programacao = CarregarProgramacao()
