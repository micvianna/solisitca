import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarViagens import viagem


inicia.abrirAmbiente()
inicia.efetuarLogin()
viagem.programcaoViagem()
viagem.criarProgramcaoViagem()
viagem.aprovarProgramcaoViagem()
viagem.criarViagem()
viagem.criarManifesto()
time.sleep(5.0)
# inicia.efetuarLogoff()
# inicia.fecharAmbiente()


