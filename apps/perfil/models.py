from django.db import models

from apps.core.models import Base
from apps.usuario.models import Usuario


class Classificacao(Base):
    """
    Modelo da classificação dos usuários.
    """

    cl_codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código da Classificação',
    )

    cl_nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        help_text='Nome da classificação',
    )

    cl_descricao = models.TextField(
        verbose_name='descricao',
        help_text='Descrição da classificação',
        blank=True,
    )

    class Meta:
        ordering = ['-id']
        db_table = 'tc_classificacao'
        verbose_name = 'Classificacao'
        verbose_name_plural = 'Classificacoes'
        indexes = [
            models.Index(fields=['cl_codigo'], name='idx_cl_codigo'),
        ]

    def __str__(self):
        return str(self.id)


class PerfilUsuario(Base):
    """
    Modelo que armazena os dados "adicionais" dos usuários(clientes e prestadores de serviço).
    """

    ps_usuario = models.OneToOneField(
        Usuario,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        related_name='rl_ps_usuario',
        help_text='Usuário vinculado ao perfil',
    )

    ps_nome = models.CharField(
        verbose_name='Nome',
        max_length=150,
        help_text='Nome do usuário',
    )

    ps_telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        help_text='Telefone fixo ex: 3100000000',
    )

    ps_celular = models.CharField(
        verbose_name='Celular',
        max_length=11,
        blank=True,
        help_text='Telefone celular ex: 31900000000',
    )

    ps_classificacao = models.ForeignKey(
        Classificacao,
        verbose_name='Classificação',
        related_name='rl_sr_classificacao',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )

    ps_media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
        help_text='Média das avaliações dos chamados',
    )

    ps_observacoes = models.CharField(
        verbose_name='Observações',
        max_length=4000,
        blank=True,
        help_text='Observações referênte ao usuário',
    )

    ativo = None
    empresa = None


    class Meta:
        db_table = 'tc_perfil_usuario'
        ordering = ['-id',]
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
        indexes = [
            models.Index(fields=['ps_usuario',], name='idx_ps_usuario'),
            models.Index(fields=['ps_media_avaliacoes',], name='idx_ps_media_avaliacoes'),
        ]

    def __str__(self):
        return str(self.id)
