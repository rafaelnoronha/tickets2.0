from django.db import models

from apps.core.models import Base, SIM_NAO_CHOICE
from apps.usuario.models import Usuario


class PoliticaPrivacidade(Base):
    """
    Modelo que vai gerenciar as políticas de privacidade.
    """

    pp_codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código da política de privacidade',
    )

    pp_titulo = models.CharField(
        verbose_name='Título da Política de Privacidade',
        max_length=100,
        help_text='Título da política de privacidade',
    )

    pp_descricao = models.TextField(
        verbose_name='Descrição',
        help_text='A descrição/conteúdo da política de privacidade',
    )

    pp_data_validade = models.DateField(
        verbose_name='Data de Validade',
        help_text='Data da vigência da política de privacidade',
    )

    class Meta:
        db_table = 'tc_politica_privacidade'
        ordering = ['-id']
        verbose_name = 'Política de Privacidade'
        verbose_name_plural = 'Políticas de Privacidade'
        indexes = [
            models.Index(fields=['pp_data_validade'], name='idx_pp_data_validade'),
        ]
        permissions = (
            ('ativar_inativar', 'Permite ativar ou inativar uma política de privacidade'),
        )


class ConsentimentoPoliticaPrivacidade(Base):
    """
    Modelo que vai gravar os consentimentos e os não consentimentos das políticas de privacidades.
    """

    cp_titular = models.ForeignKey(
        Usuario,
        verbose_name='Consentimento da Política de Privacidade',
        related_name='rl_cp_titular',
        on_delete=models.PROTECT,
        help_text='Usuário que concentiu ou não com a política de privacidade',
    )

    cp_politica_privacidade = models.ForeignKey(
        PoliticaPrivacidade,
        verbose_name='Política de Privacidade',
        related_name='rl_cp_politica_privacidade',
        on_delete=models.PROTECT,
        help_text='Política de privacidade que o usuário consentiu ou não'
    )

    cp_consentimento = models.CharField(
        verbose_name='Consentimento',
        max_length=1,
        choices=SIM_NAO_CHOICE,
        help_text='Consentimento ou não do usuário, onde o consentimento = True e o não consentimento = False',
    )

    class Meta:
        db_table = 'tc_consentimento_politica_privacidade'
        ordering = ['-id']
        verbose_name = 'Consentimento da Política de Privacidade'
        verbose_name_plural = 'Consentimentos das Políticas de Privacidade'
        indexes = [
            models.Index(fields=['cp_consentimento'], name='idx_cp_consentimento'),
        ]
