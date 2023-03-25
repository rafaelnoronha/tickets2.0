from rest_framework import serializers

from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from apps.core.serializers import BaseEmpresaSerializer
from apps.core.decorators import fields_base_serializer
from apps.empresa.models import Empresa


@fields_base_serializer
class PoliticaPrivacidadeGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()

    class Meta:
        model = PoliticaPrivacidade
        fields = [
            'id',
            'pp_codigo',
            'pp_titulo',
            'pp_descricao',
            'pp_data_validade',
        ]
        read_only_fields = fields


class PoliticaPrivacidadeListSerializer(PoliticaPrivacidadeGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')


class PoliticaPrivacidadePostSerializer(PoliticaPrivacidadeGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)

    class Meta(PoliticaPrivacidadeGetSerializer.Meta):
        read_only_fields = [field for field in PoliticaPrivacidadeGetSerializer.Meta.read_only_fields if field not in [
            'pp_codigo',
            'pp_titulo',
            'pp_descricao',
            'pp_data_validade',
            'empresa',
        ]]


class PoliticaPrivacidadeAtivarInativarSerializer(PoliticaPrivacidadeGetSerializer):
    class Meta(PoliticaPrivacidadeGetSerializer.Meta):
        read_only_fields = [field for field in PoliticaPrivacidadeGetSerializer.Meta.read_only_fields if field not in ['ativo',]]


@fields_base_serializer
class ConsentimentoPoliticaPrivacidadeGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()

    class Meta:
        model = PoliticaPrivacidade
        fields = [
            'id',
            'cp_titular',
            'cp_politica_privacidade',
            'cp_consentimento',
        ]
        read_only_fields = fields


class ConsentimentoPoliticaPrivacidadeListSerializer(PoliticaPrivacidadeGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')


class ConsentimentoPoliticaPrivacidadePostSerializer(PoliticaPrivacidadeGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)

    class Meta(PoliticaPrivacidadeGetSerializer.Meta):
        read_only_fields = [field for field in PoliticaPrivacidadeGetSerializer.Meta.read_only_fields if field not in [
            'cp_titular',
            'cp_politica_privacidade',
            'cp_consentimento',
            'empresa',
        ]]
