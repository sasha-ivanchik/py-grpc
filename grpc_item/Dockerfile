FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir grpc_item
WORKDIR /grpc_item

COPY ./requirements.txt /grpc_item/
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt
COPY ./grpc_item/ /grpc_item

CMD ["python","starter.py"]
