#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=docker.io/onguntuna/app
version=$1


kubectl get nodes

kubectl create deploy app --image=${dockerpath}:${version} --port=80 --namespace=capstone

kubectl expose deployment app --type=LoadBalancer --port=80 --target-port=80 --namespace=app

kubectl get deploy,rs,svc,pods

