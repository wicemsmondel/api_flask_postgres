FROM python:3-alpine

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip3 install flask flask-cors psycopg2-binary psycopg2 sqlalchemy  && \
 apk --purge del .build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app.py /app/
CMD python3 app.py