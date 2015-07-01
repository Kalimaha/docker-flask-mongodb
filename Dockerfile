# Create a container from Ubuntu.
FROM ubuntu:14.04

# Credits.
MAINTAINER Guido Barbaglia "guido.barbaglia@gmail.com"

# Update Ubuntu repositories.
RUN apt-get update

# Install Python.
RUN apt-get install -y python python-pip wget

# Create a working directory.
RUN mkdir geobricks

# Add requirements file.
ADD requirements.txt /geobricks/requirements.txt
ADD geobricks_common_settings.py /geobricks/geobricks_common_settings.py
ADD geobricks_rest_settings.py /geobricks/geobricks_rest_settings.py

# Add the script that will start everything.
ADD start.py /geobricks/start.py

# Install Python requirements.
RUN pip install -r /geobricks/requirements.txt