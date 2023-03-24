from rest_framework import serializers

from .models import Empresa
from apps.core.serializers import BaseEmpresaSerializer
from apps.core.decorators import fields_base_serializer


@fields_base_serializer
class EmpresaGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()

    class Meta:
        model = Empresa
        fields = [
            'id',
            'mp_cpf_cnpj',
            'mp_razao_social',
            'mp_nome_fantasia',
            'mp_logradouro',
            'mp_numero',
            'mp_complemento',
            'mp_bairro',
            'mp_municipio',
            'mp_uf',
            'mp_cep',
            'mp_pais',
            'mp_telefone',
            'mp_media_avaliacoes',
            'mp_prestadora_servico',
        ]
        read_only_fields = fields


class EmpresaListSerializer(EmpresaGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')


class EmpresaPostSerializer(EmpresaGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)

    class Meta(EmpresaGetSerializer.Meta):
        read_only_fields = [field for field in EmpresaGetSerializer.Meta.read_only_fields if field not in [
            'mp_cpf_cnpj',
            'mp_razao_social',
            'mp_nome_fantasia',
            'mp_logradouro',
            'mp_numero',
            'mp_complemento',
            'mp_bairro',
            'mp_municipio',
            'mp_uf',
            'mp_cep',
            'mp_pais',
            'mp_telefone',
            'mp_prestadora_servico',
            'empresa',
        ]]


class EmpresaPutPatchSerializer(EmpresaGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)

    class Meta(EmpresaGetSerializer.Meta):
        read_only_fields = [field for field in EmpresaGetSerializer.Meta.read_only_fields if field not in [
            'mp_cpf_cnpj',
            'mp_razao_social',
            'mp_nome_fantasia',
            'mp_logradouro',
            'mp_numero',
            'mp_complemento',
            'mp_bairro',
            'mp_municipio',
            'mp_uf',
            'mp_cep',
            'mp_pais',
            'mp_telefone',
            'empresa',
        ]]


class EmpresaAtivarInativarSerializer(EmpresaGetSerializer):
    class Meta(EmpresaGetSerializer.Meta):
        read_only_fields = [field for field in EmpresaGetSerializer.Meta.read_only_fields if field not in ['ativo',]]
