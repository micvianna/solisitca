import time

from pylibTMSU.InicializarAmbiente import inicia


inicia.abrir_browser()
inicia.realizar_login('402')
time.sleep(3)
inicia.realizar_logoff()
time.sleep(3)
inicia.fechar_browser()

