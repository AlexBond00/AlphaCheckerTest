#!/bin/sh


echo "Make migrations:"
python manage.py makemigrations

echo "Do migrations:"
python manage.py migrate

echo "Create superuser: "
python manage.py createsuperuser --username=admin --email=admin@example.com --noinput

echo "Run server: "
python manage.py runserver '0.0.0.0:8000'
