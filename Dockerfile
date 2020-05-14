FROM ubuntu:20.04

RUN apt-get update

WORKDIR /usr/src/epamp

COPY ./ ./

RUN poetry install

RUN poetry run pytest tests/test_login.py

RUN poetry run pytest tests/test_register.py
