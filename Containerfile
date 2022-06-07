FROM python:3.7-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /app
RUN mkdir -p /app/static
RUN mkdir -p /app/pip_cache
RUN mkdir -p /app/tenshi

COPY ./requirements.txt /app/tenshi
WORKDIR /app/tenshi
RUN pip install -r requirements.txt --cache-dir /app/pip_cache

COPY . .
RUN python3 manage.py makemigrations

COPY buildfiles/nginx.default /etc/nginx/sites-available/default

RUN chown -R www-data:www-data /app
EXPOSE 8080
STOPSIGNAL SIGTERM
RUN chmod 777 /app/tenshi/buildfiles/start_server.sh
RUN chmod 777 /app/tenshi/buildfiles/wait-for-it.sh
CMD ["/app/tenshi/buildfiles/start_server.sh"]
