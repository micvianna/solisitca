import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarJustBloqSubContratada import justificativa


inicia.abrir_browser()
inicia.efetuar_login('409')
justificativa.carrega_tela_justi_bloq_sub()
justificativa.consultar()
time.sleep(2)
inicia.efetuar_logoff()
time.sleep(1)
inicia.fechar_browser()


