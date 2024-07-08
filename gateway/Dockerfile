FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir gateway
WORKDIR /gateway

COPY ./requirements.txt /gateway/
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt
COPY ./gateway/ /gateway

RUN chmod +x /gateway/starter.sh
