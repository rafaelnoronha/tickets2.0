import django_filters

from .models import Usuario, ClassificacaoUsuario, UsuarioEmpresa
from apps.core.filters import lookup_types_string, lookup_types_base, lookup_types_number


class ClassificacaoUsuarioFilterSet(django_filters.FilterSet):
    class Meta:
        model = ClassificacaoUsuario
        fields = {
            'cs_codigo': lookup_types_string,
            'cs_nome': lookup_types_string,
            'cs_descricao': lookup_types_string,
        }
        fields.update(lookup_types_base)


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


class UsuarioEmpresaFilterSet(django_filters.FilterSet):
    class Meta:
        model = UsuarioEmpresa
        fields = {
            'sm_usuario': ['exact'],
        }
        fields.update([(f'sm_usuario__{chave}', valor) for chave, valor in UsuarioFilterSet.Meta.fields.items()])
        fields.update(lookup_types_base)
