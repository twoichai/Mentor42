FROM python:3.12.7-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt