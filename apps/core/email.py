from django.core import mail
from django.core.mail import EmailMessage
from django.db.models import Q
from datetime import date

from .models import Parametro


class Email:
    def __init__(self, empresa):
        self.host = self.__get_parametro__(empresa, 'EMAIL_HOST').pr_valor
        self.port = self.__get_parametro__(empresa, 'EMAIL_PORT').pr_valor
        self.username = self.__get_parametro__(empresa, 'EMAIL_HOST_USER').pr_valor
        self.password = self.__get_parametro__(empresa, 'EMAIL_HOST_PASSWORD').pr_valor
        self.use_tls = self.__get_parametro__(empresa, 'EMAIL_USE_TLS').pr_valor
        self.use_ssl = self.__get_parametro__(empresa, 'EMAIL_USE_SSL').pr_valor

    def __get_parametro__(self, empresa, parametro):
        return (
            Parametro.objects
            .filter(Q(pr_codigo=parametro), Q(empresa=empresa) | Q(empresa=None))
            .order_by('empresa')
            .first() or Parametro()
        )

    def enviar(self, destinatario, assunto, corpo, copia=None, copia_oculta=None):
        connection = mail.get_connection(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            use_tls=True if self.use_tls == 'S' else False,
            use_ssl=True if self.use_ssl == 'S' else False,
        )

        email = EmailMessage(
            connection=connection,
            from_email=self.username,
            to=destinatario,
            subject=assunto,
            body=corpo,
            cc=copia,
            bcc=copia_oculta,
            reply_to=[self.username,],
        )
        email.content_subtype = 'html'
        email.send()

        # https://stackoverflow.com/questions/36351318/django-email-message-as-html
