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

    empresa = None
    ativo = None

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
