from rest_framework import serializers
from rest_framework.decorators import action

from .models import Empresa
from apps.core.serializers import BaseSerializer
from apps.usuario.serializers import UsuarioEssentialSerializer
from apps.usuario.models import Usuario


class EmpresaListSerializer(BaseSerializer):
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
        fields += BaseSerializer.Meta.fields
        read_only_fields = fields


class EmpresaGetSerializer(EmpresaListSerializer):
    empresa = EmpresaListSerializer()
    owner_id = UsuarioEssentialSerializer()


class EmpresaPostSerializer(EmpresaListSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id', required=False, allow_null=True)
    owner_id = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True, allow_null=False)

    class Meta(EmpresaListSerializer.Meta):
        read_only_fields = [field for field in EmpresaListSerializer.Meta.read_only_fields if field not in [
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
            'owner_id'
        ]]


class EmpresaPutPatchSerializer(EmpresaListSerializer):
    class Meta(EmpresaListSerializer.Meta):
        read_only_fields = [field for field in EmpresaListSerializer.Meta.read_only_fields if field not in [
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


class EmpresaAtivarInativarSerializer(EmpresaListSerializer):
    class Meta(EmpresaListSerializer.Meta):
        read_only_fields = [field for field in EmpresaListSerializer.Meta.read_only_fields if field not in ['ativo',]]
