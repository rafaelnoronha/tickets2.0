from django.db import models

from apps.core.models import Base, SIM_NAO_CHOICE
from apps.usuario.models import Usuario, ClassificacaoUsuario


STATUS_CHOISES = [
    ('0', 'Aberto'),
    ('1', 'Processando'),
    ('2', 'Solucionado'),
    ('3', 'Finalizado'),
    ('4', 'Cancelado'),
]

AVALIACAO_CHOISES = [
    (0, 'Não Avaliado'),
    (1, 'Péssimo'),
    (2, 'Ruim'),
    (3, 'Bom'),
    (4, 'Muito Bom'),
    (5, 'Ótimo')
]

TIPO_CHOISES = [
    ('G', 'Grupo'),
    ('S', 'Subgrupo'),
]


class Agrupamento(Base):
    """
    Modelo de grupo e subgrupo dos tickets.
    """

    gr_codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código do Agrupamento',
    )

    gr_nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        help_text='Nome do Agrupamento',
    )

    gr_prioridade = models.PositiveSmallIntegerField(
        verbose_name='Prioridade',
        default=0,
        help_text='Prioridade do Agrupamento',
    )

    gr_tipo = models.CharField(
        verbose_name='Tipo',
        choices=TIPO_CHOISES,
        max_length=1,
        help_text='Tipo do Agrupamrento',
    )

    class Meta:
        db_table = 'tc_agrupamento'
        ordering = ['-id']
        verbose_name = 'Agrupamento'
        verbose_name_plural = 'Agrupamentos'
        indexes = [
            models.Index(fields=['gr_tipo'], name='idx_gr_tipo'),
            models.Index(fields=['gr_prioridade'], name='idx_gr_prioridade'),
        ]
        permissions = (
            ('ativar_inativar', 'Permite ativar ou inativar um grupo/subgrupo'),
        )


class Ticket(Base):
    """
    Modelo dos tickets, em específico do cabeçalho dos tickets, sem as mensagens/acompanhamentos.
    """

    tc_status = models.CharField(
        verbose_name='Status',
        max_length=1,
        choices=STATUS_CHOISES,
        default='0',
        help_text='Status do ticket',
    )

    tc_prioridade = models.PositiveSmallIntegerField(
        verbose_name='Prioridade',
        default=0,
        help_text='Prioridade de atendimento do ticket',
    )

    tc_solicitante = models.ForeignKey(
        Usuario,
        verbose_name='Solicitante',
        related_name='rl_tc_solicitante',
        on_delete=models.PROTECT,
        help_text='Solicitante/Cliente responsável pelo ticket'
    )

    tc_classificacao_atendente = models.ForeignKey(
        ClassificacaoUsuario,
        verbose_name='Classificação do Atendente',
        related_name='rl_tc_classificacao_atendente',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )

    tc_atendente = models.ForeignKey(
        Usuario,
        verbose_name='Atendente',
        related_name='rl_tc_atendente',
        null=True,
        on_delete=models.PROTECT,
        help_text='Atendente/Técnico responsável pelo ticket'
    )

    tc_titulo = models.CharField(
        verbose_name='Título',
        max_length=100,
        help_text='Título do ticket',
    )

    tc_descricao = models.CharField(
        verbose_name='Descrição',
        max_length=4000,
        help_text='Descrição do ticket',
    )

    tc_grupo = models.ForeignKey(
        Agrupamento,
        verbose_name='Grupo',
        related_name='rl_tc_grupo',
        null=True,
        on_delete=models.PROTECT,
        help_text='Grupo de classificação do ticket',
    )

    tc_subgrupo = models.ForeignKey(
        Agrupamento,
        verbose_name='Subgrupo',
        related_name='rl_tc_subgrupo',
        null=True,
        on_delete=models.PROTECT,
        help_text='Subgrupo de classificação do ticket',
    )

    tc_avaliacao_solicitante = models.SmallIntegerField(
        verbose_name='Avaliação do Solicitante',
        choices=AVALIACAO_CHOISES,
        default=0,
        help_text='Avaliação do solicitante referente ao chamado',
    )

    tc_observacao_avaliacao_solicitante = models.CharField(
        verbose_name='Observação Avaliação do Solicitante',
        max_length=1000,
        blank=True,
        help_text='Observações referente à avaliação do solicitante',
    )

    class Meta:
        db_table = 'tc_ticket'
        ordering = ['-id']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        indexes = [
            models.Index(fields=['tc_status'], name='idx_tc_status'),
            models.Index(fields=['tc_prioridade'], name='idx_tc_prioridade'),
            models.Index(fields=['tc_avaliacao_solicitante'], name='idx_tc_avaliacao_solicitante'),
        ]


class MensagemTicket(Base):
    """
    Modelo das mensagens/acompanhemento dos tickets.
    """

    mt_usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        related_name='rl_mt_usuario',
        on_delete=models.PROTECT,
        help_text='Usuário autor(remetente) da mensagem',
    )

    mt_ticket = models.ForeignKey(
        Ticket,
        verbose_name='Ticket',
        related_name='rl_mt_ticket',
        on_delete=models.CASCADE,
        help_text='Ticket que receberá a mensagem',
    )

    mt_mensagem = models.CharField(
        verbose_name='Mensagem',
        max_length=4000,
        help_text='Conteúdo da mensagem',
    )

    mt_mensagem_relacionada = models.ForeignKey(
        'self',
        related_name='rl_mt_mensagem_relacionada',
        on_delete=models.PROTECT,
        null=True,
        help_text='Mensagem a qual a mensagem atual estará vinculada como resposta',
    )

    mt_solucao = models.CharField(
        verbose_name='Solução',
        max_length=1,
        choices=SIM_NAO_CHOICE,
        help_text='Informa se a mensagem é uma solução para o ticket aberto',
    )

    class Meta:
        db_table = 'tc_mensagem_ticket'
        ordering = ['-id']
        verbose_name = 'Mensagem do Ticket'
        verbose_name_plural = 'Mensagens do Ticket'
        indexes = [
            models.Index(fields=['mt_solucao'], name='idx_mt_solucao'),
        ]
