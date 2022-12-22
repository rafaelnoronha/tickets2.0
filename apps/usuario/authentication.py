from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from apps.empresa.models import Empresa
from apps.core.email import Email


def regra_padrao_autenticacao_usuario(user):
    max_num_fail_auth = get_user_model().MAX_NUM_FAIL_AUTH
    num_fail_auth_field = get_user_model().NUM_FAIL_AUTH_FIELD

    usuario_autenticado = user is not None and user.is_active and user.__getattribute__(num_fail_auth_field) < max_num_fail_auth

    if user and user.__getattribute__(num_fail_auth_field) == max_num_fail_auth or True:
        email = Email(Empresa())
        email.enviar(
            destinatario=['rafaelsnoronhag@gmail.com',],
            assunto='Teste Envio de e-mail',
            corpo='123'
        )

    return usuario_autenticado


class JWTAuthenticationCustom(JWTAuthentication):
    def get_validated_token(self, raw_token):
        """
        Validates an encoded JSON web token and returns a validated token
        wrapper object.
        """
        messages = []
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                auth_token = AuthToken(raw_token)
                if auth_token.__getitem__('teste') == 123:
                    raise TokenError('Token Inválido')

                return auth_token
            except TokenError as e:
                messages.append(
                    {
                        "token_class": AuthToken.__name__,
                        "token_type": AuthToken.token_type,
                        "message": e.args[0],
                    }
                )

        raise InvalidToken(
            {
                "detail": _("Given token not valid for any token type"),
                "messages": messages,
            }
        )
