import django_filters

from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from apps.core.filters import lookup_types_string, lookup_types_date
from apps.core.decorators import fields_base_filter_set
from apps.usuario.filters import UsuarioFilterSet


@fields_base_filter_set
class PoliticaPrivacidadeFilterSet(django_filters.FilterSet):
    class Meta:
        model = PoliticaPrivacidade
        fields = {
            'pp_codigo': lookup_types_string,
            'pp_titulo': lookup_types_string,
            'pp_descricao': lookup_types_string,
            'pp_data_validade': lookup_types_date,
        }


@fields_base_filter_set
class ConsentimentoPoliticaPrivacidadeFilterSet(django_filters.FilterSet):
    class Meta:
        model = ConsentimentoPoliticaPrivacidade
        fields = {
            'cp_titular': ['exact'],
            'cp_politica_privacidade': ['exact'],
            'cp_consentimento': lookup_types_string,
        }
        fields.update([(f'cp_titular__{chave}', valor) for chave, valor in UsuarioFilterSet.Meta.fields.items()])
        fields.update([(f'cp_politica_privacidade__{chave}', valor) for chave, valor in PoliticaPrivacidadeFilterSet.Meta.fields.items()])
