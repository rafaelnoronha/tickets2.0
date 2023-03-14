from rest_framework import serializers

from .models import Base
from apps.empresa.models import Empresa


class BaseEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id',
            'mp_cpf_cnpj',
            'mp_razao_social',
            'mp_nome_fantasia',
        ]
        read_only_fields = fields


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = [
            'ativo',
            'empresa',
            'data_criacao',
            'hora_criacao',
            'data_alteracao',
            'hora_alteracao',
        ]
