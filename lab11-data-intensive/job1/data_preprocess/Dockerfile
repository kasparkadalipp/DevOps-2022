FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
 
ARG INFLUX_DB_NAME
ARG INFLUX_DB_HOST
ARG DS_NAME
ARG DS_HOST
ARG DS_PORT
 
ENV LOCAL_INFLUX_DB=${INFLUX_DB_NAME}
ENV LOCAL_INFLUX_HOST=${INFLUX_DB_HOST}
ENV NAME=${DS_NAME}
ENV HOST=${DS_HOST}
ENV PORT=${DS_PORT}
 
RUN pip3 install -r requirements.txt
COPY . .
CMD ["/bin/bash", "-c","python3 data_preprocess.py $LOCAL_INFLUX_DB $LOCAL_INFLUX_HOST $NAME $HOST $PORT"]