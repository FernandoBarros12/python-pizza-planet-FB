install:
	pip3 install -r requirements.txt

test:
	@echo "=========================================Test with pytest========================================="
	python manage.py test

linter:
	flake8 app/

run:
	python manage.py run

init-db:
	python manage.py init
	python manage.py migrate
	python manage.py upgrade

seed-db:
	python3 manage.py seed run --root app/seeds
