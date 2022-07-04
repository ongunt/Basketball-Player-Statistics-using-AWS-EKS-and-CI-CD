#!/usr/bin/env bash



echo building
docker build --tag=app:latest .

docker run -p 80:80 app
