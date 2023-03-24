from rest_framework import serializers

from .models import Parametro
from apps.usuario.models import Usuario
from apps.empresa.models import Empresa
from apps.core.serializers import BaseEmpresaSerializer
from apps.core.decorators import fields_base_serializer


@fields_base_serializer
class ParametroGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()

    class Meta:
        model = Parametro
        fields = [
            'id',
            'pr_codigo',
            'pr_descricao',
            'pr_valor',
        ]
        read_only_fields = fields


class ParametroListSerializer(ParametroGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')


class ParametroPostSerializer(ParametroGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)

    class Meta(ParametroListSerializer.Meta):
        read_only_fields = [field for field in ParametroListSerializer.Meta.read_only_fields if field not in [
            'pr_codigo',
            'pr_descricao',
            'pr_valor',
            'empresa',
        ]]


class ParametroPutPatchSerializer(ParametroGetSerializer):
    class Meta(ParametroListSerializer.Meta):
        read_only_fields = [field for field in ParametroListSerializer.Meta.read_only_fields if field not in [
            'pr_valor'
        ]]
