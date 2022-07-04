#!/usr/bin/env bash

NEWVERSION="$1"

kubectl set image deployment/capstone app=docker.io/onguntuna/capstone:$NEWVERSION --namespace=capstone
