#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=onguntuna/app
version="$1"

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
echo "$DOCKER_HUB_PW" | docker login --username onguntuna --password-stdin
docker tag browser-game:latest $dockerpath:$version

# Step 3:
# Push image to a docker repository
docker image push $dockerpath:$version
