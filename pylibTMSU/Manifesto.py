import sys

from InicializarAmbiente import inicia
from CriarManifestos import sub

# Função criada fazendo chamada da classe com a função interna

try:
    def carrega_subcontratadas():

        inicia.abrir_browser()
        inicia.realizar_login()
        sub.carrega_tela_manifesto()

except Exception as e:
    print(f'Não foi possivel executar esse script -> Aprova.py!'
          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
    sys.exit()


carrega_subcontratadas()

