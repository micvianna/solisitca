"""
Função: Gerar numero de MAC
Objetivo: Gerar numero de MAC usando número da viagem ou gerando a viagem
Dependências: CarregarXMLManifesto, CarregarXMLConexao, InicializarAmbiente
Responsavel: Michel Viana

Historico: 19/05/2022: Reorganizados impports
                       Desenvolvido função: carrega_tela_manifesto()
                       Adicionada mensagens de tratamento quando houver erros
           20/05/2022 Inserido Comentarios
"""

import random
import sys
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from CarregarXMLManifesto import CarregarXMLManifesto
from CarregarXMLConexao import CarregarXMLConexao
from InicializarAmbiente import driver, wait

# Constantes criadas
DRIVER = driver
WAIT = wait
global atual


class GerarManifesto:

    def __init__(self):

        # variaveis de chamada de classe

        self.url = CarregarXMLConexao.url_ambiente
        self.rota = CarregarXMLManifesto.rota_manifesto
        self.tipo = CarregarXMLManifesto.tipo_manifesto
        self.tracao = CarregarXMLManifesto.tracao_manifesto
        self.reboque = CarregarXMLManifesto.reboque_manifesto
        self.motorista = CarregarXMLManifesto.cpf_motorista_manifesto
        self.num_viagem = CarregarXMLManifesto.num_viagem
        self.sub_entrega = CarregarXMLManifesto.sub_entrega
        self.filial_mercadoria = CarregarXMLManifesto.filial_retira_mercadoria
        self.filial_destino = CarregarXMLManifesto.filial_manifesto
        self.sub_transferencia = CarregarXMLManifesto.sub_transferencia
        # Variaveis usadas para inserção de hora e minuto
        self.hora_s = str(random.randint(0, 1))
        self.minuto_s = str(random.randint(0, 59))
        self.horas_c = str(random.randint(1, 2))
        self.minuto_c = str(random.randint(0, 59))

    def carrega_tela_manifesto(self):

        global atual

        if self.hora_s == '1' and self.horas_c == '1':
            self.minuto_s = '0'
            self.minuto_c = '4'
        else:
            pass

        try:
            # Acessa a tela Manifesto
            time.sleep(1.5)
            acao = ActionChains(DRIVER)
            DRIVER.find_element(By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002').click()
            time.sleep(1)
            submenu = WAIT.until(
                ec.element_to_be_clickable(
                    (By.ID, 'EJCabecalho1_EJMenu1__skmMenu-menuItem002-subMenu-menuItem014')))
            acao.click(submenu).perform()
            # DRIVER.switch_to.window(DRIVER.window_handles[0])
            DRIVER.switch_to.frame('Teste')
            time.sleep(1)
            # tentativa de acessa a tela de manifesto com o link
            # DRIVER.execute_script("window.open('/NewSitex/Paginas/Operacoes/Manifestos.aspx');")
            # DRIVER.execute_script('window.location.href = "http://nshm0001.expresso.corp/Paginas/Operacoes/Manifestos.aspx" ;')
            # DRIVER.get(f'{self.url}Paginas/Operacoes/Manifestos.aspx')
            time.sleep(0.5)
        except Exception as e:
            print(f'Erro ao tentar acessar a tela de Manifesto'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        # Verifica se existe numero da viagem o tipo é igual ENTREGA / COLETA
        if self.num_viagem != '' and self.tipo == 'ENTREGA / COLETA':
            try:
                # DRIVER.switch_to.window(DRIVER.window_handles[1])
                # DRIVER.switch_to.frame('Teste')
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
            # DRIVER.switch_to.frame('Teste')
            try:
                # insere a Sub de Transferencia
                if self.sub_transferencia == '':
                    # se variavel está vazia no arquivo Manifesto.xml passa
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
                if self.sub_entrega == '':
                    # se variavel está vazia no arquivo Manifesto.xml passa
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
                if self.filial_mercadoria == '':
                    # se variavel está vazia no arquivo Manifesto.xml passa
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
                if self.filial_destino == '':
                    # se variavel está vazia no arquivo Manifesto.xml passa
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
            texto = numero_manifesto.text
            print(f'Num Manifesto ID: {str(texto)}')

        # Então Se numero da viagem ser diferende
        # vazio ou numero da viagem ser vazio e tipo diferente 'ENTREGA / COLETA'
        elif self.num_viagem != '' or self.num_viagem == '' and self.tipo != 'ENTREGA / COLETA':
            # emite alerta no Browser atraves de scrpit
            DRIVER.execute_script(
                'alert("O Tipo escolhido é diferente de ENTREGA / COLETA, Verificar o XML Manifeto");')
            time.sleep(3)
            #DRIVER.quit()
            #sys.exit()

        # ############################
        # Não contem número da viagem
        # ############################
        else:
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
                    self.rota))
                # clica no '...' para procurar a rota
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosRota_btnProcurar'))).click()
                # Aguarda em milesegundos
                time.sleep(0.7)
                # Insere Tração
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).click()
                # O valor da Tração é pego no XML Manifesto
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_txtValueColumn'))).send_keys(
                    self.tracao)
                # clica no '...' para procurar a tração
                WAIT.until(ec.element_to_be_clickable((By.ID, 'EJProcuraDadosTracao_btnProcurar'))).click()
                # Aguarda em milesegundos
                time.sleep(0.7)
                # Insere Motorista
                WAIT.until(ec.element_to_be_clickable(
                    (By.ID, 'EJProcuraDadosMotorista_txtValueColumn'))).click()
                # O valor da Tração é pego no XML Manifesto
                WAIT.until(ec.element_to_be_clickable(
                    (By.ID, 'EJProcuraDadosMotorista_txtValueColumn'))).send_keys(self.motorista)
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
                # DRIVER.find_element(By.ID, 'txtKmInicialReboque').send_keys('1')
                time.sleep(1)
                # clica no verificar
                WAIT.until(ec.element_to_be_clickable((By.ID, 'btnVerificacao'))).click()
                # acpt = DRIVER.switch_to.alert
                # acpt.accept()
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
                # Alterna para o frame
                DRIVER.switch_to.frame('Teste')
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
                    # insere a Filial de destino
                    if self.filial_destino == '':
                        # se variavel está vazia no arquivo Manifesto.xml passa
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


sub = GerarManifesto()
