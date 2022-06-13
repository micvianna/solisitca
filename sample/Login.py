import time

from pylibTMSU.InicializarAmbiente import inicia


inicia.abrirAmbiente()
inicia.efetuarLogin('403')
time.sleep(3)
inicia.efetuarLogoff()
time.sleep(3)
inicia.fecharAmbiente()

