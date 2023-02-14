from .models import Empresa
from .serializers import EmpresaSerializer
from apps.core.views import BaseModelViewSet
from apps.core.permissions import BasePemission


class EmpresaViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    # filterset_class = UsuarioFilter
