import sys

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarManifestos import sub


# Função criada fazendo chamada da classe com a função interna


inicia.abrir_browser()
inicia.realizar_login()
sub.carrega_tela_manifesto()
inicia.realizar_logoff()
inicia.fechar_browser()




