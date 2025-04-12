FROM python:3.12-slim AS base

WORKDIR /app

ARG POETRY_HOME=/etc/poetry
RUN apt-get update && \
    apt-get -y install --no-install-recommends tini curl && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python - --version 1.8.0 && \
    apt-get remove -y curl && \
    apt-get remove -y --purge build-essential && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*
ENV PATH="${PATH}:${POETRY_HOME}/bin"

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --without dev --no-cache && \
    rm -rf ~/.cache

COPY main.py ./
COPY ./app ./app

CMD ["/bin/bash", "-c", "python main.py"]   