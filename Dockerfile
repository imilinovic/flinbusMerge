FROM python:3.10.5-bullseye

WORKDIR /app

COPY api /app/api
COPY models /app/models
COPY utils /app/utils
COPY app.py /app
COPY settings.py /app
COPY start.sh /app
COPY requirements.txt /app
COPY gunicorn_config.py /app

RUN pip install -U -r requirements.txt

ENTRYPOINT ./start.sh
