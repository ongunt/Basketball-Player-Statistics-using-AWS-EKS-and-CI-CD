#!/usr/bin/env bash



echo building
docker build --tag=capstone:latest .

docker run -p 80:80 capstone
