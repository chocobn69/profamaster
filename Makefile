init:
	pipenv install --dev

install:
	pipenv install 

run:
	pipenv run python start.py

test:
	pipenv run pytest

lint:
	pipenv run flake8
