import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarImpressaoRPS import rps


inicia.abrir_browser()
inicia.realizar_login()
rps.carrega_tela_rps()
time.sleep(2)
inicia.realizar_logoff()
time.sleep(2)
inicia.fechar_browser()

