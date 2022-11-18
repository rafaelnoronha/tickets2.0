from rest_framework_simplejwt.views import TokenViewBase

class ObterParTokensView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    _serializer_class = 'apps.usuario.serializers.ObterParTokensSerializer'


