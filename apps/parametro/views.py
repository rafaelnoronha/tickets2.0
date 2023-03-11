from .models import Parametro
from .serializers import (
    ParametroListSerializer, ParametroGetSerializer, ParametroPostSerializer,
    ParametroPutPatchSerializer
)
from .filters import ParametroFilterSet
from apps.core.views import BaseModelViewSet
from apps.core.permissions import BasePemission


class ParametroViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = Parametro.objects.all()
    filterset_class = ParametroFilterSet
    serializer_class = ParametroListSerializer
    serializer_classes = {
        'retrieve': ParametroGetSerializer,
        'create': ParametroPostSerializer,
        'update': ParametroPutPatchSerializer,
        'partial_update': ParametroPutPatchSerializer,
    }
