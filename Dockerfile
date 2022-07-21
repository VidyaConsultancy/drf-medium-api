FROM python:bullseye

MAINTAINER Arpit Jain <arpit_jain@live.com>

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

EXPOSE 8000