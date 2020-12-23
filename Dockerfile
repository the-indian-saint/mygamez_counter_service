FROM ubuntu:18.04

MAINTAINER Rohan Matkar "rohan.matkar489@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8


COPY ./app/requirements.txt /requirements.txt

WORKDIR /


RUN pip3 install -r requirements.txt

COPY . /

#ENTRYPOINT [ "exec uvicorn --host 127.0.0.1 --port 7777 --reload --log-level info app.main:app" ]
CMD ["./run.sh"]