# Create a container from Ubuntu.
FROM ubuntu:14.04

# Credits.
MAINTAINER Guido Barbaglia "guido.barbaglia@gmail.com"

# Update Ubuntu repositories.
RUN apt-get update

# Add UbuntuGIS repository.
RUN apt-get install -y software-properties-common
RUN apt-get install -y python-software-properties
RUN add-apt-repository --yes ppa:ubuntugis/ppa

# Install Python.
RUN apt-get install -y -q build-essential python-gdal python-simplejson
RUN apt-get install -y python python-pip wget
RUN apt-get install -y python-numpy libgdal1h gdal-bin libgdal-dev
RUN apt-get install -y libblas-dev liblapack-dev
RUN apt-get install -y python-dev
RUN apt-get install -y python-psycopg2

# Installing stuff


# Create a working directory.
RUN mkdir geobricks

# Install VirtualEnv.
RUN pip install virtualenv

# Add requirements file.
ADD requirements.txt /geobricks/requirements.txt
ADD geobricks_common_settings.py /geobricks/geobricks_common_settings.py
ADD geobricks_rest_settings.py /geobricks/geobricks_rest_settings.py

# Add the script that will start everything.
ADD start.py /geobricks/start.py

# Run VirtualEnv.
RUN virtualenv /geobricks/env/
RUN /geobricks/env/bin/pip install wheel
RUN /geobricks/env/bin/pip install -r /geobricks/requirements.txt