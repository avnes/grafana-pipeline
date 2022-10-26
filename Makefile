.PHONY: convert install dev mypy pylint flake8 bandit lint check

PACKAGE_DIR:=grafana_settings

convert:
	poetry run python main.py

install:
	poetry install --no-dev

dev:
	poetry install && poetry run pre-commit install

flake8:
	poetry run flake8 $(PACKAGE_DIR) main.py

mypy:
	poetry run mypy $(PACKAGE_DIR) main.py

pylint:
	poetry run pylint $(PACKAGE_DIR) main.py

bandit:
	poetry run bandit -r $(PACKAGE_DIR) main.py

lint:
	$(MAKE) flake8
	$(MAKE) pylint
	$(MAKE) mypy
	$(MAKE) bandit

check:
	poetry run pre-commit run --all-files
