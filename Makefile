migrate:
	poetry run python manage.py migrate

up: migrate
	poetry run python manage.py runserver

init:
	poetry install
	poetry run python manage.py migrate
	poetry run python manage.py createsuperuser
