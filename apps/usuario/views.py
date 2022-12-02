from rest_framework_simplejwt.views import TokenViewBase
from apps.usuario.serializers import ObterParTokensSerializer, AtualizacaoTokenSerializer


class ObterParTokensView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = ObterParTokensSerializer
