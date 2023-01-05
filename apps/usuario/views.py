from rest_framework import status
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Usuario
from .serializers import (
    UsuarioSerializer, UsuarioListSerializer, UsuarioPutPathSerializer,
    UsuarioPostSerializer, ObterParTokensSerializer
)
from apps.core.views import BaseModelViewSet


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
        url_path=r'(?P<email_usuario>\w+@[a-z]+(\.[a-z]+)+)/esqueci-minha-senha',
        url_name='esqueci-minha-senha',
    )
    def esqueci_minha_senha(self, request, email_usuario):
        return Response(f'E-mail enviado para { email_usuario }!', status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=True,
        permission_classes=[AllowAny,],
        url_path=r'redefinir-senha/(?P<jwt>(\w+\.){2}\w+)',
        url_name='redefinir-senha',
    )
    def redefinir_senha(self, request, pk, jwt):
        return Response(f'A senha do usuário { pk } foi redefinida!', status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=True,
        url_path='desbloquear',
        url_name='desbloquear',
    )
    def desbloquear(self, request, pk):
        return Response(f'Usuário { pk } bloqueado/desbloqueado!', status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=True,
        url_path='ativar-inativar',
        url_name='ativar-inativar',
    )
    def ativa_invativar(self, request, pk):
        return Response(f'Usuário { pk } ativado/inativado!', status=status.HTTP_200_OK)


class ObterParTokensView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = ObterParTokensSerializer
