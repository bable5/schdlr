FROM stackbrew/ubuntu:14.04

WORKDIR /code

RUN apt-get -qq update && apt-get install -y python python-pip  python-dev

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code

EXPOSE 8000

RUN python manage.py syncdb --noinput
RUN python manage.py stock_data

CMD python manage.py runserver 0.0.0.0:8000
