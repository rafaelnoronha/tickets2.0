import django_filters

from .models import Empresa
from apps.core.filters import lookup_types_string, lookup_types_number
from apps.core.decorators import fields_base_filter_set


@fields_base_filter_set
class EmpresaFilterSet(django_filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'mp_cpf_cnpj': lookup_types_string,
            'mp_razao_social': lookup_types_string,
            'mp_nome_fantasia': lookup_types_string,
            'mp_logradouro': lookup_types_string,
            'mp_numero': lookup_types_string,
            'mp_complemento': lookup_types_string,
            'mp_bairro': lookup_types_string,
            'mp_municipio': lookup_types_string,
            'mp_uf': lookup_types_string,
            'mp_cep': lookup_types_string,
            'mp_pais': lookup_types_string,
            'mp_telefone': lookup_types_string,
            'mp_media_avaliacoes': lookup_types_number,
            'mp_prestadora_servico': lookup_types_string,
        }
