# Create a container from Ubuntu.
FROM ubuntu

# Credits.
MAINTAINER Guido Barbaglia and Simone Murzilli <guido.barbaglia@gmail.com;simone.murzilli@gmail.com>

# Update Ubuntu repositories.
RUN apt-get update

# Add UbuntuGIS repository.
RUN apt-get install -y software-properties-common
RUN apt-get install -y python-software-properties

# Update UbuntuGIS repository.
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
RUN apt-get update

# Install Python.
RUN apt-get install -y -q build-essential python-gdal python-simplejson
RUN apt-get install -y python python-pip wget
RUN apt-get install -y python-numpy python-numpy-dev libgdal1h gdal-bin libgdal-dev
RUN apt-get install -y libblas-dev liblapack-dev

# numpy dependency
RUN apt-get -y install python-dev

# scipy dependency
RUN apt-get -y install libblas3gf libc6 libgcc1 libgfortran3 liblapack3gf libstdc++6 build-essential gfortran python-all-dev libatlas-base-dev
RUN apt-get -y install libblas-dev liblapack-dev

# DB connector dependency
RUN apt-get install -y python-psycopg2


# Installing stuff

# Create a working directory.
RUN mkdir geobricks
RUN mkdir /geobricks/data

# Install VirtualEnv.
RUN pip install virtualenv

# Add requirements file.
ADD requirements-libs.txt /geobricks/requirements-libs.txt
ADD requirements-geobricks.txt /geobricks/requirements-geobricks.txt

# Run VirtualEnv.
RUN virtualenv /geobricks/env/

# Activate virual enviromnt (this avoid to use /geobricks/env/bin/pip all the time but it's possible to use pip directly)
# RUN source rasterio/bin/activate

# Dependency
RUN /geobricks/env/bin/pip install wheel

# gdal
RUN /geobricks/env/bin/pip install pygdal

# rasterio
RUN /geobricks/env/bin/pip install numpy
RUN /geobricks/env/bin/pip install rasterio

# scipy
RUN /geobricks/env/bin/pip install scipy
RUN /geobricks/env/bin/pip install pysal

# Install all the other requirements
RUN /geobricks/env/bin/pip install -r /geobricks/requirements-libs.txt
RUN /geobricks/env/bin/pip install -r /geobricks/requirements-geobricks.txt

# Install REST Egine
#RUN /geobricks/env/bin/pip install https://github.com/geobricks/geobricks_rest_engine/archive/development.zip

# create config folder for config files
RUN mkdir /geobricks/config

# NGINX
# Install Nginx.
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN apt-get install -y nginx
RUN rm -rf /var/lib/apt/lists/* && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx

#ADD nginx-app.conf /geobricks/nginx/nginx-app.conf
#RUN ln -s /geobricks/nginx/nginx-app.conf /etc/nginx/sites-enabled/

# Add the script that will start everything.
ADD start.py /geobricks/start.py
ADD start_ext.py /geobricks/start_ext.py
ADD cli.py /geobricks/cli.py
ADD start_cli.py /geobricks/start_cli.py
ADD script.sh /geobricks/script.sh
ADD script.sh script.sh
ADD start.py /geobricks/start.py

# TODO: fix
ADD start.py start.py
ADD __init__.py /geobricks/__init__.py
ADD __init__.py /geobricks/config/__init__.py


#expose 80
#CMD service nginx start

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Define working directory.
# WORKDIR /etc/nginx


#RUN rm /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf
COPY uwsgi_params.conf /etc/nginx/uwsgi_params.conf

# Expose ports.
EXPOSE 80

# Define default command.
#CMD ["nginx", "-g", "daemon off;"]
CMD ["nginx", "-t"]
# EXPOSE 443