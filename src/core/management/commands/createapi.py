import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    That class provide a base command to create a files structure for API.
    |── APP_NAME
    |   ├── api
    |   ├── __init__.py
    │   └── v1
    │       ├── __init__.py
    │       ├── serializers.py
    │       ├── urls.py
    │       └── views.py
    """

    help = "Cria uma estrutura de pasta para API."

    def _initial_message(self, app_name):
        initial_message = (
            f"Criando uma estrutura de arquivos de API para o app {app_name}."
        )
        self.stdout.write(initial_message)

    def _create_api_dir(self, api_dir):
        os.mkdir(api_dir)
        init_file = open(f"{api_dir}/__init__.py", "w+")
        init_file.close()

    def _create_version_dir(self, version_dir):
        os.mkdir(version_dir)

        files = ["__init__.py", "serializers.py", "urls.py", "views.py"]

        for file in files:
            operation_message = f"Criando o arquivo {file}..."
            self.stdout.write(operation_message)
            create_file = open(f"{version_dir}/{file}", "w+")
            create_file.close()

    def _final_message(self):
        final_message = "Operação Concluída."
        self.stdout.write(final_message)

    def add_arguments(self, parser):
        parser.add_argument(
            "createapi",
            nargs="+",
            type=str,
        )

    def handle(self, **options):
        APP_NAME = options["createapi"][0]

        DIR = os.getcwd()
        API_DIR = f"{DIR}/{APP_NAME}/api"
        VERSION_DIR = f"{API_DIR}/v1"

        self._initial_message(APP_NAME)
        self._create_api_dir(API_DIR)
        self._create_version_dir(VERSION_DIR)
        self._final_message()
