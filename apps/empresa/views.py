from .models import Empresa
from .serializers import (
    EmpresaListSerializer, EmpresaGetSerializer, EmpresaPostSerializer,
    EmpresaPutPatchSerializer, EmpresaAtivarInativarSerializer
)
from .permissions import AtivarPermission
from apps.core.views import BaseModelViewSet
from apps.core.permissions import BasePemission


class EmpresaViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = Empresa.objects.all()
    serializer_class = EmpresaListSerializer
    serializer_classes = {
        'retrieve': EmpresaGetSerializer,
        'create': EmpresaPostSerializer,
        'update': EmpresaPutPatchSerializer,
        'partial_update': EmpresaPutPatchSerializer,
    }
    actions = {
        'ativa_invativar': {
            'permission_classes': [AtivarPermission,],
            'serializer_class': EmpresaAtivarInativarSerializer
        }
    }
    # filterset_class = UsuarioFilter

    # Herdar ou colocar as actions defaults

    # @action(
    #     methods=['patch'],
    #     detail=True,
    #     url_path='ativar-inativar',
    #     url_name='ativar-inativar',
    #     permission_classes=[]
    # )
    # def ativa_invativar(self, request, pk):
    #     model = self.get_object()
    #     action = self.actions.get(frame.f_code.co_name)
    #     frame = inspect.currentframe()

    #     serializer = action.get('serializer_class')(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     model.ativo = serializer.data.get( 'ativo' )
    #     model.save()

    #     serializer = self.serializer_class(model)

    #     return Response(serializer.data, status=status.HTTP_200_OK)
