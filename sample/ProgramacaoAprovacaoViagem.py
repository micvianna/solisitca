import sys
import time

from pylibTMSU.CriarProgramacaoViagem import programacao
from pylibTMSU.CriarProgramacaoViagemAprovacao import aprova
from pylibTMSU.CriarViagens import viagem
from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarManifestos import sub

inicia.abrirAmbiente()
inicia.efetuarLogin()
programacao.criar_programacao_viagem()
programacao.criar_programacao()
aprova.realizar_pesquisa_confirma()
viagem.carrega_tela_viagens()
time.sleep(1)
inicia.fecharAmbiente()
time.sleep(2)
inicia.abrirAmbiente()
inicia.efetuarLogin('401')
sub.carrega_tela_manifesto()

