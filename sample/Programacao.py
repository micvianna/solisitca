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
import time

from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarProgramacaoViagem import programacao
from pylibTMSU.CarregarXMLProgramacaoViagem import CarregarXMLProgramacaoViagem

# Função criada fazendo chamada da classe com a função interna


inicia.abrirAmbiente()
inicia.efetuarLogin()
#CarregarXMLProgramacaoViagem.acesso('test.xml')
programacao.criar_programacao_viagem()
programacao.criar_programacao()
time.sleep(3)
inicia.efetuarLogoff()
time.sleep(3)
inicia.fecharAmbiente()




