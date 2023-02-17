from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os
import shutil


class Command(BaseCommand):
    help = "Realiza o 'makemigrations' de todos os apps criados"

    def handle(self, *args, **options):
        for app in settings.MY_APPS:
            print(f" app.split('.')[1] ".center(100, '='))
            call_command('makemigrations', app.split('.')[1])
            
        # calcl_command('migrate')
