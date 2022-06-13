import random
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from pylibTMSU.InicializarAmbiente import driver, wait
from pylibTMSU.CarregarXMLProgramacaoViagem import CarregarXMLProgramacaoViagem
from pylibTMSU.CarregarXMLManifesto import CarregarXMLManifesto
from pylibTMSU.CarregarXMLConexao import CarregarXMLConexao, banco_dados
import xml.etree.ElementTree as et

# Constante criadas
DRIVER = driver
WAIT = wait


class CriarViagem:
    """
    Criada class para:
    Acessar o menu Programação de viagem (Novo)
    inserindo tipo de operação, Rota, Justificativa, Observação, Tração, Reboque
    e motorisa, opós isso é clicado para incluir. É realizada a pesquisa e
    aprovação da viagem. Possibilitando a criação do Manifesto
    """

    def __init__(self):

        conec = CarregarXMLConexao()
        carrega_xml = CarregarXMLManifesto()
        lpv = CarregarXMLProgramacaoViagem()

        # variaveis para aprovação

        self.link = banco_dados()
        self.url = conec.url_ambiente()
        self.tipo = lpv.programacao_viagem_tipo()
        self.rota = lpv.programacao_viagem_rota()
        self.tracao = lpv.programacao_viagem_tracao()
        self.reboque = lpv.programacao_viagem_reboque1()
        self.motorista = lpv.programacao_viagem_cpf_motorista()
        self.data_saida = lpv.programacao_viagem_data_saida()
        self.hora_saida = lpv.programacao_viagem_hora_saida()

        # variaveis para preencher o Manifesto

        self.mani_rota = carrega_xml.rota_manifesto
        self.mani_tipo = carrega_xml.tipo_manifesto
        self.mani_tracao = carrega_xml.tracao_manifesto
        self.mani_reboque = carrega_xml.reboque_manifesto
        self.mani_motorista = carrega_xml.cpf_motorista_manifesto
        self.num_viagem = carrega_xml.num_viagem
        self.sub_entrega = carrega_xml.sub_entrega
        self.filial_mercadoria = carrega_xml.filial_retira_mercadoria
        self.filial_destino = carrega_xml.filial_manifesto
        self.sub_transferencia = carrega_xml.sub_transferencia
        # Variaveis usadas para inserção de hora e minuto
        self.hora_s = str(random.randint(0, 1))
        self.minuto_s = str(random.randint(0, 59))
        self.horas_c = str(random.randint(1, 2))
        self.minuto_c = str(random.randint(0, 59))

    def programcaoViagem(self):
        try:
            # Reliza o acesso a pagina de Programação de Viagem
            DRIVER.execute_script('window.open();')
            main_page = DRIVER.current_window_handle
            for handle in DRIVER.window_handles:
                if handle != main_page:
                    prog = handle
                    DRIVER.switch_to.window(prog)
                    DRIVER.maximize_window()
            time.sleep(1)
            url = f'{self.url}/Femsa.Zeus/ProgramacaoViagem?cod=613{self.link}'
            DRIVER.get(url)
            time.sleep(0.5)
        except Exception as e:
            print(e)
            print(f'Erro ao tentar acessar a tela de Programacao Viagem (Novo)'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
    def criarProgramcaoViagem(self):
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
                time.sleep(0.2)
                select.select_by_visible_text(self.tipo)
            except Exception as e:
                print(f'Erro ao selecionar o Tipo de Operação'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                # driver.quit()
                # sys.exit()
            try:
                #  Informa código do Tipo de Operação
                WAIT.until(ec.element_to_be_clickable((By.ID, 'Rota'))).click()
                time.sleep(0.3)
                DRIVER.find_element(By.ID, 'Rota').send_keys(self.rota)
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'Rota').send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                DRIVER.find_element(By.ID, 'Rota').send_keys(Keys.ENTER)
            except Exception as e:
                print(f'Erro ao selecionar a Rota'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                # driver.quit()
                # sys.exit()
            try:
                #  Informa Data de Saída
                WAIT.until(ec.element_to_be_clickable((By.ID, 'DataSaida'))).click()
                time.sleep(0.2)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'DataSaida'))).clear()
                time.sleep(0.2)
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
                time.sleep(0.2)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'HoraSaida'))).clear()
                time.sleep(0.2)
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
                time.sleep(3)

                if DRIVER.find_element(By.XPATH, '//*[@id="btnConfirmarAcao"]').is_displayed():
                    DRIVER.find_element(By.XPATH, '//*[@id="btnConfirmarAcao"]').click()
                    time.sleep(1)
                else:
                    pass

            except Exception as e:
                print(f'Não foi possivel realizar a confirmação da escolha!'
                      f'\\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
            """
            try:
                if DRIVER.find_element(By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div[1]/button').is_displayed():
                    DRIVER.find_element(By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div[1]/button').click()
                else:
                    pass
            except Exception as e:
                print('')
                print(e.__doc__)
            # f'\\nOcorreu algo inesperdado -----> {str(e)}')
            # driver.quit()
            # sys.exit()
            """
            ######################## Pesquisa e Aprovação ############################

    def aprovarProgramcaoViagem(self):
        try:
            time.sleep(1)
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
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaField_2')).select_by_value(
                '#IdentificacaoTracao')
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
            Select(DRIVER.find_element(By.ID, 'ContainerConsultaField_3')).select_by_value(
                '#IdentificacaoReboque')
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
            DRIVER.find_element(By.ID, 'JustificativaViagem').send_keys(
                '    Justificativa para aprovar a viagem')
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
            # Pop-up de confirmação
            time.sleep(1)
            btnAfirmacao = DRIVER.find_element(By.ID, 'btnConfirmarAcao')
            if btnAfirmacao.is_displayed():
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnConfirmarAcao'))).click()
                time.sleep(3)
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


        ######################## Viagens ############################

    def criarViagem(self):
        # Após a criação da programação, é acessado a tela de viagem para inserir a programação no sistema
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
            # Acessa o menu
            # Acessa a tela de viagem com parte do varivel "self.url" mais complemento
            DRIVER.get(f'{self.url}/NewSitex/Paginas/Operacoes/Viagens/Viagens.aspx?{self.link}')
            # clique no Anexar
            time.sleep(2)
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
            # Guarda na variavel o numero da viagem do label
            numero_viagem = WAIT.until(ec.element_to_be_clickable((By.ID, "lblNrViagem")))
            numero_viagem.click()
            time.sleep(1)
            # Grava Id da Viagem na variavel
            num_da_viagem = numero_viagem.text
            print(f'Numero da Viagem: {num_da_viagem}')
            # Abre o arquivo de parametros/Manifesto.xml
            tree = et.parse('../parametros/Manifesto.xml')
            # Acessa _todo o xml
            root = tree.getroot()
            for num_viagem in root.iter('NumViagem'):
                # Grava Id da Viagem em um arquivo de texto
                num_viagem.text = str(num_da_viagem)
            # Grava o XML com a nova informação
            tree.write('../parametros/Manifesto.xml')
            self.num_viagem = num_da_viagem
            # Printa o Id da Viagem
            print(f"Número da Viagem no XML:  {root.find('NumViagem').text}")
        except Exception as e:
            print(f'Erro ao tentar pegar ID Viagens'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # driver.quit()
            # sys.exit()
################## Manifesto #############################

    def criarManifesto(self):

        global atual

        if self.hora_s == '1' and self.horas_c == '1':
            self.minuto_s = '0'
            self.minuto_c = '4'
        else:
            pass
        try:
            # Acessa a tela Manifesto
            # Acesso para tela de Manifesto o link
            url = f'{self.url}/NewSitex/Paginas/Operacoes/Manifestos.aspx?cod=94{self.link}'
            DRIVER.get(url)
            time.sleep(2)
        except Exception as e:
            print(f'Erro ao tentar acessar a tela de Manifesto'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        # Verifica se existe numero da viagem o tipo é igual ENTREGA / COLETA
        if self.num_viagem != '' or self.num_viagem != '0' and self.mani_tipo == 'ENTREGA / COLETA':
            try:
                # clica no campo para inserir o número da viagem
                txtNrViagem = WAIT.until(ec.element_to_be_clickable((By.ID, 'txtNrViagem')))
                txtNrViagem.click()
                time.sleep(0.5)
                # Insere o número da viagem
                txtNrViagem.send_keys(self.num_viagem)
                time.sleep(0.5)
                # clica nos... Para carregar a viagem
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnCarregarViagem'))).click()
            except Exception as e:
                print(f'Erro ao tentar acessar o numero da viagem ou clicar no botão carregar'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            # Clica no campo para inserir uma observação
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtObservacao'))).click()
            # Insere uma observação fixa
            WAIT.until(ec.element_to_be_clickable((By.ID, 'txtObservacao'))).send_keys('Observação Manifesto')
            time.sleep(0.6)
            try:
                # insere a Sub de Transferencia
                # se variavel estiver vazia no arquivo Manifesto.xml passa
                if self.sub_transferencia == '':
                    pass
                else:
                    # se não, será selecionado conforme o valor que está no XML Manifesto
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'ddlSubcontratadaTransferencia')))
                    select = Select(DRIVER.find_element(By.ID, 'ddlSubcontratadaTransferencia'))
                    # O valor da Filial de Destino é pego no XML Manifesto
                    select.select_by_visible_text(self.sub_transferencia)
            except Exception as e:
                print(f'Erro ao tentar escolher Subcontratada Transferencia'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            time.sleep(0.6)
            try:
                # insere a Sub de Entrega
                # se variavel estiver vazia no arquivo Manifesto.xml passa
                if self.sub_entrega == '':
                    pass
                else:
                    # se não, será selecionado conforme o valor que está no XML Manifesto
                    WAIT.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="ddlSubcontratadaEntrega"]')))
                    select = Select(DRIVER.find_element(By.XPATH, '//*[@id="ddlSubcontratadaEntrega"]'))
                    # O valor da Filial de Destino é pego no XML Manifesto
                    select.select_by_visible_text(self.sub_entrega)
            except Exception as e:
                print(f'Erro ao tentar escolher Subcontratada Entrega'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            time.sleep(0.6)
            try:
                # insere a Filial de mercadoria
                # se variavel estiver vazia no arquivo Manifesto.xml passa
                if self.filial_mercadoria == '':
                    pass
                else:
                    # se não, será selecionado conforme o valor que está no XML Manifesto
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'ddlFilialRetiraMercadoria')))
                    select = Select(DRIVER.find_element(By.ID, 'ddlFilialRetiraMercadoria'))
                    # O valor da Filial de Destino é pego no XML Manifesto
                    select.select_by_visible_text(self.filial_mercadoria)
            except Exception as e:
                print(f'Erro ao tentar escolher Filial de Retira de Mercadoria'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            try:
                # insere a Filial de destino
                # se variavel estiver vazia no arquivo Manifesto.xml passa
                if self.filial_destino == '':
                    pass
                else:
                    # se não, será selecionado conforme o valor que está no XML Manifesto
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'ddlFiliaisDestino')))
                    select = Select(DRIVER.find_element(By.ID, 'ddlFiliaisDestino'))
                    # O valor da Filial de Destino é pego no XML Manifesto
                    select.select_by_visible_text(self.filial_destino)
            except Exception as e:
                print(f'Erro ao tentar escolher Filial de Destino'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

            # Clica no Incluir no Rodapé
            WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeManifesto_ibtnIncluir'))).click()
            # Acha o Número do Manivesto e guarda na variavel
            numero_manifesto = WAIT.until(ec.element_to_be_clickable((By.ID, 'lblNrManifesto')))
            # Clica no label
            numero_manifesto.click()
            time.sleep(3)
            # Numero do ma
            num_manifesto = numero_manifesto.text
            print(f'Num Manifesto ID: {str(num_manifesto)}')
        else:
            # Então Se numero da viagem ser diferende
            # vazio ou numero da viagem ser vazio e tipo diferente 'ENTREGA / COLETA'
            try:
                # Clica no raio
                WAIT.until(ec.element_to_be_clickable((By.ID, 'imgViagem'))).click()
                # Aguarda em milesegundos
                time.sleep(0.5)
                # Preenche os campos
                atual = DRIVER.window_handles
                # rand = random.randint(1, 11)
                # Alterna para a janela do raio
                DRIVER.switch_to.window(atual[1])
                # Estabelece um tamanho para a janela
                DRIVER.set_window_size(930, 350)
                # Aguarda em milesegundos
                time.sleep(0.7)
                # Insere Rota
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_txtValueColumn'))).click()
                # O valor da rota é pego do XML Manifesto
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_txtValueColumn'))).send_keys(str(
                    self.mani_rota))
                # clica no '...' para procurar a rota
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_btnProcurar'))).click()
                # Aguarda em milesegundos
                time.sleep(0.7)
                # Insere Tração
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).click()
                # O valor da Tração é pego no XML Manifesto
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).send_keys(
                    self.mani_tracao)
                # clica no '...' para procurar a tração
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_btnProcurar'))).click()
                # Aguarda em milesegundos
                time.sleep(0.7)
                # Insere Motorista
                WAIT.until(ec.element_to_be_clickable(
                    (By.ID, 'EJProcuraDadosMotorista_txtValueColumn'))).click()
                # O valor da Tração é pego no XML Manifesto
                WAIT.until(ec.element_to_be_clickable(
                    (By.ID, 'EJProcuraDadosMotorista_txtValueColumn'))).send_keys(self.mani_motorista)
                # clica no '...' para procurar a Motorista
                WAIT.until(ec.element_to_be_clickable(
                    (By.ID, 'EJProcuraDadosMotorista_btnProcurar'))).click()
                # Aguarda em milesegundos
                time.sleep(0.7)
            except Exception as e:
                print(e)
                print('--------')
                print(f'Erro ao tentar preencher Dados: Rota, Tração e Motorista'
                      f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
            try:
                # Insere a Hora de Saida
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).click()
                # Insere hora de um 'if'
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(self.hora_s)
                # Aguarda em milesegundos
                time.sleep(1)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).click()
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(':')
                # Aguarda em milesegundos
                time.sleep(1)
                # insere minuto de um 'if'
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraSaida'))).send_keys(self.minuto_s)
                # Aguarda em milesegundos
                time.sleep(0.7)
                # Insere Hora de Chegada
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).click()
                # Insere hora de um 'if'
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(self.horas_c)
                # Aguarda em milesegundos
                time.sleep(1)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).click()
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(':')
                time.sleep(1)
                WAIT.until(ec.element_to_be_clickable((By.ID, 'txtHoraChegada'))).send_keys(self.minuto_c)
                time.sleep(1)
                # clica no verificar
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnVerificacao'))).click()
                time.sleep(0.7)
                # clica no incluir
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnIncluir'))).click()
                time.sleep(3)
            except Exception as e:
                print(f'Erro ao incluir dados')
                print(e.__doc__)
            try:
                # Volta para a Page Main
                DRIVER.switch_to.window(atual[0])
            except Exception as e:
                print(f'Erro ao mudar de tela')
                print(e.__doc__)
            # verifica se o botão está visivel na tela
            # Se Sim, clica no label do número do manifesto
            if WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeManifesto_ibtnIncluir'))).is_displayed():
                # Recebe o valor que está no label do número do manifesto
                numero_manifesto = WAIT.until(ec.element_to_be_clickable((By.ID, 'lblNrManifesto')))
                numero_manifesto.click()
                time.sleep(3)
                # pega o numero do manifesto e guarda na variavel
                texto = numero_manifesto.text
                # verifica se a
                if len(texto) != 0:
                    print(f'Num Manifesto ID: {str(texto)}')
                else:
                    print('Não trouxe o número do Manifesto')
                    pass
            # Se Não
            else:
                #
                try:
                    # insere a Sub de Transferencia
                    if self.sub_transferencia == '':
                        # se variavel está vazia no arquivo Manifesto.xml passa
                        pass
                    else:
                        # se não, será selecionado conforme o valor que está no XML Manifesto
                        WAIT.until(ec.element_to_be_clickable((By.ID, 'ddlSubcontratadaTransferencia')))
                        select = Select(DRIVER.find_element(By.ID, 'ddlSubcontratadaTransferencia'))
                        # O valor da Tranferencia é pego no XML Manifesto
                        select.select_by_visible_text(self.sub_transferencia)
                except Exception as e:
                    print(f'Erro ao tentar escolher Subcontratada Transferencia'
                          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                time.sleep(0.6)
                try:
                    # insere a Sub de Entrega
                    if self.sub_entrega == '':
                        # se variavel está vazia no arquivo Manifesto.xml passa
                        pass
                    else:
                        # se não, será selecionado conforme o valor que está no XML Manifesto
                        WAIT.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="ddlSubcontratadaEntrega"]')))
                        select = Select(DRIVER.find_element(By.XPATH, '//*[@id="ddlSubcontratadaEntrega"]'))
                        # O valor da Sub Entrega é pego no XML Manifesto
                        select.select_by_visible_text(self.sub_entrega)
                except Exception as e:
                    print(f'Erro ao tentar escolher Subcontratada Entrega'
                          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                time.sleep(0.6)
                try:
                    # insere a Filial de mercadoria
                    if self.filial_mercadoria == '':
                        # se variavel está vazia no arquivo Manifesto.xml passa
                        pass
                    else:
                        # se não, será selecionado conforme o valor que está no XML Manifesto
                        WAIT.until(ec.element_to_be_clickable((By.ID, 'ddlFilialRetiraMercadoria')))
                        select = Select(DRIVER.find_element(By.ID, 'ddlFilialRetiraMercadoria'))
                        # O valor da Filial de Mercadoria é pego no XML Manifesto
                        select.select_by_visible_text(self.filial_mercadoria)
                except Exception as e:
                    print(f'Erro ao tentar escolher Filial de Retira de Mercadoria'
                          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                try:
                    if WAIT.until(ec.element_located_to_be_selected((By.ID, 'ddlFiliaisDestino'))).is_displayed():
                        time.sleep(2)
                        print('sim')
                        # insere a Filial de destino
                        if self.filial_destino == '' and self.filial_destino == '0':
                            # se variavel está vazia no arquivo Manifesto.xml passa
                            pass
                        else:
                            # se não, será selecionado conforme o valor que está no XML Manifesto
                            WAIT.until(ec.element_to_be_clickable((By.ID, 'ddlFiliaisDestino')))
                            select = Select(DRIVER.find_element(By.ID, 'ddlFiliaisDestino'))
                            # O valor da Filial de Destino é pego no XML Manifesto
                            select.select_by_visible_text(self.filial_destino)
                    else:
                        print('não')
                        pass
                except Exception as e:
                    print(f'Erro ao tentar escolher Filial de Destino'
                          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
                try:
                    # inclui
                    WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeManifesto_ibtnIncluir'))).click()
                    # Recebe o valor que está no label do número do manifesto
                    numero_manifesto = WAIT.until(ec.element_to_be_clickable((By.ID, 'lblNrManifesto')))
                    numero_manifesto.click()
                    time.sleep(3)
                    texto = numero_manifesto.text
                    # printa o numero do Manifesto
                    print(f'Num Manifesto ID: {str(texto)}')
                except Exception as e:
                    print(f'Erro ao pegar o ID do Manifesto')
                    print(e.__doc__)

viagem = CriarViagem()
