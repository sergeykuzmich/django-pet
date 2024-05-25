migrate:
	poetry run python manage.py migrate

run: migrate
	poetry run python manage.py runserver

init: clean
	poetry install
	poetry run python manage.py migrate
	poetry run python manage.py createsuperuser

clean:
	rm -f db.sqlite3

test:
	poetry run pytest
