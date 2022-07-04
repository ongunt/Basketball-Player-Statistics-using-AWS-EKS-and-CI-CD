
# Basketball Player Statistics API Deployment using EKS and CircleCI

The goal of this project is to create a REST API which extracts statistics like total distance covered within 1 minute windows for each player from a dataset that contains player positions according to timestamps and sends it to a static web service. Then, this API will be deployed by using two different methods: 

- Deployment 1: A simple deployment using AWS EC2 instances

- Deployment 2: Deploying a Docker containerized REST API to AWS EKS and automatize a pipeline with CircleCI


## Local REST API
In order to run this API, you should first install the dependencies using with: 
```
$ pip install -r requirements.txt
```
To deploy the API locally, run app.py. (If you want to deploy this API locally, then Port 5000 is required for the host.) 

You can find the player statistic by using the following links:  

- Relative speed of a player with respect to all of other players: 
http://localhost:5000/relative_speed_plots?player_id=2 

- Relative speed of a player with respect to a certain other player: 
http://localhost:5000/relative_stats?player_id1=2&player_id2=2 

- Overall stats of a player: 
http://localhost:5000/stats?player_id=2 

- Plot of the players acceleration: 
http://localhost:5000/player_acceleration_plot?player_id=2 

- Plot of the players velocity: 
http://localhost:5000/player_speed_plot?player_id=2 


## Deployment 1: A simple deployment using AWS EC2 instances

In this method, an EC2 instance will be launched and REST API will be transfered into the server using SSH. After configuring the environment and installing the dependencies, the API will be deployed. You can find the screenshots of a successful deployment in this link: https://github.com/ongunt/Basketball-Player-Statistics-using-AWS-EKS-and-CI-CD/tree/main/EC2%20Deployment%20Screenshots

Basic requirements: 
- AWS IAM credentials should be registered. (Access Key, Secret Access Key) 
- An AMI (Ubuntu Server 22.04.1 LTS 32bit, T2.micro instance with every other setting being default) should be chosen. 
- A key pair should be created and downloaded. This will be the key that you’ll use to make an ssh connection to the server.  
- Inbound rules for the firewall with source always 0.0.0.0/0 (HTTP, HTTPS, SSH, TCP port 3000) should be added. 
- If the port in app.py is 5000 or 80, it should be changed to 8080. 

After launching the instance successfully, you should ssh into the instance using: 

```
$ ssh -i /path/my-key-pair.pem my-instance-user-name@<IPv4_address> 
```
 
After sshing into the server, you should transfer the files by using: 
```
$ sudo scp -r -i /path/to/.pem /path/Folder ubuntu@IPV4_address:/path/to/copy 
``` 

Then, you should install python with:  
```
$ sudo apt update 
$ sudo apt install python3 python3-pip 
$ sudo apt-get install python3-venv 
```

After this, you can create a python environment, install the required dependencies and activate: 
```
$ python3 -m venv <name> 
$ source <name>/bin/activate 
$ pip install -r requirements.txt
$ python main.py 
```
You should be able to find the web browser at: http://IPv4address:8080 (you should use your own URLv4_address)
- Relative speed of a player with respect to all of other players (Example: Player 2): 
http://IPv4address:8080/relative_speed_plots?player_id=2 

- Relative speed of a player with respect to a certain other player (Example: Player 2):  
http://IPv4address:8080/relative_stats?player_id1=2&player_id2=2 

- Overall stats of a player (Example: Player 2): 
http://IPv4address:8080/stats?player_id=2 

- Plot of the players acceleration (Example: Player 2): 
http://IPv4address:8080/player_acceleration_plot?player_id=2 

- Plot of the players velocity (Example: Player 2): 
http://IPv4address:8080/player_speed_plot?player_id=2


## Deployment 2: Deploying a Docker containerized REST API to AWS EKS and automatize a pipeline with CircleCI  
This method aims to deploy a REST API using AWS EKS and automatize it by creating a pipeline using CircleCI. The CI\CD enironment will include pushing the built Docker container(s) to the Docker repository and deploying these Docker container(s) to a small Kubernetes cluster. For my Kubernetes cluster I used AWS Kubernetes as a Service. To deploy my Kubernetes cluster, I used Cloudformation and ran these from within Circle CI as an independent pipeline. 
You can see the screenshots of the deployment process and websites in the folder: https://github.com/ongunt/Basketball-Player-Statistics-using-AWS-EKS-and-CI-CD/tree/main/EKS%20Deployment%20Screenshots

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
- If the port in app.py is 5000 or 8080, it should be changed to 80


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

You should be able to find the web browser at: http://IPv4address:8000 
- Relative speed of a player with respect to all of other players (Example: Player 2):
http://IPv4address:8000/relative_speed_plots?player_id=2 

- Relative speed of a player with respect to a certain other player (Example: Player 2):
http://IPv4address:8000/relative_stats?player_id1=2&player_id2=2 

- Overall stats of a player: (Example: Player 2)
http://IPv4address:8000/stats?player_id=2 

- Plot of the players acceleration (Example: Player 2): 
http://IPv4address:8000/player_acceleration_plot?player_id=2 

- Plot of the players velocity (Example: Player 2): 
http://IPv4address:8000/player_speed_plot?player_id=2



Manually you can run:

- [create_cluster.sh](create_cluster.sh) to build a K8 cluster with eskctl 

- [run_docker.sh](run_docker.sh) and [run_kubernetes.sh](run_kubernetes.sh) to deploy the app

- [delete_cluster.sh](destroy_cluster.sh) to destroy the cluster

- [.circleci/config.yml](.circleci/config.yml) to create the pipeline
