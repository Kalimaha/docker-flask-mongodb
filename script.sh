cd /geobricks
env/bin/uwsgi --socket 127.0.0.1:11000 -w start:app -p 2 &
service nginx restart
