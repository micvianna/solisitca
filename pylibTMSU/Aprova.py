"""
Função: (ProgramacaoViagem.xml) e coloca-los em variaveis
Objetivo: Aprovação da Programação de Viagem
Dependências: pylibTMSU.InicializarAmbiente, pylibTMSU.AprovarProgramacaoViagem
Responsavel: Michel Viana

Historico: 20/04/2022: Reorganizados impports
                       Desenvolvido função: aprovar_programacao_viagem()
                       Adicionado mensagens de tratamento quando houver erros
           25/04/2022: Importado arquivo Viagem
"""

import sys

from AprovarProgramacaoViagem import aprova
from InicializarAmbiente import logoff
from Viagens import viagem

# Função criada fazendo chamada da classe com a função interna

try:
    def aprovar_programacao_viagem():

        aprova.realizar_pesquisa()
        viagem.carrega_tela_viagens()
        # logoff.realizar_logoff()
        # logoff.fechar_browser()

except Exception as e:
    print(f'Não foi possivel executar esse script -> Aprova.py!'
          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
    sys.exit()
