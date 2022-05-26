"""
Objetivo: Aprovar uma programação de viagem através de consultar
          uma programação de viagem criada com rota, com data e
          hora, motorista, reboque e tração
Dependências: Framework Selenium 4, pylibTMSU.LerProgramacaoViagem
Responsavel: Michel Viana

Histórico: 11/04/2022: Desenvolvido script para criação de programação de viagem com funções
           18/04/2022:  Inserida classe Aprova e foram criada as
                        função:
                        realizar_pesquisa()
           20/04/2022: Reorganizados impports
                       Adicionado mensagens de tratamento quando houver erros

"""

import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from InicializarAmbiente import driver, wait
from CarregarXMLProgramacaoViagem import CarregarXMLProgramacaoViagem

# Constantes criadas
DRIVER = driver
WAIT = wait


class Aprova:

    def __init__(self):

        lpv = CarregarXMLProgramacaoViagem()
        self.rota = lpv.programacao_viagem_rota()
        self.data_saida = lpv.programacao_viagem_data_saida()
        self.tracao = lpv.programacao_viagem_tracao()
        self.reboque = lpv.programacao_viagem_reboque1()
        self.motorista = lpv.programacao_viagem_cpf_motorista()

    def realizar_pesquisa_confirma(self):
        try:
            time.sleep(0.3)
            # Realiza a seleção da data de saída
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnConsultar'))).click()
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaField_1'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaField_1')).select_by_value('#DataSaida')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaOperator_1'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaOperator_1')).select_by_value('>=')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaValue_1'))).click()
            DRIVER.find_element(By.ID, 'ContainerConsultaValue_1').send_keys(self.data_saida)
            DRIVER.find_element(By.ID, 'ContainerConsultaAdd_1').click()
        except Exception as e:
            print(f'Não conseguiu selecionar a Data de Saida!'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        try:
            # Rota
            # Inserindo a rota na pesquisa
            time.sleep(0.3)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaField_2'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaField_2')).select_by_value('#IdentificacaoTracao')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaOperator_2'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaOperator_2')).select_by_value('=')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaValue_2'))).click()
            DRIVER.find_element(By.ID, 'ContainerConsultaValue_2').send_keys(self.tracao)
            DRIVER.find_element(By.ID, 'ContainerConsultaAdd_2').click()
        except Exception as e:
            print(f'Não conseguiu informar o valor do campo Rota'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        try:
            # Reboque
            # Inserindo o reboque na pesquisa
            time.sleep(0.3)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaField_3'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaField_3')).select_by_value('#IdentificacaoReboque')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaOperator_3'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaOperator_3')).select_by_value('=')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaValue_3'))).click()
            DRIVER.find_element(By.ID, 'ContainerConsultaValue_3').send_keys(self.reboque)
            DRIVER.find_element(By.ID, 'ContainerConsultaAdd_3').click()

        except Exception as e:
            print(f'Não conseguiu informar o valor do campo Reboque'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        try:
            # Motorista
            # Inserindo o Motorista na pesquisa
            time.sleep(0.3)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaField_4'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaField_4')).select_by_value('#NomeMotorista')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaOperator_3'))).click()
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaOperator_4')).select_by_value('>=')
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaValue_4'))).click()
            DRIVER.find_element(By.ID, 'ContainerConsultaValue_4').send_keys(self.motorista)

        except Exception as e:
            print(f'Não conseguiu informar o valor do campo Motorista'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        try:
            # Clica no botão Consulta
            time.sleep(1)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaSearch_1'))).click()
            time.sleep(2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaGrid'))).click()
            time.sleep(1)
        except Exception as e:
            print(f'Não foi possível selecionar um dos resultados da consulta!'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # #driver.quit()
            # # sys.exit()

        try:
            # Insere Justificativa fixa no codigo
            WAIT.until(ec.element_to_be_clickable((By.ID, 'JustificativaViagem'))).click()
            DRIVER.find_element(By.ID, 'JustificativaViagem').send_keys('    Justificativa teste automatizado 123')
            time.sleep(1)
        except Exception as e:
            print(f'Erro ao inserir Justificativa'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()

        try:
            # Confirma a aprovação de viagem
            btnAprovar = WAIT.until(ec.visibility_of_element_located((By.ID, 'btnAprovar')))
            if btnAprovar.is_displayed():
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnAprovar'))).click()
                time.sleep(6)
            else:
                pass
        except Exception as e:
            print(f'Erro ao Aprovar'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            # Pop de confirmação
            time.sleep(1)
            btnAfirmacao = DRIVER.find_element(By.ID, 'btnConfirmarAcao')
            if btnAfirmacao.is_displayed():
                for i in range(2):
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'btnConfirmarAcao'))).click()
                    time.sleep(1)
                time.sleep(6)

            else:
                pass
        except Exception as e:
            print(f'Erro ao Confirmar'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
        try:
            print('')
            time.sleep(5)
            # DRIVER.switch_to.window(DRIVER.)
        except Exception as e:
            print(e)
            print('Não fechou a tela de Programação de Viagem')


aprova = Aprova()
