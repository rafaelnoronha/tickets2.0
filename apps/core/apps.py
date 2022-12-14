from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .signals import gerar_registros_padroes


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self):
        post_migrate.connect(gerar_registros_padroes, sender=self)
