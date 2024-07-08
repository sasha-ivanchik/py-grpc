FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir grpc_heavy_duty
WORKDIR /grpc_heavy_duty

COPY ./requirements.txt /grpc_heavy_duty/
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt
COPY ./grpc_heavy_duty/ /grpc_heavy_duty

CMD ["python","starter.py"]
