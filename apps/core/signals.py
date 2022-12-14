from .default import DefaultData


def gerar_registros_padroes(sender, *args, **kwargs):
    default = DefaultData()
    default.gerar_parametros()
