FROM python:3.8-slim-buster
WORKDIR /app
ENV INFLUX_DB_NAME='influxdb-co2'
ENV INFLUX_DB_HOST='172.17.90.20'
COPY ./flask-frontend/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./flask-frontend/ .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
