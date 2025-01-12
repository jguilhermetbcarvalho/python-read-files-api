# Start project in development mode
dev:
	docker compose --env-file=.env -f ./docker/docker-compose.yaml up

# Start project in development mode with rebuild
dev-build:
# docker compose --env-file=.env -f ./docker/docker-compose.yaml up --build
	docker compose -f ./docker/docker-compose.yaml up --build

# Formata o código-fonte de acordo com o padrão PEP8
format:
	cd app && poetry run autopep8 --exclude="main.py" .; poetry run isort --skip=main/routes/__init__.py .

# Checa se o código-fonte está de acordo com o padrão PEP8
check_format:
	poetry run pycodestyle ./app; poetry run isort --check-only ./app

# Checa se o código-fonte possui erros de sintaxe
check_errors:
	poetry run pylint app/ --disable=all --enable=e,f