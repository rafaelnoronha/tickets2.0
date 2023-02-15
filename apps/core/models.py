from django.db import models


SIM_NAO_CHOICE = (
    ('S', 'Sim'),
    ('N', 'Não'),
)

UF_CHOICES = [
    ('RO', 'Rondônia'),
    ('AC', 'Acre'),
    ('AM', 'Amazonas'),
    ('RR', 'Roraima'),
    ('PA', 'Pará'),
    ('AP', 'Amapá'),
    ('TO', 'Tocantins'),
    ('MA', 'Maranhão'),
    ('PI', 'Piauí'),
    ('CE', 'Ceará'),
    ('RN', 'Rio Grande do Norte'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('AL', 'Alagoas'),
    ('SE', 'Sergipe'),
    ('BA', 'Bahia'),
    ('MG', 'Minas Gerais'),
    ('ES', 'Espírito Santo'),
    ('RJ', 'Rio de Janeiro'),
    ('SP', 'São Paulo'),
    ('PR', 'Paraná'),
    ('SC', 'Santa Catarina'),
    ('RS', 'Rio Grande do Sul'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('GO', 'Goiás'),
    ('DF', 'Distrito Federal'),
    ('EX', 'Exterior'),
]


class Base(models.Model):
    """
    Modelo que armazena os dados comuns a todos os registros.
    """

    ativo = models.CharField(
        verbose_name='Ativo',
        max_length=1,
        choices=SIM_NAO_CHOICE,
        default='S',
        help_text='Se o registro está ativo ou não'
    )

    empresa = models.ForeignKey(
        'empresa.Empresa',
        verbose_name='Empresa',
        on_delete=models.PROTECT,
        null=True,
        help_text='Para qual empresa o parâmetro será usado',
    )

    data_criacao = models.DateField(
        verbose_name='Data de Criação',
        auto_now_add=True,
        help_text='Data da criação do registro'
    )

    hora_criacao = models.TimeField(
        verbose_name='Hora de Criação',
        auto_now_add=True,
        help_text='Hora da criação do registro'
    )

    data_alteracao = models.DateField(
        verbose_name='Data da Alteração',
        auto_now=True,
        help_text='Data da alteração do registro'
    )

    hora_alteracao = models.TimeField(
        verbose_name='Hora da Alteração',
        auto_now=True,
        help_text='Hora da alteração do registro'
    )

    owner_id = models.ForeignKey(
        'usuario.Usuario',
        verbose_name='Owner Id',
        on_delete=models.PROTECT,
        null=True,
        help_text='Para qual empresa o parâmetro será usado',
    )

    
    class Meta:
        abstract = True
