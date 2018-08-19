init:
	pipenv install --dev
	pipenv run python setup.py install

install:
	pipenv install 
	pipenv run python setup.py install

run:
	pipenv run profamaster-server --config $(CONFIG)

test:
	pipenv run pytest

lint:
	pipenv run flake8

pkg:
	rm -rf build/
	pipenv run python setup.py sdist
