FROM python:3.10.13-bullseye

WORKDIR /alpha_checker

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "main.py"]