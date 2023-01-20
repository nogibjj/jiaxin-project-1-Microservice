install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black app/*.py

lint:
	pylint --disable=R,C app/bmi.py

test:
	python -m pytest -vv --cov=app test.py

all: install lint test