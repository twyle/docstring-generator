install-dev-reqs:
	@pip install -r requirements-dev.txt

install-prod-reqs:
	@pip install -r requirements.txt

build: clean
	@python setup.py sdist bdist_wheel

clean:
	@rm -rf build dist auth.* *.egg-info

check-build:
	@twine check dist/*

test-upload:
	@twine upload --repository testpypi dist/*

upload:
	@twine upload dist/*

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

init-cz:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog

lint:
	@black docstring_generator/
	@isort docstring_generator/
	@flake8 docstring_generator/

# install:

# build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert|bump
