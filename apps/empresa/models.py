from django.db import models

from apps.core.models import Base, SIM_NAO_CHOICE, UF_CHOICES


class Empresa(Base):
    """
    Modelo que armazena os dados das empresas dos clientes e das prestadoras de serviço.
    """

    mp_cpf_cnpj = models.CharField(
        verbose_name='CPF/CNPJ',
        max_length=14,
        unique=True,
        help_text='CPF ou CNPJ da empresa(apenas números)',
    )

    mp_razao_social = models.CharField(
        verbose_name='Razão Social',
        max_length=100,
        help_text='Razão social(nome)',
    )

    mp_nome_fantasia = models.CharField(
        verbose_name='Nome Fantasia',
        max_length=60,
        help_text='Nome fantasia(apelido)',
    )

    mp_logradouro = models.CharField(
        verbose_name='Logradouro',
        max_length=60,
        help_text='Logradouro/Endereço ex: Rua Direita',
    )

    mp_numero = models.CharField(
        verbose_name='Número',
        max_length=30,
        help_text='Número do logradouro',
    )

    mp_complemento = models.CharField(
        verbose_name='Complemento',
        max_length=30,
        blank=True,
        help_text='Complemento do endereço',
    )

    mp_bairro = models.CharField(
        verbose_name='Bairro',
        max_length=30,
        help_text='Bairro',
    )

    mp_municipio = models.CharField(
        verbose_name='Município',
        max_length=30,
        help_text='Município/Cidade',
    )

    mp_uf = models.CharField(
        verbose_name='UF',
        max_length=2,
        choices=UF_CHOICES,
        help_text='UF ex: MG',
    )

    mp_cep = models.CharField(
        verbose_name='CEP',
        max_length=8,
        help_text='CEP(apenas números)',
        # validators=[
        #     RegexValidator(regex=RegexCep.get_regex(), message=RegexCep.get_mensagem()),
        # ],
    )

    mp_pais = models.CharField(
        verbose_name='País',
        max_length=4,
        default='1058',
        help_text='Código do país de acordo com a SEFAZ',
    )

    mp_telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        help_text='Número do telefone de contato(apenas números)',
        # validators=[
        #     RegexValidator(regex=RegexTelefone.get_regex(), message=RegexTelefone.get_mensagem()),
        # ],
    )

    mp_media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
        help_text='Média das avaliações dos chamados',
    )

    mp_prestadora_servico = models.CharField(
        verbose_name='Prestadora Serviço',
        choices=SIM_NAO_CHOICE,
        help_text='Se a empresa é a prestadora dos serviços ou não',
    )

    empresa = None

    class Meta:
        db_table = 'tc_empresa'
        ordering = ['-id']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        indexes = [
            models.Index(fields=['mp_media_avaliacoes'], name='idx_mp_media_avaliacoes'),
            models.Index(fields=['mp_municipio'], name='idx_mp_municipio'),
            models.Index(fields=['mp_uf'], name='idx_mp_uf'),
            models.Index(fields=['mp_pais'], name='idx_mp_pais'),
        ]
        permissions = (
            ('ativar_inativar', 'Permite ativar ou inativar uma empresa'),
        )