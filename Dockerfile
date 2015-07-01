FROM ubuntu:14.04
MAINTAINER Guido Barbaglia "guido.barbaglia@gmail.com"

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN apt-get install unzip
RUN mkdir geobricks
ADD requirements.txt /geobricks/requirements.txt
ADD start.py /geobricks/start.py
RUN pip install -r /geobricks/requirements.txt
# RUN wget https://github.com/Kalimaha/docker-flask-mongodb/archive/no_cherrypy.zip
# RUN unzip no_cherrypy.zip