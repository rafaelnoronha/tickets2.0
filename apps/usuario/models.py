from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from apps.core.models import Base


class UserManagerCustom(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class Usuario(Base, AbstractBaseUser, PermissionsMixin):
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

    is_active = models.BooleanField(
        verbose_name='Is active',
        default=True,
        help_text='Informa se o usuário está ativo ou inativo',
    )

    ativo = None
    empresa = None

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
        )


class PerfilUsuario(Base):
    """
    Modelo que armazena os dados "adicionais" dos usuários(clientes e prestadores de serviço).
    """

    ps_usuario = models.OneToOneField(
        Usuario,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        related_name='rl_ps_usuario',
    )

    ps_nome = models.CharField(
        verbose_name='Nome',
        max_length=150,
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

    # sr_classificacao = models.ForeignKey(
    #     Classificacao,
    #     verbose_name='Classificação',
    #     related_name='rl_sr_classificacao',
    #     null=True,
    #     on_delete=models.PROTECT,
    #     help_text='A qual classificação de usuário o ticket é designado'
    # )

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

    ps_atendente = models.CharField(
        verbose_name='Atendente',
        max_length=1,
        default='N',
        help_text='Se é gerente, caso seja, existem privilégios padrões para um usuário do tipo gerente',
    )

    ps_gerente = models.CharField(
        verbose_name='Gerente',
        max_length=1,
        default='N',
        help_text='Este campo informa se o usuáio é gerente ou não',
    )

    ativo = None


    class Meta:
        db_table = 'tc_perfil_usuario'
        ordering = ['-id',]
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
        indexes = [
            models.Index(fields=['ps_usuario',], name='idx_ps_usuario'),
            models.Index(fields=['empresa',], name='idx_ps_empresa'),
        ]
        permissions = (
            ('transformar_em_gerente', 'Concede privilégios de um gerente ao usuário'),
        )
