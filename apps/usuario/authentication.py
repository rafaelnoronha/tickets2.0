def regra_padrao_autenticacao_usuario(user):
    usuario_autenticado = user is not None and user.is_active and user.authentication_failures < 3

    if user and user.authentication_failures == 3:
        # Enviar email
        pass

    # Registrar log

    return usuario_autenticado