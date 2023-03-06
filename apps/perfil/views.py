
from .models import PerfilUsuario
from .serializers import (
    PerfilUsuarioListSerializer, PerfilUsuarioGetSerializer, PerfilUsuarioPutPatchSerializer,
    PerfilUsuarioPostSerializer, PerfilUsuarioAtivarInativarSerializer, PerfilUsuarioClassificarSerializer
)
from .permissions import PerfilUsuarioAtivarInativarPermission
from apps.core.views import BaseModelViewSet
from apps.core.permissions import BasePemission
from apps.core.decorators import action_ativar_inativar


@action_ativar_inativar
class PerfilUsuarioViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioListSerializer
    serializer_classes = {
        'retrieve': PerfilUsuarioGetSerializer,
        'create': PerfilUsuarioPostSerializer,
        'update': PerfilUsuarioPutPatchSerializer,
        'partial_update': PerfilUsuarioPutPatchSerializer,
    }
    action_ativar_inativar = {
        'permission': PerfilUsuarioAtivarInativarPermission,
        'serializer': PerfilUsuarioAtivarInativarSerializer,
    }
