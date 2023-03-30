from rest_framework import serializers

from .models import Agrupamento, Ticket, MensagemTicket
from apps.core.serializers import BaseEmpresaSerializer
from apps.core.decorators import fields_base_serializer
from apps.empresa.models import Empresa
from apps.usuario.models import Usuario
from apps.usuario.serializers import (
    UsuarioListSerializer, ClassificacaoUsuarioListSerializer, UsuarioMinSerializer,
    ClassificacaoUsuarioMinSerializer, ClassificacaoUsuario
)


class AgrupamentoMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agrupamento
        fields = [
            'id',
            'gr_codigo',
            'gr_nome',
        ]
        read_only_fields = fields.copy()


@fields_base_serializer
class AgrupamentoGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()

    class Meta:
        model = Agrupamento
        fields = [
            'id',
            'gr_codigo',
            'gr_nome',
            'gr_prioridade',
            'gr_tipo',
        ]
        read_only_fields = fields


class AgrupamentoListSerializer(AgrupamentoGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')


class AgrupamentoPostSerializer(AgrupamentoGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)

    class Meta(AgrupamentoGetSerializer.Meta):
        read_only_fields = [field for field in AgrupamentoGetSerializer.Meta.read_only_fields if field not in [
            'gr_codigo',
            'gr_nome',
            'gr_prioridade',
            'gr_tipo',
            'empresa',
        ]]


class AgrupamentoPutPatchSerializer(AgrupamentoGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)

    class Meta(AgrupamentoGetSerializer.Meta):
        read_only_fields = [field for field in AgrupamentoGetSerializer.Meta.read_only_fields if field not in [
            'gr_nome',
            'gr_prioridade',
            'empresa',
        ]]


class AgrupamentoAtivarInativarSerializer(AgrupamentoGetSerializer):
    class Meta(AgrupamentoGetSerializer.Meta):
        read_only_fields = [field for field in AgrupamentoGetSerializer.Meta.read_only_fields if field not in ['ativo',]]


@fields_base_serializer
class TicketGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()
    tc_solicitante = UsuarioListSerializer()
    tc_classificacao_atendente = ClassificacaoUsuarioListSerializer()
    tc_atendente = UsuarioListSerializer()
    tc_grupo = AgrupamentoListSerializer()
    tc_subgrupo = AgrupamentoListSerializer()

    class Meta:
        model = Agrupamento
        fields = [
            'id',
            'tc_status',
            'tc_prioridade',
            'tc_solicitante',
            'tc_classificacao_atendente',
            'tc_atendente',
            'tc_titulo',
            'tc_descricao',
            'tc_grupo',
            'tc_subgrupo',
            'tc_avaliacao_solicitante',
            'tc_observacao_avaliacao_solicitante',
        ]
        read_only_fields = fields


class TicketListSerializer(TicketGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')
    tc_solicitante = UsuarioMinSerializer()
    tc_classificacao_atendente = ClassificacaoUsuarioMinSerializer()
    tc_atendente = UsuarioMinSerializer()
    tc_grupo = AgrupamentoMinSerializer()
    tc_subgrupo = AgrupamentoMinSerializer()


class TicketPostSerializer(TicketGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)
    tc_solicitante = serializers.SlugRelatedField(queryset=Usuario.objects.filter(is_active=True, is_staff=False), slug_field='-id')
    tc_classificacao_atendente = serializers.SlugRelatedField(queryset=ClassificacaoUsuario.objects.filter(ativo='S'), slug_field='-id')
    tc_atendente = serializers.SlugRelatedField(queryset=Usuario.objects.filter(is_active=True, is_staff=True), slug_field='-id')
    tc_grupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(ativo='S', gr_tipo='G'), slug_field='-id')
    tc_subgrupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(ativo='S', gr_tipo='S'), slug_field='-id')

    class Meta(TicketGetSerializer.Meta):
        read_only_fields = [field for field in TicketGetSerializer.Meta.read_only_fields if field not in [
            'tc_solicitante',
            'tc_classificacao_atendente',
            'tc_atendente',
            'tc_titulo',
            'tc_descricao',
            'tc_grupo',
            'tc_subgrupo',
            'empresa',
        ]]


@fields_base_serializer
class MensagemTicketGetSerializer(serializers.ModelSerializer):
    empresa = BaseEmpresaSerializer()
    mt_usuario = UsuarioMinSerializer()
    mt_ticket = TicketListSerializer()

    class Meta:
        model = Agrupamento
        fields = [
            'id',
            'mt_usuario',
            'mt_ticket',
            'mt_mensagem',
            'mt_mensagem_relacionada',
            'mt_solucao',
        ]
        read_only_fields = fields


class MensagemTicketListSerializer(MensagemTicketGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')
    mt_usuario = UsuarioMinSerializer()
    mt_ticket = TicketListSerializer()


class MensagemTicketPostSerializer(MensagemTicketGetSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.filter(ativo='S'), slug_field='id', required=False, allow_null=True)
    mt_usuario = serializers.SlugRelatedField(queryset=Usuario.objects.filter(is_active=True), slug_field='-id')
    mt_ticket = serializers.SlugRelatedField(queryset=Ticket.objects.filter(tc_status__in=['0', '1', '2']))
    mt_mensagem_relacionada = serializers.SlugRelatedField(queryset=MensagemTicket.objects.filter(mt_ticket=mt_ticket))

    class Meta(MensagemTicketGetSerializer.Meta):
        read_only_fields = [field for field in MensagemTicketGetSerializer.Meta.read_only_fields if field not in [
            'mt_usuario',
            'mt_ticket',
            'mt_mensagem',
            'mt_mensagem_relacionada',
            'empresa',
        ]]
