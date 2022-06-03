import time


from selenium.webdriver.support import expected_conditions as ec
from pylibTMSU.InicializarAmbiente import driver, wait
from pylibTMSU.CarregarXMLConexao import CarregarXMLConexao, banco_dados

# Constantes criadas
DRIVER = driver
WAIT = wait


class Cte:

    def __init__(self):
        xml = CarregarXMLConexao()
        self.url = xml.url_ambiente()
        self.link = banco_dados()

    def carrega_tela_cte(self):
        # Acessa a tela CTE
        time.sleep(1)
        janela = DRIVER.window_handles
        print(janela)
        linkcte = f'{self.url}/NewSitex/Paginas/Operacoes/Conhecimentos/Complemento/Complemento.aspx?cod=464{self.link}'
        DRIVER.get(linkcte)
        time.sleep(0.5)
        try:
            WAIT.until(ec.alert_is_present())
            alert = DRIVER.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception as e:
            print("no alert", e)
        # DRIVER.switch_to.window(DRIVER.window_handles[0])
        # DRIVER.switch_to.frame('Teste')
        time.sleep(1)
        # DRIVER.switch_to.window(DRIVER.window_handles[0])
        # tentativa de acessa a tela de manifesto com o link DRIVER.execute_script("window.open(
        # '/NewSitex/Paginas/Operacoes/Manifestos.aspx');") DRIVER.execute_script('window.location.href =
        # self.url}Paginas/Operacoes/Manifestos.aspx')
        time.sleep(0.5)


cte = Cte()
