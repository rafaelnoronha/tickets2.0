class DefaultData:
    def __init__(self):
        self.__parametros = [
        {
            'pr_codigo': 'EMAIL_HOST',
            'pr_descricao': 'O host a ser usado para enviar e-mail. ',
            'pr_valor': '',
            'empresa': None
        },
        {
            'pr_codigo': 'EMAIL_HOST_USER',
            'pr_descricao': 'Nome de usuário a ser usado para o servidor SMTP definido em EMAIL_HOST.',
            'pr_valor': '',
            'empresa': None
        },
        {
            'pr_codigo': 'EMAIL_HOST_PASSWORD',
            'pr_descricao': 'Senha a ser usada para o servidor SMTP definido em EMAIL_HOST.',
            'pr_valor': '',
            'empresa': None
        },
        {
            'pr_codigo': 'EMAIL_PORT',
            'pr_descricao': 'Porta a ser usada para o servidor SMTP definido em EMAIL_HOST.',
            'pr_valor': '',
            'empresa': None
        },
        {
            'pr_codigo': 'EMAIL_USE_TLS',
            'pr_descricao': 'Se deve usar uma conexão TLS (segura) ao falar com o servidor SMTP. S(Sim) ou N(Não)',
            'pr_valor': 'N',
            'empresa': None
        },
        {
            'pr_codigo': 'EMAIL_USE_SSL',
            'pr_descricao': 'Se deve usar uma conexão implícita TLS (segura) ao falar com o SMTP servidor. S(Sim) ou N(Não)',
            'pr_valor': 'N',
            'empresa': None
        },
    ]

    def gerar_parametros(self):
        pass
        # from apps.parametro.models import Parametro

        # for parametro in self.__parametros:
        #     parametro_criado, criado = Parametro.objects.get_or_create(
        #         pr_codigo=parametro.get('pr_codigo'),
        #         empresa=parametro.get('empresa'),
        #         defaults=parametro
        #     )

        #     if criado:
        #         print(f"-> Parâmetro { parametro_criado.pr_codigo } criado.")
