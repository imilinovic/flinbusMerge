import settings


bind = f"0.0.0.0:{settings.GUNICORN_PORT}"
workers = 2
