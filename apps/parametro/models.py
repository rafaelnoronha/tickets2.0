from django.db import models

from apps.core.models import Base


class Parametro(Base):
    """
    Modelo que armazena os dados auxiliares para o funcionamento do sistema, os parâmetros de configuração.
    """

    pr_codigo = models.CharField(
        verbose_name='Código',
        max_length=50,
        help_text='Código do parâmetro'
    )

    pr_descricao = models.CharField(
        verbose_name='Descrição',
        max_length=150,
        help_text='Descrição do parâmetro',
    )

    pr_valor = models.CharField(
        verbose_name='Valor',
        max_length=4000,
        help_text='Descrição do parâmetro',
    )
    

    class Meta:
        db_table = 'tc_parametro'
        verbose_name = 'Parâmetro'
        verbose_name_plural = 'Parâmetros'
        ordering = ['-id',]
        indexes = [
            models.Index(fields=['pr_codigo',], name='idx_pr_codigo'),
            models.Index(fields=['empresa',], name='idx_pr_empresa'),
            # models.Index(fields=['owner_id',], name='idx_bs_owner_id'),
        ]
        unique_together = [
            ['pr_codigo', 'empresa'],
        ]
