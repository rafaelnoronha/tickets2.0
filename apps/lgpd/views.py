from rest_framework import mixins

from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from .serializers import (
    PoliticaPrivacidadeGetSerializer, PoliticaPrivacidadeListSerializer, PoliticaPrivacidadePostSerializer,
    PoliticaPrivacidadeAtivarInativarSerializer, ConsentimentoPoliticaPrivacidadeGetSerializer,
    ConsentimentoPoliticaPrivacidadeListSerializer, ConsentimentoPoliticaPrivacidadePostSerializer
)
from .permissions import PoliticaPrivacidadeAtivarInativarPermission
from .filters import PoliticaPrivacidadeFilterSet, ConsentimentoPoliticaPrivacidadeFilterSet
from apps.core.views import EssentialModelViewSet
from apps.core.decorators import action_ativar_inativar
from apps.core.permissions import BasePemission


@action_ativar_inativar
class PoliticaPrivacidadeViewSet(
        mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        EssentialModelViewSet
    ):
    permission_classes = (BasePemission, )
    queryset = PoliticaPrivacidade.objects.all()
    filterset_class = PoliticaPrivacidadeFilterSet
    serializer_class = PoliticaPrivacidadeListSerializer
    serializer_classes = {
        'retrieve': PoliticaPrivacidadeGetSerializer,
        'create': PoliticaPrivacidadePostSerializer,
    }
    action_ativar_inativar = {
        'permission': PoliticaPrivacidadeAtivarInativarPermission,
        'serializer': PoliticaPrivacidadeAtivarInativarSerializer,
    }


class ConsentimentoPoliticaPrivacidadeViewSet(
        mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        EssentialModelViewSet
    ):
    permission_classes = (BasePemission, )
    queryset = ConsentimentoPoliticaPrivacidade.objects.all()
    filterset_class = ConsentimentoPoliticaPrivacidadeFilterSet
    serializer_class = ConsentimentoPoliticaPrivacidadeListSerializer
    serializer_classes = {
        'retrieve': ConsentimentoPoliticaPrivacidadeGetSerializer,
        'create': ConsentimentoPoliticaPrivacidadePostSerializer,
    }
