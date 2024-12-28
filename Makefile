
project = xion

type:
	poetry run python -m mypy --ignore-missing-imports **/*.py

lint: type
	poetry run python -m flake8 --ignore E501,F841 $(project)/

test: type
	poetry run pytest --cov-branch --cov=xion --cov-fail-under=90 --disable-warnings -s

run: lint
	# run the first example
	poetry run python $(shell pwd)/$(project)/__main__.py -f ./examples/1.b -p


