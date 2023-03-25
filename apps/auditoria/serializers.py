from rest_framework import serializers

from .models import LogAutenticacao
from apps.core.serializers import BaseEmpresaSerializer
from apps.core.decorators import fields_base_serializer
from apps.empresa.models import Empresa


@fields_base_serializer
class LogAutenticacaoGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()

    class Meta:
        model = LogAutenticacao
        fields = [
            'id',
            'lt_ip',
            'lt_user_agent',
            'lt_usuario',
            'lt_autenticado',
        ]
        read_only_fields = fields


class LogAutenticacaoListSerializer(LogAutenticacaoGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')
