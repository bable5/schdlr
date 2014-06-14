FROM stackbrew/ubuntu:14.04

WORKDIR /code

RUN apt-get -qq update && apt-get install -y python python-pip  python-dev

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code

EXPOSE 8000
