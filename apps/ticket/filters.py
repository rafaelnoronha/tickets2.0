import django_filters

from .models import Agrupamento, Ticket, MensagemTicket
from apps.core.filters import lookup_types_string, lookup_types_number
from apps.core.decorators import fields_base_filter_set
from apps.usuario.filters import UsuarioFilterSet, ClassificacaoUsuarioFilterSet


@fields_base_filter_set
class AgrupamentoFilterSet(django_filters.FilterSet):
    class Meta:
        model = Agrupamento
        fields = {
            'gr_codigo': lookup_types_string,
            'gr_nome': lookup_types_string,
            'gr_prioridade': lookup_types_number,
        }


@fields_base_filter_set
class TicketFilterSet(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = {
            'tc_status': lookup_types_string,
            'tc_prioridade': lookup_types_number,
            'tc_solicitante': ['exact'],
            'tc_classificacao_atendente': ['exact'],
            'tc_atendente': ['exact'],
            'tc_titulo': lookup_types_string,
            'tc_descricao': lookup_types_string,
            'tc_grupo': ['exact'],
            'tc_subgrupo': ['exact'],
            'tc_avaliacao_solicitante': lookup_types_number,
            'tc_observacao_avaliacao_solicitante': lookup_types_string,
        }
        fields.update([(f'tc_solicitante__{chave}', valor) for chave, valor in UsuarioFilterSet.Meta.fields.items()])
        fields.update([(f'tc_classificacao_atendente__{chave}', valor) for chave, valor in ClassificacaoUsuarioFilterSet.Meta.fields.items()])
        fields.update([(f'tc_atendente__{chave}', valor) for chave, valor in UsuarioFilterSet.Meta.fields.items()])
        fields.update([(f'tc_grupo__{chave}', valor) for chave, valor in AgrupamentoFilterSet.Meta.fields.items()])
        fields.update([(f'tc_subgrupo__{chave}', valor) for chave, valor in AgrupamentoFilterSet.Meta.fields.items()])


@fields_base_filter_set
class MensagemTicketFilterSet(django_filters.FilterSet):
    class Meta:
        model = MensagemTicket
        fields = {
            'mt_usuario': ['exact'],
            'mt_ticket': ['exact'],
            'mt_mensagem': lookup_types_string,
            'mt_mensagem_relacionada': ['exact'],
            'mt_solucao': lookup_types_string,
        }
        fields.update([(f'mt_usuario__{chave}', valor) for chave, valor in UsuarioFilterSet.Meta.fields.items()])
        fields.update([(f'mt_ticket__{chave}', valor) for chave, valor in TicketFilterSet.Meta.fields.items()])
