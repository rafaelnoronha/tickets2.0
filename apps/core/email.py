from django.core import mail
from django.core.mail.backends.base import BaseEmailBackend

from apps.empresa.models import Empresa


class Email:
    def __init__(self, empresa: Empresa):
        self.__email_backend = {
            'host': Parametro,
            'port': Parametro,
            'username': Parametro,
            'password': Parametro,
            'use_tls': Parametro,
            'use_ssl': Parametro,
        }
        self.__connection = None

    def enviar(self):
        self.__connection = mail.get_connection(
            host='smtp.forteplus.com.br',
            port='587',
            username='rafael.noronha@forteplus.com.br',
            password='Rafael@2020!123',
            use_tls=None,
            use_ssl=None,
        )
        self.__connection.open()

        email = mail.EmailMessage(
            connection=self.__connection,
            from_email='rafael.noronha@forteplus.com.br',
            to=['rafaelsnoronhag@gmail.com',],
            subject='Assunto do e-mail',
            body='Teste',
            cc=['rafael.noronha@forteplus.com.br',],
            bcc=['davi.rafacho@forteplus.com.br',],
            reply_to=['rafael.noronha@forteplus.com.br',],
            headers={

            },
        )
        email.send()
