from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.core.models import Base
from apps.core.validators import TelefoneValidator, CelularValidator
from apps.usuario.models import Usuario


class ClassificacaoUsuario(Base):
    """
    Modelo da classificação dos usuários.
    """

    cs_codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código da Classificação',
    )

    cs_nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        help_text='Nome da classificação',
    )

    cs_descricao = models.TextField(
        verbose_name='descricao',
        blank=True,
        help_text='Descrição da classificação',
    )


    class Meta:
        ordering = ['-id']
        db_table = 'tc_classificacao_usuario'
        verbose_name = 'Classificação do Usuário'
        verbose_name_plural = 'Classificações de Usuário'
        indexes = [
            models.Index(fields=['cs_codigo'], name='idx_cs_codigo'),
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
        validators=[
            TelefoneValidator()
        ],
        help_text='Telefone fixo ex: 3100000000',
    )

    ps_celular = models.CharField(
        verbose_name='Celular',
        max_length=11,
        blank=True,
        validators=[
            CelularValidator()
        ],
        help_text='Telefone celular ex: 31900000000',
    )

    ps_classificacao = models.ForeignKey(
        ClassificacaoUsuario,
        verbose_name='Classificação',
        related_name='rl_sr_classificacao',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )

    ps_media_avaliacoes = models.FloatField(
        verbose_name='Média das avaliações',
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        help_text='Média das avaliações dos chamados',
    )

    ps_observacoes = models.CharField(
        verbose_name='Observações',
        max_length=4000,
        blank=True,
        help_text='Observações referênte ao usuário',
    )


    class Meta:
        db_table = 'tc_perfil_usuario'
        ordering = ['-id',]
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
        indexes = [
            models.Index(fields=['ps_media_avaliacoes',], name='idx_ps_media_avaliacoes'),
        ]

    def __str__(self):
        return str(self.id)


class PerfilUsuarioEmpresa(Base):
    pm_perfil = models.ForeignKey(
        PerfilUsuario,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        related_name='rl_pm_perfil',
        help_text='Perfil de usuário que terá acessoa à empresa',
    )


    class Meta:
        db_table = 'tc_perfil_usuario_empresa'
        verbose_name = 'Perfil Usuário Empresa'
        verbose_name_plural = 'Perfis Usuário Empresa'
        ordering = ['-id',]
        unique_together = ['pm_perfil', 'empresa']
        indexes = [
            models.Index(fields=['pm_perfil',], name='idx_pm_perfil'),
        ]

    def __str__(self):
        return str(self.id)
