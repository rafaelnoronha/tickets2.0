import django_filters

from .models import LogAutenticacao
from apps.core.filters import lookup_types_string
from apps.core.decorators import fields_base_filter_set
from apps.usuario.filters import UsuarioFilterSet


@fields_base_filter_set
class LogAutenticacaoFilterSet(django_filters.FilterSet):
    class Meta:
        model = LogAutenticacao
        fields = {
            'lt_ip': lookup_types_string,
            'lt_user_agent': lookup_types_string,
            'lt_usuario': ['exact'],
            'lt_autenticado': lookup_types_string,
        }
        fields.update([(f'lt_usuario__{chave}', valor) for chave, valor in UsuarioFilterSet.Meta.fields.items()])
