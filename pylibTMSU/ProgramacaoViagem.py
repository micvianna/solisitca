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
from CarregarXMLProgramacaoViagem import CarregarXMLProgramacaoViagem
from CarregarXMLConexao import CarregarXMLConexao

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

        lpv = CarregarXMLProgramacaoViagem()
        conec = CarregarXMLConexao()
        self.url = conec.url_ambiente()
        self.tipo = lpv.programacao_viagem_tipo()
        self.rota = lpv.programacao_viagem_rota()
        self.tracao = lpv.programacao_viagem_tracao()
        self.reboque = lpv.programacao_viagem_reboque1()
        self.motorista = lpv.programacao_viagem_cpf_motorista()
        self.data_saida = lpv.programacao_viagem_data_saida()
        self.hora_saida = lpv.programacao_viagem_hora_saida()

    def criar_programacao_viagem(self):
        # Executado via JavaScript um get no endereço "ProgramacaoViagem"
        # Acha o Número do Manivesto e guarda na variavel

        try:
            DRIVER.execute_script('window.open();')
            # DRIVER.execute_script(f"window.open('{self.url}')")
            main_page = DRIVER.current_window_handle
            for handle in DRIVER.window_handles:
                if handle != main_page:
                    prog = handle
                    DRIVER.switch_to.window(prog)
                    DRIVER.maximize_window()
            time.sleep(1)
            DRIVER.get(f'{self.url}/Femsa.Zeus/ProgramacaoViagem')
        except Exception as e:
            print(e)
            print(f'Erro ao tentar acessar a tela de Programacao Viagem (Novo)'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
        # Reliza a troca da pagina inicial para a pagina de Programação de Viagem

    def criar_programacao(self):
        # Função para inserir os dados na tela, clicando nos campos e inserindo dados de variaveis
        if self.tipo == '':
            DRIVER.execute_script('alert("Não foi selecionado o Tipo, Verificar o XML ProgramacaoViagem");')
            time.sleep(1)
            DRIVER.quit()
            sys.exit()
        else:
            try:
                WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoTipoOperacao'))).click()
                select = Select(DRIVER.find_element_by_id('CodigoTipoOperacao'))
                select.select_by_visible_text(self.tipo)
            except Exception as e:
                print(f'Erro ao selecionar o Tipo de Operação'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                # driver.quit()
                # sys.exit()
            try:
                #  Informa código do Tipo de Operação
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Rota'))).click()
                DRIVER.find_element(By.ID, 'Rota').send_keys(self.rota)
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'Rota').send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'Rota').send_keys(Keys.ENTER)
                # WAIT.until(ec.element_to_be_clickable((By.ID, 'ui-id-3'))).click()
            except Exception as e:
                print(f'Erro ao selecionar a Rota'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                # driver.quit()
                # sys.exit()
            try:
                #  Informa Data de Saída
                WAIT.until(ec.element_to_be_clickable((By.ID, 'DataSaida'))).click()
                WAIT.until(ec.element_to_be_clickable((By.ID, 'DataSaida'))).clear()
                WAIT.until(ec.element_to_be_clickable(
                        (By.ID, 'DataSaida'))).send_keys(self.data_saida)
            except Exception as e:
                print(f'Erro ao selecionar a Data Saida'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                # driver.quit()
                # sys.exit()
            try:
                #  Informa Hora de Saída
                WAIT.until(ec.element_to_be_clickable((By.ID, 'HoraSaida'))).click()
                WAIT.until(ec.element_to_be_clickable((By.ID, 'HoraSaida'))).clear()
                WAIT.until(ec.element_to_be_clickable(
                    (By.ID, 'HoraSaida'))).send_keys(self.hora_saida)
            except Exception as e:
                print(f'Erro ao selecionar a Hora Saida'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                # driver.quit()
                # sys.exit()
            try:
                # Insere uma observação fixa no codigo
                time.sleep(2)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Observacao'))).click()
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'Observacao').send_keys('Observação teste automatizado')
            except Exception as e:
                print(f'Erro ao inserir Observações'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                # driver.quit()
                # sys.exit()
            try:
                # Insere Justificativa fixa no codigo
                WAIT.until(ec.element_to_be_clickable((By.ID, 'JustificativaViagem'))).click()
                DRIVER.find_element(By.ID, 'JustificativaViagem').send_keys('Justificativa teste automatizado')
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
                DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(self.tracao)
                DRIVER.find_element(By.ID, 'CodigoRecurso')
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(Keys.ENTER)
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
                DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(self.reboque)
                DRIVER.find_element(By.ID, 'CodigoRecurso')
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(Keys.ENTER)
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
                    Select(DRIVER.find_element_by_id('CodigoTipoRecurso')).select_by_visible_text('Motorista')
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'CodigoRecurso'))).click()
                    DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(self.motorista)
                    DRIVER.find_element(By.ID, 'CodigoRecurso')
                    time.sleep(0.5)
                    DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(Keys.ARROW_DOWN)
                    time.sleep(0.5)
                    DRIVER.find_element(By.ID, 'CodigoRecurso').send_keys(Keys.ENTER)
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

                if DRIVER.find_element(By.XPATH, '//*[@id="btnConfirmarAcao"]').is_displayed():
                    for i in range(2):
                        DRIVER.find_element(By.XPATH, '//*[@id="btnConfirmarAcao"]').click()
                        time.sleep(1)
                    time.sleep(5)
                else:
                    pass

            except Exception as e:
                print(f'Não foi possivel realizar a confirmação da escolha!'
                      f'\\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

            try:
                if DRIVER.find_element(By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div[1]/button').is_displayed():
                    DRIVER.find_element(By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div[1]/button').click()
                else:
                    pass
            except Exception as e:
                print('')
                      # f'\\nOcorreu algo inesperdado -----> {str(e)}')
            # driver.quit()
            # sys.exit()


programacao = CarregarProgramacao()
