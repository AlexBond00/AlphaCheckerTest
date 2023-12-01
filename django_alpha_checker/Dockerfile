FROM python:3.10.13-bullseye

WORKDIR /django_alpha_checker

COPY ./alpha_checker .

COPY ./entrypoint.sh .

COPY requirements.txt .

RUN ["chmod",  "+x", "/django_alpha_checker/entrypoint.sh"]

RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt