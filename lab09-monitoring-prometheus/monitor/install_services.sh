docker stop $PROMO_CONTAINER || true
docker rm $PROMO_CONTAINER || true

docker stop $CADVISOR_CONTAINER || true
docker rm $CADVISOR_CONTAINER || true

docker stop $NODE_EXPORTER_CONTAINER || true
docker rm $NODE_EXPORTER_CONTAINER || true

docker stop $ALERT_CONTAINER || true
docker rm $ALERT_CONTAINER || true

#docker stop $GRAFANA_CONTAINER || true
#docker rm $GRAFANA_CONTAINER || true

# CADVISOR container for controller VM
# UPDATE THE BELOW DOCKER STATEMENT IF REQUIRED
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


# NODE-EXPORTER container for controller VM
# UPDATE THE BELOW DOCKER STATEMENT IF REQUIRED
docker run -d -p 9100:9100 --name $NODE_EXPORTER_CONTAINER prom/node-exporter

# Grafana for visualization of resources used by containers and VMs
# UPDATE THE BELOW DOCKER STATEMENT IF REQUIRED
#docker run -d -p 3000:3000 --name $GRAFANA_CONTAINER grafana/grafana:6.5.0

# PROMETHEUS for collecting metrics using NODE-EXPORTER and CADVISOR
# UPDATE THE BELOW STATEMENTS IF REQUIRED
rm -f $HOME/monitor/prometheus.yml || true
rm -r $HOME/monitor || true
mkdir -p $HOME/monitor/
cp $PWD/monitor/prometheus.yml $HOME/monitor/
docker run -d -p 9090:9090  \
   -v $PWD/monitor/rules.yml:/etc/prometheus/rules.yml \
   -v $PWD/monitor/prometheus.yml:/etc/prometheus/prometheus.yml \
   --name $PROMO_CONTAINER prom/prometheus


# ALERT CONTAINER
docker run -d -p 9093:9093 \
          	-v $PWD/monitor/alertmanager.yml:/alertmanager.yml  \
          	--name $ALERT_CONTAINER prom/alertmanager \
          	--config.file=/alertmanager.yml \
          	--cluster.advertise-address=172.17.91.131:9093