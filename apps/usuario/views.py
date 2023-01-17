from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import exceptions
from decouple import config
from datetime import datetime, timezone, timedelta
from jwt import encode as jwt_encode, decode as jwt_decode
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError
import uuid

from .models import Usuario
from .serializers import (
    UsuarioSerializer, UsuarioListSerializer, UsuarioPutPathSerializer,
    UsuarioPostSerializer, ObterParTokensSerializer, UsuarioRedefinirSenhaSerializer,
    UsuarioAlterarSenhaSerializer, UsuarioSerializer, UsuarioAtivarInativarSerializer
)
from apps.core.views import BaseModelViewSet
from apps.core.email import EmailHTML


class UsuarioViewSet(BaseModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer

    serializer_classes = {
        'retrieve': UsuarioSerializer,
        'create': UsuarioPostSerializer,
        'update': UsuarioPutPathSerializer,
        'partial_update': UsuarioPutPathSerializer,
    }

    @action(
        methods=['get'],
        detail=False,
        permission_classes=[AllowAny,],
        url_path=r'(?P<email_usuario>\w+@[a-z]+(\.[a-z]+)+)/solicitar-redefinicao-senha',
        url_name='solicitar-redefinicao-senha',
    )
    def esqueci_minha_senha(self, request, email_usuario):
        usuario = get_object_or_404(Usuario, email=email_usuario)
        uuid_password_reset = str(uuid.uuid4())

        try:
            jwt_redefinir_senha = jwt_encode(
                {
                    'token_type': 'password-reset',
                    'iat': datetime.now(tz=timezone.utc),
                    'exp': datetime.now(tz=timezone.utc) + timedelta(minutes=15),
                    'jti': uuid_password_reset,
                    'user_email': usuario.email,
                },
                config('SECRET_KEY'),
                algorithm='HS256'
            )

            email = EmailHTML()
            email.enviar(
                destinatario=[usuario.email,],
                assunto='Recuperação de Senha',
                corpo={
                    'template': 'email_recuperacao_senha.html',
                    'dados': {'usuario': usuario, 'jwt': jwt_redefinir_senha}
                }
            )

            usuario.uuid_password_reset = uuid_password_reset
            usuario.save()

        except:
            pass

        return Response({ 'token': jwt_redefinir_senha }, status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=False,
        permission_classes=[AllowAny,],
        url_path=r'redefinir-senha/(?P<jwt>[\w\-]+\.[\w\-]+\.[\w\-]+)',
        url_name='redefinir-senha',
    )
    def redefinir_senha(self, request, jwt):
        try:
            jwt_redefinir_senha = jwt_decode(
                jwt,
                config('SECRET_KEY'),
                algorithms=['HS256']
            )

            usuario = get_object_or_404(Usuario, email=jwt_redefinir_senha.get('user_email'))

            if not usuario.uuid_password_reset or jwt_redefinir_senha.get('jti') != usuario.uuid_password_reset:
                raise ValueError('O token é inválido')

            serializer = UsuarioRedefinirSenhaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            usuario.authentication_failures = 0
            usuario.uuid_password_reset = ''
            usuario.set_password(serializer.data.get('password'))
            usuario.save()

        except (InvalidSignatureError, ExpiredSignatureError, ValueError):
            return Response({'detail': 'O token é inválido ou expirado.' }, status=status.HTTP_401_UNAUTHORIZED)

        return Response(f'A senha do usuário { jwt_redefinir_senha } foi redefinida!', status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=True,
        url_path='alterar-senha',
        url_name='alterar-senha',
    )
    def alterar_password(self, request, pk):
        usuario = self.get_object()
        serializer = UsuarioAlterarSenhaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = authenticate(username=usuario.username, password=serializer.data.get('current_password'))

        if usuario is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        usuario.set_password(serializer.data.get('new_password'))
        usuario.save()

        serializer = UsuarioSerializer(usuario)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=True,
        url_path='desbloquear',
        url_name='desbloquear',
    )
    def desbloquear(self, request, pk):
        usuario = self.get_object()
        usuario.authentication_failures = 0
        usuario.save()

        serializer = UsuarioSerializer(usuario)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=True,
        url_path='ativar-inativar',
        url_name='ativar-inativar',
    )
    def ativa_invativar(self, request, pk):
        usuario = self.get_object()

        serializer = UsuarioAtivarInativarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario.is_active = serializer.data.get( 'is_active' )
        usuario.save()

        serializer = UsuarioSerializer(usuario)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ObterParTokensView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = ObterParTokensSerializer
