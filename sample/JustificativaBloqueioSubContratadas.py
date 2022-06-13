from pylibTMSU.InicializarAmbiente import inicia
from pylibTMSU.CriarJustBloqSubContratada import justificativa


inicia.abrirAmbiente()
inicia.efetuarLogin()
justificativa.carrega_tela_justi_bloq_sub()
justificativa.consultar()
inicia.efetuarLogoff()


