FROM python:3.10-alpine

RUN apk add make

COPY ./requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app 

RUN pip install -r requirements.txt 

CMD ["make", "run_with_gunicorn"]