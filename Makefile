install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702 app/app.py

test:
	python -m pytest -vv --cov=app test.py

all: install lint test