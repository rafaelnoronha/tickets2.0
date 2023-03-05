from .models import Empresa
from .serializers import (
    EmpresaListSerializer, EmpresaGetSerializer, EmpresaPostSerializer,
    EmpresaPutPatchSerializer, EmpresaAtivarInativarSerializer
)
from .permissions import AtivarInativarPermission
from .filters import EmpresaFilterSet
from apps.core.views import BaseModelViewSet
from apps.core.decorators import action_ativar_inativar
from apps.core.permissions import BasePemission


@action_ativar_inativar
class EmpresaViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = Empresa.objects.all()
    filterset_class = EmpresaFilterSet
    serializer_class = EmpresaListSerializer
    serializer_classes = {
        'retrieve': EmpresaGetSerializer,
        'create': EmpresaPostSerializer,
        'update': EmpresaPutPatchSerializer,
        'partial_update': EmpresaPutPatchSerializer,
    }
    action_ativar_inativar = {
        'permission': AtivarInativarPermission,
        'serializer': EmpresaAtivarInativarSerializer,
    }
    # filterset_class = UsuarioFilter
