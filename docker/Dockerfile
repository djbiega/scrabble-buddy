from python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry

RUN poetry install --no-root --no-dev
