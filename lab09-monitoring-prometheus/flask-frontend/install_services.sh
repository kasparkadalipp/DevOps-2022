docker stop $FLASK_CONTAINER || true
docker rm $FLASK_CONTAINER || true

docker stop $NODE_EXPORTER_CONTAINER || true
docker rm $NODE_EXPORTER_CONTAINER || true

docker stop $CADVISOR_CONTAINER || true
docker rm $CADVISOR_CONTAINER || true

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

# Build flask application container image
docker build -t $TEST_IMAGE_NAME -f ./flask-frontend/Dockerfile .

# Run the flask application container
docker run -d -p 8082:5000 --name $FLASK_CONTAINER $TEST_IMAGE_NAME
