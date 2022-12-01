run:
	@python warehouse/manage.py runserver

makemigration ${app_name}:
	@python warehouse/manage.py makemigrations ${app_name}

migrate ${app_name}:
	@python warehouse/manage.py migrate ${app_name}