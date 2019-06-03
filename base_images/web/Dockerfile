FROM python:3-alpine3.7

ADD requirements.txt /home/app/
WORKDIR /home/app/

RUN apk add --update curl gcc g++ &&\
	apk add --no-cache postgresql-dev gcc python3 python3-dev musl-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    python3 -m pip install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install --upgrade -r requirements.txt