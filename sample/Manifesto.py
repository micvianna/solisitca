import sys

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarManifestos import sub


# Função criada fazendo chamada da classe com a função interna


inicia.abrirAmbiente()
inicia.efetuarLogin()
sub.carrega_tela_manifesto()
inicia.efetuarLogoff()
inicia.fecharAmbiente()




