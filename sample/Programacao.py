"""
Função: (ProgramacaoViagem.xml) e coloca-los em variaveis
Objetivo: Realizar a criação de Programação de Viagem
Dependências: pylibTMSU.InicializarAmbiente, pylibTMSU.ProgramacaoViagem e requeriments.txt
Responsavel: Michel Viana

Historico: 20/04/2022: Reorganizados imports
                       Desenvolvido função: criar_programacao_viagem()
                       Adicionada mensagens de tratamento quando houver erros

"""

import sys

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.ProgramacaoViagem import programacao

# Função criada fazendo chamada da classe com a função interna

try:
    def criar_programacao_viagem():
        inicia.abrir_browser()
        inicia.realizar_login()
        programacao.criar_programacao_viagem()
        programacao.criar_programacao()
except Exception as e:
    print(f'Não foi possivel executar esse script -> Programacao.py!'
          f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
    sys.exit()


criar_programacao_viagem()

