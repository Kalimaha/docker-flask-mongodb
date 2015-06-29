# Docker for Flask/MongoDB
Docker container template for Flask/MongoDB web applications.

# Fix docker-compose on Ubuntu

1) Change the DOCKER_OPTS in /etc/default/docker to:
DOCKER_OPTS="-H tcp://127.0.0.1:4243 -H unix:///var/run/docker.sock"

2) Restart docker
sudo restart docker

3) Make sure that docker is running on localhost:4243 
$ netstat -ant  |grep 4243
tcp        0      0 127.0.0.1:4243          0.0.0.0:*               LISTEN

4) Set DOCKER_HOST (.bashrc)
export DOCKER_HOST=tcp://localhost:4243

$ echo $DOCKER_HOST
tcp://localhost:4243 

5) And now
docker-compose build
