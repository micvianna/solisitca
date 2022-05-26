"""
Função: Script principal para chamar a programação e a aprovação
Objetivo: através do Script principal cahamar as funções
          criar_programacao_viagem()
          aprovar_programacao_viagem()
Dependências: Programacao, Aprova e requeriments.txt
Responsavel: Michel Viana

Histórico: 20/04/2022: Criação do Script Main
                       Fazendo chamadas nas funções:
                              criar_programacao_viagem()
                            aprovar_programacao_viagem()
"""
from sample import Programacao
import Aprova


Programacao.criar_programacao_viagem()
Aprova.aprovar_programacao_viagem()


