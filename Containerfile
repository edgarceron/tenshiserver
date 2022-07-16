FROM python:3.10.5-buster

RUN apt-get update && apt-get install vim gcc python3-dev libpq-dev postgresql postgresql-contrib -y --no-install-recommends
RUN pip install gunicorn

RUN mkdir -p /app
RUN mkdir -p /app/media
RUN mkdir -p /app/static
RUN mkdir -p /app/tenshi

COPY ./requirements.txt /app/tenshi
WORKDIR /app/tenshi

RUN \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apt-get autoremove gcc libpq-dev python3-dev postgresql postgresql-contrib -y

COPY . .
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN chown -R www-data:www-data /app

STOPSIGNAL SIGTERM
RUN chmod 777 /app/tenshi/buildfiles/start_server.sh
CMD ["/bin/bash", "/app/tenshi/buildfiles/start_server.sh"]
