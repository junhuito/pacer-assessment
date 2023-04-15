# Bonus Task

FROM python:3.9

RUN mkdir -p /app
RUN mkdir -p /pacer-dev

RUN pip install virtualenv

COPY ./requirements.txt ./
COPY ./pacer-dev ./pacer-dev
COPY ./app ./app
COPY ./.env ./.env

RUN . pacer-dev/bin/activate

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

RUN python manage.py test

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
