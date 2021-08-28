FROM python:3.9-alpine as base

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./ /app/

########### START NEW IMAGE : DEBUG ###################
FROM base as debug
RUN pip install ptvsd

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0.0 -p 5000

########### START NEW IMAGE: PRODUCTION ###################
FROM base as prod

CMD flask run -h 0.0.0.0 -p 5000