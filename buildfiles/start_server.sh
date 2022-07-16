#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --username $DJANGO_SUPERUSER_USERNAME --noinput --email "$DJANGO_SUPERUSER_EMAIL")
fi
(gunicorn tenshiserver.wsgi --user www-data --bind 0.0.0.0:8080 --workers 3)
# python manage.py runserver 0.0.0.0:8080