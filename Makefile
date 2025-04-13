include .env

DOCKER_COMPOSE=docker compose -f docker-compose.yml
DOCKER_COMPOSE_RUN=${DOCKER_COMPOSE} run --rm syncer

build:
	- docker build -t gamehinter .

up: build
	docker run --env-file=.env -p 8000:8000 -it gamehinter
format:
	- isort --profile black .
	- black .

flake: 
	flake8 app main.py

SOURCE_CODE_PATHS = main.py app

mypy:
	mypy --ignore-missing-imports $(SOURCE_CODE_PATHS)