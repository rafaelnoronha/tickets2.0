from django.contrib.auth import get_user_model


def regra_padrao_autenticacao_usuario(user):
    max_num_fail_auth = get_user_model().MAX_NUM_FAIL_AUTH
    num_fail_auth_field = get_user_model().NUM_FAIL_AUTH_FIELD

    usuario_autenticado = user is not None and user.is_active and user.__getattribute__(num_fail_auth_field) < max_num_fail_auth

    if user and user.__getattribute__(num_fail_auth_field) == max_num_fail_auth:
        # Enviar email
        pass

    return usuario_autenticado