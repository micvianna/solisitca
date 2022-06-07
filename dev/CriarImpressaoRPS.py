import time

from pylibTMSU.CarregarXMLConexao import CarregarXMLConexao, banco_dados
from pylibTMSU.InicializarAmbiente import driver, wait


# Constantes criadas
DRIVER = driver
WAIT = wait


class GerarImpressaoRPS:

    def __init__(self):

        # variaveis de chamada de classe
        conec = CarregarXMLConexao()
        self.link = banco_dados()
        self.url = conec.url_ambiente()

    def carrega_tela_rps(self):

        global atual

        try:
            # Acessa a tela Manifesto
            # Acesso para tela de Impressao RPS atraves do link
            url = f'{self.url}/NewSitex/Paginas/Operacoes/Conhecimentos/Impressao/ConhecimentoRPS.aspx?cod=425{self.link} '
            DRIVER.get(url)
            time.sleep(0.5)
        except Exception as e:
            print(f'Erro ao tentar acessar a tela de Impressao RPS atraves do link'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')



rps = GerarImpressaoRPS()
