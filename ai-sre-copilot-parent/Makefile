.PHONY: setup up down restart status logs test test-python clean help
setup:
	bash scripts/setup.sh
up:
	docker compose -f infra/compose.yaml up --build -d

down:
	docker compose -f infra/compose.yaml down
restart:
	docker compose -f infra/compose.yaml down
	docker compose -f infra/compose.yaml up --build -d
status:
	docker compose -f infra/compose.yaml ps
logs:
	docker compose -f infra/compose.yaml logs -f --tail=100
test:
	docker compose -f infra/compose.yaml up --build -d
	python3 -m venv .venv || true
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/pytest -q tests
clean:
	docker compose -f infra/compose.yaml down -v --remove-orphans
	rm -rf .venv
help:
	@echo 'make setup | up | down | status | logs | test | clean'
