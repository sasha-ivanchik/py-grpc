FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir grpc_auth
WORKDIR /grpc_auth

COPY ./requirements.txt /grpc_auth/
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt
COPY ./grpc_auth/ /grpc_auth

CMD ["python","starter.py"]
