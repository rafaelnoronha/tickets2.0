def regra_padrao_autenticacao_usuario(user):
    return user is not None and user.is_active and user.authentication_failures < 3