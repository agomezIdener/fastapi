# syntax=docker/dockerfile:1
FROM python:3.11.3-slim-buster
RUN apt-get update
WORKDIR /src
COPY ./src/requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
WORKDIR /src/src
CMD ["python","main.py"]
