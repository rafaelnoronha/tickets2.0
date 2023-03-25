from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.core.models import Base
from apps.core.validators import TelefoneValidator, CelularValidator


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
        verbose_name_plural = 'Classificações do Usuário'
        indexes = [
            models.Index(fields=['cs_codigo'], name='idx_cs_codigo'),
        ]
        permissions = (
            ('ativar_inativar', 'Permite ativar ou inativar a classificação de usuário'),
        )


class UserManagerCustom(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Modelo que armazena os dados de autenticação dos usuários(clientes e prestadores de serviço).
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name='Username',
        max_length=100,
        unique=True,
        help_text='Nome de usuário',
        validators=[username_validator],
        error_messages={
            'unique': 'Um usuário com esse username já existe.',
        },
    )

    email = models.EmailField(
        verbose_name='E-mail',
        unique=True,
        help_text='E-mail do usuário',
    )

    authentication_failures = models.PositiveSmallIntegerField(
        verbose_name='Authentication Failures',
        default=0,
        help_text='Número de falhas de autenticação',
    )

    uuid_password_reset = models.CharField(
        verbose_name='UUID Password Reset',
        max_length=36,
        blank=True,
        help_text='UUID da última solicitação de redefinição de senha'
    )

    is_active = models.BooleanField(
        verbose_name='Is active',
        default=True,
        help_text='Informa se o usuário está ativo ou inativo',
    )

    is_staff = models.BooleanField(
        verbose_name='Is staff',
        default=False,
        help_text='Informa se o usuário é um atendente',
    )

    is_manager = models.BooleanField(
        verbose_name='Is manager',
        default=False,
        help_text='Informa se o usuário é um gerente',
    )

    sr_nome = models.CharField(
        verbose_name='Nome',
        max_length=150,
        blank=True,
        help_text='Nome do usuário',
    )

    sr_telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        blank=True,
        validators=[
            TelefoneValidator()
        ],
        help_text='Telefone fixo ex: 3100000000',
    )

    sr_celular = models.CharField(
        verbose_name='Celular',
        max_length=11,
        blank=True,
        validators=[
            CelularValidator()
        ],
        help_text='Telefone celular ex: 31900000000',
    )

    sr_classificacao = models.ForeignKey(
        ClassificacaoUsuario,
        verbose_name='Classificação',
        related_name='rl_sr_classificacao',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        help_text='Informa a classificação do usuário'
    )

    sr_media_avaliacoes = models.FloatField(
        verbose_name='Média das avaliações',
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        help_text='Média das avaliações dos chamados',
    )

    sr_observacoes = models.CharField(
        verbose_name='Observações',
        max_length=4000,
        blank=True,
        help_text='Observações referênte ao usuário',
    )

    data_criacao = models.DateField(
        verbose_name='Data de Criação',
        auto_now_add=True,
        help_text='Data da criação do registro'
    )

    hora_criacao = models.TimeField(
        verbose_name='Hora de Criação',
        auto_now_add=True,
        help_text='Hora da criação do registro'
    )

    data_alteracao = models.DateField(
        verbose_name='Data da Alteração',
        auto_now=True,
        help_text='Data da alteração do registro'
    )

    hora_alteracao = models.TimeField(
        verbose_name='Hora da Alteração',
        auto_now=True,
        help_text='Hora da alteração do registro'
    )


    class Meta:
        db_table = 'tc_perfil_usuario'
        ordering = ['-id']
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
        indexes = [
            models.Index(fields=['ps_media_avaliacoes'], name='idx_ps_media_avaliacoes'),
        ]
        permissions = (
            ('ativar_inativar', 'Permite ativar ou inativar um perfil de usuário'),
        )


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    NUM_FAIL_AUTH_FIELD = 'authentication_failures'
    MAX_NUM_FAIL_AUTH = 5

    objects = UserManagerCustom()


    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-id',]
        indexes = [
            models.Index(fields=['username',], name='idx_username'),
            models.Index(fields=['email',], name='idx_email'),
        ]
        permissions = (
            ('ativar_inativar', 'Permite ativar ou inativar um usuário'),
            ('desbloquear', 'Permite desbloquear um usuário bloqueado por errar a senha x vezes'),
            ('transformar_admin', 'Permite transformar um usuário em administrador'),
            ('transformar_gerente', 'Permite transformar um usuário em gerente'),
            ('classificar', 'Permite classificar um usuário'),
        )
    

class UsuarioEmpresa(Base):
    """
    Modelo que une um usuário à uma empresa.
    """

    sm_usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        related_name='rl_sm_usuario',
        on_delete=models.CASCADE,
        help_text='Usuário que terá acesso a uma determinada empresa'
    )


    class Meta:
        ordering = ['-id']
        db_table = 'tc_usuario_empresa'
        verbose_name = 'Usuário Empresa'
        verbose_name_plural = 'Usuários Empresa'
        permissions = (
            ('ativar_inativar', 'Permite ativar ou inativar o acesso de um usuário a uma empresa'),
        )
