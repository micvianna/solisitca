import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarMonitorAprovacaoDocs import monior

inicia.abrir_browser()
inicia.realizar_login()
monior.carrega_tela_monitor_aprova_doc_sub()
time.sleep(3)
# inicia.realizar_logoff()
# inicia.fechar_browser()

