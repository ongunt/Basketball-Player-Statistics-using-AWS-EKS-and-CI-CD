
## Udacity Cloud Nanodegree Capstone

This project aims to deploy a REST API using AWS EKS and automatize it by creating a pipeline using CircleCI.
Basic requirements for this project are:
- AWS IAM credentials (Access Key, Secret Access Key)
- An AMI (Ubuntu Server 22.04.1 LTS 32bit, T2.micro instance with every other setting being default)
- A key pair for EC2
- Inbound rules for the firewall with source always 0.0.0.0/0 (HTTP, HTTPS, SSH, TCP port 3000) 
- Minikube should be installed 
- A DockerHub account
- A CircleCI account
- Registeration of SSH key pair to CircleCI
- Configuration of the environment variables in CircleCI 


After configuring everything, just run the pipeline.

### Steps of the pipeline:
- Step 1: linting

Installing the dependencies and linting the code

- Step 2: docker

Pushing the app to Docker

- Step 3: Kubernetes cluster creation

Creating an K8 cluster named "app" using AWS EKS 

- Step 4: Kubernetes cluster deployment

Deploying to the K8 cluster

- Step 5: Kubernetes cluster test

Testing the K8 cluster

After running everything successfully, you should see an URL with port 8000 that leads to our website. You can find the player statistic by using the following links (you should use your own URLv4_address):  

Relative speed of a player with respect to all of other players (Example: Player 2): http://URLv4_address:8000/relative_speed_plots?player_id=2 

Relative speed of a player with respect to a certain other player (Example: Player 1 and Player 2): 

http://URLv4_address:8000/relative_stats?player_id1=2&player_id2=2 

Overall stats of a player (Example: Player 2): 

http://URLv4_address:8000/stats?player_id=2 

Plot of the players acceleration (Example: Player 2): 

http://URLv4_address:8000/player_acceleration_plot?player_id=2 

Plot of the players velocity (Example: Player 2): 

http://URLv4_address:8000/player_speed_plot?player_id=2 


Manually you can run:

- [create_cluster.sh](create_cluster.sh) to build a K8 cluster with eskctl 

- [run_docker.sh](run_docker.sh) and [run_kubernetes.sh](run_kubernetes.sh) to deploy the app

- [delete_cluster.sh](destroy_cluster.sh) to destroy the cluster

- [.circleci/config.yml](.circleci/config.yml) to create the pipeline
