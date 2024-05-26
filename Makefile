default: setup migrate data init run

migrate:
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver

setup:
	poetry install

init:
	poetry run python manage.py createsuperuser

clean:
	rm -f db.sqlite3

test:
	poetry run pytest

data:
	poetry run python manage.py loaddata blog/fixtures/initdata.json
