# Docker for Flask/MongoDB
Docker container template for Flask/MongoDB web applications.

```
docker build -t geobricks:from_file .
docker run -it -p 5000:5000 geobricks:from_file python /geobricks/start.py
```