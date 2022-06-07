import time

from pylibTMSU.InicializarAmbiente import inicia


inicia.abrir_browser()
inicia.efetuar_login('402')
time.sleep(3)
inicia.efetuar_logoff()
time.sleep(3)
inicia.fechar_browser()

