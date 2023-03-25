from rest_framework import mixins

from .models import LogAutenticacao
from .serializers import LogAutenticacaoGetSerializer, LogAutenticacaoListSerializer
from .filters import LogAutenticacaoFilterSet
from apps.core.views import EssentialModelViewSet
from apps.core.permissions import BasePemission


class LogAutenticacaoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, EssentialModelViewSet):
    permission_classes = (BasePemission, )
    queryset = LogAutenticacao.objects.all()
    filterset_class = LogAutenticacaoFilterSet
    serializer_class = LogAutenticacaoListSerializer
    serializer_classes = {
        'retrieve': LogAutenticacaoGetSerializer,
    }
