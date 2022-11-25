from django.db import models

from apps.core.models import Base, SIM_NAO_CHOICE
from apps.usuario.models import Usuario


class LogAutenticacao(Base):
    """
    Modelo que armazena as tentativas de login, tanto as que tiveram sucesso quanto as que falharem.
    """

    lt_ip = models.GenericIPAddressField(
        verbose_name='IP',
        help_text='Endereço IP do cliente/dispositivo',
    )

    lt_user_agent = models.CharField(
        verbose_name='User Agent',
        max_length=200,
        help_text='Descrição do dispositivo que está autenticando',
    )

    lt_usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        related_name='rl_lt_usuario',
        on_delete=models.PROTECT,
        help_text='Usuário da tentativa de autenticação',
    )

    lt_autenticado = models.CharField(
        verbose_name='Autenticado',
        max_length=1,
        choices=SIM_NAO_CHOICE,
        help_text='Se a tentativa de autenticação foi bem-sucedida ou não',
    )

    ativo = None
    empresa = None
    owner_id = None


    class Meta:
        db_table = 'tc_log_autenticacao'
        ordering = ['-id']
        verbose_name = 'Log de autenticação'
        verbose_name_plural = 'Logs de autenticação'
        indexes = [
            models.Index(fields=['lt_ip'], name='idx_lt_ip'),
            models.Index(fields=['lt_usuario'], name='idx_lt_usuario'),
        ]
