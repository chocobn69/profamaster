init:
	pipenv install --dev

run:
	pipenv run python start.py

test:
	pipenv run pytest

lint:
	pipenv run flake8
