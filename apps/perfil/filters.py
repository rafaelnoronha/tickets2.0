import django_filters

from .models import ClassificacaoPerfil, PerfilUsuario
from apps.core.filters import lookup_types_string, lookup_types_base, lookup_types_number


class ClassificacaoPerfilFilterSet(django_filters.FilterSet):
    class Meta:
        model = ClassificacaoPerfil
        fields = {
            'cp_codigo': lookup_types_string,
            'cp_nome': lookup_types_string,
            'cp_descricao': lookup_types_string,
        }
        fields.update(lookup_types_base)


class PerfilUsuarioFilterSet(django_filters.FilterSet):
    class Meta:
        model = PerfilUsuario
        fields = {
            'ps_usuario': ['exact'],
            'ps_nome': lookup_types_string,
            'ps_telefone': lookup_types_string,
            'ps_celular': lookup_types_string,
            'ps_classificacao': ['exact'],
            'ps_media_avaliacoes': lookup_types_number,
            'ps_observacoes': lookup_types_string,
        }
        fields.update(lookup_types_base)
