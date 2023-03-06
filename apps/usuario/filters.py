from django_filters import rest_framework as filter

from .models import Usuario
from apps.core.filters import lookup_types_base, lookup_types_string


def lookup_types_usuario():
    lookup = {
        'username': lookup_types_string,
        'email': lookup_types_string,
        'is_active': ['exact',],
        'is_superuser': ['exact',],
        'is_staff': ['exact',],
        'is_manager': ['exact',]
    }
    lookup.update(lookup_types_base)

    del lookup['ativo']
    del lookup['empresa']

    return lookup


class UsuarioFilterSet(filter.FilterSet):
    class Meta:
        fields_usuario = lookup_types_usuario()

        model = Usuario
        fields = fields_usuario
