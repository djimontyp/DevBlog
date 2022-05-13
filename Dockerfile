FROM python:3.9-slim

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ../DevBlog/backend ./