import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarMonitorAprovacaoDocs import monior

inicia.abrirAmbiente()
inicia.efetuarLogin()
monior.carrega_tela_monitor_aprova_doc_sub()
time.sleep(3)
# inicia.efetuarLogoff()
# inicia.fecharAmbiente()

