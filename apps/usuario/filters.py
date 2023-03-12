from django_filters import rest_framework as filter

from .models import Usuario
from apps.core.filters import lookup_types_string


class UsuarioFilterSet(filter.FilterSet):
    class Meta:
        model = Usuario
        fields = {
            'username': lookup_types_string,
            'email': lookup_types_string,
            'is_active': ['exact',],
            'is_superuser': ['exact',],
            'is_staff': ['exact',],
            'is_manager': ['exact',]
        }
