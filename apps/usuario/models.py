from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator


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
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name='username',
        max_length=100,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': 'Um usuário com esse username já existe.',
        },
    )

    email = models.EmailField(
        verbose_name='E-mail',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    objects = UserManagerCustom()


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-id',]
        permissions = (
            ('permite_ativar_inativar_usuario', 'Permite ativar ou inativar um usuário'),
        )


class PerfilUsuario(models.Model):
    ps_usuario = models.OneToOneField(
        Usuario,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        related_name='rl_ps_usuario',
    )

    ps_nome = models.CharField(
        verbose_name='Nome',
        max_length=150,
        blank=True,
    )


    class Meta:
        db_table = 'tk_perfil_usuario'
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
        ordering = ['-id',]
