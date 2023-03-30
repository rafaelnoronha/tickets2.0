from .models import Agrupamento, Ticket, MensagemTicket
from .serializers import (
    AgrupamentoGetSerializer, AgrupamentoListSerializer, AgrupamentoPostSerializer,
    AgrupamentoPutPatchSerializer, AgrupamentoAtivarInativarSerializer, TicketGetSerializer,
    TicketListSerializer, TicketPostSerializer, MensagemTicketGetSerializer,
    MensagemTicketListSerializer, MensagemTicketPostSerializer
)
from .permissions import AgrupamentoAtivarInativarPermission
from .filters import AgrupamentoFilterSet, TicketFilterSet, MensagemTicketFilterSet
from apps.core.views import BaseModelViewSet
from apps.core.decorators import action_ativar_inativar
from apps.core.permissions import BasePemission


@action_ativar_inativar
class AgrupamentoViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = Agrupamento.objects.all()
    filterset_class = AgrupamentoFilterSet
    serializer_class = AgrupamentoListSerializer
    serializer_classes = {
        'retrieve': AgrupamentoGetSerializer,
        'create': AgrupamentoPostSerializer,
        'update': AgrupamentoPutPatchSerializer,
        'partial_update': AgrupamentoPutPatchSerializer,
    }
    action_ativar_inativar = {
        'permission': AgrupamentoAtivarInativarPermission,
        'serializer': AgrupamentoAtivarInativarSerializer,
    }


class TicketViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = Ticket.objects.all()
    filterset_class = TicketFilterSet
    serializer_class = TicketListSerializer
    serializer_classes = {
        'retrieve': TicketGetSerializer,
        'create': TicketPostSerializer,
    }


class MensagemTicketViewSet(BaseModelViewSet):
    permission_classes = (BasePemission, )
    queryset = MensagemTicket.objects.all()
    filterset_class = MensagemTicketFilterSet
    serializer_class = MensagemTicketListSerializer
    serializer_classes = {
        'retrieve': MensagemTicketGetSerializer,
        'create': MensagemTicketPostSerializer,
    }
