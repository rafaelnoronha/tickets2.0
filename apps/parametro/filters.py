import django_filters

from .models import Parametro
from apps.core.filters import lookup_types_string, lookup_types_base


class ParametroFilterSet(django_filters.FilterSet):
    class Meta:
        model = Parametro
        fields = {
            'pr_codigo': lookup_types_string,
            'pr_descricao': lookup_types_string,
            'pr_valor': lookup_types_string,
        }
        fields.update(lookup_types_base)
