# Docker for Flask/MongoDB
Docker container template for Flask/MongoDB web applications.

```
docker build -t geobricks:from_file .
docker run -it -p 5000:5000 geobricks:from_file python /geobricks/start.py
```

# To add a DNS to docker
```
sudo sublime-text /etc/default/docker

# Use DOCKER_OPTS to modify the daemon startup options.
DOCKER_OPTS="-H tcp://127.0.0.1:4243 -H unix:///var/run/docker.sock --dns 168.202.2.78"

# Google DNS
DOCKER_OPTS="--dns 208.67.222.222 --dns 208.67.220.220"
  
# Restart the docker service
sudo service docker restart
```


```
# How to configure the filesystem access of the host from the container 

sudo docker run -it -p 5000:5000 -v /home/vortex/repos/docker/geobricks_config/:/geobricks/config/ -v /home/vortex/repos/docker/geobricks_data/geoserver_data_dir/:/geobricks/data/geoserver_data_dir/ geobricks:geobricks /geobricks/env/bin/python /geobricks/start_ext.py

### with a more complete configuration

sudo docker run -it -p 5000:5000 -v /home/vortex/repos/docker/geobricks_config/:/geobricks/config/ -v /home/vortex/repos/dockergeobricks_data/geoserver_data_dir/:/geobricks/data/geoserver_data_dir -v /home/vortex/repos/docker/geobricks_data/storage/:/geobricks/data/storage/ -v /home/vortex/repos/docker/geobricks_data/distribution/:/geobricks/data/distribution/ -v /home/vortex/repos/docker/geobricks_data/distribution_sld/:/geobricks/data/distribution_sld/ -v /home/vortex/repos/docker/geobricks_data/tmp/:/geobricks/data/tmp geobricks/geobricks:0.1 /geobricks/env/bin/python /geobricks/start_ext.py
```

