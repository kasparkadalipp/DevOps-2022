FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
 
ARG INFLUX_DB_NAME
ARG INFLUX_DB_HOST
 
ENV INFLUX_DB=${INFLUX_DB_NAME}
ENV INFLUX_HOST=${INFLUX_DB_HOST}
RUN pip3 install -r requirements.txt
COPY . .
CMD ["/bin/bash", "-c","python3 data_process.py $INFLUX_DB $INFLUX_HOST"]