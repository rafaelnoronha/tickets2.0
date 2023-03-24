import django_filters

from .models import Usuario, ClassificacaoUsuario, UsuarioEmpresa
from apps.core.filters import lookup_types_string, lookup_types_number
from apps.core.decorators import fields_base_filter_set


@fields_base_filter_set
class ClassificacaoUsuarioFilterSet(django_filters.FilterSet):
    class Meta:
        model = ClassificacaoUsuario
        fields = {
            'cs_codigo': lookup_types_string,
            'cs_nome': lookup_types_string,
            'cs_descricao': lookup_types_string,
        }


class UsuarioFilterSet(django_filters.FilterSet):
    class Meta:
        model = Usuario
        fields = {
            'username': lookup_types_string,
            'email': lookup_types_string,
            'sr_nome': lookup_types_string,
            'sr_telefone': lookup_types_string,
            'sr_celular': lookup_types_string,
            'sr_classificacao': ['exact'],
            'sr_media_avaliacoes': lookup_types_number,
            'sr_observacoes': lookup_types_string,
            'is_active': ['exact',],
            'is_superuser': ['exact',],
            'is_staff': ['exact',],
            'is_manager': ['exact',]
        }
        fields.update([(f'sr_classificacao__{chave}', valor) for chave, valor in ClassificacaoUsuarioFilterSet.Meta.fields.items()])


@fields_base_filter_set
class UsuarioEmpresaFilterSet(django_filters.FilterSet):
    class Meta:
        model = UsuarioEmpresa
        fields = {
            'sm_usuario': ['exact'],
        }
        fields.update([(f'sm_usuario__{chave}', valor) for chave, valor in UsuarioFilterSet.Meta.fields.items()])
