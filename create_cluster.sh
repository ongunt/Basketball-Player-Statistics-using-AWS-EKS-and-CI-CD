#!/usr/bin/env bash

# create a low cost cluster
eksctl create cluster --name=app --region=us-west-2 --instance-types=t2.micro


