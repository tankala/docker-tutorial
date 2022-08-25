FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./ /app/

CMD flask run -h 0.0.0.0 -p 5000