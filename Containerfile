FROM ubuntu:22.04

RUN mkdir /tenshi
COPY ./requirements.txt /tenshi
WORKDIR /tenshi
RUN apt update
RUN apt install python3 python3-pip -y
RUN pip install -r ./requirements.txt
COPY . /tenshi/
RUN python3 ./manage.py makemigrations
RUN python3 ./manage.py migrate
RUN python3 ./manage.py runserver 8000