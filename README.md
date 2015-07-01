# Docker for Flask/MongoDB
Docker container template for Flask/MongoDB web applications.

```
docker build -t geobricks:from_file .
docker run -it -p 5000:5000 geobricks:from_file python /geobricks/start.py
```

```
sudo sublime-text /etc/default/docker

# Use DOCKER_OPTS to modify the daemon startup options.
DOCKER_OPTS="-H tcp://127.0.0.1:4243 -H unix:///var/run/docker.sock --dns 168.202.2.78"
```