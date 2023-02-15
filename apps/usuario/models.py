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

    owner_id = models.ForeignKey(
        'usuario.Usuario',
        verbose_name='Owner Id',
        on_delete=models.PROTECT,
        null=True,
        help_text='Para qual empresa o parâmetro será usado',
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
            ('transformar_admin', 'Permite transformar um usuário em administrador ou não'),
            ('transformar_gerente', 'Permite transformar um usuário em gerente ou não'),
        )

    def __str__(self):
        return str(self.id)


class UsuarioEmpresa(Base):
    sm_usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        related_name='rl_sm_usuario',
        help_text='Usuário que terá acessoa à empresa',
    )

    sm_empresa = models.ForeignKey(
        'empresa.Empresa',
        verbose_name='Empresa',
        on_delete=models.CASCADE,
        related_name='rl_sm_usuario',
        help_text='Empresa que será acessada pelo usuário',
    )

    empresa = None

    class Meta:
        db_table = 'tc_usuario_empresa'
        verbose_name = 'Usuário Empresa'
        verbose_name_plural = 'Usuários Empresa'
        ordering = ['-id',]
        unique_together = ['sm_usuario', 'sm_empresa']
        indexes = [
            models.Index(fields=['sm_usuario',], name='idx_sm_usuario'),
            models.Index(fields=['sm_empresa',], name='idx_sm_empresa'),
        ]

    def __str__(self):
        return str(self.id)
