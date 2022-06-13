import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarImpressaoRPS import rps


inicia.abrirAmbiente()
inicia.efetuarLogin()
rps.carrega_tela_rps()
time.sleep(2)
inicia.efetuarLogoff()
time.sleep(2)
inicia.fecharAmbiente()

