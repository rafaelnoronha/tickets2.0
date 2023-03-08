
from rest_framework import mixins

from .models import PerfilUsuario, PerfilUsuarioEmpresa, ClassificacaoPerfil
from .serializers import (
    PerfilUsuarioListSerializer, PerfilUsuarioGetSerializer, PerfilUsuarioPutPatchSerializer,
    PerfilUsuarioPostSerializer, PerfilUsuarioAtivarInativarSerializer, PerfilUsuarioClassificarSerializer,

    PerfilUsuarioEmpresaListSerializer, PerfilUsuarioEmpresaGetSerializer, PerfilUsuarioEmpresaPostSerializer,
    PerfilUsuarioEmpresaAtivarInativarSerializer,

    ClassificacaoPerfilListSerializer, ClassificacaoPerfilGetSerializer, ClassificacaoPerfilPutPatchSerializer,
    ClassificacaoPerfilPostSerializer, ClassificacaoPerfilAtivarInativarSerializer
)
from .permissions import (
    PerfilUsuarioAtivarInativarPermission, PerfilUsuarioEmpresaAtivarInativarPermission,
    ClassificacaoPerfilAtivarInativarPermission
)
from apps.core.views import BaseModelViewSet, EssentialModelViewSet
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


@action_ativar_inativar
class PerfilUsuarioEmpresaViewSet(
        mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        mixins.DestroyModelMixin, EssentialModelViewSet
    ):
    permission_classes = (BasePemission, )
    queryset = PerfilUsuarioEmpresa.objects.all()
    serializer_class = PerfilUsuarioEmpresaListSerializer
    serializer_classes = {
        'retrieve': PerfilUsuarioEmpresaGetSerializer,
        'create': PerfilUsuarioEmpresaPostSerializer,
    }
    action_ativar_inativar = {
        'permission': PerfilUsuarioEmpresaAtivarInativarPermission,
        'serializer': PerfilUsuarioEmpresaAtivarInativarSerializer,
    }


@action_ativar_inativar
class ClassificacaoPerfilViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = ClassificacaoPerfil.objects.all()
    serializer_class = ClassificacaoPerfilListSerializer
    serializer_classes = {
        'retrieve': ClassificacaoPerfilGetSerializer,
        'create': ClassificacaoPerfilPostSerializer,
        'update': ClassificacaoPerfilPutPatchSerializer,
        'partial_update': ClassificacaoPerfilPutPatchSerializer,
    }
    action_ativar_inativar = {
        'permission': ClassificacaoPerfilAtivarInativarPermission,
        'serializer': ClassificacaoPerfilAtivarInativarSerializer,
    }
