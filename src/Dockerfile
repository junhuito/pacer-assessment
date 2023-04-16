# Bonus Task

FROM python:3.9

RUN mkdir -p /app

COPY ./requirements.txt ./
COPY ./app ./app
COPY ./.env ./.env

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app

RUN python manage.py collectstatic --noinput

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py test

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
