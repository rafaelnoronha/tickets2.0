from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenViewBase

from .models import Usuario
from .serializers import UsuarioSerializer, ObterParTokensSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ObterParTokensView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = ObterParTokensSerializer
