from django.core.management.base import BaseCommand
from django.conf import settings
import os
import shutil


class Command(BaseCommand):
    help = 'Apaga a pasta migrations e __pycache__ de todos os apps criados'

    def handle(self, *args, **options):
        path_db_sqlite = os.path.join(settings.BASE_DIR.resolve(), 'db.sqlite3')

        for app in settings.MY_APPS:
            print(f" {app.split('.')[1]} ".center(100, '='))
            
            path_pycache = os.path.join(settings.BASE_DIR.resolve(), '/'.join(app.split('.')) + '/__pycache__')
            path_migrations = os.path.join(settings.BASE_DIR.resolve(), '/'.join(app.split('.')) + '/migrations')

            if os.path.exists(path_pycache):
                shutil.rmtree(path_pycache)
                print("- Excluindo diretório '__pycache__'.")

            if os.path.exists(path_migrations):
                shutil.rmtree(path_migrations)
                print("- Excluindo diretório 'migrations'.")

            if not os.path.exists(path_migrations):
                os.mkdir(path_migrations)
                print("- Criando diretório 'migrations'.")


        if os.path.exists(path_db_sqlite):
            os.remove(path_db_sqlite)
            print(f"-> Banco db.sqlite3 excluido.")
            
