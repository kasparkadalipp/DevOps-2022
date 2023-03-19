
docker stop $NODE_EXPORTER_CONTAINER || true
docker rm $NODE_EXPORTER_CONTAINER || true

docker stop $CADVISOR_CONTAINER || true
docker rm $CADVISOR_CONTAINER || true

docker stop $BACKEND_CONTAINER || true
docker rm $BACKEND_CONTAINER || true

# Create volume for influxdb
docker volume create $INFLUX_VOL || true

# CADVISOR to monitor the container resource utilization of frontend system
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8081:8080 \
  --detach=true \
  --name=$CADVISOR_CONTAINER \
  --privileged \
  --device=/dev/kmsg \
  gcr.io/cadvisor/cadvisor:v0.45.0

# NODE-EXPORTER to monitor the resource utilization of frontend  system
docker run -d -p 9100:9100 --name $NODE_EXPORTER_CONTAINER prom/node-exporter

#INFLUXDB container
docker run -d \
  -p 8086:8086 \
  --name $BACKEND_CONTAINER \
  -v $INFLUX_VOL:/var/lib/influxdb2 \
  influxdb:1.1.1

pip install -r ./influx-backend/requirements.txt || true

# Insert CSV data in to influxdb
python3 ./influx-backend/csvToInflux.py 
