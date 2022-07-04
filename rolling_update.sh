#!/usr/bin/env bash

NEWVERSION="$1"

kubectl set image deployment/app app=docker.io/onguntuna/app:$NEWVERSION --namespace=app
