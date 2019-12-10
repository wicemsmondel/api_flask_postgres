FROM python:3.8
RUN apt-get install libpq-dev && mkdir api
WORKDIR /api
COPY . /api/
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 app.py