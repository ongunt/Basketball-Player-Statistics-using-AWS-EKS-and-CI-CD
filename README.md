
## Udacity Cloud Nanodegree Capstone

This project aims to create app by using AWS EKS and automatize it by creating a pipeline using CircleCI.
You need eksctl, kubectl and awscli installed.
Manually you can run:

- [create_cluster.sh](create_cluster.sh) to build a K8 cluster with eskctl 

- [run_docker.sh](run_docker.sh) and [run_kubernetes.sh](run_kubernetes.sh) to deploy the app

- [destroy_cluster.sh](destroy_cluster.sh) to destroy the cluster

- [.circleci/config.yml](.circleci/config.yml) to create the pipeline


### Steps of the pipeline:
- Step 1: linting

installing the dependencies and linting the code

- Step 2: docker

pushing the app to Docker

- Step 3: Kubernetes cluster creation

creating an K8 cluster named "app" using AWS EKS 

- Step 4: Kubernetes cluster deployment

deploying to the K8 cluster

- Step 5: Kubernetes cluster test

testing the K8 cluster

