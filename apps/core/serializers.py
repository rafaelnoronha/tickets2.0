from rest_framework import serializers

from .models import Base


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
            'owner'
        ]
