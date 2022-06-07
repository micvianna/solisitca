import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarMonitorAprovacaoDocs import monior

inicia.abrir_browser()
inicia.efetuar_login()
monior.carrega_tela_monitor_aprova_doc_sub()
time.sleep(3)
# inicia.efetuar_logoff()
# inicia.fechar_browser()

