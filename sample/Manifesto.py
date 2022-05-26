import sys

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarManifestos import sub

# Função criada fazendo chamada da classe com a função interna

try:
    def carrega_subcontratadas():
        inicia.abrir_browser()
        inicia.realizar_login()
        sub.carrega_tela_manifesto()
        #logoff.realizar_logoff()
        #logoff.fechar_browser()


except Exception as e:
    print(f'Não foi possivel executar esse script -> Manifesto.py!'
          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
    # sys.exit()

manifesto = carrega_subcontratadas()

