from django.db import models


SIM_NAO_CHOICE = (
    ('S', 'Sim'),
    ('N', 'Não'),
)


class Base(models.Model):
    ativo = models.CharField(
        verbose_name='Ativo',
        max_length=1,
        choices=SIM_NAO_CHOICE,
        default='S',
        help_text='Se o registro está ativo ou não'
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

    
    class Meta:
        abstract = True
