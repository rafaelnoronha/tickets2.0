import django_filters

from .models import Parametro
from apps.core.filters import lookup_types_string
from apps.core.decorators import fields_base_filter_set


@fields_base_filter_set
class ParametroFilterSet(django_filters.FilterSet):
    class Meta:
        model = Parametro
        fields = {
            'pr_codigo': lookup_types_string,
            'pr_descricao': lookup_types_string,
            'pr_valor': lookup_types_string,
        }
