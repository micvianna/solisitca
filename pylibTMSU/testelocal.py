
import sys

from InicializarAmbiente import inicia
from ProgramacaoViagem import programacao
from AprovarProgramacaoViagem import aprova

# Função criada fazendo chamada da classe com a função interna


inicia.abrir_browser()
inicia.realizar_login('401')
programacao.criar_programacao_viagem()
programacao.criar_programacao()
inicia.realiza_logoff()
inicia.realizar_login('402')
aprova.realizar_pesquisa_confirma()
inicia.efetuar_logoff()
inicia.fecha_Janela()
inicia.abrir_browser()
programacao.carrega_xml('prog2.xml')
programacao.carrega_tela()
programacao.criar_programacao()
inicia.realizar_login()

