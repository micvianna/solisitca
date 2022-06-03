import sys
import time

from pylibTMSU.CriarProgramacaoViagem import programacao
from pylibTMSU.CriarProgramacaoViagemAprovacao import aprova
from pylibTMSU.CriarViagens import viagem
from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarManifestos import sub

inicia.abrir_browser()
inicia.realizar_login()
programacao.criar_programacao_viagem()
programacao.criar_programacao()
aprova.realizar_pesquisa_confirma()
viagem.carrega_tela_viagens()
time.sleep(1)
inicia.fechar_browser()
time.sleep(2)
inicia.abrir_browser()
inicia.realizar_login('401')
sub.carrega_tela_manifesto()

