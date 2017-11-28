setup:
	python3 -m venv ~/.py35env

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

all: install lint test
