FROM python:3
ENV PYTHONUNBUFFERED=1

ADD . /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt