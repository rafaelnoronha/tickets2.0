from rest_framework import serializers

from .models import PerfilUsuario, PerfilUsuarioEmpresa, ClassificacaoPerfil
from apps.core.serializers import BaseSerializer
from apps.empresa.serializers import EmpresaListSerializer
from apps.empresa.models import Empresa
from apps.usuario.serializers import UsuarioEssentialSerializer
from apps.usuario.models import Usuario


class PerfilUsuarioListSerializer(BaseSerializer):
    class Meta:
        model = PerfilUsuario
        fields = [
            'ps_usuario',
            'ps_nome',
            'ps_telefone',
            'ps_celular',
            'ps_classificacao',
            'ps_media_avaliacoes',
            'ps_observacoes',
        ]
        fields += BaseSerializer.Meta.fields
        read_only_fields = fields


class PerfilUsuarioGetSerializer(PerfilUsuarioListSerializer):
    empresa = EmpresaListSerializer()
    owner_id = UsuarioEssentialSerializer()


class PerfilUsuarioPostSerializer(PerfilUsuarioListSerializer):
    ps_usuario = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True, allow_null=False)
    ps_classificacao = serializers.SlugRelatedField(queryset=ClassificacaoPerfil.objects.all(), slug_field='id', required=True, allow_null=False)
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id', required=False, allow_null=True)
    owner_id = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True, allow_null=False)

    class Meta(PerfilUsuarioListSerializer.Meta):
        read_only_fields = [field for field in PerfilUsuarioListSerializer.Meta.read_only_fields if field not in [
            'ps_usuario',
            'ps_nome',
            'ps_telefone',
            'ps_celular',
            'ps_classificacao',
            'ps_observacoes',
            'empresa',
            'owner_id'
        ]]


class PerfilUsuarioPutPatchSerializer(PerfilUsuarioListSerializer):
    class Meta(PerfilUsuarioListSerializer.Meta):
        read_only_fields = [field for field in PerfilUsuarioListSerializer.Meta.read_only_fields if field not in [
            'ps_nome',
            'ps_telefone',
            'ps_celular',
            'ps_observacoes',
            'empresa',
        ]]


class PerfilUsuarioClassificarSerializer(PerfilUsuarioListSerializer):
    ps_classificacao = serializers.SlugRelatedField(queryset=ClassificacaoPerfil.objects.all(), slug_field='id', required=True, allow_null=False)

    class Meta(PerfilUsuarioListSerializer.Meta):
        read_only_fields = [field for field in PerfilUsuarioListSerializer.Meta.read_only_fields if field not in ['ps_classificacao',]]


class PerfilUsuarioAtivarInativarSerializer(PerfilUsuarioListSerializer):
    class Meta(PerfilUsuarioListSerializer.Meta):
        read_only_fields = [field for field in PerfilUsuarioListSerializer.Meta.read_only_fields if field not in ['ativo',]]


class PerfilUsuarioEmpresaListSerializer(BaseSerializer):
    class Meta:
        model = PerfilUsuarioEmpresa
        fields = [
            'pm_perfil',
        ]
        fields += BaseSerializer.Meta.fields
        read_only_fields = fields


class PerfilUsuarioEmpresaGetSerializer(PerfilUsuarioEmpresaListSerializer):
    empresa = EmpresaListSerializer()
    owner_id = UsuarioEssentialSerializer()


class PerfilUsuarioEmpresaPostSerializer(PerfilUsuarioEmpresaListSerializer):
    pm_perfil = serializers.SlugRelatedField(queryset=PerfilUsuarioEmpresa.objects.all(), slug_field='id', required=True, allow_null=False)
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id', required=True, allow_null=False)
    owner_id = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True, allow_null=False)

    class Meta(PerfilUsuarioEmpresaListSerializer.Meta):
        read_only_fields = [field for field in PerfilUsuarioEmpresaListSerializer.Meta.read_only_fields if field not in [
            'pm_perfil',
            'empresa',
            'owner_id'
        ]]


class PerfilUsuarioEmpresaAtivarInativarSerializer(PerfilUsuarioEmpresaListSerializer):
    class Meta(PerfilUsuarioEmpresaListSerializer.Meta):
        read_only_fields = [field for field in PerfilUsuarioEmpresaListSerializer.Meta.read_only_fields if field not in ['ativo',]]


class ClassificacaoPerfilListSerializer(BaseSerializer):
    class Meta:
        model = ClassificacaoPerfil
        fields = [
            'cp_codigo',
            'cp_nome',
            'cp_descricao',
        ]
        fields += BaseSerializer.Meta.fields
        read_only_fields = fields


class ClassificacaoPerfilGetSerializer(ClassificacaoPerfilListSerializer):
    empresa = EmpresaListSerializer()
    owner_id = UsuarioEssentialSerializer()


class ClassificacaoPerfilPostSerializer(ClassificacaoPerfilListSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id', required=False, allow_null=True)
    owner_id = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True, allow_null=False)

    class Meta(ClassificacaoPerfilListSerializer.Meta):
        read_only_fields = [field for field in ClassificacaoPerfilListSerializer.Meta.read_only_fields if field not in [
            'cp_codigo',
            'cp_nome',
            'cp_descricao',
            'empresa',
            'owner_id'
        ]]


class ClassificacaoPerfilPutPatchSerializer(ClassificacaoPerfilListSerializer):
    class Meta(ClassificacaoPerfilListSerializer.Meta):
        read_only_fields = [field for field in ClassificacaoPerfilListSerializer.Meta.read_only_fields if field not in [
            'cp_nome',
            'cp_descricao',
            'empresa',
        ]]


class ClassificacaoPerfilAtivarInativarSerializer(ClassificacaoPerfilListSerializer):
    class Meta(ClassificacaoPerfilListSerializer.Meta):
        read_only_fields = [field for field in ClassificacaoPerfilListSerializer.Meta.read_only_fields if field not in ['ativo',]]
