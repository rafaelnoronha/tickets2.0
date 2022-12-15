from django.core import mail
from django.core.mail.backends.smtp import EmailBackend

from apps.empresa.models import Empresa


class Email:
    def __init__(self, empresa: Empresa):
        self.__email_backend = EmailBackend(
            host='smtp.forteplus.com.br',
            port='587',
            username='rafael.noronha@forteplus.com.br',
            password='Rafael@2020!123',
            use_tls=None,
            use_ssl=True,
        )
        self.__connection = None

    def enviar(self):
        self.__connection = mail.get_connection(backend=self.__email_backend)
        self.__connection.open()

        email = mail.EmailMessage(
            connection=self.__connection,
            from_email='rafael.noronha@forteplus.com.br',
            to='rafaelsnoronhag@gmail.com',
            subject='Assunto do e-mail',
            body='Mensagem',
            cc=['rafael.noronha@forteplus.com.br',],
            bcc=['davi.rafacho@forteplus.com.br',],
            reply_to=['rafael.noronha@forteplus.com.br',],
            headers={'Message-ID': 'foo'},
        )
        email.send()
