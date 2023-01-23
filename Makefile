install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black app/*.py

lint:
	pylint --disable=R,C app/*.py

test:
	python -m pytest -vv --cov=app --cov=main app/test_*.py

all: install lint test