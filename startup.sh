#!/usr/bin/env bash
# runing uwsgi
cd /geobricks

# check if exist the enviroment variable $UWSGI_PROCESSES set by cli interface.
#TODO: collect all the uwsgi paramenters and add to the startup sequence
if [ -z "$UWSGI_PROCESSES" ];
then
    env/bin/uwsgi --socket 127.0.0.1:11000 -w run_geobricks_engine:app &
else
    env/bin/uwsgi --socket 127.0.0.1:11000 -w run_geobricks_engine:app -p $UWSGI_PROCESSES &
fi

# TODO: check if it is needed to restart NGINX
service nginx restart
